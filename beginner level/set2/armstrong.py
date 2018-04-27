s=0
a=[]
a=input()
b=len(a)
for i in range(b):
  c=a[i]
  d=pow(int(c),b)
  s=s+d
print(s)

if(a==str(s)):
  print('armstrong number')
else:
  print('not an armstrong number')
