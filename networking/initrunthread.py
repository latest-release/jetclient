#  initrunthread.py
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
 ---initrunthread.py
     This file initializes the thread to handle the connection
     to the server as a separate thread
"""

from jetclient.networking import clientnetworking
from jetclient.networking import communication
import threading
import traceback 
import socket 
import wx
import time 

class ClientThread(threading.Thread):
    """
    thread object to help run as separate from
    the gui. manages the data and sends it
    to the gui thread
    """
    
    def __init__(self, host, connected, display, lost):
        threading.Thread.__init__(self)
        
        #attributes
        self.connected = connected
        self.display = display
        self.disconnected = lost 
        self.host = host 
        self.msg_lock = threading.Lock()
        self.msg = [ ]
        self.established = False 
        
        #initialize the networking 
        self.networking = clientnetworking.Networking(self.host[0], self.host[1])
        
    def run(self):
        """
        called internal when the start method is called
        it should not be called directly.
        NOTE: the actual heavey weight code is placed here
        """
        
        #while(self.established != True):
        try:
            self.ret_code = self.networking.connect()
        except socket.error as error:
            self.msg = "Unable to connect to server %s %s Reconnecting" %(self.networking.gethostname(), self.networking.gethostport())
            self.disconnected(self.msg)
            time.sleep(2)
                 
        else:
            #notify the GUI thread that we are connected
            self.established=True
            self.connected() 
                
        while(True):
            try:
                self.data =self.networking.receive()
                if(len(str(self.data))):
                    print self.data 
                else: 
                   print "A disconnect"
                   self.networking.getsock().close()
                   self.networking.init_clientsock()
                   try:
                       self._reconnect(True)
                   except socket.error as error:
                       continue 
                
                    
            except socket.error:
                raise       
        self.networking.getsock().close()
         
    def reconnect(self):
        pass 
        '''
        #receive the data 
        while(True):
            try:
                self.data = self.networking.receive()
            except:
                raise 
            #else:
            #     print self.data 
                     
        #End the client receiving loop
        self.networking.shutdown_sock(socket.SHUT_RDWR, self.networking._sock)
        
        '''
    def send(self, data):
        """
        called from the GUI to send
        message
        """
        try:
            self.msg_lock.acquire()
            self.networking.send_msg(data)
            self.msg_lock.release()
        except:
            print traceback.exc()
            
    
    def _reconnect(self, bool_):
        """
        function called internal to perform
        a reconnect to the server when either
        the server has disconnected or not yet
        started
        """
        if(bool_ == True):
      
            try:
                self.ret_code = self.networking.connect()
                if(self.ret_code == True):
                    #successfuly connected
                    #some action to be perform here
                    #like notifying and posting messages
                    #to listerne
                    pass 
                else:
                    #not yet connected
                    #we could show the status from here
                    pass 
            except socket.error as error:
                raise 
            except:
                raise        
        
        
