def case(x):
    if(x<=14):
        if(x==0 or (x>=5 and x<=14)):
            print("рублей", end=" ")
            return
        if(x>=2 and x<=4):
            print("рубля", end=" ")
            return
        if (x == 0):
            print( "рубль", end=" ")
            return
    else:
        if(x%10==1):
            print("рубль", end=" ")
            return
        if(x%10>=2 and x%10<=4):
            print( "рубля", end=" ")
            return
        if((x%10>=5 and x%10<=9) or x%10==0):
            print("рублей", end=" ")
            return

def casecoins(x):
    if((x>=10 and x<=20) or x%10==0):
        print( "копеек", end=" ")
        return
    else:
        if(x%10==1):
            print("копейка", end=" ")
            return
        if(x%10>=2 and x%10<=4):
            print( "копейки", end=" ")
            return
        print("копеек", end=" ")
unic = ("","одинадцать","двенадцать","тринадцать","четырнадцать","пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать")
units = ("","один","два","три","четыре","пять","шесть","семь","восемь","девять")
decades = ("","десять","двадцать","тридцать","сорок","пятьдесят","шестьдесят","семьдесят","восемьдесят","девяноста")
hundreds = ("","сто","двести","триста","четыреста","пятьсот","шестьсот","семьсот","восемьсот","девятьсот")
def number(x):
    if(x==10):
        print(decades[1], end=" ")
    elif(x==0):
        print("ноль",end=" ")
    elif(x%100//10==1):
        print(hundreds[x//100],end=" ")
        print(unic[x%10], end=" ")
    else:
        print(hundreds[x//100],end=" ")
        print(decades[x//10%10],end=" ")
        print(units[x%10], end=" ")
unicc = ("","одинадцать","двенадцать","тринадцать","четырнадцать","пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать")
unitsc = ("","одна","две","три","четыре","пять","шесть","семь","восемь","девять")
decadec = ("","десять","двадцать","тридцать","сорок","пятьдесят","шестьдесят","семьдесят","восемьдесят","девяноста")
hundredc = ("","сто","двести","триста","четыреста","пятьсот","шестьсот","семьсот","восемьсот","девятьсот")
def numbercoins(x):
    if(x==10):
        print(decadec[1], end=" ")
    elif(x==0):
        print("ноль",end=" ")
    elif(x%100//10==1):
        print(hundredc[x//100],end=" ")
        print(unicc[x%10], end=" ")
    else:
        print(hundredc[x//100],end=" ")
        print(decadec[x//10%10],end=" ")
        print(unitsc[x%10], end=" ")

x = float(input("Введите сумму от 0.00 до 999.99\n"))
i = int(x)
f=int(x*100%100)
number(i)
case(i)
numbercoins(f)
casecoins(f)
print(f)