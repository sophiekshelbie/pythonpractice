user_string = input("Enter words with spaces: ")

def backwards(a):
  b = a.split(" ")      # spliting str
  i = len(b) - 1
  backs = ""
  while i >= 0:
    if i == len(b) - 1:
      backs = str(backs) + b[i]
    else:
      backs = str(backs) + " " + b[i]
    i -= 1
  print(backs)

backwards(user_string)