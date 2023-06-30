# name gender age
class People:
    def __init__(self, name, age, gender):
        self.myname = name
        self.myage = age
        self.mygender = gender

    def onyesha(self):
        print(self.myname, self.myage, self.mygender)


myobj = People("Kimberly", 19, "Female")
myobj.onyesha()
myobj=People("Sasha", 14, "Female")
myobj.onyesha()
myobj=People("Darren", 20, "Male")
myobj.onyesha()
