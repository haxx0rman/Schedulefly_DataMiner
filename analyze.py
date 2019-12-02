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

        self.start()

    def personal_history(self):
        for day in self.data.keys():
            for emp in self.data[day]["day"]:
                pass
            for emp in self.data[day]["evening"]:
                uid = emp["profile"].split("=")[1]

                if uid in self.phistory.keys():
                    self.phistory[uid].append()
                else:
                    self.phistory[uid] = []
                pass
