import datetime

order_type = {
    "E": 1,
    "Q": 3,
    "N": 7,
    "F": 14
}

def leap_year(y):
    y = y - 543
    if not y%400 or (y%4==0 and y%100!=0):
        return True
    else:
        return False

total = []

while(1):
    n = input()
    if n == "END":
        break
    order_no, _type, date, month, year = n.split()
    yon = [4, 6, 9, 11]
    if int(year) < 2558:
        print("Error: {} --> Invalid year".format(''.join(n)))
    elif int(month) < 0 or int(month) > 12:
        print("Error: {} --> Invalid month".format(''.join(n)))
    elif (int(month) in yon and int(date) > 30) or (not leap_year(int(year)) and int(date) == 29 and int(month) == 2) or (int(month) == 2 and int(date) > 29) or (int(date) > 31 or int(date) < 1):
        print("Error: {} --> Invalid date".format(''.join(n)))
    elif not _type in order_type:
        print("Error: {} --> Invalid delivery type".format(''.join(n)))
    else:
        date_format = datetime.datetime.strptime("{} {} {}".format(date, month, year), '%d %m %Y')

        delivery_date = date_format + datetime.timedelta(days=order_type[_type])
        total.append([order_no, delivery_date])

total.sort()
total.sort(key=lambda x:x[1])

for i in total:
    print("{}: delivered on {}".format(i[0], datetime.datetime.strftime(i[1], "%e/%m/%Y").replace('/0', '/').replace(' ', '')))