a = []
b,n = 0,0
print("Введите матрицу:")
while True:
    b = [i for i in input().split()] 
    if b == ['end']: 
        break
    m=len(b) 
    n+=1
    a=a+[b]  

c = [[0 for j in range(m)] for i in range(n)] 

for i in range(n):
    for j in range(m):
        c[i][j] = int(a[(i-1)%n][j]) + int(a[(i+1)%n][j]) + int(a[i][(j-1)%m]) + int(a[i][(j+1)%m]) 
for i in range(len(c)): 
    print(*c[i])
