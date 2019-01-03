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

######

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

##holidaysVariables = [["New Year's Day", NewYears],
##                     ["Martin Luther King, Jr. Day", MLKDay]
##                     ]

holidaysData = [["New Year's Day", "Fixed", datetime.date(now.year, 1, 1), "Closed"],
                ["Martin Luther King, Jr. Day", "Variable", 'January', 'Monday', 3, "Closed"],
                ["President's Day", "Variable", 'February', 'Monday', 3, "Closed"],
                ]

def floatingHoliday(holidayMonth, holidayWeekday, holidayWeekdayCount):
    i = 1
    for j in range(1,monthsInYear[holidayMonth][0]):
        fullDate = datetime.date(now.year, monthsInYear[holidayMonth][1], j)
        weekdayInt = datetime.date(now.year, monthsInYear[holidayMonth][1], j).weekday()
        if weekdayInt == 0:
            if i == holidayWeekdayCount:
                marketHolidays.append(fullDate)
            i+=1


for x in range(0,3):
    if holidaysData[x][1] == "Fixed":
        marketHolidays.append(holidaysData[x][2])
    else:
        floatingHoliday(holidaysData[x][2],holidaysData[x][3],holidaysData[x][4])

print(marketHolidays)



##15 January 2018 
##Martin Luther King, Jr. Day 
##Closed 
##19 February 2018 
##President's Day 
##Closed 
##30 March 2018 
##Good Friday 
##Closed
##28 May 2018 
##Memorial Day 
##Closed 
##3 July, 2018 
##Early Market Close 
##1:00 PM EST 
##4 July 2018 
##Independence Day (Observed) 
##Closed 
##3 September 2018 
##Labor Day 
##Closed 
##22 November 2018 
##Thanksgiving Day	Closed 
##23 November 2018 
##Early Market Close 
##1:00 p.m. EST
##24 December 2018 
##Christmas Eve -- Early Market Close 
##1:00 p.m. EST
##25 December 2018 
##Christmas Day (Observed) 
##Closed


##datetime_object = datetime.date(now.year, 12, 21)
##print(datetime_object)
##
##holidays = []
##
##months = ['January','February','March','April', 'May','June', 'July', 'August', 'September', 'October', 'November', 'December']

#https://www.wikiwand.com/en/Federal_holidays_in_the_United_States#/List_of_federal_holidays
#See floating Days


