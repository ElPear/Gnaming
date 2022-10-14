import random as rnd

mode = input("generate or verify: ")

if mode.lower() == "generate":
    gender = input("Man eller kvinna: ")
else:
    gender = "not important"

year = rnd.randint(1900, 2022)
month = rnd.randint(1, 12)
lits = [1, 3, 5, 8, 9, 12]

if month in lits:
    day = rnd.randint(1, 31)
elif month == 2:
    day = rnd.randint(1, 28)
else:
    day = rnd.randint(1, 30)

if day < 10:
    day = "0"+str(day)

if month < 10:
    month = "0"+str(month)

if gender.lower() == "man":
    threeLast = rnd.randrange(1, 999, 2)
elif gender.lower() == "kvinna":
    threeLast = rnd.randrange(2, 998, 2)
else:
    threeLast = 123

if threeLast < 100:
    threeLast = "0"+str(threeLast)
elif threeLast < 10:
    threeLast = "00"+str(threeLast)

if mode.lower() == "generate":
    print(f"{year} {month} {day} {threeLast}")

year = str(year)[len(str(year))-2:]

theListOne = [str(year), str(month), str(day), str(threeLast)]

if mode.lower() == "generate":
    actualListOne = "".join(theListOne)
elif mode.lower() == "verify":
    actualListOne = input("Personnummer: ")
    lastDude = str(actualListOne)[len(str(actualListOne))-1:]
    actualListOne = actualListOne[0:len(actualListOne)-1]


processedList = ""
index = 1

for i in range(0, len(actualListOne)):
    if index % 2 != 0:
        processedList += str(2*int(actualListOne[index-1]))
    else:
        processedList += str(actualListOne[index - 1])
    index += 1

theSum = 0
index = 0
for i in range(0, len(processedList)):
    theSum += int(processedList[index])
    index += 1

theLastFuckingOne = round(theSum+5, -1) - theSum

if mode.lower() == "generate":
    personNummer = f"{year}{month}{day}-{threeLast}{theLastFuckingOne}"
    print(personNummer)

if mode.lower() == "verify":
    if str(lastDude) == str(theLastFuckingOne):
        print("valid")
    else:
        print("invalid")

