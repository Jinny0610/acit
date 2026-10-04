import dow


def getDayOfTheWeekForUserDate():
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Date: "))

    day_of_week = dow.getDayOfTheWeek(year, month, day)
    print(f"{month}-{day}-{year} is a {day_of_week}.")


dow.makeCalendar()
getDayOfTheWeekForUserDate()