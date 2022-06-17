import random

gender = str(input("Man eller Kvinna?: "))

if gender == "Man":
    kon = random.randrange(103, 999, 2)
else:
    pass

if gender == "Kvinna":
    kon = random.randrange(102, 998, 2)
else:
    pass

year = (random.randrange(1950, 2001))

year2 = str(year)[2:4]

month = (random.randrange(1, 12))

day = (random.randrange(1, 30))

if month < 10:
    month = "0" + str(month)
else:
    pass

if day < 10:
    day = "0" + str(day)

if month == 2:
    day = day - 2
else:
    pass

print()

print(year, month, day)

pernum = str(year2), str(month), str(day), str(kon)

yearNum1 = str(year)[2]
yearNum2 = str(year)[3]
monthNum1 = str(month)[0]
monthNum2 = str(month)[1]
dayNum1 = str(day)[0]
dayNum2 = str(day)[1]
konNum1 = str(kon)[0]
konNum2 = str(kon)[1]
konNum3 = str(kon)[2]

yearNum11 = int(yearNum1) * 2
yearNum22 = int(yearNum2) * 1
monthNum11 = int(monthNum1) * 2
monthNum22 = int(monthNum2) * 1
dayNum11 = int(dayNum1) * 2
dayNum22 = int(dayNum2) * 1
konNum11 = int(konNum1) * 2
konNum22 = int(konNum2) * 1
konNum33 = int(konNum3) * 2

if yearNum11 >= 10:
    yearNum11 = int(str(yearNum11)[0]) + int(str(yearNum11)[1])
else:
    pass

if monthNum11 >= 10:
    monthNum11 = int(str(monthNum11)[0]) + int(str(monthNum11)[1])
else:
    pass

if dayNum11 >= 10:
    dayNum11 = int(str(dayNum11)[0]) + int(str(dayNum11)[1])
else:
    pass

if konNum11 >= 10:
    konNum11 = int(str(konNum11)[0]) + int(str(konNum11)[1])
else:
    pass

if konNum33 >= 10:
    konNum33 = int(str(konNum33)[0]) + int(str(konNum33)[1])
else:
    pass

summ = int(yearNum11) + int(yearNum22) + int(monthNum11) + int(monthNum22) + int(dayNum11) + int(dayNum22) + int(
    konNum11) + int(konNum22) + int(konNum33)

summ2 = int(str(summ)[1])

kontroll = 10 - summ2

personNum = str(year2) + str(month) + str(day) + "-" + str(kon) + str(kontroll)

personNum2 = str(year) + str(month) + str(day) + "-" + str(kon) + str(kontroll)

print()

print(personNum)

print()

print(personNum2)

input()
