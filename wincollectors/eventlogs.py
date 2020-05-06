import win32evtlog 
# path = 'C:\\Users\\radmin\\Desktop\\eventlogs\\data\\event-logs.txt'
path = 'event-logs.txt'

server = 'localhost'
logtype = 'System'
hand = win32evtlog.OpenEventLog(server, logtype)

flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
total = win32evtlog.GetNumberOfEventLogRecords(hand)
i = 0
while i < 2000:
    with open(path, "r+", encoding="utf-8") as file1:
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if events:
            for event in events:
                #print ('Event Category:', event.EventCategory)
                file1.write('Event Category:' + str(event.EventCategory) + "\n")

                #print ('Time Generated:', event.TimeGenerated)
                file1.write('Time Generated:'+ str(event.TimeGenerated) + "\n")

                #print ('Source Name:', event.SourceName)
                file1.write('Source Name:' + str(event.SourceName) + "\n")

                #print ('EventID:', event.EventID)
                file1.write('EventID:' + str(event.EventID) + "\n")

                #print ('Event Type:', event.EventType)
                file1.write('Event Type:' + str(event.EventType) + "\n")

                data = event.StringInserts
                if data:
                    #print ('Event Data:')
                    file1.write('Event Data:\n')
                    for msg in data:
                        #print (msg)
                        file1.write(msg)
                #print("----------------------")
                file1.write("\n\n")
        i += 1