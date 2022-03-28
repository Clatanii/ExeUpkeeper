import psutil
import time
import os

exes = ["test1", "test1"]
program_dirs = ["test1.exe", "test2.exe"]

def checkIfProcessRunning(processName):
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

while True:
    for program in exes:
        if not checkIfProcessRunning(program):
            print("Program " + program + " was seen offline. Rebooting .exe file.")
            os.startfile(program_dirs[exes.index(program)])

    time.sleep(30)