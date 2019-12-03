import json
import requests
import time
from bs4 import BeautifulSoup

#first crib sheet
#https://m.schedulefly.com/(S(1oy5wwqntes4qsmvlvzymbmq))/crib.aspx?day=11/16/2015


class Scheduledaddy():
    def __init__(self):
        self.url = "https://m.schedulefly.com/(S(1oy5wwqntes4qsmvlvzymbmq))"
        with open('data.json') as f:
            self.data = json.load(f)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        }
        self.start()


    def start(self):
        self.loop()
        pass

    def loop(self):
        day = {"month": 9, "day": 9, "year": 2017}
        leap = True if day["year"] % 4 == 0 else False
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
        while True:
            #time.sleep(5)
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
            self.crib("{}/{}/{}".format(day["month"], day["day"], day["year"]))



    def save(self):
        with open('data.json', 'w') as outfile:
             json.dump(self.data, outfile, indent=4, sort_keys=True)
        pass

    def crib(self, date):
        page = requests.get(self.url + "/crib.aspx?day=" + date, headers = self.headers)
        soup = BeautifulSoup(page.content.decode('latin-1'), 'html.parser')
        shift = "None"
        role = "None"
        day = []
        evening = []
        for el in soup.findAll():
            #print(el.name)
            if el.name == "b":
                role = el.text.split(" (")[0]
            if el.name == "div":
                print(el)
                if el.get('id') == 'person':
                    if shift == "Day":
                        time = el.find("span").text.split(" ")[0]
                        details = el.find("span").text.replace(time + " ", "")
                        dict = {
                            'Name': el.find("a").text,
                            "Profile": el.find("a").get("href"),
                            "In Time": time.split("-")[0] if "-" in time else time,
                            "Out Time": time.split("-")[1] if "-" in time else None,
                            "Role": role,
                            "Details": details
                        }
                        #print(dict)
                        day.append(dict)
                    if shift == "Evening":
                        time = el.find("span").text.split(" ")[0]
                        details = el.find("span").text.replace(time + " ", "")
                        dict = {
                            'Name': el.find("a").text,
                            "Profile": el.find("a").get("href"),
                            "In Time": time.split("-")[0] if "-" in time else time,
                            "Out Time": time.split("-")[1] if "-" in time else None,
                            "Role": role,
                            "Details": details
                        }
                        #print(dict)
                        evening.append(dict)

                #print(el)
            elif el.name == "h5":
                #print(el.text)
                if el.text == "Day":
                    shift = "Day"
                    #print("Daytime Start")
                elif el.text == "Evening":
                    shift = "Evening"
                    #print("Evening Start")

        self.data[date] = {"evening": evening, "day": day}
        self.save()
        print("Day")
        print(json.dumps(day, indent=4))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Evening")
        print(json.dumps(evening, indent=4))

Scheduledaddy()
