a = int(input('first number: ')) 
b = int(input('second number: ')) 
c = int(input('third number: ')) 

seq = [a,b,c] 
seq.sort() 

print (seq[2],' is the largest') 
print ('followed by ',seq[1]) 
print ('then ', seq[0])