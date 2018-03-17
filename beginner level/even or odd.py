N=int(input('input : '))
if(1<=N<=100000):
    if(N%2==0):
      print('output : even')
    else:
      print('output : odd')
elif(N%2==0):
    print('even')
else:
    print('odd')
