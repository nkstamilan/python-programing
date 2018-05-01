a=[1,2,3,456,51,45,74]
def even(x):
  if (x%2==0):
    print('even')
  else:
    print('odd')
print (list(map(even,a)))
print (list(map(lambda x:x%2,a)))
