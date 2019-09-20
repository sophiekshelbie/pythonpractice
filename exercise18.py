import random

x = list(str(random.sample(range(1001, 10000), 1)))
x.remove("[")
x.remove("]")

print(x)

count = 0
cows = 0

def cows_and_bulls():
  z = list(input("Please enter 4 digits:"))
  if str("".join(z)) == "exit":
    print("Thanks for the game!")
  else:
    global cows  
    cows = 0
    bulls = 0

    for i in range(4):
      for j in range(4):
        if z[i] == x[j]:
          if i == j:
            cows += 1
          elif z[j] == x[j]:
            bulls == bulls      
          else:
            bulls += 1
    
    print("Cows:  " + str(cows))
    print("Bulls: " + str(bulls))

while cows < 4:
 cows_and_bulls()
 count += 1

if cows == 4:
  print("Congrats! You guessed " + str(count) + " times.")