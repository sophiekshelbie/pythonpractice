def in_the_list (user_list, user_number):
  if user_number in user_list:
    print("Yes number exists")
  else:
    print("False")

  
x = input("Give me a list of numbers: ")
y = input("Give me a number: ")

in_the_list(x, y)