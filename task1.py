"""таск 1"""
n = int(input("Введите n "))
s=0
for i in range(n+1):
    for j in range(i):
        print(i, end=" ")
        s+=1
        if(s==n):
            exit(0)
