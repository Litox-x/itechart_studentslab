import numpy
import os
import math

class tribon:
    def __iter__(self):
        a=[0,0,1]
        print(a[0])
        print(a[1])
        print(a[2])
        k=3
        while k<=35:
            a[0],a[1],a[2]=a[1],a[2],a[1]+a[2]+a[0]
            k+=1
            yield a[2]


import math
class leib():
    def __init__(self,x):
        self.x = x
        self.k = 0
        self.i = 0

    def __iter__(self):
        zn = 1
        while(round(self.k,2)!=round(self.x,2)):

            if (self.i % 2 == 0):
                self.k += 1 / zn
            else:
                self.k -= 1 / zn
            self.i += 1;
            zn+=2
            yield self.k


import time

if(input("Введите номер задания:\n")=="1"):
    main_iter = tribon()
    for line in main_iter:
        print(line)
        time.sleep(0.25)
else:
    ss = float(input("Введите ожидаемое значение\n"))
    while( ss > 1 or ss < 0.78):
        ss=float(input("Введите другое значение (0.78-1)\n"))
    main_iter1 = leib(ss)
    for line in main_iter1:
        print(line)
        time.sleep(0.25)