board = [[0,0,0],[0,0,0],[0,0,0]]

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
        if (state[k][0] == state[k][1]) and (state[k][1] == state[k][2]) and (state[k][0] != 0):
            return True
    #for vertical win        
    for l in range(len(state[0])): 
        if (state[0][l] == state[1][l]) and (state[1][l] == state[2][l]) and (state[0][l] != 0):
            return True
    #for daignol win
    if (state[0][0] == state[1][1]) and (state[1][1] == state[2][2]) and (state[1][1] != 0):
        return True
    if (state[0][2] == state[1][1]) and (state[1][1] == state[2][0]) and (state[1][1] != 0):
        return True
    #if game not ended
    return False

def utility(state):
    #For O
    #for horizontal win
    for k in range(len(state)): 
        if state[k][0] == "O" and (state[k][0] == state[k][1]) and (state[k][1] == state[k][2]):
            return -1
    #for vertical win        
    for l in range(len(state[0])): 
        if state[0][l] == "O" and (state[0][l] == state[1][l]) and (state[1][l] == state[2][l]):
            return -1
    #for daignol win
    if state[0][0] == "O" and (state[0][0] == state[1][1]) and (state[1][1] == state[2][2]):
        return -1
    if state[0][2] == "O" and (state[0][2] == state[1][1]) and (state[1][1] == state[2][0]):
        return -1
    #For X
    #for horizontal win
    for k in range(len(state)): 
        if state[k][0] == "X" and (state[k][0] == state[k][1]) and (state[k][1] == state[k][2]):
            return 1
    #for vertical win        
    for l in range(len(state[0])): 
        if state[0][l] == "X" and (state[0][l] == state[1][l]) and (state[1][l] == state[2][l]):
            return 1
    #for daignol win
    if state[0][0] == "X" and (state[0][0] == state[1][1]) and (state[1][1] == state[2][2]):
        return 1
    if state[0][2] == "X" and (state[0][2] == state[1][1]) and (state[1][1] == state[2][0]):
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

def game_playing_x(initial):    
    print("controls:")
    print("Y-Axis")
    print("For top: t")
    print("For middle: m")
    print("For Bottom: b")    
    print("X-Axis")
    print("For Left: l")
    print("For Center: c")
    print("For Right: r")
    print("Give command as tr")
    state = initial
    while is_ended(state) == False:
        display(state)
        command = input("Enter move: ")
        if command == "tl":
            move = [["X",0,0],[0,0,0],[0,0,0]]
        elif command == "tc":
            move = [[0,"X",0],[0,0,0],[0,0,0]]
        elif command == "tr":
            move = [[0,0,"X"],[0,0,0],[0,0,0]]
        elif command == "ml":
            move = [[0,0,0],["X",0,0],[0,0,0]]
        elif command == "mc":
            move = [[0,0,0],[0,"X",0],[0,0,0]]
        elif command == "mr":
            move = [[0,0,0],[0,0,"X"],[0,0,0]]
        elif command == "bl":
            move = [[0,0,0],[0,0,0],["X",0,0]]
        elif command == "bc":
            move = [[0,0,0],[0,0,0],[0,"X",0]]
        elif command == "br":
            move = [[0,0,0],[0,0,0],[0,0,"X"]]
        state = result(state,move)
        display(state)
        #call minimax
    if utility(state) == 1:
        print("You won the game")
    elif utility(state) == -1:
        print("You lost the game")
    elif utility(state) == 0:
        print("The game was a draw")
    else:
        print("Error")
        
game_playing_x(board)

