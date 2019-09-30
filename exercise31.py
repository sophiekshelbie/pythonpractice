import random 

with open("sowpods.txt", "r") as dictionary: 
    words = dictionary.readlines() 
    
word_selected = list(str(random.choice(words)).lower().strip()) 
print(str(len(word_selected)) + " letters word.") 
word_displayed = ["*" for letter in range(len(word_selected))] 
letters_guessed = [] 
counter = 0 

while word_displayed != word_selected: 
    while True:      # In case the user entered the letter again, it doesn't add to the counter 
    letter_guessed = input("Guess : ") 
    if letter_guessed in letters_guessed: 
        print("Already guessed.") 
    else: 
        letters_guessed.append(letter_guessed) 
        break 
        
    for index in range(len(word_selected)): 
        if letter_guessed == word_selected[index]: 
            word_displayed[index] = letter_guessed 
        counter += 1 
        print("".join(word_displayed)) 
        
    print("Took you " + str(counter) + " tries.")