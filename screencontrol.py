#  screencontrol.py
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
from jetclient import sidecontrolpanel
from jetclient import adpanel 
from jetclient import motionpanel

class ScreenControl(wx.Frame):
    """
    A wx.frame object which will be called when ever
    the time is over
    """
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self,*args, **kwargs)
        """
        constructor
        """
        self.ToggleWindowStyle(wx.STAY_ON_TOP)
        self.initialize_cursor()
        self.SetFocus()
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        self.initScreen()
        
    def initialize_cursor(self):
        self.cursor = wx.StockCursor(wx.CURSOR_BLANK)
        self.SetCursor(self.cursor)
        
    def OnMotion(self, event):
        event.Skip()
        
    def initScreen(self):
        """
        initialized the required actions
        from here
        """
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.init_panel() #initialize and create the panel
        
    def init_panel(self):
        """
        call the panels we created earlier on
        """
        self.panel_sizer = wx.BoxSizer(wx.HORIZONTAL)
        try:
            self.side_control = sidecontrolpanel.SideControlPanel(self, -1)
            self.image_gif_panel = motionpanel.MotionPanel(self, -1)
            
            #add the panels to the sizers
            self.panel_sizer.Add(self.side_control, 0, wx.EXPAND)
            self.panel_sizer.Add(self.image_gif_panel, -1, wx.EXPAND)
            
            #add the panel_sizers to the main sizer
            self.main_sizer.Add(self.panel_sizer, -1, wx.EXPAND | wx.ALL,0)
            self.SetSizer(self.main_sizer)
        except:
            raise  
                
    def show_fullscreen(self, boolean, style=None):
        """
        run the window in full screen mode
        """
        try:
            if(boolean == True): 
                self.Show()
                self.Center()
                self.displaysize = wx.GetDisplaySize()
                self.SetSize(self.displaysize)                
                wx.CallLater(20, self.SetWindowStyleFlag, wx.FRAME_NO_TASKBAR  | wx.STAY_ON_TOP)
                
                wx.CallLater(95, self.ShowFullScreen, True, style=wx.FRAME_NO_TASKBAR | wx.FULLSCREEN_NOMENUBAR | wx.FULLSCREEN_NOTOOLBAR | 
                                                wx.FULLSCREEN_NOSTATUSBAR | wx.FULLSCREEN_NOBORDER | wx.FULLSCREEN_NOCAPTION
                             )
                
                self.Refresh()
        except:
            print "Error"
            
            
    def run_fullscreen(self):
        self.ShowFullScreen(True)
        
    def OnClose(self, event):
        """
        event called whenever
        there is a need to close
        """
        #print "Closing Me"
        event.Veto()
        #self.Destroy()

    def OnHide(self):
        """
        Called to hide the frame
        """
        wx.CallAfter(self._HideFrame, status=False)

    def _HideFrame(self, status=None):
        """hide the frame function called internatly"""
        self.Hide()



