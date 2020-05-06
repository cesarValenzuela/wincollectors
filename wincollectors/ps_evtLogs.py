import subprocess
import sys
import os

path = "C:\\Users\\User\\Desktop\\eventlogs\\data\\"
path1 = os.getcwd()
print(path1)

def get_eventlogs(logType='System', duration=24):
    print(duration)
    print(logType)
    print(path)
    subprocess.Popen(["powershell.exe", "Get-EventLog {} -After (Get-Date).AddHours(-{})".format(logType, duration), "|", "ConvertTo-HTML", "|", "Out-File", f"{path1}\\data\\{logType}_Event_Logs.htm"])
    print("Done")

get_eventlogs('Application', 2)