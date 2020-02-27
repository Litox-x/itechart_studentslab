# ВАРИАНТ 5

class Tech:
    def __init__(self,name,price,number):
        self.price = price
        self.name = name
        self.number = number

    def Count(self):
        print("Count is -", self.number)

class Printer(Tech):
    def Prints(self):
        print("The printer prints")

class Computer(Tech):
    def Click(self):
        print("I am working")

class Tablet(Tech):
    games = []
    def installgame(self,game):
        self.games += [game]
        print("game",game,"installed")

class Scanner(Tech):
    def Scan(self,doc):
        print("Doc",doc,"has been scaned")

class Goods:
    def __init__(self):
        self.goodslist = []

    def Goodscout(self):
        k=0
        for i in self.goodslist:
            k+=i.number
        print(k)

list = Goods()
PK = Computer("Asus",32,5)
PrinterOne = Printer("HP laserjet",10,6)
GameTablet = Tablet("IPad",1000,1)
GameTablet.installgame("Wow!")
PrinterOne.Prints()
Scan = Scanner("Dell",10,200)
Scan1 = Scanner("Dellz",10,200)
Scan.Count()
list.goodslist.append(PK)
list.goodslist.append(Scan)
list.goodslist.append(GameTablet)
list.goodslist.append(PrinterOne)
list.goodslist.append(Scan1)
list.Goodscout()