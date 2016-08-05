#  app.py
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
 
#import window 
from jetclient import window
import wx
#import contextmenu 
from jetclient import contextmenu

class RunApp(wx.App):
    def __init__(self):
        #This calls the OnInit when run
        super(RunApp, self).__init__()
        
        self.Init()
   
    def Init(self):
        """initialize runtimme"""
        size = wx.GetDisplaySize()
        print size 
        
        self.window = window.ClientWindow(None, -1, title="", 
                    style=wx.FRAME_SHAPED | wx.CLIP_CHILDREN| wx.STAY_ON_TOP |
                    wx.FRAME_NO_TASKBAR, size=(260,55), pos=(size.width, 0))
         
        try:
            self.config = contextmenu.getconfigs()
            self.hostname = self.config['hostname']
            self.portname = self.config['portname']
            self.server_address = {"hostname":self.hostname, "hostport":int(self.portname)}
        except:
            raise 
        else:
            print self.server_address 
            self.window.ShowFrame(self.server_address)
        
        
if __name__=="__main__":
    app = RunApp()
    app.MainLoop()
