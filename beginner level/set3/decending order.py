  a=[]
  n=int(input("enter the number of digits"))
  for i in range(1,n+1):
    b=int(input('digits'))
    a.append(b)
    c=sorted(a)
    c.reverse()
  print(c)
