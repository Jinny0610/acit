MONTH_CODES = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_OF_WEEK = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def getDayOfTheWeek(year, month, day):
    last_two_digits = year % 100
    how_many_twelves = last_two_digits // 12
    rem = last_two_digits % 12
    how_many_fours = rem // 4
    month_code = MONTH_CODES[month - 1]

    if 1600 <= year <= 1699:
        month_code = month_code + 6
    elif 1700 <= year <= 1799:
        month_code = month_code + 4
    elif 1800 <= year <= 1899:
        month_code = month_code + 2
    elif 2000 <= year <= 2099:
        month_code = month_code + 6
    elif 2100 <= year <= 2199:
        month_code = month_code + 4

    if isLeapYear(year) and (month == 1 or month == 2):
        month_code = month_code - 1

    total = how_many_twelves + rem + how_many_fours + day + month_code
    day_number = total % 7

    return DAYS_OF_WEEK[day_number]


def makeCalendar():
    year = 2026

    if isLeapYear(year):
        DAYS_IN_MONTH[1] = 29
    else:
        DAYS_IN_MONTH[1] = 28

    for month in range(12):
        for day in range(1, DAYS_IN_MONTH[month] + 1):
            day_of_week = getDayOfTheWeek(year, month + 1, day)

            print(f"{month + 1}-{day}-{year} is a {day_of_week}.")
    
