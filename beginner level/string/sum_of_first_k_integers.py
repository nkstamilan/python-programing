n=int(input('enter the number of integers :'))
k=int(input('number of first k integers : '))
s=0
a=[]
for i in range(n):
    b=int(input('enter the integer : '))
    a.append(b)
for j in range(k):
    s=s+a[j]
print('sum of first k integers : ',s)
