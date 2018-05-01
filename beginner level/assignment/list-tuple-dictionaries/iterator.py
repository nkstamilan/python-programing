list_=[1, 2, 3, 4, 3, 2]
print(dir(list_))
a=iter(list_)
b=reversed(list_)
print(a,b)
for i in a:
  print(i)
print("\n")
for j in b:
  print(j)
