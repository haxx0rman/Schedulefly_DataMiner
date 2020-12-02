import json, datetime
# import matplotlib.pyplot as plt
import numpy as np
# find every employee in the schedule database

# find every alias of theirs and save it in the alias data file using the profile number
# as the main unifier

# save in people.json a count of every time they have worked in every role

# make another database and count how many of each runner they had for each day and calculate the average
# ( maybe do the same for every role )


class Analyze():
    def __init__(self):
        self.open_databases()
        self.days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        self.d8s = []
        self.start()

    def start(self):
        #self.personal_history()
        #self.daays()
        #self.plot_role("Runner")
        self.role_stats("Runner")

        #self.plot_shifts_per_week()

        #self.personal_history()
        pass

    def get_monday(self, date):
        d8 = date.split("/")
        t = datetime.date(int(d8[2]), int(d8[0]), int(d8[1]))
        #today = today + datetime.timedelta(days=-today.weekday(), weeks=1)
        monday = t - datetime.timedelta(days=t.weekday())
        monday = str(monday).split("-")
        monday = "{}/{}/{}".format(monday[1], monday[2], monday[0])

        return monday

    def plot_role(self, role = None):
        if role is None:
            # get role input
            pass
        role = self.find(role, self.roles.keys())
        shifts = {}
        for e in self.roles[role]:
            if self.ppl[e]["Roles"][role]["Shift Count"] < 5:
                continue
            shifts[e] = { "Name": self.ppl[e]["Name"],
                           "Shifts Per Week": self.get_weekly_shifts(e, role) }


        #print(json.dumps(shifts, indent=4))
    def get_weekly_shifts(self, uid, role):
        # if employee is None:
        #     employee = input("Type in an employee: ")
        # name = self.find(employee, self.alias.keys())
        # uid = self.alias[name]
        first = self.get_monday(self.ppl[uid]["First Shift"])
        b = False
        mondays = []
        weekly_shifts = {}
        print(first)

        last = self.get_monday(self.phistory[uid][-1]["Date"])
        for w in self.weeks:
            if first in  w:
                b = True
                #print("B is true")
            if b:
                mondays.append(w)
                weekly_shifts[w] = 0
                if last in w:
                    #print("B  is False")
                    break
        #print(json.dumps(weekly_shifts, indent=4))
        for shift in self.phistory[uid]:
            if role in shift["Role"]:
                monday = self.get_monday(shift["Date"])
                weekly_shifts[monday] += 1
        #print(json.dumps(weekly_shifts, indent=4))
        return weekly_shifts

    def plot_shifts_per_week(self, employee = None):
        if employee is None:
            employee = input("Type in an employee: ")
        name = self.find(employee, self.alias.keys())
        uid = self.alias[name]
        first = self.get_monday(self.ppl[uid]["First Shift"])
        b = False
        mondays = []
        weekly_shifts = {}
        print(first)

        last = self.get_monday(self.phistory[uid][-1]["Date"])
        for w in self.weeks:
            if first in  w:
                b = True
                print("B is true")
            if b:
                mondays.append(w)
                weekly_shifts[w] = 0
                if last in w:
                    print("B  is False")
                    break
        #print(json.dumps(weekly_shifts, indent=4))
        for shift in self.phistory[uid]:
            monday = self.get_monday(shift["Date"])
            weekly_shifts[monday] += 1
        print(json.dumps(weekly_shifts, indent=4))
        y = []
        x = mondays
        for m in mondays:
            y.append(weekly_shifts[m])

        plt.plot(x, y)
        plt.xlabel("Weeks")
        plt.ylabel("Shifts")

        plt.title(name)
        plt.show()

        pass

    def role_stats(self, role):
        print(len(self.data.keys()))
        if role not in self.roles:
            print("Role Doesnt Exist")
            return
        l = []
        print("{} People have had at least 1 {} shift...".format(str(len(self.roles[role])), role))
        for p in self.roles[role]:
            #print(self.ppl[p][])
            # if self.ppl[p]["Roles"][role]["Shift Count"] < 100:
            #     continue
            dank = "{} has worked {} {} shifts.".format(self.ppl[p]["Name"], self.ppl[p]["Roles"][role]["Shift Count"], role)
            print(dank)

    def track_roles(self, p):
        if p["Role"] in self.roles.keys():
            if p["uid"] not in self.roles[p["Role"]]:
                self.roles[p["Role"]].append(p["uid"])
        else:
            self.roles[p["Role"]] = [ p["uid"] ]
        pass

    def what_week(self):
        pass

    def daays(self):
        day = {"month": 11, "day": 16, "year": 2015}
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
        self.weeks = []
        while True:
            #time.sleep(5)
            #print(day)
            t = datetime.date(day["year"], day["month"], day["day"])
            #today = today + datetime.timedelta(days=-today.weekday(), weeks=1)
            monday = t - datetime.timedelta(days=t.weekday())
            monday = str(monday).split("-")
            monday = "{}/{}/{}".format(monday[1], monday[2], monday[0])
            if len(self.weeks) < 1 or monday not in self.weeks[-1]:
                self.weeks.append(monday)
            #self.weeks["{}/{}/{}".format(day["month"], day["day"], day["year"])] = monday
            datetime.date(day["year"], day["month"], day["day"]).weekday()

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
                return self.d8s
                break
            self.d8s.append("{}/{}/{}".format(day["month"], day["day"], day["year"]))

    def personal_history(self):
        print("Running Full History Analysis...")
        days = self.daays()
        for day in days:
            if day not in self.data.keys():
                continue
            for emp in self.data[day]["day"]:
                uid = emp["Profile"].split("=")[1]
                self.alias[emp["Name"]] = uid
                d8 = day.split("/")
                DOW = int(datetime.date(int(d8[2]), int(d8[0]), int(d8[1])).weekday())
                dict = {
                        "Date": day,
                        "DOW": self.days[DOW],
                        "Name": emp["Name"],
                        "uid": uid,
                        "Role": emp["Role"],
                        "In Time": emp["In Time"],
                        "Details": emp["Details"]
                }
                self.track_stats(dict)
                self.track_roles(dict)
                if uid in self.phistory.keys():
                    self.phistory[uid].append(dict)
                else:

                    self.phistory[uid] = [dict]
            for emp in self.data[day]["evening"]:
                uid = emp["Profile"].split("=")[1]
                self.alias[emp["Name"]] = uid
                d8 = day.split("/")
                DOW = int(datetime.date(int(d8[2]), int(d8[0]), int(d8[1])).weekday())
                dict = {
                        "Date": day,
                        "DOW": self.days[DOW],
                        "Name": emp["Name"],
                        "uid": uid,
                        "Role": emp["Role"],
                        "In Time": emp["In Time"],
                        "Details": emp["Details"]
                }
                self.track_stats(dict)
                self.track_roles(dict)
                if uid in self.phistory.keys():
                    self.phistory[uid].append(dict)
                else:
                    self.phistory[uid] = [dict]

                #print(self.phistory)

        self.save_all()
        #print(json.dumps(self.phistory, indent=4, sort_keys=True))

    def track_stats(self, emp):
        """
        For every employee we want to track:
        what roles they have worked,
        how many shifts they have done for each role,
        how many of each day of the week they have worked,
        the date of their first day for each role,
        frequency of in-time
        profile id,
        whatever contact info can be found on schedulefly,
        """

        # check if this user is saved yet
        #print(self.ppl.keys())
        if emp["uid"] in self.ppl.keys():
            self.ppl[emp["uid"]]["Shift Count"] += 1

            newd8 = emp["Date"].split("/")
            newd8 = datetime.date(int(newd8[2]), int(newd8[0]), int(newd8[1]))
            oldd8 = self.ppl[emp["uid"]]["First Shift"].split("/")
            oldd8 = datetime.date(int(oldd8[2]), int(oldd8[0]), int(oldd8[1]))
            if oldd8 > newd8:
                self.ppl[emp["uid"]]["First Shift"] = emp["Date"]
            # check if that role has been saved under this employee yet
            if emp["Role"] in self.ppl[emp["uid"]]["Roles"]:
                self.ppl[emp["uid"]]["Roles"][emp["Role"]]["Shift Count"] += 1

                newd8 = emp["Date"].split("/")
                newd8 = datetime.date(int(newd8[2]), int(newd8[0]), int(newd8[1]))
                oldd8 = self.ppl[emp["uid"]]["Roles"][emp["Role"]]["First Shift"].split("/")
                oldd8 = datetime.date(int(oldd8[2]), int(oldd8[0]), int(oldd8[1]))
                if oldd8 > newd8:
                    self.ppl[emp["uid"]]["Roles"][emp["Role"]]["First Shift"] = emp["Date"]

                # if that day of the week is recorded already
                if emp["DOW"] in self.ppl[emp["uid"]]["Roles"][emp["Role"]]["Days"]:
                    self.ppl[emp["uid"]]["Roles"][emp["Role"]]["Days"][emp["DOW"]] += 1

                #if that day hasnt been recorded yet then initialize it yo
                else:
                    self.ppl[emp["uid"]]["Roles"][emp["Role"]]["Days"][emp["DOW"]] = 1

                # if that in time is recorded already there
                if emp["In Time"] in self.ppl[emp["uid"]]["Roles"][emp["Role"]]["In Times"]:
                    self.ppl[emp["uid"]]["Roles"][emp["Role"]]["In Times"][emp["In Time"]] += 1

                #if that in time hasnt been recorded yet then initialize it yo
                else:
                    self.ppl[emp["uid"]]["Roles"][emp["Role"]]["In Times"][emp["In Time"]] = 1

                # if that detail is recorded already there
                if emp["Details"] in self.ppl[emp["uid"]]["Roles"][emp["Role"]]["Details"]:
                    self.ppl[emp["uid"]]["Roles"][emp["Role"]]["Details"][emp["Details"]] += 1

                #if that detail hasnt been recorded yet then initialize it yo
                else:
                    self.ppl[emp["uid"]]["Roles"][emp["Role"]]["Details"][emp["Details"]] = 1

            # if the role hasnt been saved yet then create one...
            else:
                self.ppl[emp["uid"]]["Roles"][emp["Role"]] = {
                    "First Shift": emp["Date"],
                    "Shift Count": 1,
                    "Days": {
                        emp["DOW"]: 1
                    },
                    "In Times": {
                        emp["In Time"]: 1
                    },
                    "Details": {
                        emp["Details"]: 1
                    }
                }

        # if the user doesnt exist in the database yet then...
        else:
            user = {
                "Name": emp["Name"],
                "uid": emp["uid"],
                "First Shift": emp["Date"],
                "Shift Count": 1,
                "Roles": {
                    emp["Role"]: {
                        "First Shift": emp["Date"],
                        "Shift Count": 1,
                        "Days": {
                            emp["DOW"]: 1
                        },
                        "In Times": {
                            emp["In Time"]: 1
                        },
                        "Details": {
                            emp["Details"]: 1
                        }
                    }
                }
            }
            self.ppl[emp["uid"]] = user

        #self.save_all()
    def find(self, input, data):
        high = 99
        best_guess = ""
        for item in data:
            #print(item)
            dist = self.levenshtein_ratio_and_distance(input, item)
            if dist < high:
                best_guess = item
                high = dist
                #print("Best Guess: " + best_guess)
                #print("Distance: " + str(dist))
        return best_guess
    def levenshtein_ratio_and_distance(self, s, t, ratio_calc = False):
        """ levenshtein_ratio_and_distance:
            Calculates levenshtein distance between two strings.
            If ratio_calc = True, the function computes the
            levenshtein distance ratio of similarity between two strings
            For all i and j, distance[i,j] will contain the Levenshtein
            distance between the first i characters of s and the
            first j characters of t
        """
        # Initialize matrix of zeros
        rows = len(s)+1
        cols = len(t)+1
        distance = np.zeros((rows,cols),dtype = int)

        # Populate matrix of zeros with the indeces of each character of both strings
        for i in range(1, rows):
            for k in range(1,cols):
                distance[i][0] = i
                distance[0][k] = k

        # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions
        for col in range(1, cols):
            for row in range(1, rows):
                if s[row-1] == t[col-1]:
                    cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
                else:
                    # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                    # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                    if ratio_calc == True:
                        cost = 2
                    else:
                        cost = 1
                distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                     distance[row][col-1] + 1,          # Cost of insertions
                                     distance[row-1][col-1] + cost)     # Cost of substitutions
        if ratio_calc == True:
            # Computation of the Levenshtein Distance Ratio
            Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
            return Ratio
        else:
            # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
            # insertions and/or substitutions
            # This is the minimum number of edits needed to convert string a to string b
            return int(distance[row][col])

    def open_databases(self):
        with open('data.json') as f:
            self.data = json.load(f)

        try:
            with open('ppl_history.json') as f:
                self.phistory = json.load(f)
        except json.decoder.JSONDecodeError:
            self.phistory = {}
        #self.phistory = {}  # # DEBUG: this will prevent building on top of old data an counting shifts twice etc

        try:
            with open('roles.json') as f:
                self.roles = json.load(f)
        except json.decoder.JSONDecodeError:
            self.roles = {}

        try:
            with open('people.json') as f:
                self.ppl = json.load(f)
        except json.decoder.JSONDecodeError:
            self.ppl = {}
        #self.ppl = {} # # DEBUG: this will prevent building on top of old data an counting shifts twice etc

        try:
            with open('alias.json') as f:
                self.alias = json.load(f)
        except json.decoder.JSONDecodeError:
            self.alias = {}

    def save_all(self):
        # with open('data.json', 'w') as outfile:
        #      json.dump(self.data, outfile, indent=4, sort_keys=True)

        with open('ppl_history.json', 'w') as outfile:
              json.dump(self.phistory, outfile, indent=4, sort_keys=True)

        with open('roles.json', 'w') as outfile:
             json.dump(self.roles, outfile, indent=4, sort_keys=True)

        with open('people.json', 'w') as outfile:
             json.dump(self.ppl, outfile, indent=4, sort_keys=True)

        with open('alias.json', 'w') as outfile:
             json.dump(self.alias, outfile, indent=4, sort_keys=True)


Analyze()
