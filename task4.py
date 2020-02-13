n = int(input("Введите n"+'\n'))
a = [0]*n

for i in range(n):
    a[i]=[0]*n

k,i,j=1,0,0

while(k!=n*n+1):
    a[i][j]=k
    if(i<=j and i+j<n-1 ):
        j+=1       
    elif(i<j and i+j>=n-1):
        i+=1
    elif(i>=j and i+j>n-1):
        j-=1
    elif(a[i-1][j]==0):
        i-=1
    else: 
        j+=1
    k+=1

for i in range(n):
    print(*a[i])