
import os
import threading

#Size of the file
MAX_FILE_SIZE   1 * 1024 * 1024 

       
        
#Main method`
def main():
    #Initialize
    lgc = LogClass()  

    #Start logging
    lgc.start_logging()


class LogClass:
    #Init
    def __init__(self):
        #lets start a 1min timer
        logtimer = threading.timer(60.0, checklogssize)
        #Open MIOpen log file
        logfp = open("miopen_nan.log")
    #Init logging
    def start_logging():
        #start logign for system logs
        system_logs()

        #start logging for pytorch tests
        pytorchtests()

    def system_logs():
        #start system logs
        print(" Calling the system logs shell script ")
        os.system('./rocm_techsupport.sh >&systemlogs.log')

    def pytorchtests():
        print("Collecting MIOpen logs")
        os.system('export MIOPEN_CHECK_NUMERICS=0x01 >&miopen_nan.log')

    #Check Log Size
    def checklogssize():
        #Size of the file
        sz = Path('miopen_nan.log').stat().st_size
        #Check if the size is less than MAX size
        if( sz > MAX_FILE_SIZE):
            #close the miopen file
            logfp.close()
            #move the contents to another file
            os.system('mv miopen_nan.log miopen_nan.log.old')
            #open the file again
            logfp = open("miopen_nan.log")


if __name__ == "__main__":
    main()


