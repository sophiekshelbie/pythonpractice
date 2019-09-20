number_of_sequence = int(input("Enter the length of sequence: "))

def fibonacci(a):
  if a == 0:
    return None
  elif a == 1:
    print([1])
  else:
    fibo = [1, 1]
    while len(fibo) < a:
      elem = int(fibo[-2]) + int(fibo[-1])
      fibo.append(elem)
    print(fibo)
    
fibonacci(number_of_sequence) 