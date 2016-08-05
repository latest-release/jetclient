import wx
import math 

#self.CG.CreateLinearGradientBrush(10,810,0,0, "#4D4D4D","#FFFFFF")
#self.CG.CreateRadialGradientBrush(85,75,95-60.0, 75-60.0,115*math.pi, "#4D4D4D","#FFFFFF")

class MotionPanel(wx.Panel):
    line_x = 1
    going_left = False
    going_right = True
    
    def __init__(self, *args, **kwargs):
        super(MotionPanel, self).__init__(*args, **kwargs)
        
        self.initialize_cursor()
        
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyPresses)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        self.timer.Start(5)
        self.SetBackgroundColour("#E6E6FA")

    def initialize_cursor(self):
        self.cursor = wx.StockCursor(wx.CURSOR_BLANK)
        self.SetCursor(self.cursor)
        
    def OnMotion(self, event):
        event.Skip()
        
    def OnTimer(self, event):
        if self.line_x == self.GetSize()[1] or self.line_x==0:
            #Reverse directions
            self.going_left = not self.going_left
            self.going_right = not self.going_right
        if self.going_left:
            self.line_x -= 1 #Go to the left
            self.Refresh()
        else:
            self.line_x += 1 #Go to the right
            self.Refresh()
         
    
    def OnPaint(self, event):
       
        self.DC = wx.PaintDC(self)
        
        self.CG = wx.GraphicsContext.Create(self.DC)
        
        #get working rect
        self.size = self.DC.GetSize()
        #self.size1 = self.GetClientSize()
        #self.DrawGradient(self.DC, self.size.width, self.size.height)
        #self.CG.SetPen(wx.Pen("#008000"))
          
        self.radius = math.pi* 40
        
        self.drawRectangle(self.CG, 0, self.line_x, 250, 250, self.radius)
        self.drawRectangle(self.CG, 270, self.line_x, 250, 250, self.radius)
        self.drawRectangle(self.CG, 560, self.line_x, 250, 250, self.radius)
        self.drawRectangle(self.CG, 840,self.line_x, 250, 250, self.radius)
        self.font = wx.Font(20, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.DC.SetFont(self.font)
        self.DC.DrawText(str(self.line_x), self.size.width/2, 120)
        self.DC.DrawText("Welcome to Jet An Ubuntu Internet Cafe", self.size.width/4, 90)
    def drawRectangle(self, CG, pos_x, pos_y, size_x, size_y, radius):
        """
        draw the rectangle
        """
        colors = ["#000000", "#7F7F7F", "#8B6914", "#90EE90"]
        #c = random.choice(colors)
        
        self.radial_brush = CG.CreateLinearGradientBrush(10,810,0,0, "#ADD8E6","#0000FF") 
        #self.radial_brush = CG.CreateLinearGradientBrush(10,810,0,0, "#ADD8E6","#800080") 
        CG.SetBrush(self.radial_brush)
        
        CG.DrawRoundedRectangle(pos_x, pos_y, size_x, size_y, self.radius)
        
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
            print "GOT KEYBOARD INTERRUPT ALT"
            pass 
        elif(self.keycode == wx.WXK_CONTROL):
            print "GOT KEYBOARD INTERUPT CTRL"
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
        self.linear_gradient_brush = self.GC.CreateLinearGradientBrush(10,810,0,0, "#800080", '#FFFFFF')
        self.GC.SetBrush(self.linear_gradient_brush)
        
        #draw the rectangle on the entire client area
        self.GC.DrawRectangle(self.x, self.y, self.working_rect.width, self.working_rect.height)
        return 
        
    def OnEraseBackground(self, event):
        """
        leave this event emptry to avoid redraw of the entire
        panel
        """
        pass
