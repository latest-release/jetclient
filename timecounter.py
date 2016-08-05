#
#timecounter.py will be responsible for counting time
# given to the client
#
import wx
import time 
from wx.lib.pubsub import Publisher as Publisher
from jetclient import savetime 
import wx.lib.agw.balloontip as BT
from jetclient import popnotify 

class TimeCounter(object):
    """
    object for keeping track of the
    running time given to client.
    """
    DEFAULT_TIME = 0
    MAX_COUNTER = 59
    
    def __init__(self, parent, count_interval ):
        """
        constructor
        
        @param:--> Parent: the parent object of either wx.frame or wx.Panel
                           which we shall bind the timer with.
        """
        self._parent = parent 
        self._count_interval = count_interval
        self._run_time = 0
        self._minutes = 0
        self._seconds = 0
        
        self.msg = """Your session has been started with [ %d ].
                      Any inquiry check with  our staffs
                      THANKS FOR CHOOSING OUR INTERNET CAFE 
                   """ % self.getClientMinutes()
       
        #bind time event
        self.timer = wx.Timer(self._parent)
        self._parent.Bind(wx.EVT_TIMER, self.OnTrackTime, self.timer)
        
        self.initialize_listeners()
        
    def initialize_listeners(self):
        """
        this are the listners who wait for the messages
        to be sent from the sender
        """
        Publisher.subscribe(self.receivedMessage, "receivedMSG")
        
    def initCounter(self):
        """initialize the counter"""
        self._parent.running_time.SetLabel(str(self._parent.run_time))
        self._parent.owed_timetext.SetLabel(str(self._parent.owed_time))
        self._parent.seconds_text.SetLabel(str(self._parent.seconds))
        
    def OnTrackTime(self, event):
        """
        Event triggered when timer is started.
        """ 
        if(self.getClientMinutes() > 0):
            if(self.getClientSeconds() == 60):
                self.setClientSeconds(0)
                self.decrementClientMinutes(1)
                self.sendNotification() #called everytime minutes have been decremented
                
            self.incrementSeconds(self._seconds)
            self._seconds += 1
                
        #client does not have any minutes
        #puase the timer
        else:
            if(self._stopTimer() == True):
                # A stop was successful
                self.sendNotification()
                self.msg = "Your Session has FINALLY ended with ( %d ) Minutes left" % self.getClientMinutes()
                self.show_notification("YOUR SESSION IS OVER", self.msg)
            else:
                #manually pause
                self.timer.Stop()
            
    def reset_all(self):
        """
        Resets all the given time.
        """
        try:
            self.pauseTimer()
            self._parent.seconds_text.SetLabel("0")
            self._parent.owed_timetext.SetLabel("0")
            self._parent.running_time.SetLabel("0")
            
            self._run_time = 0
            self._minutes = 0
            self._seconds = 0
        except:
            raise 
            
    def stop_timer_nosaving(self):
        """
        Called rudely to stop the timer without saving
        it's status to the disk.
        """
        if(self.timer.IsRunning()):
            self.timer.Stop()
        else:
            return None 
            
    def _stopTimer(self):
        """
        stop the timer only and only if
        it is running.
        
        NOTE: this function is used internally
              instead of stoping use pauseTimer()
        """
        if(self.timer.IsRunning()):
            #Yes it is running
            #first save the current time status to the disk
            if(self.getClientMinutes()):
                self.saveRunningStatus(self.getClientMinutes())
                self.timer.Stop()
            else:
                self.timer.Stop()
            return True
        else:
            #No it is not running
            return False 
            
    def startTimer(self):
        """start the timer first check if it is running"""
        
        try:
            if(self.timer.IsRunning()):
                #It is running we can ignore but let's return a
                #meaningful signal
                return None 
            else:
                self.msg = "Your Session has been Started ( %d )" % self.getClientMinutes()
                
                wx.CallLater(10, self.show_notification, "Session Start", self.msg)
                #print "Hi timer ", self.timer 
                self.timer.Start(self.getCountInterval())
        except:
            print "some failure"
            #an error occured return false
            return False 
            
            
    def pauseTimer(self):
        """
        function to pause the timer
        """
        #NOTE: there is no standard timer function to pause
        #we have to code it ourself by first stopping it
        #save the status to the disk.
        try:
            if(self.timer.IsRunning()):
                #stop and then save to the disk
                self._stopTimer()
                return True #success
            else:
                #it's not running
                return None #not running
        except:
            return False #exception
            
    def resumeTimer(self):
        """resume running the timer"""
        try:
            if(self.timer.IsRunning()):
                #can't start an already running timer
                return -1
            else:
                self.startTimer()
        except:
            return False #exception like failure
            
            
    def destroyTimer(self):
        """
        According to wx.Python DOCs, timers are destroyed by normal
        reference count
        """
        #TODO: if you want try to destroy it
        pass 
        
    def update_usertime(self, newtime):
        """
        given the time update it
        with the proviews given to the client
        """
        try:
            self.pauseTimer()
            self.setClientMinutes(int(newtime), increment=True)
            self.saveRunningStatus(self.getClientMinutes())
            self.resumeTimer()
            try:
                Publisher.sendMessage("sendRemainingMinutes", data=str(self.getClientMinutes()))
            except:
                raise 
        except:
            raise 
            
    def saveRunningStatus(self, time):
        """
        save the status of our timer
        mostly the minutes used, seconds, hours
        to the disk
        """
        try:
            if(time):
                self.saved = savetime.writetime(time)
            
        except:
            raise 
            
        
    #setters
    def incrementRunInterval(self, new_interval):
        """
        set the running interval
        """
        self._count_interval += new_interval
        
    def setClientSeconds(self, new_seconds):
        """
        set the client running seconds.Called every time
        """
        self._seconds = new_seconds
    
    def incrementSeconds(self, new):
        """
        increment the seconds
        """
        #NOTE: while we increment the second we shall
        #request for the publisher to send the second to the
        #server to set the second of the client.
        try:
            self._parent.seconds_text.SetLabel(str(new))# += int(new)
            
            #NOTE: the listener of this message is in the window.py file,
            #who will do the sending.
            Publisher.sendMessage("sendRemaingSeconds",data=new)
        except:#/secondTrue #/secondsessionEnded /secondsessionBegins
            raise 
        
    def incrementRuntime(self, new):
        """
        increment the client runtime
        """
        #We would like to show to the server the time the
        #client has used so far. so we shall publish
        #a message of runtime.
        try:
            self._parent.running_time.SetLabel(str(new))
            Publisher.sendMessage("sendRuntime",data=new)
        except:
            print "Exception"
            
    def setClientMinutes(self, new_minutes, increment=False):
        """
        set the client minutes
        """
        try:
            if(increment == False):
                self._minutes = int(new_minutes)
            else:
                
                #increment the client time
                self._minutes += int(new_minutes)
        except:
            return False
            
    def setClientRuntime(self, runtime):
        """
        set new running time
        """
        self._run_time = runtime 
        
       
    def decrementClientMinutes(self, subminutes):
        """
        subtrack some of the minutes the client is having
        """
        Publisher.sendMessage("sendingRemaing.Minutes",  data=subminutes)
        self.decrement = self.getClientMinutes() - subminutes
        self.saveRunningStatus(self.decrement)
        
        if(self.setClientMinutes(self.decrement) == False):
            raise ValueError("Unable to set client time")
        else:
            try:
                #print "Doing something like sending to the server"
                #Publish a message to the window.py which will send a message to
                #the server.
                try:
                    #print "Duplicating"
                    Publisher.sendMessage("sendRemainingMinutes", data=str(self.getClientMinutes()))
                except:
                    raise 
                else:
                    self._parent.owed_timetext.SetLabel(str(self.getClientMinutes()))
                    
            except:
                return False
            
        #set the client runtime
        self.setClientRuntime(self.getClientRuntime() + int(subminutes))
        try:
            self.incrementRuntime(self.getClientRuntime())
        except:
            raise 
            
    def getClientSeconds(self):
        """
        return the client remiaing seconds
        """
        return self._seconds
        
    def getClientMinutes(self):
        """
        return the current minutes which
        the client is having
        """
        return self._minutes 
        
    def getClientRuntime(self):
        """
        get the time of minutes/hours the client has
        used so far
        """
        return self._run_time
    
    def getCountInterval(self):
        """
        return the count interval given 
        of the runtime
        """
        return self._count_interval
        
    def getInterval(self):
        """Note: Only like the getCounterInterval()
            but the difference is that this
            one we used the wx.GetInterval()
        """
        return self.timer.GetInterval()
        
    def sendNotification(self):
        """
        Send the notification to any listeners
        """
        try:
            Publisher.sendMessage("screenControl",  data=self.getClientMinutes())
        except:
            raise  
            
    def show_notification(self, title, msg):
        """
        use the popnotify to dislay a notification
        message
        """
        notify = popnotify.ClientNotification(msg)
        notify.InitNotfication()
        notify.showMessage(title, msg)

    def receivedMessage(self, message="cmsg", control=None):
        """
        some data has been received
        """
        pass 
            

