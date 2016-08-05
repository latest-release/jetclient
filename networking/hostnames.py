#  hostnames.py
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

""""***filename:hostnames.py****
   just crabs the hostname and sends it to the server
   immediately we are connected to the server. This helps
   the server associate client icon with it's hostname
"""

import socket 
import traceback

def my_hostname():
    """
    get's the hostname of the computer on which it is
    run on.
    
    >>> import hostnames
    >>> 
    >>> h = hostnames.my_hostname()
    >>>
    >>> h
    's8workspc1-OptiPlex-3020'
    >>>
    """
    try:
        return socket.gethostname() 
    except:
        raise 
        
def my_ip():
    """
    get's the ip address of the computer on which it is running
    
    >>> import hostnames
    >>>
    >>> ip = hostnames.my_ip()
    >>>
    >>> ip
    '127.0.1.1'
    >>> 
    """
    #NOTE: in mostly cases it will return '127.0.0.1'
    # but netifaces is apropriate for just kind of task
    try:
        return socket.gethostbyname(my_hostname())
    except:
        raise 
        
def get_service_by_port(port, protocol):
    """
    grabs a particular service running on the given
    port by the given protocol
    """
    #TODO:
    pass 
    
