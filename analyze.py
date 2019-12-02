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

        with open('ppl_history.json') as f:
            self.phistory = json.load(f)

        with open('people.json') as f:
            self.ppl = json.load(f)

        with open('alias.json') as f:
            self.alias = json.load(f)
        self.days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        self.start()

    def start(self):
        self.personal_history()

    def save_all(self):
        # with open('data.json', 'w') as outfile:
        #      json.dump(self.data, outfile, indent=4, sort_keys=True)

        with open('ppl_history.json', 'w') as outfile:
             json.dump(self.phistory, outfile, indent=4, sort_keys=True)

        with open('people.json', 'w') as outfile:
             json.dump(self.ppl, outfile, indent=4, sort_keys=True)

        with open('alias.json', 'w') as outfile:
             json.dump(self.alias, outfile, indent=4, sort_keys=True)

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

                if uid in self.phistory.keys():
                    self.phistory[uid].append(dict)
                else:
                    self.phistory[uid] = [dict]

                #print(self.phistory)

        self.save_all()
        print(json.dumps(self.phistory, indent=4, sort_keys=True))

    def track_stats(self):
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

        base = {
            "Name": name,
            "uid": uid,
            "Roles": {
                "Runner": "uughh"
            }
        }
Analyze()
