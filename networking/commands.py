#  commands.py
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

import string 
from wx.lib.pubsub import Publisher as Publisher

#let the dictionary be global for easy acces
#but dangerous for easy modification by multiple threads.
cmd_dict = { }

def insert_dictcomands(command, description):
    """
    inserts the given commands into the
    dictionary associating it with the
    given description.
    """
    global cmd_dict
    
    #first check if the command already exists
    if(not len(cmd_dict)):
        #dick it emptry
        return -1
    else:
        if(cmd_dict.get(command)):
            return -2 #already exists 
        else:
            #Insert
            #but first ensure it has values
            if(not(len(str(command)))):
                return False 
                
            cmd_dict[command]=description
    
    #return the dictionary
    return cmd_dict 
             
def publisher(listener, message, data):
    """
    publish the given mesage to
    the given listerner if she/he
    is listening.
    """
    try:
        Publisher.sendMessage(listener, data=data)
    except:
        raise 
    else:
        return True 
        
def translate_protocol(msg):
    """
    given the message check and verify if
    it belongs to some of our known
    networking protocols.
    """
    prefix = "/" #command from server start with "/"
    
    if(msg.startswith(prefix+"time")):
        #the user is being given time
        time = string.replace(msg, prefix+"time", "",1)
        
        #call the publisher to send
        publisher("newSessionReceived", message=None, data=time)
        
    elif(msg.startswith(prefix+"minus")):
        #deduct the user time
        deduct = string.replace(msg, prefix+"minus", "", 1)
        
        publisher("deductClientime", message=None, data=deduct)
        
    elif(msg.startswith(prefix+"ticket")):
        #ticket received
        ticket = string.replace(msg, prefix+"ticket", "",1)
        publisher("handleTicket", message=None, data=ticket)
        
    elif(msg.startswith(prefix+"reboot")):
        reboot = string.replace(msg, prefix+"reboot", "",1)
        publisher("rebootClient", message=None, data=time)
        
    elif(msg.startswith(prefix+"shutdown")):
        shutdown = string.replace(msg, prefix+"shutdown", "",1)
        publisher("shutdownClient", message=None, data=shutdown)
        
    elif(msg.startswith(prefix+"cmd")):
        cmds = string.replace(msg, prefix+"cmd", "",1)
        publisher("runExternalCMD", message=None, data=cmds)
        
    elif(msg.startswith(prefix+"lock")):
        lock = string.replace(msg, prefix+"lock", "", 1)
        publisher("lockScreen", message=None, data=lock)
        
    elif(msg.startswith(prefix+"endpeer")):
        lock = string.replace(msg, prefix+"endpeer", "", 1)
        publisher("EndPeerSession", message=None, data=lock)
        
    elif(msg.startswith(prefix+"reserve")):
        reserve = string.replace(msg, prefix+"reserve", "", 1)
        publisher("reserveNeeded", message=None, data=reserve)
        
    elif(msg.startswith(prefix+"broadcasted")):
        receive_broadcast = string.replace(msg, prefix+"broadcasted", "", len(msg))
        publisher("NewBroadcast", message=None, data=receive_broadcast)
        
    elif(msg.startswith(prefix+"pause")):
        print "It is a pause"
        receive_broadcast = string.replace(msg, prefix+"pause", "", len(msg))
        publisher("PauseSession", message=None, data=receive_broadcast)
        
    elif(msg.startswith(prefix+"resume")):
        print "it is a resume"
        receive_broadcast = string.replace(msg, prefix+"resume", "", len(msg))
        publisher("ResumeSession", message=None, data=receive_broadcast)
        
    else:
        #probably it's not a special command
        publisher("messageFromServer", message=msg, data=msg)
        

def translate_ticket(ticket):
    """
    A function which translate the given
    ticket into appropriate time.
    """
    try:
        if(len(ticket)):
            try:
                ticket = ticket
                value = ticket.replace("ticket", "", len(ticket))
                if(value):
                    try:
                        if("15" in value):
                            return 15
                        elif("30" in value):
                            return 30
                        elif("1hr" in value):
                            return 60
                        elif("2hrs" in value):
                            return 120
                        elif("windup" in value):
                            return 5
                        else:
                            return None 
                    except:
                        raise 
                else:
                    return False 
            except:
                raise 
        else:
            return -1
    except:
        raise 
        
                            
