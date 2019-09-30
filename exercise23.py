# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4. 
# Time for some fake graphics! Let’s say we want to draw game boards that look like this: 

def horizontal_line ( size ): 
    return " ---" * size + " \n" 
    
def vertical_lines ( size ): 
    return "| " * size + "|\n" 
    
def gameboard ( size ): 
    board = """""" 
    for i in range(size): 
        board += horizontal_line(size) 
        board += vertical_lines(size) 
    board += horizontal_line(size) 
    return board 
    
if __name__ == "__main__": 
    size = int(input("What size game board do You want? ")) 
    print(gameboard(size))