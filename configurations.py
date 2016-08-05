#configuration.py will handle the entire configuration of
#the application
#
#
"""
Configuration setting for application
"""
HAS_CONFIG=False

try:
    import configobj
    HAS_CONFIG=True
except ImportError as error:
    raise ImportError("MOdule named config not found")
    HAS_CONFIG=False

import os
import sys

#getting user home this is compatible
#with non linux systems
USER_HOME = os.path.expanduser("~")
CONFIG_DIR = ".jetclient"
CONFIG_FILE = "jconfig.conf"

def createhomedir():
    """
    create the configuration home directory
    """
    if(os.path.exists(getconfighome())):
        #it exists
        pass
    else:
        try:
            os.makedirs(getconfighome())
        except OSError as error:
            raise OSError("Exception Handled while creating dir " + error)

def getconfighome():
    """
    return the home where configuraton are saved
    """
    return os.path.join(USER_HOME, CONFIG_DIR)

def getconfigfile():
    """
    return the configuration files
    """
    return os.path.join(getconfighome(), CONFIG_FILE)


def createconfigfile(*args):
    """
    create configuration file
    """
    if(HAS_CONFIG):
       createhomedir()
       config = configobj.ConfigObj()
       config.filename = getconfigfile()
       if(args):
           CONFIG_FILE=args[0]
       else:
           config["HOSTNAME"]=0
           config["PORTNAME"]=0
           config.write()    

def create_timetracking(filename):
    try:
        config = configobj.ConfigObj()
        config.filename = filename 
        config["CURRENT_TIME"]=0
        config.write()
    except:
        raise 
        
