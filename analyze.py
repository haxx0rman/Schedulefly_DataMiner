import json, datetime
# find every employee in the schedule database

# find every alias of theirs and save it in the alias data file using the profile number
# as the main unifier

# save in people.json a count of every time they have worked in every role

# make another database and count how many of each runner they had for each day and calculate the average
# ( maybe do the same for every role )


class Analyze():
    def __init__(self):
        with open('data.json') as f:
            self.data = json.load(f)

        try:
            with open('ppl_history.json') as f:
                self.phistory = json.load(f)
        except json.decoder.JSONDecodeError:
            self.phistory = {}

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

        try:
            with open('alias.json') as f:
                self.alias = json.load(f)
        except json.decoder.JSONDecodeError:
            self.alias = {}
        self.days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        self.start()

    def start(self):
        self.personal_history()

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

    def track_roles(self, p):
        if p["Role"] in self.roles.keys():
            if p["uid"] not in self.roles[p["Role"]]:
                self.roles[p["Role"]].append(p["uid"])
        else:
            self.roles[p["Role"]] = [ p["uid"] ]
        pass
    def personal_history(self):
        for day in self.data.keys():
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
                        "In Time": emp["In Time"]
                }

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
                        "In Time": emp["In Time"]
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

        example:
        ex = {
            "Name": name,
            "uid": uid,
            "Shift Count": 0,
            "Roles": {
                "Runner": {
                    "First Shift": "1/1/1",
                    "Shift Count": 0,
                    "Days": {
                        "mon": 0,
                        "tues": 0,
                        "wed": 0,
                        "thur": 0,
                        "fri": 0,
                        "sat": 0,
                        "sun": 0
                    },
                    "In Times": {

                    }
                }
            }
        }

            name:
                info
                info
                info
                roles:
                    runner:
                    first runner shift: 9/11/2000
                        days worked:
                            saturday: 9
                            sunday: 5
                            monday: 6
                            etc...
                        in time:
                            430: 8 times,
                            600: 1000 times
                            etc...
                    server:
                        etc...
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
                        }
                    }
                }
            }
            self.ppl[emp["uid"]] = user

        #self.save_all()



Analyze()
