#Get market holiday dates
#Get market hours of operations
#For market hours of operations except holidays and weekends schedule execution every 5 minutes

##from datetime import datetime
##from pytz import timezone, common_timezones
##
##
##tz = timezone('EST')
##tz = timezone('US/Hawaii')
##print(datetime.now(tz))
##print(common_timezones)

marketHolidays = []
dayOccurences = []

import datetime

#get year

now = datetime.datetime.now()

MLKDay = datetime.date(now.year, 1, 1)

#check if leap year
if not(int(now.year) % 4 == 0):
    print(str(now.year) + " Common Year")
    febDays = 28
elif not(int(now.year) % 100 == 0):
    print(str(now.year) + " Leap Year")
    febDays = 29
elif not(int(now.year) % 400 == 0):
    print(str(now.year) + " Common Year")
    febDays = 28
else:
    print(str(now.year) + " Common Year")
    febDays = 28

##### Determine holidays

daysInWeek = ["Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
        ]

monthsInYear = {'January': [31, 1],
                'February': [febDays, 2],
                'March': [31, 3],
                'April': [30, 4],
                'May': [31, 5],
                'June': [30, 6],
                'July': [31, 7],
                'August': [31, 8],
                'September': [30, 9],
                'October': [31, 10],
                'November': [30, 11],
                'December': [31, 12]
                }

holidaysData = [["New Year's Day", "Fixed", datetime.date(now.year, 1, 1), "Closed"],
                ["Martin Luther King, Jr. Day", "Variable", 'January', 'Monday', 3, "Closed"],
                ["President's Day", "Variable", 'February', 'Monday', 3, "Closed"],
                #["Good Friday", "Variable", '', '', 0, "Closed"],
                ["Memorial Day", "Variable", 'May', 'Monday', -1, "Closed"],
                ["Independence  Day", "Fixed", datetime.date(now.year, 7, 4), "Closed"],
                ["Labor  Day", "Variable", 'September', 'Monday', -2, "Closed"],
                ["Thanksgiving", "Variable", 'November', 'Thursday', 4, "Closed"],
                ["Christmas", "Fixed", datetime.date(now.year, 12, 25), "Closed"]
                ]

def floatingHoliday(holidayMonth, holidayWeekday, holidayWeekdayCount):
    i = 1
    for j in range(1,monthsInYear[holidayMonth][0]+1):
        fullDate = datetime.date(now.year, monthsInYear[holidayMonth][1], j)
        weekdayInt = datetime.date(now.year, monthsInYear[holidayMonth][1], j).weekday()
        if weekdayInt == daysInWeek.index(holidayWeekday):
            if i == holidayWeekdayCount:
                marketHolidays.append(fullDate)
            if -1 == holidayWeekdayCount:
                dayOccurences.append(fullDate)
            if -2 == holidayWeekdayCount:
                marketHolidays.append(fullDate)
                break
            i+=1
        if -1 == holidayWeekdayCount and j == monthsInYear[holidayMonth][0]:
            marketHolidays.append(dayOccurences[len(dayOccurences)-1])
            dayOccurences.clear()


for x in range(0,8):
    if holidaysData[x][1] == "Fixed":
        #If the holiday falls on a Saturday, the market will close on the preceding Friday.
        if holidaysData[x][2].weekday() == 5:
            marketHolidays.append((holidaysData[x][2]) + datetime.timedelta(days=-1))
        #If the holiday falls on a Sunday, the market will close on the subsequent Monday.
        if holidaysData[x][2].weekday() == 6:
            marketHolidays.append((holidaysData[x][2]) + datetime.timedelta(days=1))
        else:
            marketHolidays.append(holidaysData[x][2])
    else:
        floatingHoliday(holidaysData[x][2],holidaysData[x][3],holidaysData[x][4])

print(marketHolidays)

