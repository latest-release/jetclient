#  window.py
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
import wx

import wx.lib.wxcairo
import cairo
from jetclient import notifypanel
from jetclient import contextmenu
from jetclient.networking import communication
#from networking.tests import recvthread  
from jetclient.networking import networking1
from jetclient.networking import commands 
import os
import config 
import configobj 
from jetclient import confighandler 
#from wx.lib.pubsub import pub as Publisher
from wx.lib.pubsub import Publisher as Publisher
#print Publisher 
from jetclient.networking import hostnames
from jetclient import notifypanel

class ClientWindow(wx.Frame):
    """
    object for holding client information
    """
    def __init__(self, *args, **kwargs):
        super(ClientWindow, self).__init__(*args, **kwargs)
    
        self.sending_seconds = True
        self.sending_minutes = False
        self.sending_runtime = False 
        self.setListeners()
        self.Init()
        self.init_configs()
        
    def Init(self):
        #bind a motion event
        
        self.host = ""
        self.port = 8018
        self.established = False 
        self.sending_minutes = False 
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        #self.init_configs()
        
        #setup the communication
        self.communication = communication.Communication(self.displaymsg,
                                                         self.connected,
                                                         self.parse_message,
                                                         self.disconnected,
                                                         self.gui_reconnect
                                                         )
                                                         
        self.MakeWidgets()
        
    def MakeWidgets(self):
        """handle the creation of widgets"""
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel = notifypanel.NotificationPanel(self, -1)
        
        self.main_sizer.Add(self.panel, -1, wx.EXPAND | wx.TOP,15)
        self.SetSizer(self.main_sizer)
        
    def init_configs(self):
        """
        initialize and set the needed configurations
        """
        try:
            self.config = confighandler.getconfigurations()
            if(os.path.exists(self.config)):
                return #it exists
            else:
                standard_config = configobj.ConfigObj()
                standard_config.filename = self.config 
                standard_config['hostname']=''
                standard_config['portname']=0
                standard_config.write()
        except:
            raise 
            
    def OnClose(self, event):
        event.Veto()
        
    def OnMotion(self, event):
        """
        event handled when a motion is
        detected. But we are interested in the dragging
        of the frame.
        """
        self.event = event 
        try:
            if not self.event.Dragging():
                self._dragging_pos=None
                #print "Dragging detected"
                return 
            
            if not self._dragging_pos:
                """setting the dragging position by
                getting the current position
                """
                self._dragging_pos = self.event.GetPosition()
            else:
                self.setframe_pos()
        except:
            raise 
            
    def setframe_pos(self):
        """set the frame position during movement
        of dragging
        """
        try:
            self.current_pos = self.event.GetPosition()
            self.new_loc = self._dragging_pos - self.current_pos
            self.SetPosition(self.GetPosition() - self.new_loc)
        except:
            #silent death of an exception
            pass 
            
    def OnPaint(self,event):
        """event triggered when our window needs to be
        redrawn
        """
        #print "Called to do something painting"
        self.DC = wx.PaintDC(self)
        self.DC = self.GetClientSize()
        self.red = 0
        self.blue = 0
        self.green = 0
        self.aplpha = 255
        self._WHITE = wx.WHITE
        self._BLUE = wx.BLUE
        self._RED = wx.RED
        self._GREEN = wx.GREEN
        
        self.Draw(self.DC)
        
    def Draw(DC, *args):
        """perform the drawing of a rounded racatangle
        """
        pass 
        
    def OnRightDown(self,event):
        """
        event triggered when a right clicked
        event is detected
        """
        
        self.PopupMenu(contextmenu.PopupMenu(self), event.GetPosition())
            
    def ShowFrame(self, hostinfo):
        """
        show the given frame
        """
        self.Show()
        wx.CallAfter(self.initializeClient, hostinfo)
        
    def initializeClient(self, hostinfo):
        """
        initialize and start the connection to server
        """
        try:
            self.hostname = hostinfo.get("hostname")
            self.hostport = hostinfo.get("hostport")
        except KeyError as error:
            print "Unable to get requested keys"
        else:
            print hostinfo
            self.hosts = (self.hostname, self.hostport)
            self.network = networking1.ConnectionThread(self.hosts,
                                                      self.communication.displaylog,
                                                      self.communication.connected,
                                                      self.communication.datareceived,
                                                      self.communication.disconnected,
                                                      self.communication.reconnect 
                                                      )
            #start the networking thread and
            #also setup the listerns to listen for messages
            #from the publishers
            self.network.start()
            
            
    def setListeners(self):
        """
        set up a listening function to subscribe function that will
        subscriber to publisher and recieved any messages from them
        """
        Publisher.subscribe(self.OnSessionBegins, "sessionBegins")
        #Publisher.subscribe(self.OnSessionBegins)
        Publisher.subscribe(self.OnSessionEnds, "sessionEnded")
        
        #it's publisher is in the timecounter.py
        Publisher.subscribe(self.OnRecieveSeconds, "sendRemaingSeconds")
        Publisher.subscribe(self.OnRecieveMinutes, "sendRemainingMinutes")
        Publisher.subscribe(self.OnRecieveRuntime, "sendRuntime")
        
    def OnRecieveSeconds(self, message):
        """
        Receives data from the publisher the seconds that
        should be sent to the server.
        """
       
        try:
            #NOTE: seconds are sent every tick. There was a problem
            #that raised when the client is sending the runtime, It turned out that
            #they all arrived at the same time. and the Server received them as one
            #message and yet they are separate so, the trick I used was to use
            #the  wxpython wx.CallLater(seconds, func, **kwargs) to at least delay
            #the sending of seconds to the server. This didn't change anything and the message
            #of runtime didn't arrive at server end at the same time with the
            #second.
            #NOTE: still they at times arrive at the same time.
            if(message.data != None):
                if(self.sending_minutes == True):
                    #ignore we are sending minutes chances of seconds and minutes
                    #arriving together is greate so pause for a while until the minutes
                    #I have been sent.
                    pass 
                else:
                    #No minutes are being sent.
                    wx.CallLater(19, self.network.sendmsgs, "/second" + str(message.data))
                    
        except:
            raise 
            
    def OnRecieveMinutes(self, message):
        """
        Receives data from publisher the minutes that
        should be sent to the server.
        """ 
        try:
            #This solves the problem as noted above on the NOTE:
            #wait for the server to receive the seconds, then set the send
            #the minutes. and send the runtime to the server also.
            #The problem is that if we don't use wx.CallLater, they mostly
            #arrive at the same time on the time. And the server doens't 
            #separate them as one message.
            #NOTE: They still arrive the same time but with a little delay
            
            if(message.data != None):
                self.sending_minutes = True
                self.Refresh()
                wx.CallLater(200, self.network.sendmsgs, "/minutes" + str(message.data))
                self.sending_minutes = False 
                self.Refresh()
            else:
                print"Void void void void void void"
                
        except:
            raise 
            
    def OnRecieveRuntime(self, message):
        """
        Function called when the subscriber receives
        message from the publisher about the client
        runtime
        """
         
        try:
            #This gives the server time to set the greedy seconds that arrive at every intervals.
            #before this is being sent to the server.
            
            #wx.CallLater(3, self.network.msg_handler.send_msg, "/runtime" + str(client_runtime))
            pass    
        except:
            raise 
            
    def OnSessionBegins(self, message):
        """
        We have received the message from the publisher
        Most notably the publisher is on the notifypanel
        and then we send the message to the server
        """
        try:
            wx.CallLater(100, self.network.sendmsgs, '/'+str(message.data))
        except:
            raise 
             
    def OnSessionEnds(self, message):
        """
        Recieves message from the publisher if the client
        session has come to an end
        """
        if(self.established == True):
            #We are not yet connected
            try:
                wx.CallLater(1000, self.network.sendmsgs, "/"+str(message.data)) #Exception
            except:
                raise 
        else:
            print "We are not yet connected"
            
    def displaymsg(self, log):
        """
        function for displaying some logging error
        mesage to the console
        """
        print log 
        
    def connected(self):
        """
        Since we are connected to the server
        perform some checking if we have some time
        """
        self.two_minutes = 200 #in miliseconds
        self.established=True
        try:
            #when we are connected send the hostname to the serve
            #self.network.sendmsgs("/hostname" + hostnames.my_hostname())
            wx.CallLater(self.two_minutes, self.network.sendmsgs, "/hostname" + hostnames.my_hostname())
            Publisher.sendMessage("RestoreRecentSession", data=True)
        except:
            raise 
            '''
            try:
                #this will mostly apply when this is our second time to connect to the
                #server.
                #If we were connected previous and the connection was lost
                #and again we connect to the server. The sever will display
                #the client icon with RED indicating that the client time is
                #over. yet the client still has some time. So if this is our
                #second time to connect we check if the client still has
                #some time and send to the server to set the client icon
                #to the appropriate.
               
                if(self.panel.timetracker.getClientMinutes() != 0):
                    wx.CallLater(2000000, self.network.sendmsgs, "/"+"sessionBegins")
            except:
                 raise 
            '''  
    
    def parse_message(self, msg):
        """
        message has been received from the server
        here we shall see how we can process the
        message filter the commands.
        """
        try:
            print "Parsing message from ", msg
            self.cmd = commands.translate_protocol(msg)
        except:
            raise  
        
    def disconnected(self, host):
        print  host 
        
   
    def gui_reconnect(self, server):
        """
        Called when a connection to the server
        could not be made or we were disconnected
        from the server end.
        """
        print "We are performing  a reconnect"
        try:
            self.network = networking1.ConnectionThread(self.hosts,
                                                      self.communication.displaylog,
                                                      self.communication.connected,
                                                      self.communication.datareceived,
                                                      self.communication.disconnected,
                                                      self.communication.reconnect 
                                                      )
            #start the networking thread
            #After the start of the networking thread the
            #It wil also be able to start the message listerning
            #thread
            self.network.start()
        except:
            raise 
   
