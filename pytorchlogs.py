
import os
import io
import threading
import time
from contextlib import redirect_stdout

#Size of the file
MAX_FILE_SIZE =  1 * 1024 * 1024 
        
#Main method`
def main():
    #Initialize
    lgc = LogClass()  

    #Start logging
    lgc.start_logging()

    while True:
        print("In sleep ")
        time.sleep(60)


class LogClass:
    #Init
    def __init__(self):
        #lets start a 1min timer
        logtimer = threading.Timer(60.0, self.checklogssize)
        #Open MIOpen log file
        logfp = open("miopen_nan.log", "a")
        #size
        sz = 0

    #Init logging
    def start_logging(self):
        #start logign for system logs
        self.system_logs()
        #start logging for pytorch tests
        self.pytorchtests()

    def system_logs(self):
        #start system logs
        print(" Calling the system logs shell script ")
        os.system('./rocm_techsupport.sh >&systemlogs.log')

    def pytorchtests(self):
        print("Collecting MIOpen logs")
        redirect_stdout(logfp) 
        redirect_stderr(logfp) 

    #Check Log Size
    def checklogssize(self):
        #Size of the file
        self.sz = Path('miopen_nan.log').stat().st_size
        #Check if the size is less than MAX size
        if( self.sz > MAX_FILE_SIZE):
            #close the miopen file
            logfp.close()
            #move the contents to another file
            os.system('mv miopen_nan.log miopen_nan.log.old')
            #open the file again
            self.logfp = open("miopen_nan.log")

if __name__ == "__main__":
    main()

