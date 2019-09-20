with open('test.txt','w') as f:           # this is how you write to files
  f.write('Hello')
  
with open ('test.txt','r') as f:
  f_contents=f.read()
  print(f_contents)
  
with open('test.txt','w') as f:
  f.write('I have written over this file')
  
with open('test.txt','r') as f:
  contents=f.read()
  print(contents)