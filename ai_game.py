def ConstBoard(board):
    print("Current State of the Board: \n\n")
    for i in range(0,9):
        if((i>0) and (i%3) ==0):
            print("\n")
        if(board[i] ==0):
            print("_", end=" ")  # If the value of i is 0, then print an underscore, we should also provice spacing also
        if(board[i]==-1):
            print("X ", end=" ")
        if(board[i]==1):
            print("O ", end=" ")
    print("\n\n")

def User1Turn(board):       # This function is for HUMAN player 1
    pos = input("Enter X's position from [1,2,3.....,9] ")
    pos = int(pos)
    if(board[pos-1]!=0): #This means there is already something present over here, either an X or a O
        print("wrong Move") #This is an invalid move. There's already and X or O over here.
        exit(0) # Stop the execution of the code. Stop the game
    board[pos-1]=-1

def User2Turn(board):       # This function is for HUMAN player 2
    pos = input("Enter O's position from [1,2,3.....,9] ")
    pos = int(pos)
    if(board[pos-1]!=0): #This means there is already something present over here, either an X or a O
        print("wrong Move") #This is an invalid move. There's already and X or O over here.
        exit(0) # Stop the execution of the code. Stop the game.
    board[pos-1]=1

def minmax(board, player): # We are creating a Recursive function, right over here. (A function that calls upom itself again and again)
    x =analyzeboard(board)      # First we are going to check if someone has won or lost
    if(x!=0): #If x is not equal to 0, that means somebody has won.
        return (x*player)        # Then return who has won. We multiply x with player so that the answer always remains consistent
    pos = -1
    value = -2
    for i in range(0, 9):
        if(board[i]==0):
            board[i]=player     # Here we put 'player' because a player can be another human or AI as well. We don't know.
            score=-minmax(board, player *-1)
            board[i] = 0
            if(score>value):
                value = score   #we are updating the score here
                pos=i
    if(pos==-1):        #The player is not able to figure out where to put his X or O.  The value of pos is -1
        return 0        #It is a DRAW
    return value    #Return the value as the highest value possible. We are propagating the value back up the tree (min-max algorithm tree). This is called 'Back Tracking', which we have implemented using Recursion.


def CompTurn(board): # This is the Computer's turn. AI's turn.
    pos = -1
    value = -2
    for i in range(0, 9):
        if(board[i]==0):
            board[i]=1  # The 1 means it's the computer's turn because the Computer is O
            score=-minmax(board, -1)
            board[i] = 0
            if(score>value):
                value = score   #we are updating the score here
                pos=i
    board[pos] =1


def analyzeboard(board):
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]] # The first 3 elements are the rows, the second 3 elements are the columns and the last 2 elements are the diagonals on the board game.

    for i in range(0, 8): # This is going over every single element in the big list (cb). If i=0, we are on the FIRST small list (element)
        if(board[cb[i][0]]!=0 and       #The board should not be blank
           board[cb[i][0]]==board[cb[i][1]] and #This is checking all the rows
           board[cb[i][0]]==board[cb[i][2]]): 
            return board[cb[i][0]]      #This particular person has won the game
    return 0    #If no one has won, then return 0



def main():
    choice = input("Enter 1 for Single Player, 2 for Multiplayer: ") #At the start of the game, select if you want to play with the AI or another human.
    choice = int(choice)            # We are converting the choice from string to integer.
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]     # This represents the entire board of the game with only 9 possible moves.
    if(choice ==1):         # If you chose 1, then you'll play with the AI.
        print("Computer: O Vs. You: X ")
        player = input("Enter to play 1(st) or 2(nd): ")    # Here you indicate if you'd like to play first or second
        player = int(player)
        for i in range(0, 9):
            if(analyzeboard(board)!=0): #If someone has won, the entire thing (game) will close. Check 'break'.
                break
            if((i+player)%2==0):
                CompTurn(board)
            else:
                ConstBoard(board)
                User1Turn(board)

    else:                   # Otherwise, you chose 2, and you'll play with another human.
        for i in range(0, 9):
            if(analyzeboard(board)!=0): #If someone has won, the entire thing (game) will close. Check 'break'.
                break
            if(i%2==0):
                User1Turn(board)
            else:
                ConstBoard(board)
                User2Turn(board)

    x = analyzeboard(board)     # This analyses who has won. This is the final value of analyze board
    if(x==0):
        ConstBoard(board)
        print("Draw!") 
    if(x==-1):
        ConstBoard(board)
        print("Player X Wins!!!  O Looses!")  
    if(x==1):
        ConstBoard(board)
        print("Player O Wins!!!  X Looses!")         


main()





