
import portion
from datetime import datetime

startTimeString = input('Enter start date(YYYY-MM-DD HH:MM AM/PM): ')
endTimeString = input('Enter end date(YYYY-MM-DD HH:MM AM/PM): ')

startTime = datetime.strptime(startTimeString, '%Y-%m-%d %H:%M %p')
endTime = datetime.strptime(endTimeString, '%Y-%m-%d %H:%M %p')

def calculateDifference(startDate, endDate):
    nightHours = portion.closed(0,6)
    
    dayTime = portion.closed(startDate.replace(hour=nightHours.upper,minute=0), endDate.replace(hour=nightHours.lower,minute=0))
    nightTime = portion.closed(startDate.replace(hour=nightHours.lower,minute=0), endDate.replace(hour=nightHours.upper,minute=0))
    
    timeDifference = (endDate - startDate).total_seconds() / 3600
    if dayTime.overlaps(nightTime):
        nightOverlap = dayTime & nightTime
        overlapHours = (nightOverlap.upper - nightOverlap.lower).total_seconds() / 3600
        timeDifference -= overlapHours
    return timeDifference
        
result = calculateDifference(startTime,endTime)
print(f'Time difference after removing night-time is {result}')
