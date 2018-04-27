s=0
a=[]
e=int(input())
b=int(input())
for j in range(e,b+1):
  a=str(j)
  s=0
  k=len(a)
  for i in range(k):
     c=a[i]
     d=pow(int(c),k)
     s=s+d

  if(j==s):
    print(s)

