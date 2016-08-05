#  confighandler.py
#  
#  Copyright 2014 s8works-pc1 <s8works-pc1@s8workspc1-OptiPlex-3020>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import os

home = os.path.expanduser("~")
config = ".config" #include by default on most if not all linux distros
flamingo = "flamingo" #shall be creatd inside of .config

def getconfigurations():
    """
    return the configuration directory
    """
    
    flamingo_file = "hostconfig"
    
    #do the joins of paths
    try:
        home_config = os.path.join(home, config)
        home_config_flamingo = os.path.join(home_config, flamingo)
        if(os.path.exists(home_config_flamingo)):
            flam_file = os.path.join(home_config_flamingo,flamingo_file)
            return flam_file
        else:
            #create it
            print "Doing some creation"
            try:
                dirs = os.makedirs(home_config_flamingo)
                return os.path.join(home_config_flamingo, flamingo_file)
            except OSError as error:
                print "Failed to create dir maybe be permission isues"
    except:
        raise 
        

def getconfiguration_dirs():
    try:
        home_config = os.path.join(home, config)
        return os.path.join(home_config, flamingo)
    except:
        raise 
        
