import subprocess
import os
#import win32com.shell.shell as shell
import ctypes, sys
from datetime import datetime

dir_win_collectors = os.getcwd()
dir_wire_shark = 'C:\\Program Files\\Wireshark'
now = datetime.now()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


# Tshark
def tshark_runner(duration=5):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d-%H%M")
    
    if (os.path.exists(dir_wire_shark)):

        proc = subprocess.run('tshark -D', shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        output = proc.stdout

        output_list = output.splitlines()


        for item in output_list:
            if ("Ethernet" in item):
                netint = item[0]
            elif ("Wireless" in item):
                netint = item[0]

        
        p0 = subprocess.run('tshark -i {} -w {}\\data\\TSHARK\\{}_capture.pcap -a duration:{}'.format(netint, dir_win_collectors, dt_string, duration))
        if(p0.returncode == 0):
            print("tshark complete")
        else:
            print("Error with Tshark")
    else:
        print("Check Wireshark Installation Directory")



def eventLogs(duration=24, logType='System'):
    dt_string = now.strftime("%Y-%m-%d-%H%M")
    
    if(logType == 'System' or 'Application' or 'Security'):
        p1 = subprocess.run("powershell.exe Get-EventLog {} -After (Get-Date).AddHours(-{}) | ConvertTo-HTML | Out-File {}\\data\\EVENTLOGS\\{}_Event_Logs-{}.htm".format(logType, duration, dir_win_collectors, logType, dt_string))
        if(p1.returncode == 0):
            print("Event Logs complete")
        else:
            print("Error with Event Logs")
    else:
        print("Please input valid event log name (System, Application, Security")
    

if is_admin():
    
    # p2 = subprocess.run(["C:\\Users\\User\\Desktop\\eventlogs\\procmonScript.bat"], shell=False)
    tshark_runner()
    eventLogs(24,"System")
else:
    # rerun program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)








