#  config.py
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


def make_config_path():
    """
    make and return the configuration path
    """
    config_dir = ".config" #standard linux/unix configuation folder for most apps
    app_config_dir = "flamingo"
    home_dir = os.path.expanduser("~")
    
    join = os.path.join(home_dir, config_dir)
    return os.path.join(join, app_config_dir)

def make_config_file(*filename):
    """
    optinally accept the filename
    """
    configfile = "hostconfig.conf"
    get_path = make_config_path()
    if(os.path.exists(get_path)):
        if(filename):
            configfile = filename[0]
            return os.path.join(get_path, configfile)
        
        #no filenam given 
        return os.path.join(get_path, configfile)
    else:
        #just create it
        try:
            os.makedirs(get_path)
        except OSError as error:
            print "Failed could be performission errors"
        except:
            raise 
    
