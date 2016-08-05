#  clientnetworking.py
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
"""
---clientnetworking.py
   Client networking holds the networking codes which are responsible
   for creating socket and recieving and managing the communication
   to the server connected at the endpoint.
---
"""

import traceback
import sys
import socket 
import threading 
import time 

class Networking(object):
    """
    object to handle the networking
    managing and establishing the connection
    to the server..
    """
    
    def __init__(self, threadobj, servername, serverport, max_buffer=None):
        """
        @param:servername--> Server name/ip
        @param:serverport--> server listening address default(8018)
        """
        self.threadobj = threadobj
        self._servername = servername 
        self._serverport = serverport 
        self.max_buffer = max_buffer
        self.running = True
        self.established = False 
        
        if(self.max_buffer == None):
            self.max_buffer = 1024
            
        self._sock = None 
        
        #start  initializing the socket
        #self.init_clientsock()
        
    def init_clientsock(self):
        """
        method called when the object initialized
        """
        try:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            #self._sock.settimeout(60)
            return self._sock
            
        except socket.error as error:
            raise 
        except:
            raise 
            
    def est_connect(self, host=None, port=None):
        """
        perform a connection to the server
        host,port can be provided
        """
        try:
            if(self._sock is not None):
                
                if(host and port):
                    self._servername=host 
                    self._serverport=port
                    
                #while(True):
                try:
                    self._sock.connect((self._servername, self._serverport))
                except socket.gaierror as error:
                    self.msg = "Got address related error [ %s ]" % error 
                    #continue 
                except socket.error as error:
                    #print "Failed to connect to server attempting to perform a reconnect"
                    #time.sleep(3)
                    #continue
                    raise   
                except:
                    raise 
            
            #socket not yet initialized raise
            else:
                raise RuntimeError("Client socket is not yet initialized this could be a BUG")
        except:
            raise 
            
    def receive(self, sock=None):
        """
        recieve for data when we are connected
        """
        try:
           
            if(sock is not None):
                self._sock = sock 
                  
            if(self._sock is not None):
                #while(self.running):
                try:
                    self.data = self._sock.recv(self.max_buffer)
                    if (len(str(self.data))):
                        return self.data 
                    else:
                        #In case the server disconnects us
                        #close the current socket and then establish a new
                        #connection to the server
                        #NOTE: We could just have called connect from here.
                        #but to follow the simple design request for a connection.
                        self._sock.close()
                        self.threadobj.wx_reconnect(self._sock) 
                        
                except socket.error as error:
                    #self.msg = "An error [ %s ] Time [ %s ]" % (str(error),time.asctime())
                    #self.threadobj.wx_displaylog(self.msg)
                    self._sock.close()
                    self.threadobj.wx_reconnect(self._sock)
                    print "Something is wrong with the server may be we have been disconnected" 
                    
                except:
                      self._sock.close()
                      self.threadobj.wx_reconnect(self._sock) 
            else:
                raise RuntimeError("Client socket is not yet initialized while receving")
        except:
            print traceback.print_exc() 
            
    def send_msg(self, data, sock=None):
        """
        send the given data to the
        server
        @param: data---> The data that should be send to sesrver
        Optional pass the sock
        """
        try:
            if(sock):
                try:
                    self.sent = sock.send(str(data))
                    return self.sent 
                except socket.error as error:
                    raise 
                    
            else:
                if(self._sock):
                    try:
                        self.sent = self._sock.send(str(data))
                        return self.sent
                    except socket.error as error:
                        '''
                        print "Am in the sending session begugging" 
                        if(self._sock):
                            print "Sock am there but performing a reconnect"
                            self.threadobj.wx_reconnect(self._sock)
                        else:
                            print "Sock am existing and performing a reconnect"
                            self._sock = self.init_clientsock()
                            self.threadobj.wx_reconnect(self._sock)
                        '''
                else:
                    raise RuntimeWarning("Could not send on un initialized socket...")
        except:
            print traceback.print_exc() 
        
    def shutdown_sock(self, flags, sock):
        """
        shutdown the socket of the client
        NOTE: According to python socket document. One could just call sock.close()
        and closes the socket endpoint. But it is always advised to use sock.shutdown first
        and close either writing/reading or both. To avoid confusion on the server
        end
        
        This is what the wrapper function does
        """
        try:
            if(sock):
                #yes socket was initialized
                try:
                    sock.shutdown(socket.SHUT_RDWR)
                    #we could call close from here like sock.close()
                    #but first check for the exception
                except socket.error as error:
                     print traceback.print_exc()
                finally:
                    #if the shutdown failed
                    #just close
                    sock.close()
            else:
                #socket was none
                return -1
        except:
              print traceback.print_exc()
    #---getters and setters || mutaters and accessers----#
    
    def sethostname(self, hostname):
        """
        given the host name
        set it to be used for connection
        """
        self._servername = hostname
        
    def sethostport(self, hostport):
        """
        set the new hostport
        """
        self._serverport = hostport
        
    def setmaxbuffer(self, maxbuffer):
        """
        set new data recving size
        """
        self.maxbuffer = maxbuffer
        
    def gethostname(self):
        return self._servername
        
    def gethostport(self):
        return self._serverport
        
    def getmaxbuffer(self):
        return self.max_buffer
        
    def setsock(self, newsock):
        """
        Set the socket that shall be used for the connection.
        """
        self._sock = newsock 
        
    def getsock(self):
        """
        return the socket initillized on the client side
        """
        return self._sock 
        
    def __unicode__(self):
        """
        return the string representation of both
        hostname and port
        """
        return "%s %s" % (self.gethostname(), self.gethostport())
        
                     
