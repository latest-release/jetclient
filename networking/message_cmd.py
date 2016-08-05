#  message_cmd.py
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
import string 


def make_protocol_commands(*args):
    """
    make and return protocl commands
    """ 
    command_list = []
    if(args):
        for arg in args:
            if "/" in arg:
                command_list.append(arg)
            args = "/" + arg
            command_list.append(args)
    else:
        #build commands
        cmd = ["/time", "/sub", "/ticket", "/reboot", "/shutdown", "/lock", 
               "/reserve", "/cmd"]
               
        for cmds in cmd:
            command_list.append(cmds)
    return command_list
    

def manipulate_cmd(cmd):
    """
    check for the message and perform
    some kind of replacement
    
    >>>
    >>> import message_cmd
    
    >>> t = "/time 10"
    >>> print message_cmd.manipulate_cmd(t)
     10
    >>> t = "/ticket adak12"
    >>> print message_cmd.manipulate_cmd(t)
     adak12
    >>>
    """
    cmds = make_protocol_commands()
    for cmd_s in cmds:
        if(cmd_s in cmd):
            if(cmd == "/shutdown"):
                return string.replace(cmd, "/", '', 1)
            elif(cmd == "/reboot"):
                return string.replace(cmd, "/", '', 1)
            elif(cmd ==  "/lock"):
                return string.replace(cmd, "/", '', 1)
            else:
                new_cmd = string.replace(cmd, cmd_s, "",1)


