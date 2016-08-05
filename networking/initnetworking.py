#  initnetworking.py
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
from jetclient.networking import messagingthread 
from jetclient.networking import networking 
from jetclient.networking import communication 

DEFAULT_HOST="localhost"
DEFAULT_PORT=8018

def start_connection(**kwargs):
    """
    called from GUI to start initialized the networking
    """
    if(**kwargs):
        DEFAULT_HOST = kwargs.get("host")
        DEFAULT_PORT = kwargs.get("port")
        
        
