import os
import threading
import time 

def stress_server():
    """
    Execute multiple clients to connect to the server at the
    same time.
    """
    try:
        print "Hello World"
        #os.system("python app.py")
    except OSError as error:
        print error
    except:
        raise 
            
class ServerStressTestingThreads(threading.Thread):
    """
    threads will be execute to stress test the server
    with simulatenous connection.
    """
    def __init__(self, myname):
        threading.Thread.__init__(self, name=myname)
        
        self.myname = myname 
        self.time = time.asctime()
        self.run_lock = threading.Lock()
        
    def run(self):
        """
        testing threads are placed here
        """
        try:
            print "My name is", self.getName(), "Stress testing the server"
            print "My name is ", self.getName(), "I have acquired a lock"
            self.run_lock.acquire()
            stress_server()
            self.run_lock.release()
            print self.run_lock.locked()
            print "My name is ", self.getName(), "I am releasing the lock."
        except:
            raise 

def main(howmany=2):
    for i in range(0,howmany):
        stress  = ServerStressTestingThreads(i)
        stress.start()
        
if __name__=="__main__":
    main()
    
