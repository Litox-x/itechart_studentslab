# ВАРИАНТ 10

import sys
class Carlist:
    def __init__(self):
        self.list = []

    def marksearch(self,target):
        for i in self.list:
            if(i.mark == target):
                print(i.mark)


    def modelsearch(self,model,year):
        for i in self.list:
            if (year < i.YearsOld() and model == i.model ):
                print(i.model)




class Car:

    def __init__(self,mark,model,date,color,price,regnum):
        self.mark = mark
        self.model = model
        self.date = date
        self.color = color
        self.price = price
        self.regnum = regnum
        print("Object was created")

    def changecolor(self,color):
        print("Car ",self.mark," succesfully colored:\n","Old color - ",self.color)
        self.color = color
        print("New color - ",self.color)

    def YearsOld(self):
        import  datetime
        now = datetime.datetime.now()
        now = now.year - int(self.date)
        return now

    def __del__(self):
        print("object is deleted")


carlist = Carlist()
BMW = Car("BMW","x5","2010","black",5000,"ZX4141EQ")
Audi = Car("Audi","r8","2017","black",25000,"ZX5141EQ")
BMWx6 = Car("BMW","x6","2018","black",15000,"ZX3212341EQ")
Renault = Car("Reanault","Logan","2010","black",5000,"ZX213141EQ")
Porche = Car("Porche","Careera","2017","black",50000,"ZX413224Q")
BMW.changecolor("white")
print(BMW.YearsOld())
carlist.list.append(BMW)
carlist.list.append(Audi)
carlist.list.append(BMWx6)
carlist.list.append(Porche)
carlist.list.append(Audi)
carlist.list.append(Renault)
carlist.marksearch("BMW")
carlist.modelsearch("x5",5)
