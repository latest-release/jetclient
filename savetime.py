import confighandler 
import configobj
import os 

filename = "currenttime.conf"

def create_trackconf():
    """
    Write the given client time.
    """
    try:
        print "Called on runtime to create config"
        config = configobj.ConfigObj()
        config.filename = filename 
        
        foldername = confighandler.getconfiguration_dirs()
        joined_filename = os.path.join(foldername, filename)
        config.filename = joined_filename
        if(os.path.exists(joined_filename)):
            return joined_filename
        else:
            config["CURRENT_TIME"]=''
            config.write()
    except:
        raise 
        

def writetime(time):
    try:
        print "Writing on startup ", time 
        config = configobj.ConfigObj()
        config.filename = filename 
        dirname = confighandler.getconfiguration_dirs()
        
        join_dir = os.path.join(dirname, filename)
        config.filename = join_dir
        if(os.path.exists(join_dir)):
            config["CURRENT_TIME"]=str(time)
            config.write()
        else:
            create_trackconf()
    except:
        raise 
 
if __name__=="__main__":
    writetime(1011)       

