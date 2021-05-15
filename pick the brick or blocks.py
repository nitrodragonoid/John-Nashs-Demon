bricks = 10
turn = 1
board = [bricks,turn]

def is_ended(state):
    if state[0] > 0:
        return False
    else:
        return True

def utility(state):
    if (state[0] == 0) and (state[1] == 1): #turn being 2 means that player 2 did the last move
        return -1
    elif (state[0] == 0) and (state[1] == 2): #turn being 2 means that player 1 did the last move
        return 1

def action(state):
    if state[1] == 1: #If we are looking at player 1's move then set the next move to player 2 
        next = 2
    else: #If we are looking at player 2's move then set the next move to player 1
        next = 1
    out = []
    out.append((1,next)) #you can alway pick 1 brick, so we add that as a possible move   
    if state[0] > 1: #if more than 1 brick is left, then you can also pick 2 bricks, thus we add that as a move.
        out.append((2,next))
    return out

def result(state,move):
    temp = state.copy() #make a copy of the board so the og board isnt effected
    temp[0] = temp[0] - move[0] #remove the pbricks that the move tells to remove
    temp[1] = move[1] #set the turn to the next player
    return temp

def display(state):
    print("Blocks left: ", state[0])
    print("Next move is of player " + str(state[1]) + "\n")


def max_value(state):
    if is_ended(state) == True:
        return utility(state)
    v = -9999999
    for a in action(state):
        v = max(v,min_value(result(state,a)))
    return v

def min_value(state):
    if is_ended(state) == True:
        return utility(state)
    v = 9999999
    for a in action(state):
        v = min(v,max_value(result(state,a)))
    return v

def MAX(state):
    val = -9999999
    for a in action(state):
        check = state.copy()
        y = min_value(result(check,a))
        if y > val:
            val = y
            best = a
    return best

def MIN(state):
    val = 9999999
    for a in action(state):
        check = state.copy()     
        x = max_value(result(check,a))
        if x < val:
            val = x
            best = a
    return best

def minimax(state):
    if state[1] == 2:
        return MIN(state)
    elif state[1] == 1:
        return MAX(state)


def game_1st(state):
    display(state)
    while is_ended(state) != True:
        x = int(input("enter 1 to remove a brick, and 2 to remove 2: "))
        state = result(state, (x,2))
        display(state)
        if is_ended(state) == True:
            break
        state = result(state, minimax(state))
        display(state)
    if utility(state) == 1:
        print("player 1 won")
    else:
        print("player 2 won")

def game_2nd(state):
    display(state)
    while is_ended(state) != True:
        state = result(state, minimax(state))
        display(state)
        if is_ended(state) == True:
            break
        x = int(input("enter 1 to remove a brick, and 2 to remove 2: "))
        state = result(state, (x,2))
        display(state)
    if utility(state) == 1:
        print("player 1 won")
    else:
        print("player 2 won")

#game_1st(board)
game_2nd(board)
