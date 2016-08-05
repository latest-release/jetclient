#  sidecontrolpanel.py
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
from wx.lib import analogclock as ac

class LabelPanel(wx.Panel):
    """
    placing some text with words
    """
    def __init__(self, *args, **kwargs):
        super(LabelPanel, self).__init__(*args, **kwargs)
        
        self.initialize_cursor()
        
        self.initLabel()
       
        self.interval = 50
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyPresses)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        
    def initialize_cursor(self):
        self.cursor = wx.StockCursor(wx.CURSOR_BLANK)
        self.SetCursor(self.cursor)
        
    def OnMotion(self, event):
        event.Skip()
        
    def initLabel(self):
        """
        initialize labels
        """
        self.font = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.font1 = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        self.mainsizer  = wx.BoxSizer(wx.VERTICAL)
        
        self.name = wx.StaticText(self, -1, "Flamingo CyberManager")
        
        self.version = wx.StaticText(self, -1, "Version 0.0.1")
        
        self.release_status = wx.StaticText(self, -1, "Release Status: Pre-Alpha")
        
        #self.developers = wx.StaticText(self, -1, "Developers: www.s8systems.com")
    
        self.labels = [ self.name, self.version, 
                        self.release_status
                      ]
        for l in self.labels:
            try:
                l.SetFont(self.font)
            except:
                raise 
               
        self.laylabels()
        
    def OnKeyPresses(self, event):
        self.keycode = event.GetKeyCode()
        if(self.keycode == wx.WXK_LEFT):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass 
            pass
            
        if(self.keycode == wx.WXK_RIGHT):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass 
            pass
            
        if(self.keycode == wx.WXK_DOWN):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass 
            pass
            
        if(self.keycode == wx.WXK_UP):
            print "We have key interrupt"
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass 
            pass
            
        elif(self.keycode == wx.WXK_F1):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass 
            pass
        elif(self.keycode == wx.WXK_F2):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_F3):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_F4):
            if(event.ControlDown() and event.AltDown()):
                pass 
            if(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass
            pass  
        elif(self.keycode == wx.WXK_F5):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_F6):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_F7):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass 
        elif(self.keycode == wx.WXK_F8):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_F9):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_F10):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_F11):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_F12):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass 
            pass 
        elif(self.keycode == wx.WXK_F12):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass 
            pass
        elif(self.keycode == wx.WXK_WINDOWS_LEFT):
            pass 
        elif(self.keycode == wx.WXK_WINDOWS_RIGHT):
            pass 
        elif(self.keycode == wx.WXK_WINDOWS_MENU):
            pass 
        elif(self.keycode == wx.WXK_PRINT):
            pass 
        elif(self.keycode == wx.WXK_SELECT):
            pass 
        elif(self.keycode == wx.WXK_PAGEDOWN):
            pass 
        elif(self.keycode == wx.WXK_PAGEUP):
            pass 
        elif(self.keycode == wx.WXK_SCROLL):
            pass 
        elif(self.keycode == wx.WXK_SNAPSHOT):
            pass 
        elif(self.keycode == wx.WXK_RETURN):
            pass 
        elif(self.keycode == wx.WXK_ESCAPE):
            pass 
        elif(self.keycode == wx.WXK_DELETE):
            pass 
        elif(self.keycode == wx.WXK_HOME):
            pass 
        elif(self.keycode == wx.WXK_RETURN):
            pass 
        elif(self.keycode == wx.WXK_ALT):
            print "ALT HAS BEEN PRESSED "
            pass 
        elif(self.keycode == wx.WXK_CONTROL):
            print "CTRL HAS BEEN PRSSE"
            pass 
        elif(self.keycode == wx.WXK_SHIFT):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_NUMPAD_DIVIDE):
            pass 
        elif(self.keycode == wx.WXK_NUMPAD_DECIMAL):
            pass 
        elif(self.keycode == wx.WXK_NUMPAD_SUBTRACT):
            pass 
        elif(self.keycode == wx.WXK_NUMPAD_SEPARATOR):
            pass 
        elif(self.keycode == wx.WXK_NUMPAD_ADD):
            pass 
        elif(self.keycode == wx.WXK_NUMPAD_MULTIPLY):
            pass 
        elif(self.keycode == wx.WXK_NUMPAD_EQUAL):
            pass 
        elif(self.keycode == wx.WXK_NUMPAD_DELETE):
            pass 
        elif(self.keycode == wx.WXK_NUMPAD_INSERT):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL1):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL2):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL3):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL4):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL5):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL6):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL7):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL8):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL9):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL10):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL11):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL12):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL13):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL14):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL15):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL16):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL17):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL18):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL19):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL20):
            pass 
        else:
            event.Skip()
            pass
                 
    def laylabels(self):
        """create sizers and then just lay
           with appropriate labels with there appropirate
           sizers
        """
        self.sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_1.Add(self.name)
        
        self.sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_2.Add(self.version)
        
        self.sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_3.Add(self.release_status)
        
        #self.sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        #self.sizer_4.Add(self.developers)
        
        #add all the sizers to the main sizer
        self.mainsizer.Add(self.sizer_1)
        self.mainsizer.Add(self.sizer_2)
        self.mainsizer.Add(self.sizer_3)
        #self.mainsizer.Add(self.sizer_4)
        
        #set the sizer
        self.SetSizer(self.mainsizer)
        self.Layout()
       
    def OnTimer(self, event):
        """timer event called every time
        """
        event.Skip()
        
    def OnPaint(self, event):
        """called whenever there is a need to
        paint the frame
        """
        self.DC = wx.PaintDC(self) #paint dc event
        
        self.size = self.GetClientSize()
        
        if(self.DrawGradient(self.DC, self.size.width, self.size.height) == None):
            #we don't have any working rect
            return None # we could do something like this event.Skip()
        
    def DrawGradient(self, DC, w, h):
        """
        given the DrawContext(DC) and the Height & width
        draw the entire panel with gradient
        """
        self.y = 0
        self.x = 0
        #create a graphcis context from the Given PaintDC
        #the graphicscContext enables us perform some advanced
        #drawing like creating gradient brush and pens
        self.GC = wx.GraphicsContext.Create(DC) 
        
        #grab the underlaying system colour schem
        self.sys_setting = wx.SystemSettings
        #get the working rect, but we have w, h
        self.working_rect = self.GetClientRect()
        if(not self.working_rect):
            #we don't have any drawing area yet
            return None 
            
        self.sys_color = self.sys_setting.GetColour(wx.SYS_COLOUR_CAPTIONTEXT) #used for drawing text
        
        #greate a linear gradient brush
        self.linear_gradient_brush = self.GC.CreateLinearGradientBrush(10,810,0,0, "#4D4D4D", '#FFFFFF')
        self.GC.SetBrush(self.linear_gradient_brush)
        
        #draw the rectangle on the entire client area
        self.GC.DrawRectangle(self.x, self.y, self.working_rect.width, self.working_rect.height)
        
    def OnEraseBackground(self, event):
        """
        leave this event emptry to avoid redraw of the entire
        panel
        """
        pass 
        
