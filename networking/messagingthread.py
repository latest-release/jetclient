#  messagingthread.py
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

import socket
import threading 
import time 

class MessageThread(threading.Thread):
    """
    thread will work on sending and receiving of
    messages to the server
    """
    def __init__(self, t_sockobject, t_sockclient):
        """
        @param: t_sockobject --> Object from the Networking Thread which will enable
                                 us use some of it's defined attributes and methods.
        @param: t_sockclient --> Object for the client socket created and initialized
                                 on start. it will help us use it for receiving and
                                 sending.
        """
        threading.Thread.__init__(self)
        
        self.t_sockobject = t_sockobject
        self.t_sockclient = t_sockclient
        
        #notable attributes
        self.running = True
        self.max_buffer = 45609
        self.msg_lock = threading.Lock()
        
    def send_msg(self, msg):
        """
        send the message to the server
        """
        try:
            if(len(msg)):
                if(self.t_sockclient):
                    #acquire a lock before sending the messaget
                    #to the server
                    self.msg_lock.acquire()
                    #print "TSOCKET IS ", self.t_sockclient
                    #print "TSOCOB IS", self.t_sockobject
                    self.t_sockclient.send(msg)
                    self.msg_lock.release()
                else:
                    raise RuntimeError("Unable to send message to client becuase socketobject is NONE")
                    
            else:
                return -1
        except:
            raise 
        
        finally:
            if(self.msg_lock.locked()):
                #lock was acquired but an error occured
                #release
                self.msg_lock.release()
                
    def run( self ):
        """
        OVERRIDE the run method. This class should not be
        called rather called it's start method that will
        be able to start the thread.
        NOTE: codes that do heavy work are placed here.
        """
        try:
            self.peer = self.t_sockclient.getpeername()
        except socket.error as error:
            self.msg = "Socket endpoint might not be conected"
            self.t_sockobject.wx_disconnected(self.msg)
            
        #start recicing the messages
        while(self.running):
            if(self.t_sockclient is not None):
                #socket is not none
                try:
                    self.data = self.t_sockclient.recv(self.max_buffer)
                    if(len(str(self.data))):
                        self.t_sockobject.wx_display(self.data )
                    else:
                        self.msg =  "Connection Might have been Reset by Peer"
                        
                        #Post a message/notification to the GUI thread and
                        #it should reconnect back
                        self.t_sockobject.wx_disconnected(self.msg)
                        self.t_sockobject.wx_reconnect(self.peer)
                        self.t_sockclient.close()
                        #continue 
                except socket.error as error:
                    self.msg =  "Connection to the server might have been closed"
                    self.t_sockobject.wx_disconnected(self.msg)
                    self.running = False 
                except:
                    raise 
            else:
                raise RuntimeError("Client socket not yet initialized exiting")
                break
                    
        
        #break the loop of network send and receive
        self.t_sockclient.close()
