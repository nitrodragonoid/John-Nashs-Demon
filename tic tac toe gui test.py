import pygame
import sys
import time

#import tictactoe as ttt
####### BOT #######
X = "X"
O = "O"
EMPTY = 0
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

def action(state):
    moves = []
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == 0:
                moves.append((i,j))
    return moves

def result(state,move):
    temp = []
    for i in state:
        temp.append(i.copy())
    temp[move[0]][move[1]] = check_turn(state)
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
    print("\n")

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
        y = min_value(result(state,a))
        if y > val:
            val = y
            best = a
    return best

def MIN(state):
    val = 9999999
    for a in action(state):    
        x = max_value(result(state,a))
        if x < val:
            val = x
            best = a
    return best

def minimax(state):
    if check_turn(state) == "O":
        return MIN(state)
    elif check_turn(state) == "X":
        return MAX(state)

def winner(state):
    if utility(state) == 1:
        return "Player 1"
    elif utility(state) == -1:
        return "Player 2"
    elif utility(state) == 0:
        return None
    else:
       return False
        
#game_playing_x(board)
####### END #######

pygame.init()
size = width, height = 600, 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

user = None
ai_turn = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    # Let user choose a player.
    if user is None:

        # Draw title
        title = largeFont.render("Play Tic-Tac-Toe", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Draw buttons
        playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        playX = mediumFont.render("Play as X", True, black)
        playXRect = playX.get_rect()
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, white, playXButton)
        screen.blit(playX, playXRect)

        playOButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
        playO = mediumFont.render("Play as O", True, black)
        playORect = playO.get_rect()
        playORect.center = playOButton.center
        pygame.draw.rect(screen, white, playOButton)
        screen.blit(playO, playORect)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                time.sleep(0.2)
                user = X
            elif playOButton.collidepoint(mouse):
                time.sleep(0.2)
                user = O

    else:

        # Draw game board
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size),
                       height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)

                if board[i][j] != EMPTY:
                    move = moveFont.render(board[i][j], True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        game_over = is_ended(board)
        player = check_turn(board)

        # Show title
        if game_over:
            win = winner(board)
            if win == None:
                title = f"Game Over: Tie."
            else:
                title = f"Game Over: {win} wins."
        elif user == player:
            title = f"Play as {user}"
        else:
            title = f"Computer thinking..."
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        # Check for AI move
        if user != player and not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = minimax(board)
                board = result(board, move)
                ai_turn = False
            else:
                ai_turn = True

        # Check for a user move
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and user == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if (board[i][j] == EMPTY and tiles[i][j].collidepoint(mouse)):
                        board = result(board, (i, j))

        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Play Again", True, black)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = None
                    board = [[0,0,0],[0,0,0],[0,0,0]]
                    ai_turn = False

    pygame.display.flip()
