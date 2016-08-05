#  communication.py
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
"""
---file:communication.py
   Basically what this file does is just manage the communication 
   between the GUI code and the networking. For example a message
   sent when we are connected to the server. When a message is reeived
   from the server. and when a disconnected on the server End.
   
   This Also helps with the responsiveness of our gui not super
   freezy. And attempting to hide the networking code from the
   GUI code and the same.
---
"""

import wx
import string 
import time 

class  Communication(object):
    """
    object to hold the messages from the networking.
    and then push them to the gui thread. when approriate
    event handler is triggered.
    """
    
    def __init__(self, wx_displaylog, wx_connected, wx_datareceived, wx_disconnected, wx_reconnect ):
        
        """
        @param: wx_connected--> Triggered when we are connected to the server
        @param: wx_datareceied--> There is some data to be processed from server
        @param: wx_disconnected--> When either the server has shutdown.
        @param: wx_reconnect --> When we are disconnected from the server. we might
                                 perform a reconnection back.
                                 
        """
        self.wx_connected = wx_connected 
        self.wx_datareceived = wx_datareceived
        self.wx_disconnected = wx_disconnected
        self.wx_reconnect = wx_reconnect
        self.wx_displaylog = wx_displaylog 
        
    def connected(self):
        """
        send a notification to the GUI that we area connected
        """
        wx.CallAfter(self.wx_connected)
        
    def datareceived(self, data):
        """
        notify the GUI that we have some data received
        """
        wx.CallAfter(self.wx_datareceived, data)
        
    def disconnected(self, last_data):
        """
        notify the GUI that we have lost connection
        or we could not connect
        """
        wx.CallAfter(self.wx_disconnected, last_data)
        
    def reconnect(self, server):
        """
        Notify the GUI that wer have been disconnected
        and request a reconnect back to the server
        """
        #NOTE: this operation could have been done on the disconcted
        #function. But for convience as we have to reinitilize the
        #sock to perform connections.
        wx.CallAfter(self.wx_reconnect, server)
        
    def displaylog(self, log):
        """
        Display some log information to the console
        """
        wx.CallAfter(self.wx_displaylog, log)
        
