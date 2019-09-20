user_input = int(input("Give me a number: "))

def prime(a):
  i = a - 1
  count = 0
  
  while i > 1:
    if a % i == 0:
      count += 1
    i -= 1
  
  if count > 0:
    print("The given number is not prime.")
  else:
    print("The given number is prime")

prime(user_input)    
    