class SideControlPanel(wx.Panel):
    """
    object to hold the side on the client screen
    controller
    """
    def __init__(self, *args, **kwargs):
        super(SideControlPanel, self).__init__(*args, **kwargs)
        
        self.initialize_cursor()
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        #attributes
        self.initPanel()

    def initialize_cursor(self):
        self.cursor = wx.StockCursor(wx.CURSOR_BLANK)
        self.SetCursor(self.cursor)
        
    def OnMotion(self, event):
        event.Skip()
        
    def initPanel(self):
        """
        run during panel initialization
        by the parent
        """
        self.mainsizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.mainsizer)
        self.initWidget()
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyPresses)
    
    def OnKeyPresses(self, event):
        self.keycode = event.GetKeyCode()
        if(self.keycode == wx.WXK_LEFT):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass 
            pass
        elif(self.keycode == wx.WXK_F1):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass 
            pass
        elif(self.keycode == wx.WXK_F2):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_F3):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_F4):
            if(event.ControlDown() and event.AltDown()):
                pass 
            if(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass
            pass  
        elif(self.keycode == wx.WXK_F5):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_F6):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_F7):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass 
        elif(self.keycode == wx.WXK_F8):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_F9):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_F10):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_F11):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_F12):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass 
            pass 
        elif(self.keycode == wx.WXK_F12):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass 
            pass
        elif(self.keycode == wx.WXK_WINDOWS_LEFT):
            pass 
        elif(self.keycode == wx.WXK_WINDOWS_RIGHT):
            pass 
        elif(self.keycode == wx.WXK_WINDOWS_MENU):
            pass 
        elif(self.keycode == wx.WXK_PRINT):
            pass 
        elif(self.keycode == wx.WXK_SELECT):
            pass 
        elif(self.keycode == wx.WXK_PAGEDOWN):
            pass 
        elif(self.keycode == wx.WXK_PAGEUP):
            pass 
        elif(self.keycode == wx.WXK_SCROLL):
            pass 
        elif(self.keycode == wx.WXK_SNAPSHOT):
            pass 
        elif(self.keycode == wx.WXK_RETURN):
            pass 
        elif(self.keycode == wx.WXK_ESCAPE):
            pass 
        elif(self.keycode == wx.WXK_DELETE):
            pass 
        elif(self.keycode == wx.WXK_HOME):
            pass 
        elif(self.keycode == wx.WXK_RETURN):
            pass 
        elif(self.keycode == wx.WXK_ALT):
            pass 
        elif(self.keycode == wx.WXK_CONTROL):
            pass 
        elif(self.keycode == wx.WXK_SHIFT):
            if(event.ControlDown() and event.AltDown()):
                pass 
            elif(event.ControlDown()):
                pass 
            elif(event.AltDown()):
                pass 
            else:
                pass  
            pass
        elif(self.keycode == wx.WXK_NUMPAD_DIVIDE):
            pass 
        elif(self.keycode == wx.WXK_NUMPAD_DECIMAL):
            pass 
        elif(self.keycode == wx.WXK_NUMPAD_SUBTRACT):
            pass 
        elif(self.keycode == wx.WXK_NUMPAD_SEPARATOR):
            pass 
        elif(self.keycode == wx.WXK_NUMPAD_ADD):
            pass 
        elif(self.keycode == wx.WXK_NUMPAD_MULTIPLY):
            pass 
        elif(self.keycode == wx.WXK_NUMPAD_EQUAL):
            pass 
        elif(self.keycode == wx.WXK_NUMPAD_DELETE):
            pass 
        elif(self.keycode == wx.WXK_NUMPAD_INSERT):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL1):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL2):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL3):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL4):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL5):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL6):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL7):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL8):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL9):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL10):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL11):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL12):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL13):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL14):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL15):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL16):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL17):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL18):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL19):
            pass 
        elif(self.keycode == wx.WXK_SPECIAL20):
            pass 
        else:
            event.Skip()
            pass
            
    def initWidget(self):
        """make the clock"""
        #self.label_panel = LabelPanel(self, -1)
        self.c1 = ac.AnalogClock(self, size=(250,400), 
                                hoursStyle=ac.TICKS_DECIMAL,
                                minutesStyle=ac.TICKS_DECIMAL,
                                clockStyle=ac.SHOW_QUARTERS_TICKS| \
                                           ac.SHOW_MINUTES_TICKS| \
                                           ac.SHOW_HOURS_HAND| \
                                           ac.SHOW_MINUTES_HAND| \
                                           ac.SHOW_SECONDS_HAND |\
                                           ac.SHOW_HOURS_TICKS |\
                                           ac.OVERLAP_TICKS | \
                                           
                                           ac.ROTATE_TICKS)
        self.cursor = wx.StockCursor(wx.CURSOR_BLANK)
        self.c1.SetCursor(self.cursor)
        
        self.c1.SetBackgroundColour("#FFFFFF")
        self.c1.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)   
        self._dolayout()

    def  OnRightDown(self, event):
        pass  

    def _dolayout(self):
        #self.label_panel_sizer = wx.BoxSizer(wx.HORIZONTAL)
        #self.label_panel_sizer.Add(self.label_panel)
        
        self.clock_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.clock_sizer.Add(self.c1, -1, wx.EXPAND | wx.ALL,0)
        
        #add the clock_sizer, label_sizer to the main sizer
        #self.mainsizer.Add(self.label_panel_sizer, 0, wx.ALL,0)
        self.mainsizer.Add(self.clock_sizer, -1, wx.EXPAND | wx.ALL,0)

    def OnPaint(self, event):
        """
        event called whenever our object needs to be
        redrawn
        """
        self.DC = wx.PaintDC(self) #paint dc event
        
        self.size = self.GetClientSize()
        
        if(self.DrawGradient(self.DC, self.size.width, self.size.height) == None):
            #we don't have any working rect
            return None # we could do something like this event.Skip()
        
    def DrawGradient(self, DC, w, h):
        """
        given the DrawContext(DC) and the Height & width
        draw the entire panel with gradient
        """
        self.y = 0
        self.x = 0
        #create a graphcis context from the Given PaintDC
        #the graphicscContext enables us perform some advanced
        #drawing like creating gradient brush and pens
        self.GC = wx.GraphicsContext.Create(DC) 
        
        #grab the underlaying system colour schem
        self.sys_setting = wx.SystemSettings
        #get the working rect, but we have w, h
        self.working_rect = self.GetClientRect()
        if(not self.working_rect):
            #we don't have any drawing area yet
            return None 
            
        self.sys_color = self.sys_setting.GetColour(wx.SYS_COLOUR_CAPTIONTEXT) #used for drawing text
        
        #greate a linear gradient brush
        self.linear_gradient_brush = self.GC.CreateLinearGradientBrush(10,810,0,0, "#4D4D4D", '#FFFFFF')
        self.GC.SetBrush(self.linear_gradient_brush)
        
        #draw the rectangle on the entire client area
        self.GC.DrawRectangle(self.x, self.y, self.working_rect.width, self.working_rect.height)
        
    def OnEraseBackground(self, event):
        """
        leave this event emptry to avoid redraw of the entire
        panel
        """
        pass 
