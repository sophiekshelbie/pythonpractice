# This exercise is Part 3 of 4 of the birthday data exercise series. The other exercises are: Part 1, 
# Part 2, and Part 4. 
# In the previous exercise we saved information about famous scientists’ names and birthdays to disk. 
# In this exercise, load that JSON file from disk, extract the months of all the birthdays, and count 
# how many scientists have a birthday in each month. 

# Your program should output something like: 
# { 
#        "May": 3, 
#        "November": 2, 
#        "December": 1 
# } 
import json 
from collections import Counter

# Load data from json file.. 
with open('birthday.json', 'r') as openfile: 
    data = json.load(openfile) 
    
monthdict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'} 
             
def extractMonth(dob): 
    dates = [] 
    for name in data: 
        dates.append(data.get(name)) 
    print(dates) 
    months = [] 
    for item in dates: 
        months.append(int(item[3:5])) 
    print(months) 
    return months 
    
output = extractMonth(data) 
final = [] 

for item in output: 
    final.append(monthdict.get(item)) 

print(Counter(final))