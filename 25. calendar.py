import calendar

# calendar.prmonth(theyear=2020, themonth=7)
c = calendar.TextCalendar(calendar.MONDAY)

# print(check_month(2020, 7))


# for i in c.itermonthdates(year=2020, month=7):
#     print(i.day)


# li = []
# # print(type(c.itermonthdays(year=2020, month=7)))
# for i in c.itermonthdays(year=2020, month=7):
#     if i > 27:
#         li.append(i)


def check_month(year, month):
    # задаем список для проверки последних дней месяца
    c = calendar.TextCalendar(calendar.MONDAY)
    check_list = []
    # print(type(c.itermonthdays(year=2020, month=7)))
    for i in c.itermonthdays(year=year, month=month):
        if i > 0:
            check_list.append(i)

        # check_list.append(i)
    return check_list


print(check_month(2020, 7))
