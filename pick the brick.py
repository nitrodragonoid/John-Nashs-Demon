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



""" GUI for the Game""" # to be integrated with the bot

import pygame

pygame.init()

# making the main screen
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption( 'Pick the Block' )
BG_COLOR = (100, 200, 160)
screen.fill( BG_COLOR )

# a function for making buttons
def button(screen, position, text):
    font = pygame.font.SysFont('timesnewroman', 50)
    text_render = font.render(text, 1, (150, 100, 100))
    x, y, width , height = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (0, 0, 150), (x, y), (x + width , y), 5)
    pygame.draw.line(screen, (0, 0, 150), (x, y - 2), (x, y + height), 5)
    pygame.draw.line(screen, (0, 0, 150), (x, y + height), (x + width , y + height), 5)
    pygame.draw.line(screen, (0, 0, 150), (x + width , y + height), [x + width , y], 5)
    pygame.draw.rect(screen, (0, 255, 255), (x, y, width , height))
    return screen.blit(text_render, (x, y))
 
# main function for the game and bot
def menu():
    """ This is the main game GUI and bot function """
    # initialising co=ordinates for the blocks and the buttons
    x = 75
    y = 50

    # making circular blocks numbered 1-10

        pygame.draw.circle(screen,(200,200,100),(x,y),20)
    font = pygame.font.SysFont('timesnewroman', 20)
    text_1 = font.render("1",True,(150, 100, 100))
    textRect_1 = text_1.get_rect()
    textRect_1.center = (x, y)
    screen.blit(text_1,textRect_1)
    x += 50
    pygame.draw.circle(screen,(255,255,0),(x,y),20)
    font = pygame.font.SysFont('timesnewroman', 20)
    text_2 = font.render("2",True,(150, 100, 100))
    textRect_2 = text_2.get_rect()
    textRect_2.center = (x, y)
    screen.blit(text_2,textRect_2)
    x += 50
    pygame.draw.circle(screen,(200,200,100),(x,y),20)
    font = pygame.font.SysFont('timesnewroman', 20)
    text_3 = font.render("3",True,(150, 100, 100))
    textRect_3 = text_3.get_rect()
    textRect_3.center = (x, y)
    screen.blit(text_3,textRect_3)
    x += 50
    pygame.draw.circle(screen,(255,255,0),(x,y),20)
    font = pygame.font.SysFont('timesnewroman', 20)
    text_4 = font.render("4",True,(150, 100, 100))
    textRect_4 = text_4.get_rect()
    textRect_4.center = (x, y)
    screen.blit(text_4,textRect_4)
    x += 50
    pygame.draw.circle(screen,(170,200,230),(x,y),20)
    font = pygame.font.SysFont('timesnewroman', 20)
    text_5 = font.render("5",True,(150, 100, 100))
    textRect_5 = text_5.get_rect()
    textRect_5.center = (x, y)
    screen.blit(text_5,textRect_5)
    x += 50
    pygame.draw.circle(screen,(170,200,230),(x,y),20)
    font = pygame.font.SysFont('timesnewroman', 20)
    text_6 = font.render("6",True,(150, 100, 100))
    textRect_6 = text_6.get_rect()
    textRect_6.center = (x, y)
    screen.blit(text_6,textRect_6)
    x += 50
    pygame.draw.circle(screen,(255,255,0),(x,y),20)
    font = pygame.font.SysFont('timesnewroman', 20)
    text_7 = font.render("7",True,(150, 100, 100))
    textRect_7 = text_7.get_rect()
    textRect_7.center = (x, y)
    screen.blit(text_7,textRect_7)
    x += 50
    pygame.draw.circle(screen,(200,200,100),(x,y),20)
    font = pygame.font.SysFont('timesnewroman', 20)
    text_8 = font.render("8",True,(150, 100, 100))
    textRect_8 = text_8.get_rect()
    textRect_8.center = (x, y)
    screen.blit(text_8,textRect_8)
    x += 50
    pygame.draw.circle(screen,(255,255,0),(x,y),20)
    font = pygame.font.SysFont('timesnewroman', 20)
    text_9 = font.render("9",True,(150, 100, 100))
    textRect_9 = text_9.get_rect()
    textRect_9.center = (x, y)
    screen.blit(text_9,textRect_9)
    x += 50
    pygame.draw.circle(screen,(200,200,100),(x,y),20)
    font = pygame.font.SysFont('timesnewroman', 20)
    text_10 = font.render("10",True,(150, 100, 100))
    textRect_10 = text_10.get_rect()
    textRect_10.center = (x, y)
    screen.blit(text_10,textRect_10)
    
    x = 75

    # making the buttons for picking either 1 or 2 blocks
    b1 = button(screen, (185, 150), "Pick 1 Block")
    b2 = button(screen, (175, 300), "Pick 2 Blocks")

    # main game loop
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            # checks if the mouse has been clicked 
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                # checks if 1 block has to be picked or 2 according to the move. Makes the bot unravel its algorithm, and make the move accordingly. To be updated with the bot, changes to be made as the bot will not click the mouse so the blocks still have to be removed when the bot makes a move.
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.circle(screen,(100, 200, 160),(x,y),20)
                    x += 50
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.circle(screen,(100, 200, 160),(x,y),20)
                    x += 50
                    pygame.draw.circle(screen,(100, 200, 160),(x,y),20)
                    x += 50                    
        pygame.display.update()
    pygame.quit()
 
menu()
