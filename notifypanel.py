#  notifypanel.py
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
from jetclient import timecounter
from wx.lib.pubsub import Publisher as Publisher
from jetclient import screencontrol
from jetclient.networking import commands  as commands 
from jetclient import confighandler 
import configobj
from jetclient import savetime 
import os
from jetclient import popnotify 

class NotificationPanel(wx.Panel):
    """notification panel handles
    simple notifications for the client display
    """
    def __init__(self,*args, **kwargs):
        super(NotificationPanel, self).__init__(*args, **kwargs)
        
        
        self.parent = self.GetParent()
        self.screen = screencontrol.ScreenControl(None, -1)
        self.timetracker  = timecounter.TimeCounter(self, 1000)
        self.timetracker.startTimer()
        self.screen_is_running = False
            
        #initialize attributes
        self.subscribers()
        
        self.Init()
        
     
    def get_saved_session(self):
        """
        Check if there is any previously saved session.
        """
        try:
            print "Attempting to initialize current session"
            
            self.session_dir = confighandler.getconfiguration_dirs()
            self.config = configobj.ConfigObj(os.path.join(self.session_dir, savetime.filename))
            
            self.currenttime = self.config["CURRENT_TIME"]
            if(self.currenttime != 0):
                return self.currenttime
            else:
                return None 
        except:
            raise  
            
    def subscribers(self):
        """
        This functions creates and initializes
        subscribers
        """
        Publisher.subscribe(self.restore_previous_session, "RestoreRecentSession")
        Publisher.subscribe(self.newSessionReceived, "newSessionReceived")
        Publisher.subscribe(self.ControlScreen, "screenControl")
        Publisher.subscribe(self.deductTime, "deductClientime")
        Publisher.subscribe(self.lockScreen, "lockScreen")      
        Publisher.subscribe(self.ticketReceived, "handleTicket")
        Publisher.subscribe(self.newbroadcast, "NewBroadcast")
        Publisher.subscribe(self.PauseSession, "PauseSession")
        Publisher.subscribe(self.ResumeSession, "ResumeSession")
        Publisher.subscribe(self.EndPeerSession, "EndPeerSession")
        
    
    def EndPeerSession(self, data):
        """
        Ends the whole user sessions.
        """
        try:
            self.timetracker.stop_timer_nosaving()
            self.timetracker.reset_all()
            wx.CallAfter(self.sendSessionEnd, status=False)
            self.lock_screen()
        except:
            raise 
            
    def PauseSession(self, data):
        try:
            self.timetracker.pauseTimer()
        except:
            raise 
        
    def ResumeSession(self, data):
        try:
            self.timetracker.resumeTimer()
        except:
            raise  
        
    def OnRecieveMinutes(self, message, minutes):
        print "Iam the minutes", minutes
        
    def lockScreen(self, data):
        """
        called to lock the client screen from the
        server end
        """
        try:
            self.pause_locksession(data.data)
        except:
            raise 
    
    def newbroadcast(self, data):
        """
        POP up a notification dialog.
        """
        try:
            #print "Sending popup from othe admin interface", data.data 
            self.show_popup("Notification From Administrators To You", data.data)
        except:
            pass 
            
    def ticketReceived(self, data):
        """
        Received ticket of client.
        """
        try:
            self.ticket = commands.translate_ticket(data.data)
            if(self.ticket):
                try:
                    self.timetracker.update_usertime(int(self.ticket))
                    
                    if(self.timetracker.getClientMinutes > 0):
                       wx.CallAfter(self.openScreen, boo_l=False)
                       wx.CallAfter(self.notifyServer,status=True)
                       
                except:
                    raise 
            else:
                #probably not a ticket 
                pass 
        except:
            raise 
    
    def deductTime(self, data):
        """
        reduce client given time
        """
        #message received through the publisher
        try:
            self.data = data
            if(not len(str(self.data))):
                #no data received
                pass
            wx.CallAfter(self.timetracker.decrementClientMinutes, int(self.data.data)) 
            
        except:
            raise 
            
    def newSessionReceived(self,data):
        """
        Recieves message from the sender
        to add/start client session
        """        
        try:
            self.timetracker.update_usertime(int(data.data))
            
            if(self.timetracker.getClientMinutes > 0):
               wx.CallAfter(self.openScreen, boo_l=False)
               wx.CallAfter(self.notifyServer, status=True)
        except:
            raise 
    
    def restore_previous_session(self, data):
        """
        At what status should we restore the previous
        session.
        """
        try:
            if(data.data == True):
                try:
                    self.recent_session = self.get_saved_session()
                    if(self.recent_session):
                        self.restore_session(self.recent_session)
                    else:
                        print "No session to restore"
                except:
                    raise 
            else:
                print "Can't restore your session"
        except:
            raise 
                              
    def restore_session(self, session_time):
        """
        Given the session time restore it.
        """
        try:
            if(session_time):
                self.msg = "Attempting to restore previous session"\
                           "Your session has been successfuly restored"\
                           "Session is [ %d ]" % int(session_time)
                try:
                    if(self.timetracker.getClientMinutes() > 0):
                        #It's not a session restore
                        print "Your Session is already enough"
                        pass 
                    else:
                        print "Restoring user session"
                        self.timetracker.update_usertime(int(session_time))
                except:
                    raise 
                else:
                    if(self.timetracker.getClientMinutes() > 0):
                        wx.CallAfter(self.openScreen, boo_l=False)
                        wx.CallAfter(self.notifyServer, status=True)
                        self.show_popup("Session Restoration", self.msg)
        except:
            raise  
            
    def show_popup(self, title, msg):
        """
        Show a notification to the user
        that he or she has been given
        time.
        """
        try:
            self.pop = popnotify.ClientNotification("Notification")
            self.pop.InitNotfication()
            self.pop.showMessage(title, msg)
        except:
            #We can live without notification silently end
            raise 
            #pass 
            
    def openScreen(self, boo_l=None):
        """
         open the given screen"
        """
        try:
            self.screen.OnHide()
        except:
           raise 

    def notifyServer(self, status):
        """notify the server that the session
           as began this enables the server to
           set the client icon on the approprpiate.
        """
        try:
           if(status == True):
               self.sendSessionEnd(status)
        except:
           raise 

    def ControlScreen(self, control):
        """
        screen control, receives
        messages to lock the screen
        """
        if(int(control.data) == 0):
            #initialize the screen control and block the user
            #first send a message to the server that the client session
            # has ended
            wx.CallAfter(self.sendSessionEnd, status=False)
            
            self.screen.show_fullscreen(True)
      
        elif(int(control.data) == 5):
            Publisher.sendMessage("receivedMSG",data=control.data) #send message to the Listener on this address (receivedMSG)
            
        elif(control == True):
            #but before that we need to pause the client session
            #and also notify the client that his session will be
            #paused for 5 minutes. After the collpse of the five
            #minutes the session will be resumed automatically
            wx.CallAfter(self.timetracker.pauseTimer)
            self.msg = "Your session has been paused contact"\
            "your session provider either to resume"\
            "or stop. NOTE: this session is paussed for"\
            "A limited time only"
            wx.CallAfter(self.timetracker.show_notification, "Session Paused", self.msg)
            wx.CallAfter(self.lock_screen)
        else:
            pass 
            
    def pause_locksession(self,  data):
        
        # probably we just want to lock the client screen
        try:
            #but before that we need to pause the client session
            #and also notify the client that his session will be
            #paused for 5 minutes. After the collpse of the five
            #minutes the session will be resumed automatically
            wx.CallAfter(self.timetracker.pauseTimer)
            self.msg = "Your session has been paused contact"\
            "your session provider either to resume"\
            "or stop. NOTE: this session is paussed for"\
            "A limited time only"
            wx.CallAfter(self.timetracker.show_notification, "Session Paused", self.msg)
            wx.CallAfter(self.lock_screen)
        except:
              raise 
      
    def sendSessionEnd(self, status=None):
        """send a session end to the server
        """
        if(status==False):
            #Publisher.sendMessage("sessionEnds", message="sessionover", sessioname="sessionEnded")
            Publisher.sendMessage("sessionEnded", data="sessionEnded")
        elif(status == True):
            Publisher.sendMessage("sessionBegins", data="sessionBegins")
        else:
            #unknown session command
            print "Unknown command", status
    
    def lock_screen(self):
        """
        called only to lock the screen
        """
        self.screen.show_fullscreen(True)
        
    def Init(self):
        """run initializers
        """
        print "Initializing"
        self.font_size = 12
        self.font = wx.Font(self.font_size, wx.FONTFAMILY_MODERN , wx.FONTSTYLE_NORMAL ,wx.FONTWEIGHT_BOLD, True, "Courier 10 Pitch")
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.setSizer(self.main_sizer)
        self.SetBackgroundColour("#FFA500")
        self.SetForegroundColour("WHITE")
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        self.InnitWidgets()
        
    def OnPaint(self, event):
        """whenever a panel needs to be redrawn
        this function will be called
        """
        event.Skip()
    
    def OnMotion(self, event):
        """
        whenever a panel detects motions on it
        """
        event.Skip()
        
    def InnitWidgets(self):
        """
        create and initialize widgets
        """
        print "Making widgets"
        self.makelabeltext()
        self.makeruntime()
        
    def makelabeltext(self):
        """create label text that will represent
        the running time
        """
        self.text_sizer = wx.FlexGridSizer(3,4, 5,25) #wx.BoxSizer(wx.HORIZONTAL)
        #make the sizer and then pass them to the laytext
        self.runtime_text = wx.StaticText(self, -1, "Used")
        self.owed_text = wx.StaticText(self, -1, "Minutes")
        self.second_time = wx.StaticText(self, -1, "Seconds")
        
        self.text_list = [ self.runtime_text, self.owed_text, self.second_time]
        #add the widgets to their sizer
        self.Layouttext(self.text_sizer, self.text_list, 5, False)
         
        self.setFont(self.text_list)
        
    def makeruntime(self):
        """
        make the widgets for holding the counting
        time
        """
        self.runtime_sizer = wx.FlexGridSizer(3,3, 15, 65) #wx.BoxSizer(wx.VERTICAL)
        self.running_time = wx.StaticText(self, -1, str(0))
        self.owed_timetext = wx.StaticText(self, -1, str(0))
        self.seconds_text = wx.StaticText(self, -1, str(0))
        
        self.widgetlist = [self.running_time, self.owed_timetext, self.seconds_text]
        self.Layouttext(self.runtime_sizer, self.widgetlist, 5, True,15)
         
        self.setFont(self.widgetlist)
        
    def setFont(self, text):
        if(isinstance(text, list)):
            for w in text:
                w.SetFont(self.font)
        else:
            try:
                text.SetFont(self.font)
            except:
                #silently ignore
                pass 
                
    def Layouttext(self,sizer, widgets, border, border_on_main=True, border_size_on_main=5):
        """
        given the widget lay it out
        to the given sizer
        """
        for widget in widgets:
            sizer.Add(widget, -1, wx.LEFT,border)
            
        #add the sizer to the main sizer
        if(border_on_main):
            self.main_sizer.Add(sizer, 0, wx.LEFT, border_size_on_main)
        else:
            self.main_sizer.Add(sizer, 0, wx.ALL,0)
        
    def setSizer(self, sizer):
        """
        set the sizer to the main panel
        """
        self.SetSizer(sizer)
        sizer.Layout()
