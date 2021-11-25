from datetime import datetime

# Defines the function getTime, this function set the current time by. First the hour, then the minute and then the seconds.
def getTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time
#print (getTime())

# Defines the function getDate, returns the current date. First the the day, then the month and then the current year.
def getDate():
    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y")
    return current_time
