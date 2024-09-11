def is_leap_year(year):
    if year % 4 != 0:
        print(year, "- не високосный год")
    elif year % 100 == 0:
        if year % 400 == 0:
            print(year, "- високосный год")
        else:
            print(year, "- не високосный год")
    else:
        print(year, "- високосный год")
