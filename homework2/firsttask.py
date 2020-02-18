def case(x):
    if(x<=14):
        if(x==0 or (x>=5 and x<=14)):
            print(x,end=" ")
            return "рублей"
        if(x>=2 and x<=4):
            print(x, end=" ")
            return "рубля"
        if (x == 0):
            print(x, end=" ")
            return "рубль"
    else:
        if(x%10==1):
            print(x,end=" ")
            return "рубль"
        if(x%10>=2 and x%10<=4):
            print(x, end=" ")
            return "рубля"
        if((x%10>=5 and x%10<=9) or x%10==0):
            print(x, end=" ")
            return "рублей"

x = int(input("Введите сумму "))
print(case(x))
