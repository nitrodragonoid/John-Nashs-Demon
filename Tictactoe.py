board =[[0,0,0],[0,0,0],[0,0,0]]

def is_ended(state):
    #check if draw
    end = True
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                end = False
    if end == True:
        return True
    #check if a win condition is met
    #for horizontal win
    for k in range(len(state)): 
        if (state[k][0] == state[k][1]) and (state[k][1] == state[k][2]):
            return True
    #for vertical win        
    for l in range(len(state[0])): 
        if (state[0][l] == state[1][l]) and (state[1][l] == state[2][l]):
            return True
    #for daignol win
    if (state[0][0] == state[1][1]) and (state[1][1] == state[2][2]):
        return True
    if (state[0][2] == state[1][1]) and (state[1][1] == state[2][1]):
        return True
    #if game not ended
    return False

def utility(state):
    #For O
    #for horizontal win
    for k in range(len(state)): 
        if state[0][0] == "O" and (state[k][0] == state[k][1]) and (state[k][1] == state[k][2]):
            return -1
    #for vertical win        
    for l in range(len(state[0])): 
        if state[0][0] == "O" and (state[0][l] == state[1][l]) and (state[1][l] == state[2][l]):
            return -1
    #for daignol win
    if state[0][0] == "O" and (state[0][0] == state[1][1]) and (state[1][1] == state[2][2]):
        return -1
    if state[0][0] == "O" and (state[0][2] == state[1][1]) and (state[1][1] == state[2][1]):
        return -1
    #For X
    #for horizontal win
    for k in range(len(state)): 
        if state[0][0] == "X" and (state[k][0] == state[k][1]) and (state[k][1] == state[k][2]):
            return 1
    #for vertical win        
    for l in range(len(state[0])): 
        if state[0][0] == "X" and (state[0][l] == state[1][l]) and (state[1][l] == state[2][l]):
            return 1
    #for daignol win
    if state[0][0] == "X" and (state[0][0] == state[1][1]) and (state[1][1] == state[2][2]):
        return 1
    if state[0][0] == "X" and (state[0][2] == state[1][1]) and (state[1][1] == state[2][1]):
        return 1
    #For draw
    end = True
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                end = False
    if end == True:
        return 0
    return False

def action(state,turn):
    out = []
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                move = [[0,0,0],[0,0,0],[0,0,0]]
                move[i][j] = turn
                out.append(move) 
    return out

def result(state,move):
    for i in range(len(move)):
        for j in range(len(move[i])):
            if move[i][j] != 0:
                state[i][j] = move[i][j] 
    return state
    
def check_turn(state):
    Xs = 0
    Os = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == "X":
                Xs += 1
            elif state[i][j] == "O":
                Os += 1
    if Xs != Os:
        return "O"
    else:
        return "X"

def display(state):
    for i in state:
        print(i)

#Will add minimax algorithm here tomorrow        
        
def game(initial):
    state = initial
    while is_ended != True:
        display(state)
        x = input()
        #if conditions for playing
        result(state,move)
        display(state)
        #call minimax
    if utility(state) == 1:
        print("X won the game")
    elif utility(state) == -1:
        print("O won the game")
    else:
        print("The game was a draw")

game(board)


