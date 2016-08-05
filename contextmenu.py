#  contextmenu.py
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
import wx
from jetclient  import confighandler 
import configobj 
import config 

def getconfigs():
    """
    open the config file and return a configobj
    """
    try:
        path = confighandler.getconfigurations()
        return configobj.ConfigObj(path)
    except:
        raise 
        
class PopupMenu(wx.Menu):
    def __init__(self, parent):
        super(PopupMenu, self).__init__()
        
        self.parent = parent 
        
        self.init_menu()
        
        
    def init_menu(self):
        """
        initialize the menus
        """
        self.sethostname = wx.MenuItem(self, wx.NewId(), "Set hostname")
        self.AppendItem(self.sethostname)
        self.Bind(wx.EVT_MENU, self.OnSethostname, self.sethostname)
        
        self.sethostport = wx.MenuItem(self, wx.NewId(), "Set Hostport")
        self.AppendItem(self.sethostport)
        self.Bind(wx.EVT_MENU, self.OnSetHostPort, self.sethostport)
        
        self.restart = wx.MenuItem(self, wx.NewId(), "Close")
        self.AppendItem(self.restart)
        self.Bind(wx.EVT_MENU, self.OnRestart, self.restart)
        
        self.sendmsg = wx.MenuItem(self, wx.NewId(), "Send Msg")
        self.AppendItem(self.sendmsg)
        self.Bind(wx.EVT_MENU, self.OnSendMSG, self.sendmsg)
        
    
            
    #----defining the event callbacks-----#
    def OnSethostname(self, event):
        """
        event triggered when set hostname menu is triggered
        """
        self.box = wx.TextEntryDialog(None, "Set Hostname Defaults to localhost","Set New Servername", 'localhost')
        #self.box.ShowModal()
        if(self.box.ShowModal() == wx.ID_CANCEL):
            print "cancelling"
        else:
            if(self.box.GetValue() == ' '):
                print "Nothing"
            else:
                self.config = getconfigs()
                self.config["hostname"]=self.box.GetValue()
                self.config.write()
               
    def OnSetHostPort(self, event):
        """
        event triggered when sethostport is triggered
        """
        self.box = wx.TextEntryDialog(None, "Set Hostport or Defaults to localhost","Set New Serverportname", '5120')
        if(self.box.ShowModal() == wx.ID_CANCEL):
            print "cancelling"
        else:
            if(self.box.GetValue() == ' '):
                print "Nothing"
            else:
                self.config = getconfigs()
                self.config["portname"]=self.box.GetValue()
                self.config.write()
           
    def OnRestart(self, event):
        """
        event triggered when restart is envoked
        """
        event.Skip()
        
    def OnSendMSG(self, event):
        """
        event triggered when send msg is called
        """
        event.Skip()
        
