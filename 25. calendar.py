import calendar

# calendar.prmonth(theyear=2020, themonth=7)
c = calendar.TextCalendar(calendar.MONDAY)



for i in c.itermonthdates(year=2020, month=7):
    print(i.day)
