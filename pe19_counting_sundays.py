# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

days_of_months = {1:31, 2:0, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11: 30, 12:31}

def feb_days(year):
    if year % 4 == 0 :
        if year % 100 == 0 and year % 400 != 0:
            return 28
        else:
            return 29
    else:
        return 28

def increment_month(month):
    if month == 12:
        return 1
    else:
        return month + 1

def get_days_of_month(month, year):

    day_of_month = days_of_months[month]
    if day_of_month == 0:
        day_of_month = feb_days(year)
    return day_of_month

def count_sundays():
    # 7 Jan 1900 = Sunday 
    day = 6
    month = 1
    year = 1901
    # dow = 1
    first_sundays = 0
    first_sundays_per_year = 0
    days_of_month = get_days_of_month(month, year)
    while year < 2001:
        if day == 1:
            first_sundays += 1
            first_sundays_per_year += 1
        print(f"{year = } {month = } {day = }")
        #increment date by a week
        day += 7 # add 7 days
        if day > days_of_month:
            extra_days = day - days_of_month
            month = increment_month(month)
            if month == 1:
                # print(f"{year} Sundays = {first_sundays_per_year}")
                year += 1
                first_sundays_per_year = 0
            days_of_month = get_days_of_month(month, year)
            day = extra_days
            print(f"{year} {month} {day}")

    return first_sundays





if __name__ == "__main__":
    sun_count = count_sundays()
    print(f"{sun_count = }")
    # print(days_of_months[12])
    print(feb_days(2000))
    print(feb_days(1900))
    # print(feb_days(1999))
    print(feb_days(1996))
    