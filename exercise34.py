#!/usr/bin/python 
import json 
birthday_dict = json.load(open("birthday_dict.txt")) 
choice = int(input("\nHello. Welcome to your b-day dictionary. Would you like to lookup (1) or add? (2): ")) 
choices = [1,2] 
while choice not in choices: 
    print ("Invalid choice. Try Again.") 
    choice = int(input("\nHello. Welcome to your b-day dictionary. Would you like to lookup (1) or add? (2): ")) 
if choice == 1: 
    for x in birthday_dict: 
        print (x) 
    who = input("Who's birthday would you like to look up?: ") 
    if who not in birthday_dict: 
        print ("I'm sorry, that birthday doesn't exist in the dictionary.") 
    else: 
        print ("\n" + str(who) + "'s birthday is: " + str(birthday_dict[who]) + "\n") 
    exit(0) 
elif choice == 2: 
    addmore = True 
    while addmore == True: 
        name = input("Give me the persons first name: ") 
        b_day = input("Give me their birthday in the form of month/day. ") 
        birthday_dict[name] = b_day print ("\n" + str(name) + "'s birthday of: " + str(birthday_dict[name]) + " has been added to the dictionary.\n") answ = input("Would you like to enter another birthday? yes (y) or no (n):") 
        if answ == 'y': 
            addmore = True 
        elif answ == 'n': 
            addmore = False 
        with open("birthday_dict.txt", 'w') as dictionary: 
            json.dump(birthday_dict, dictionary) 
        dictionary.close() 
        exit(0) 