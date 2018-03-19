names=['pradeep','nks']
def times(x):
  print x*3
def something(times,names):
  for items in names:
    times(items)
something(times,names)
