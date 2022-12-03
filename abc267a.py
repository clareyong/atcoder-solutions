from xmlrpc.server import SimpleXMLRPCDispatcher


day = input()
saturday = 6
weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
print(saturday - (weekdays.index(day) + 1))