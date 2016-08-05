#  adpanel.py
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

HAS_LIB_CAIRO = True
HAS_WXCAIRO = True #cairo binding for wxPython

try:
    import wx.lib.wxcairo
except ImportError as error:
    HAS_WXCAIRO = False 
    
try:
    import cairo 
except ImportError as error:
    HAS_LIB_CAIRO = False 
    
from jetclient  import motionpanel

class GifAddPanel(wx.Panel):
    """
    object to hold both gifs and image
    """
    def __init__(self, *args, **kwargs):
        super(GifAddPanel, self).__init__(*args, **kwargs)
        
        #initialize some attributes
        self.x = 0 
        self.y = 0
        
        self.init_addpanel()
        
    def init_addpanel(self):
        """
        initialize the adpanel
        """
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.panel = motionpanel.MotionPanel(self, -1)
        
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.panel)
        self.SetSizer(self.sizer)
        
    def  OnEraseBackground(self, event):
        """
        this event helps us avoid flickers while performing
        drawing on the system. Best left empty to avoid
        redraws
        """
        pass 
        
    def OnPaint(self, event):
        """
        caled whenever our panel needs to perform a 
        redraw
        """
        self.DC = wx.PaintDC(self)
        
        #get the client area
        self.client_area = self.GetClientSize()
        
        #Let's do the drawing in another function
        self.DrawAdGradient(self.DC, self.client_area)
        
    def DrawAdGradient(self, DC, client_area):
        """
        Given the DC and the client_area perform
        the drawing of the gradient
        """
        
        #check if we have a working rectangle
        if(not client_area):
            return None 
            
        self.CG = wx.lib.wxcairo.ContextFromDC(DC)
        
        #create a gradient pattern using cairo
        self.gradient_pattern = cairo.LinearGradient(10.2, 10.0, 25.0, 960.0)
        self.gradient_pattern.add_color_stop_rgba(1,0,0,0,1)
        self.gradient_pattern.add_color_stop_rgba(0,1,1,1,1)
        self.CG.rectangle(0,0, client_area.width, client_area.height)
        self.CG.set_source(self.gradient_pattern)
        self.CG.fill()
