import re

dataRe = re.compile(r"([0-3]\d)/([0|1]\d)/([1|2]\d{3})")
mo = dataRe.search("Tu madre nació en 26/02/1927")

day = int(mo.group(1))
month = int(mo.group(2))
year = int(mo.group(3))

leapYears = []
months30 = [2, 4, 6, 9, 11]


def isValidDate():
    if (
        year % 4 == 0
        and not year % 100 == 0
        or year % 4 == 0
        and year % 100 == 0
        and year % 400 == 0
    ):
        leapYears.append(year)

    if month in months30 and day in range(0, 31):
        if (
            month == 2
            and day in range(0, 29)
            or month == 2
            and day in range(0, 30)
            and year in leapYears
            or month != 2
        ):
            return True
    elif month not in months30 and day in range(0, 32):
        return True

    else:
        return False


if isValidDate() == True:
    print(mo.group(0) + " is a valid date")
else:
    print(mo.group(0) + " is not a valid date")
