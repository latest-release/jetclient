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
        
        self.connection = True
        self.host = ""
        self.port = 8018
        self.msg_handler=None
        self._sock = None 
        if(len(host) > 1):
            self.host = host[0]
            self.port = host[1]
            
        #self.init_sock()
        
    def init_sock(self):
        """
        initialize the socket on runtime
        """
        try:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            return self._sock
        except socket.error as error:
            raise  
        except:
            raise 
            
    def connect(self, host, port):
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
                if(self._sock is None):
                    self._sock = self.init_sock()
                    
                self._sock.connect((self.gethostname(), self.gethostport()))
                
            except socket.gaierror as error:
                raise 
            except socket.error as error:
                self.msg = "A connection to the server failed or disconnected but we shall reconnect again"
                self.wx_displaylog(self.msg)
                time.sleep(3)
                continue 
            else:
                #post a notification that we are connected
                self.wx_connected()
                break 
    
    def run(self):
        """
        when start is called this will be 
        evoked automatically.
        NOTE: this is not always called directly
        """
        try:
            if len(self.host) > 1:
                self.connect(self.host[0], self.host[1])
            else:
                #connect to localhost we were not given anything
                self.connect("localhost", 5512)
        except:
            raise 
            
        #call the message handling thread
        try:
            try:
                #self.sock = init_sock()
                #if(self.sock):
				self.msg_handler = messagingthread.MessageThread(self, self._sock)
				#start the thread inside of a thread
				#which will be started when the threads
				#start method is called in the GUI.
				self.msg_handler.start()
                #else:
                #    raise AttributeError("Unable to initialize socket object")
            except:
                raise 
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
                    if(self.msg_handler):
                        self.msg_handler.send_msg(msg)
                    else:
                        raise AttributeError("HANDLE is None")
                except:
                    raise 
            else:
                return False 
        except:
            raise 
            
