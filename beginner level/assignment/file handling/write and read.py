def main():
  fhandle= open("file location or file name"+"w+)  '''w+ for write mode of a file'''
  fhandle.write("something")  
  fhandle.seek(0)         '''to rewind the function at the begining'''
  print(fhandle.read())   '''if this is given after line 3 it wont read because it acts as tape recorder'''
