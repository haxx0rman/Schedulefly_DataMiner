
import datetime
def tiem(month, day, year):
    day = {"month": 11, "day": day, "year": year}
    diy = 365
    day1 = "saturday"
    dow = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
    leapdays = int(year/4)
    leap = True if year % 4 == 0 else False

    if leap:
        diy = 366

    months = { 1: "jan",
               2: "feb",
               3: "mar",
               4: "apr",
               5: "may",
               6: "jun",
               7: "jul",
               8: "aug",
               9: "sep",
               10: "oct",
               11: "nov",
               12: "dec"
              }

    dom = {
        "jan": 31,
        "feb": 29 if leap else 28,
        "mar": 31,
        "apr": 30,
        "may": 31,
        "jun": 30,
        "jul": 31,
        "aug": 31,
        "sep": 30,
        "oct": 31,
        "nov": 30,
        "dec": 31
    }

    dom_rev = {
        "dec": 31,
        "nov": 30,
        "oct": 31,
        "sep": 30,
        "aug": 31,
        "jul": 31,
        "jun": 30,
        "may": 31,
        "apr": 30,
        "mar": 31,
        "feb": 29 if leap else 28,
        "jan": 31
    }

    cal = []
    while True:
        print(day)
        if day["day"] < dom[months[day["month"]]]:
            day["day"] = day["day"] + 1

        elif day["day"] == dom[months[day["month"]]]:

            if day["month"] < 12:
                day["day"] = 1
                day["month"] = day["month"] + 1
            elif day["month"] == 12:
                day["month"] = 1
                day["day"] = 1
                day["year"] = day["year"] + 1

        if day["year"] > 2020:
            break





#tiem(11, 16, 2015)
gay = 1

gay += 1

# print(datetime.date(2002, 12, 4).weekday())
print(gay)


# day = int((2013 * 365.25) % 7)
# dow = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
# print(dow[day])
# print(day)
