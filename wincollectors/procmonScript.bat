set PM=C:\Users\User\Desktop\Procmon\Procmon64
start %PM% /quiet /minimized /backingfile C:\Users\User\Desktop\eventlogs\data\test.pml
%PM% /waitforidle
start /wait notepad.exe
%PM% /terminate