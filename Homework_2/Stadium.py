
class Stadium:
    def __init__(self, name, date, country, city, countPeople):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.countPeople = countPeople

    def printStats(self):
        print(f"Name:   {self.name}  date:   {self.date}  country:   {self.country}  city:   {self.city}  countPeople:  {self.countPeople}")

    def editStadium(self):
        self.country = input("Enter new country: ") or self.country
        self.date = input("Enter new date: ") or self.date
        self.country = input("Enter new country: ") or self.country
        self.city = input("Enter new city: ") or self.city
        self.countPeople = input("Enter new count: ") or self.countPeople

stat = Stadium("Name",124,"Country","City","People")
stat.printStats()
