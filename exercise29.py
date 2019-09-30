from os import system, 
name from time import sleep 
def clear(): 
    if name == 'nt': 
        s = system('cls') 
    else: 
        s = system('clear') 
        
def draw(L1,L2,L3): 
    print("",end=" ") 
    for i in range(5): 
        print(L1[i],end=" ") 
    print("\n-----------") 
    print("", end=" ") 
    for i in range(5): 
        print(L2[i],end=" ") 
    print("\n-----------") 
    print("", end=" ") 
    for i in range(5): 
        print(L3[i],end=" ") 
    print("") 
    
def allot(pos1,pos2,i,L1,L2,L3): 
    if i==1: 
        if (pos1 == 1): 
            L1[2 * pos2] = 'X' 
        elif (pos1 == 2): 
            L2[2 * pos2] = 'X' 
        elif (pos1 == 3): 
            L3[2 * pos2] = 'X' 
        else: 
            print("Please enter a valid position of x") 
        draw(L1, L2, L3) 
        sleep(2) 
        clear() 
        i = i + 1 
    else: 
        if (pos1 == 1): 
            L1[2 * pos2] = 'O' 
        elif (pos1 == 2): 
            L2[2 * pos2] = 'O' 
        elif (pos1 == 3): 
            L3[2 * pos2] = 'O' 
        draw(L1, L2, L3) 
        sleep(2) 
        clear() 
        i = i - 1 
    return i 
    
    def check(pos1,pos2,L1,L2,L3): 
        if pos1==1: 
            if L1[2 * pos2] == 'X' or L1[2*pos2]=='O': 
                return True 
            else: 
                return False 
        elif pos1==2: 
            if L2[2 * pos2] == 'X' or L2[2*pos2]=='O': 
                return True 
            else: 
                return False 
        elif pos1==3: 
            if L3[2 * pos2] == 'X' or L3[2*pos2]=='O': 
                return True 
            else: 
                return False 
        
    def result(L1,L2,L3): 
        if (L1[0]=="X" and L1[2]=="X" and L1[4]=="X") or (L2[0]=="X" and L2[2]=="X" and L2[4]=="X") \ 
                or (L3[0]=="X" and L3[2]=="X" and L3[4]=="X") or (L1[0]=="X" and L2[2]=="X" and L3[4]=="X") \ 
                or (L1[4] == "X" and L2[2] == "X" and L3[0] == "X") or (L1[0]=="X" and L1[2]=="X" and L1[4]=="X") \ 
                or (L1[0]=="X" and L2[0]=="X" and L3[0]=="X") or (L1[2]=="X" and L2[2]=="X" and L3[2]=="X") \ 
                or (L1[4]=="X" and L2[4]=="X" and L3[4]=="X"): 
            return 1 
        elif (L1[0]=="O" and L1[2]=="O" and L1[4]=="O") or (L2[0]=="O" and L2[2]=="O" and L2[4]=="O") \ 
                or (L3[0]=="O" and L3[2]=="O" and L3[4]=="O") or (L1[0]=="O" and L2[2]=="O" and L3[4]=="O") \ 
                or (L1[4] == "O" and L2[2] == "O" and L3[0] == "O") or (L1[0]=="O" and L1[2]=="O" and L1[4]=="O") \ 
                or (L1[0]=="O" and L2[0]=="O" and L3[0]=="O") or (L1[2]=="O" and L2[2]=="O" and L3[2]=="O") \ 
                or (L1[4]=="O" and L2[4]=="O" and L3[4]=="O"): 
            return 0 
        else: 
            return -1 
            
    print("Welcome to Tic Tac Toe Game") 
    print("To play this game you need to enter the co-ordinates of the position you want to put X's or O's") 
    print("x co-ordinates are the rows position\ny co-ordinates are the columns position") 
    L1=[' ','|',' ','|',' '] 
    L2=[' ','|',' ','|',' '] 
    L3=[' ','|',' ','|',' '] 
    draw(L1,L2,L3) 
    i=1; 
    while True: 
        try: 
            if(i==1): 
                pos1 = int(input("1st player->Enter your position of x co-ordinate :")) 
                pos2 = int(input("1st player->Enter your position of y co-ordinate :")) 
                if pos1 > 3 or pos2 > 3 or pos1 < 1 or pos2 < 1: 
                    print("Enter valid position") 
                else: 
                    pos2 = pos2 - 1 
                    if(check(pos1,pos2,L1,L2,L3)): 
                        print("Already filled") 
                    else: 
                        i=allot(pos1,pos2,i,L1,L2,L3) 
            else: 
                pos1=int(input("2nd player->Enter your position of x co-ordinate :")) 
                pos2=int(input("2nd player->Enter your position of y co-ordinate :")) 
                if pos1 > 3 or pos2 > 3 or pos1 < 1 or pos2 < 1: 
                    print("Enter valid position") 
                else: 
                    pos2 = pos2 - 1 
                    if(check(pos1,pos2,L1,L2,L3)): 
                        print("Already filled") 
                    else: 
                        i=allot(pos1,pos2,i,L1,L2,L3) 
            a=result(L1,L2,L3) 
            if a==1: 
                print("Player 1 wins the Game!!!!!") 
                break 
            elif a==0: 
                print("Player 2 wins the Game!!!!!") 
                break 
            a=0 
        except ValueError: 
            print("Please enter integers") 
    print("Thank you for playing!!!!!")