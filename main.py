import psutil
from datetime import datetime
import time

if __name__ == '__main__':
    while(True):
        time.sleep(5)
        print("Searching for the process...")
        pidsList = psutil.pids()
        procPid = 'notFound'

        client_proc_name = 'cymbus.exe'
        
        for pid in pidsList:
            try:
                p = psutil.Process(pid)
                if(p.name() == client_proc_name):
                    print("Process Found!")

                    if(procPid != 'notFound'):
                        print("WARNING: Multiple instances of " + client_proc_name + " found! May test the incorrect one...")
                        print(datetime.now().strftime('%d.%b.%Y_%I.%M.%S%p'))
                        if(proc.memory_percent() < p.memory_percent()):
                            procPid = pid
                            proc = p
                    else:
                        procPid = pid
                        proc = p

            except:
                print("Bypassing Access Exception...")