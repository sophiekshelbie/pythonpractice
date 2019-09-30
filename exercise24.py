# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
# One .txt file has a list of all prime numbers under 1000, and the other 
# .txt file has a list of happy numbers up to 1000. 

#File Overlap 
f1 = open("one.txt", "r") 
f2 = open("other.txt", "r") 
f2_list = f2.readlines() 
result = list() 

for line in f1: 
    if line in f2_list: 
        result.append(line.strip() ) 
        
f1.close() 
f2.close() 
print (result)