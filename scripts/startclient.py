#  startclient.py
#  
#  Copyright 2015 Wangolo Joel <s8software@wangolo>
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
from jetclient import app

# Initailze a function to run the client
def run_client(baseapp=None):
   """
   Runs the main client GUI.
   @ Param baseapp coresponds to the wx.app
   """
   if(baseapp):
      baseapp.MainLoop()
   else:
      # Just initialize a new one not passed.
      baseapp = app.RunApp()
      baseapp.MainLoop()

if __name__=="__main__":
   print "App can't be called from commandline"
else:
   run_client()
