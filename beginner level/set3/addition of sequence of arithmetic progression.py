  s=0
  a=int(input('initial value'))
  n=int(input('number of sequence'))
  d=int(input('difference'))
  for i in range(1,n+1):
      b=a+((i-1)*d)
      s=s+b
  print(s)
