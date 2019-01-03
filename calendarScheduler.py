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



import datetime

#get year

now = datetime.datetime.now()

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

months = [['January', 31],
          ['February', febDays],
          ['March', 31],
          ['April', 30],
          ['May', 31],
          ['June', 30],
          ['July', 31],
          ['August', 31],
          ['September',30],
          ['October', 31],
          ['November', 30],
          ['December', 31]
          ]

days = ["Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
            ]

i = 0
while i < 12:
    j = 1
    while j <= months[i][1]:
        fullDate = datetime.date(now.year, i+1, j)
        weekdayInt = datetime.date(now.year, i+1, j).weekday()
        if weekdayInt < 5:
            print(str(fullDate) + " " + days[weekdayInt])
        j += 1
    i +=1


##datetime_object = datetime.date(now.year, 12, 21)
##print(datetime_object)
##
##holidays = []
##
##months = ['January','February','March','April', 'May','June', 'July', 'August', 'September', 'October', 'November', 'December']

#https://www.wikiwand.com/en/Federal_holidays_in_the_United_States#/List_of_federal_holidays
#See floating Days


