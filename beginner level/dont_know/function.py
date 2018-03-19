def a(x):
  print (x)
def b(function, *args, **kwargs):
    function(*args, **kwargs)
b(a, 'hello', 'guvi')
