#  networking.py
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

import threading 
import socket 
import traceback 
import time 
from jetclient.networking import messagingthread
from jetclient.networking import hostnames
import wx
from jetclient.networking import clientnetworking

class ConnectionThread(threading.Thread):
    """
    connection thread will be responsible for initializing
    the connection to the server and creating the socket
    leaving the recieving of data for other threads.
    """
    def __init__(self, host, wx_displaylog, wx_connected, wx_display, wx_disconnected, wx_reconnect):
        threading.Thread.__init__(self)
        
        self.host = host 
        self.wx_connected = wx_connected
        self.wx_display = wx_display
        self.wx_disconnected = wx_disconnected
        self.wx_reconnect = wx_reconnect
        self.wx_displaylog = wx_displaylog
        self.sendlock = threading.Lock()
        self.connection = True
        self.running = True
        self.hosts = ""
        self.ports = 0
        
        self.networking = None
        
        if(len(self.host) == 2):
            self.hosts = self.host[0]
            self.ports = self.host[1]
        else:
            self.ports = 5500
                
    def startserver(self, host, port):
        """
        Attempt to establish a connection to the
        server.
        """
        
        #Some times we might start when the server has not yet
        #started. So we need to keep connecting to the server
        #until acceptions. That's why we need to put
        #connect inside a loop
        
        while(self.connection):
            try:
                self.networking = clientnetworking.Networking(self, host, int(port))
                try:  
                    self.sock = self.networking.init_clientsock()
                    if(self.sock):
                        self.networking.setsock(self.sock)
                        self.networking.est_connect()
                    else:
                        raise AttributeError("Socket is not yet initialized.")
                        
                except socket.gaierror as error:
                    self.msg = "ERROR!!!! %s" % str(error)
                    self.wx_displaylog(self.msg) 
                    break 
                    
                except socket.error as error:
                    self.msg = "A connection to the server failed or disconnected but we shall reconnect again"
                    self.wx_displaylog(self.msg)
                    time.sleep(3)
                    continue
              
                else:
                    #post a notification that we are connected
                    self.wx_connected()
                    break #immeidately we are connected break off the loop
            except:
                raise 
                
    
    def run(self):
        """
        when start is called this will be 
        evoked automatically.
        NOTE: this is not always called directly
        """
        try:
            self.startserver(self.hosts, self.ports)
            try:
                while(self.running):
                    try:
                        self.data = self.networking.receive()
                        if(self.data):
                            self.wx_display(self.data)
                        else:
                            self.running = False 
                    except:
                        raise
                        
            except socket.error as error:
                self.running = False  
        except:
            raise 
            
    def gethostname(self):
        """
        return the hostname used for connecctions
        """
        return self.host
        
    def gethostport(self):
        """
        return the hostport used for making a connection
        """
        return self.port 
        
    def sendmsgs(self, msg):
        try:
            if len(msg):
                try:
                    if(self.networking):
                        #Networking has been initialized
                        #we are are connected to the server.
                        #print "Sending ", msg, "NAME ", self.getName()
                        try:
                            self.sendlock.acquire()
                            #print "Locking ", self.sendlock.locked()
                            self.networking.send_msg(msg) 
                            self.sendlock.release()
                            #print "Releasing ", self.sendlock.locked()
                        except socket.error as error:
                            #Probably BROKEN PIPE
                            #Which occurs when the server closed our socket connection
                            #or the server end has disconnected us.
                            #Just ignore it's a normal error.
                            print "Hey there they have broken me down"  
                        finally:
                            if(self.sendlock.locked()):
                                self.sendlock.release()
                    else:
                        raise AttributeError("HANDLE is None")
                except:
                    raise 
            else:
                return False 
        except:
            raise 
            
