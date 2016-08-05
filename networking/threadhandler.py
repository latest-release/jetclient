#  threadhandler.py
#  
#  Copyright 2014 wangolo joel <wangolo@wangolo-3020>
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
from jetclient.networking import clientconnection 
import threading 
from jetclient.networking import message_cmd
import socket 
from wx.lib.pubsub import Publisher 
import string 
import socket 
import wx

def getuser_login():
    import os
    #return the user login name
    return os.getlogin()

class ConnectionHandler(threading.Thread):
    """
    thread responsible for starting a connection
    to the server
    """
    def __init__(self, clientobject, exe):
        threading.Thread.__init__(self, name="void")
        self.clientobject = clientobject
        self.sending_lock = threading.Lock()
        self.receiving_lock = threading.Lock()
        self.exe = exe
        Publisher.subscribe(self.sessionEnded, "sessionEnds")        
        Publisher.subscribe(self.sessionBegins, "sessionBegins")

    def sessionEnded(self, data):
        """Function called to reeive message from publisher"""
        print "Iam attempting to send the session [ %s ]" % data.data
        try:
            self.data = "/" + data.data
            if(len(str(self.data)) > 1 ):
                wx.CallAfter(self.sendMSG, self.data)
            else:
                print "No data to send to server"
        except:
            raise 

    def sessionBegins(self, data):
        """Receive a message from publisher and send
           it to the server
        """
        try:
            self.data = "/" + data.data
            if(len(str(self.data)) > 1):
               wx.CallAfter(self.sendMSG, self.data)
            else:
                #no data to send to the server
                print "No data to send to server"
        except:
            raise 

    def handleData(self, data):
        """handle and manipulate the given data
        """
        #check if the message is on any of the defined
        #protocol commands
        if(data.startswith("/time")):
            self.data = string.replace(data, "/time", "",1)
            Publisher.sendMessage("newSessionReceived", data=self.data)
                
        elif(data.startswith("/sub")):
            self.data = string.replace(data, "/sub", "",1)
            print "Replacing", self.data
            Publisher.sendMessage("deductClientime", data=self.data)
                
        elif(data.startswith("/ticket")):
            self.data = string.replace(data, "/ticket", "",1)
            Publisher.sendMessage("handleTicket", data=self.data)
                
        elif(data.startswith("/reboot")):
            self.data = string.replace(data, "/reboot", "",1)
            Publisher.sendMessage("rebootClient", data=self.data)
                
        elif(data.startswith("/shutdown")):
            self.data = string.replace(data, "/shutdown", "",1)
            Publisher.sendMessage("shutdownClient", data=self.data)
                
        elif(data.startswith("/cmd")):
            self.data = string.replace(data, "/cmd", "",1)
            Publisher.sendMessage("runExternalCMD", data=self.data)
            
        elif(data.startswith("/lock")):
            self.data = string.replace(data, "/lock", "",1)
            Publisher.sendMessage("lockScreen", data=self.data)
        
        elif(data.startswith("/reserve")):
            self.data = string.replace(data, "/reserve", "",1)
            Publisher.sendMessage("reserveNeeded", data=self.data)
        else:
            #It's probably not a protocol command
            Publisher.sendMessage("messageFromServer", data=self.data)
            
    def sendMSG(self, data):
        """send the given data tot he server
        """
        print "Iam sending data", data
        
        try:
            self.sending_lock.acquire()
            self.ret_code = self.clientobject.senddata(data)
            self.sending_lock.release()
        except RuntimeError as error:
            raise 
           # print "Error doing some sending"
        #finally:
        #    self.sending_lock.release()
        
    def run(self):
        """
        establish a socket connection
        inside of the thread
        handles until the server disconnects or it itself
        disconnects
        """
        while(self.clientobject.connected !=True):
            self.clientobject.connect_to_server()
            #find out if we are connected to the server
            if(self.clientobject.client_socket == None):
                raise RuntimeError("Client has not yet connect to the server")
            
            #attempt to receive data from the server
            try:
                #acquire a lock while receiving data
                self.receiving_lock.acquire()
                self.data = self.clientobject.client_socket.recv(self.clientobject.max_receive)
                self.receiving_lock.release()
                if(not len(str(self.data))):
                    print "A disconnect in the server end"
                    try:
                        self.clientobject.end_connection()
                        break
                    except socket.error as error:
                        print "Unable to end connection"
                else:
                    self.handleData(self.data)
                    
            except socket.error as error:
                #could be a bad file discriptor
                print "Unable to receive because connection closed"

class ExecuteConnection(object):
    """initializing object"""
    def __init__(self, notification, hostname, portname):
        """accepting nothing"""
        self.notification = notification
        self.hostname = hostname
        self.portname = portname
        self.client_object = clientconnection.ClientConnection(self.hostname, self.portname, None, None)
        
    def log(self, msg):
        """
        log the given msg or error
        """
        print msg
        
    def execute(self):
        """
        execution starts here
        """
        self.connection_thread = ConnectionHandler(self.client_object, self)
        self.connection_thread.start()
    
    
