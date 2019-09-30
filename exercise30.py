import random 
with open ("sowpods.txt" ,"r") as rf: 
    text = rf.read() 
a_list = random.choice(text.split("\n")) 
print(a_list)