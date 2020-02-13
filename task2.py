print("Введите строку с числами")
lst = (input().split())
x=int(input("Введите искомое число"+'\n'))

for i in range(len(lst)):
    if x==int(lst[i]):
        print(i,end=" ")
