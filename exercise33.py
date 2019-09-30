birthday_dictionary = {"roy": '1-jan',"joy": '2-jan',"doy": '3-jan',"toy":'4-jan'} 

a=input('enter name to find his/her birthday = ') 
if a in birthday_dictionary.keys(): 
    print('birthday of {} is {}'.format(a, birthday_dictionary[a])) 
elif a not in birthday_dictionary.keys(): 
    print('{}, this name is not in the dictionary'.format(a)) 
b=input('do you want to add to birthday_dictionary? y/n') 
if b=='y': 
    c=input('when is the birthday?') 
    birthday_dictionary[a]=c 
print('name has been added')