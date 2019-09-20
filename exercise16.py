  
import random

user_input = int(input("How many characters long password do you need?"))

characters = "abcde23456789.:,?;<>#&@"

def password(a):
  output = []
  i = 1
  while i <= a:
    b = random.choice(characters)         
    output.append(b)
    i += 1
  print("Your password: " + "".join(output))

password(user_input)