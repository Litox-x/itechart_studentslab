def casecoins(x):
    if((x>=10 and x<=20) or x%10==0):
        print(x,end=" ")
        return "копеек"
    else:
        if(x%10==1):
            print(x, end=" ")
            return "копейка"
        if(x%10>=2 and x%10<=4):
            print(x, end=" ")
            return "копейки"
        print(x, end=" ")
        return "копеек"


x = int(input("Введите количество копеек (1-99) "))
print(casecoins(x))
