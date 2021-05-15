def possible_combinations(node):
    req = []
    for i in range(1, 3):
        if node[0]-i >= 0:
            req.append((node[0]-i, node[1] + (i,)))
    return req


def enQueue(queue, item):
    queue.append(item)


def deQueue(queue):
    return queue.pop(0)


def front(queue):
    return queue[-1]


def is_empty(queue):
    return len(queue) == 0


def addNodes(G, nodes):
    for i in nodes:
        G[i] = list()
    return G


def addEdges(G, edges, directed=False):
    if directed:
        for i, j, k in edges:
            try:
                G[i].append((j, k))
            except:
                return False
    else:
        for i, j, k in edges:
            try:
                G[i].append((j, k))
                G[j].append((i, k))
            except:
                return False
    return G


game_tree = dict()
nodes = []
edges = []
queue = []
start_node = (10, tuple())
enQueue(queue, start_node)
nodes.append(start_node)
while not(is_empty(queue)):
    parent = deQueue(queue)
    if parent[0] == 0:
        continue
    else:
        a = possible_combinations(parent)
        for i in a:
            enQueue(queue, i)
            nodes.append(i)
            edges.append((parent, i, 1))

addNodes(game_tree, nodes)
addEdges(game_tree, edges, True)
for i in game_tree:
    for j in game_tree[i]:
        if j[0][0] == 0:
            print(i)
            break

            
            
          
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
                    pygame.draw.circle(screen,(20, 200, 160),(x,y),20)
                    x += 50
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.circle(screen,(20, 200, 160),(x,y),20)
                    x += 50
                    pygame.draw.circle(screen,(20, 200, 160),(x,y),20)
                    x += 50                    
        pygame.display.update()
    pygame.quit()
 
menu()
