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

def result(state, move):
    temp = []
    for i in state:
        temp.append(i.copy())
    for i in range(len(move)):
        for j in range(len(move[i])):
            if move[i][j] != 0:
                temp[i][j] = move[i][j]
    return temp
    
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

def max_value(state):
    if is_ended(state) == True:
        return utility(state)
    v = -9999999
    for a in action(state,check_turn(state)):
        if v < min_value(result(state,a)):
            v = min_value(result(state,a))
            best = a
    return v

def min_value(state):
    if is_ended(state) == True:
        return utility(state)
    v = 9999999
    for a in action(state,check_turn(state)):
        if v > max_value(result(state,a)):
            v = max_value(result(state,a))
            best = a
    return v

def MAX(state):
    val = -9999999
    for a in action(state,check_turn(state)):
        if max_value(result(state,a)) > val:
            val = max_value(result(state,a))
            best = a
    return best

def MIN(state):
    val = 9999999
    for a in action(state,check_turn(state)):
        if min_value(result(state,a)) < val:
            val = min_value(result(state,a))
            best = a
            print(best)
    return best

def minimax(state):
    if check_turn(state) == "O":
        return MIN(state)
    elif check_turn(state) == "X":
        return MAX(state)


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
        state = result(state,minimax(state))
        display(state)
    if utility(state) == 1:
        print("You won the game")
    elif utility(state) == -1:
        print("You lost the game")
    elif utility(state) == 0:
        print("The game was a draw")
    else:
        print("Error")
        
game_playing_x(board)


\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# GUI commit

import pygame, sys
import numpy as np
pygame.init()

# designing the tic tac toe game board
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
END_OF_GAME_LINE = 15
ROWS = 3
COLUMNS = 3
MOVE_SPACE_SIZE = 200
CIRCLE_RAD = 60
CIRCLE = 15
CROSS = 25
SPACE = 55

RED = (255, 0, 0)
BG_COLOR = (20, 200, 160)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE' )
screen.fill( BG_COLOR )

game_board = np.zeros( (ROWS, COLUMNS) )

# drawslines on the game board
def lines():
	
	pygame.draw.line( screen, LINE_COLOR, (0, MOVE_SPACE_SIZE), (WIDTH, MOVE_SPACE_SIZE), LINE_WIDTH )
	
	pygame.draw.line( screen, LINE_COLOR, (0, 2 * MOVE_SPACE_SIZE), (WIDTH, 2 * MOVE_SPACE_SIZE), LINE_WIDTH )

	pygame.draw.line( screen, LINE_COLOR, (MOVE_SPACE_SIZE, 0), (MOVE_SPACE_SIZE, HEIGHT), LINE_WIDTH )

	pygame.draw.line( screen, LINE_COLOR, (2 * MOVE_SPACE_SIZE, 0), (2 * MOVE_SPACE_SIZE, HEIGHT), LINE_WIDTH )

# draws either a cross or a circle as a move depending on the player
def shapes():
	for row in range(ROWS):
		for col in range(COLUMNS):
			if game_board[row][col] == 1:
				pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * MOVE_SPACE_SIZE + MOVE_SPACE_SIZE//2 ), int( row * MOVE_SPACE_SIZE + MOVE_SPACE_SIZE//2 )), CIRCLE_RAD, CIRCLE )
			elif game_board[row][col] == 2:
				pygame.draw.line( screen, CROSS_COLOR, (col * MOVE_SPACE_SIZE + SPACE, row * MOVE_SPACE_SIZE + MOVE_SPACE_SIZE - SPACE), (col * MOVE_SPACE_SIZE + MOVE_SPACE_SIZE - SPACE, row * MOVE_SPACE_SIZE + SPACE), CROSS )	
				pygame.draw.line( screen, CROSS_COLOR, (col * MOVE_SPACE_SIZE + SPACE, row * MOVE_SPACE_SIZE + SPACE), (col * MOVE_SPACE_SIZE + MOVE_SPACE_SIZE - SPACE, row * MOVE_SPACE_SIZE + MOVE_SPACE_SIZE - SPACE), CROSS )

def square(row, col, player):
	game_board[row][col] = player

# checks if a move space is empty or not
def vacant_move_space(row, col):
	return game_board[row][col] == 0

# checks if the board is full or not
def game_board_full():
	for row in range(ROWS):
		for col in range(COLUMNS):
			if game_board[row][col] == 0:
				return False

	return True

# checks if there are 3 moves in succession on the board and then calls line functions to draw a line
def check_3_moves(player):
	for col in range(COLUMNS):
		if game_board[0][col] == player and game_board[1][col] == player and game_board[2][col] == player:
			win_line_verical(col, player)
			return True

	for row in range(ROWS):
		if game_board[row][0] == player and game_board[row][1] == player and game_board[row][2] == player:
			win_line_horizontal(row, player)
			return True

	if game_board[2][0] == player and game_board[1][1] == player and game_board[0][2] == player:
		return True

	if game_board[0][0] == player and game_board[1][1] == player and game_board[2][2] == player:
		descending_diagonal_line(player)
		return True

	return False

# draws a line if the 3 winning moves are in a vertical line
def win_line_verical(col, player):
	posX = col * MOVE_SPACE_SIZE + MOVE_SPACE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )

# draws a line if the 3 winning moves are in a horizontal line
def win_line_horizontal(row, player):
	posY = row * MOVE_SPACE_SIZE + MOVE_SPACE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), END_OF_GAME_LINE )

# draws a line if the 3 winning moves are in the ascending diagonal
def ascending_diagonal_line(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), END_OF_GAME_LINE )

# draws a line if the 3 winning moves are in the descending diagonal
def descending_diagonal_line(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), END_OF_GAME_LINE )

def restart():
	screen.fill( BG_COLOR )
	lines()
	for row in range(ROWS):
		for col in range(COLUMNS):
			game_board[row][col] = 0

# the defined game functions above are used to construct the interface below this line
lines()

player = 1
game_over = False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

			X = event.pos[0] 
			Y = event.pos[1] 

			click_r = int(Y // MOVE_SPACE_SIZE)
			click_c = int(X // MOVE_SPACE_SIZE)

			if vacant_move_space( click_r, click_c ):

				square( click_r, click_c, player )
				if check_3_moves( player ):
					game_over = True
				player = player % 2 + 1

				shapes()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				restart()
				player = 1
				game_over = False

	pygame.display.update()
    
    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
