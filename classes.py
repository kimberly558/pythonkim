class Cars:
    def __init__(self, modelname, color, year, cc):
        self.model = modelname
        self.mycolor = color
        self.myyear = year
        self.capacity=cc
    def onyesha(self):
        print(self.model, self.mycolor, self.myyear,self.capacity)
# create an object
myobj=Cars("Toyota", "White", 2020, 2000)
myobj.onyesha()
myobj=Cars("Jeep","yellow", 2022, 2000)
myobj.onyesha()