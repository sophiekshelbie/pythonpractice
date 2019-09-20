  
first_list = [34, 34, 5, 6, 21, 34, 5, 89, 21, 34]

# solution with sets

def kill_duplicates(a):
  print(list(set(a)))
  
kill_duplicates(first_list)

# solution with loop

def new_list(a):
  new_list = []

  for i in first_list:
    if i not in new_list:
      new_list.append(i)
    
  print(new_list)
  
new_list(first_list)