import socket 
import time 
import threadhandler

class ConnectionError(Exception):
    """
    connection error custom exception
    """
    def __init__(self, error):
        self.error = erro 
        
    def __str__(self):
        """format and return the exception"""
        
def get_hostname():
    """
    return the hostname
    """
    return socket.gethostname()
    
class ClientConnection(object):
    """
    object for creating and maniuplating the socket
    on the client endpoint
    """
    def __init__(self, host_name, host_port, max_retries, notification):
        """
        our constructor
        
        @param: host_name, port_name--> server hostname and portname
        @param: max_retries---> Maximum number of retries to be performed
                when the server is either not there
        @param: notification: --> a simple notification wrapper for showing
                popups
        """
        self._hostname = host_name
        self._portname = host_port
        self._max_retries = max_retries
        self.notification = notification
        self.running = True
        self.logtime = time.asctime()
        self.max_receive = 1024
        self.client_socket = None
        self.connected = False 
        #initialize the socket on startup
        self.initsocket()
        
    def initsocket(self):
        """initialize the socket"""
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            return self.client_socket
        except socket.error as error:
            return False 
            
    def connect_to_server(self, **kwargs):
        """
        perform a connection to the server
        """
        if(len(kwargs) >= 2):
            self._host_name = kwargs.get("hostname")
            self._port_name = kwargs.get("portname")
        
        else:
            if(self.client_socket == None):
                self.clientsocket = self.initsocket()
                try:
                    self.clientsocket.connect((self.getHostname(), self.getHostport()))
                    return True
                except socket.error as error:
                    raise  #socket.error("Unable to connect to server")
                else:
                    print "Everything is okay"
            else:
                #print "Entered another runlevel"
                while(self.connected != True):
                    try:
                        self.client_socket.connect((self.getHostname(), self.getHostport()))
                        self.connected = True
                    except socket.error as error:
                        #print "Reconnecting"
                        #time.sleep(5)
                        pass 
                    else:
                        return self.client_socket
    
    
    def senddata(self, msg_data):
        """
        send the given data to the server
        """
        try:
            if(self.client_socket == None):
                raise RuntimeError("Socket connection was not initialized on startup")
            else:
                if(len(msg_data) > 0):
                    print "Here is the socket",
                    self.send = self.client_socket.send(msg_data)
                    if(self.send == 0):
                        raise RuntimeError("Connection closed by remote host")
                        
        except socket.error as error:
            raise #socket.error("Unable to send data to server")
        except:
            return -1
    
    '''     
    def receive_data(self):
        """
        receive data from the server
        """
        self.server_data = []
        try:
            if(self.client_socket == None):
                raise RuntimeError("Client socket not yet initialize(READY)")
            else:
                print "Connected to ", self.client_socket.getpeername()
                while(True):
                    self.data = self.client_socket.recv(self.max_receive)
                    if(self.data == ''):
                        raise RuntimeError("A connection might have been closed on remote host")
                    self.server_data.append(self.data)
                return ''.join(self.server_data)
                
            #self.end_connection()
            
        except socket.error as error:
            raise socket.error("Error attempting to recieved msg")
        except:
            raise ValueError 
    ''' 
    def end_connection(self):
        """
        close the socket at the
        """
        try:
            if(self.client_socket == None):
                #just pass we are not connected
                pass 
            else:
                try:
                    self.client_socket.shutdown(socket.SHUT_RDWR)
                    self.client_socket.close()
                except socket.error as error:
                    raise socket.error("Unable to shutdown connection")
                finally:
                    self.client_socket.close()
        except:
            raise socket.error("And error while trying to shutdown client connection")
            
    def getHostname(self):
        """
        return the current hostname to be used
        for connection
        """
        return self._hostname
        
    def getHostport(self):
        """
        return the hostport to be used for connection
        """
        return self._portname
