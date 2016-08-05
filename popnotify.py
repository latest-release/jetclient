import pynotify

class ClientNotification(object):
    """
    objects to provide notification popup
    with pynotify
    """
    def __init__( self, msg):
        """
        constructor
        @param:--> funcobject --> function object or class
        """
        self._msg = msg
        self.ERROR = False
        #initialize
        self.InitNotfication()
        
    def InitNotfication(self):
        """
        initialize the notification
        """
        try:
            pynotify.init("Client Notification")
        except:
            ERROR=True 
            
    def showMessage(self, title, msg):
        """
        given the message
        show it to the desktop
        """
        try:
            self.notify = pynotify.Notification(title, msg)
            self.notify.show()
        except Exception as e:
            print "ERROR %s " % e.message
            

if __name__=="__main__":
    s = ClientNotification("what")
    s.InitNotfication()
    s.showMessage("Welcome to our world", "Hi there this is to show how we want you to work with us")

