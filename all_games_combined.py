from numpy.lib.function_base import append
import pygame
import numpy as np
pygame.init()
import time
import sys 
from numpy.core.fromnumeric import diagonal

""" Domineering code """
def Domineering():
    grid = [[0 for _ in range(4)] for __ in range(3)]


    def lines():
        pygame.draw.line(interface, (255, 255, 255), (20, 100), (620, 100), 5)
        pygame.draw.line(interface, (255, 255, 255), (20, 250), (620, 250), 5)
        pygame.draw.line(interface, (255, 255, 255), (20, 400), (620, 400), 5)
        pygame.draw.line(interface, (255, 255, 255), (20, 550), (620, 550), 5)
        pygame.draw.line(interface, (255, 255, 255), (20, 100), (20, 550), 5)
        pygame.draw.line(interface, (255, 255, 255), (170, 100), (170, 550), 5)
        pygame.draw.line(interface, (255, 255, 255), (320, 100), (320, 550), 5)
        pygame.draw.line(interface, (255, 255, 255), (470, 100), (470, 550), 5)
        pygame.draw.line(interface, (255, 255, 255), (620, 100), (620, 550), 5)


    game_tree = dict()


    def push(stack, item):
        stack.append(item)


    def pop(stack):
        return stack.pop()


    def top(stack):
        return stack[-1]


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


    def enQueue(queue, item):
        queue.append(item)


    def deQueue(queue):
        return queue.pop(0)


    def front(queue):
        return queue[-1]


    def is_empty(queue):
        return len(queue) == 0


    def list_to_tuple(grid):
        tmp = grid.copy()
        req = tuple()
        for i in tmp:
            req += (tuple(i),)
        return req


    def player_determiner(grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    count += 1
        count = count//2
        if count % 2 == 1:
            return 2
        return 1


    def is_full(grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    if i+1 >= len(grid):
                        pass
                    else:
                        if grid[i+1][j] == 0:
                            return False
                    if j+1 >= len(grid[i]):
                        pass
                    else:
                        if grid[i][j+1] == 0:
                            return False
        return True


    def possible_combinations(grid, p_no):
        a = [list(i) for i in grid]
        req = []
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == 0:
                    if i+1 < len(a) and a[i+1][j] == 0:
                        new_comb = []
                        for x in a:
                            new_comb.append(x.copy())
                        new_comb[i][j] = str(p_no) + "v"
                        new_comb[i+1][j] = str(p_no) + "v"
                        b = list_to_tuple(new_comb.copy())
                        req.append(b)
                    if j+1 < len(a[i]) and a[i][j+1] == 0:
                        new_comb = []
                        for x in a:
                            new_comb.append(x.copy())
                        new_comb[i][j] = str(p_no)+"h"
                        new_comb[i][j+1] = str(p_no) + "h"
                        b = list_to_tuple(new_comb.copy())
                        req.append(b)
        return req


    def update_grid(grid, idx1, idx2, p_no):
        a = idx1
        b = idx2
        if (a[0]+1 == b[0] and a[1] == b[1]):
            grid[a[0]][a[1]] = str(p_no)+"v"
            grid[b[0]][b[1]] = str(p_no)+"v"
        elif (a[0] == b[0] and a[1]+1 == b[1]):
            grid[a[0]][a[1]] = str(p_no)+"h"
            grid[b[0]][b[1]] = str(p_no)+"h"


    def display_grid(grid):
        for i in grid:
            print(i)


    def dfs(graph, current_state, comp_no, visited, parent):
        visited.append(current_state)
        for i in graph[current_state]:
            if not(i[0] in visited):
                parent[i[0]] = current_state
                if len(graph[i[0]]) == 0 and player_determiner(current_state) != comp_no:
                    return
                else:
                    dfs(graph, i[0], comp_no, visited, parent)


    def bot(grid, p_no, graph):
        visited = []
        parent = dict()
        temp = list_to_tuple(grid.copy())
        parent[temp] = temp
        dfs(graph, temp, p_no, visited, parent)
        a = tuple()
        cd = True
        for i in visited:
            if len(graph[i]) == 0:
                a = i
                break
        if len(a) == 0:
            for i in visited:
                if i != temp:
                    a = i
                    cd = False
                    break
        sequence = list()
        while a != temp:
            sequence.append(a)
            a = parent[a]
        sequence.append(temp)
        for i in sequence:
            display_grid(i)
            print()
        if cd:
            return sequence[-2]
        else:
            for i in sequence:
                if i != temp:
                    return i


    def tuple_to_list(grid):
        lst = []
        for i in grid:
            lst.append(list(i))
        return lst


    def list_coordinates(cod):
        x = float('inf')
        y = float('inf')
        if cod[0] in range(20, 171):
            y = 0
        elif cod[0] in range(171, 321):
            y = 1
        elif cod[0] in range(321, 471):
            y = 2
        elif cod[0] in range(471, 621):
            y = 3
        if cod[1] in range(100, 251):
            x = 0
        elif cod[1] in range(251, 401):
            x = 1
        elif cod[1] in range(401, 551):
            x = 2
        return (x, y)


    def is_adjacent(pos_1, pos_2):
        if pos_1[0]+1 == pos_2[0] and pos_1[1] == pos_2[1]:
            return True
        elif pos_1[0] == pos_2[0] and pos_1[1]+1 == pos_2[1]:
            return True
        return False


    def is_vertical(st1, st2):
        if st1[0]+1 == st2[0]:
            return True


    def make_square(interface, player_no, st1, st2):
        if player_no == 1:
            color = red
            color_1 = blue
        else:
            color = blue
            color_1 = red

        if st1[0]+1 == st2[0]:
            a = pygame.Rect(left_scale[st1[1]]+2,
                            top_scale[st1[0]]+2, 146, 296)
            text = font.render(str(player_no), True, color_1)
            textrect = text.get_rect()
            textrect.center = (
                (left_scale[st1[1]]+75, (top_scale[st1[0]]+150)))
        else:
            a = pygame.Rect(left_scale[st1[1]]+2,
                            top_scale[st1[0]]+2, 296, 146)
            text = font.render(str(player_no), True, color_1)
            textrect = text.get_rect()
            textrect.center = (
                (left_scale[st1[1]]+150), (top_scale[st1[0]]+75))
        pygame.draw.rect(interface, color, a)
        b = pygame.Rect(0, 0, 640, 97.5)
        pygame.draw.rect(interface, black, b)
        interface.blit(text, textrect)


    def add_cods(previous, now):
        req = []
        for i in range(len(previous)):
            for j in range(len(previous[i])):
                if previous[i][j] != now[i][j]:
                    req.append((i, j))
        return req


    def comes_after(pos_1, pos_2):
        if pos_1[0] > pos_2[0]:
            return True
        elif pos_1[1] > pos_2[1]:
            return True
        return False


    red = (255, 0, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)
    test1 = [['1h', '1h', 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    count = 0


    nodes = []
    edges = []
    queue = []

    a = list_to_tuple(grid)
    enQueue(queue, a)
    nodes.append(a)
    while not(is_empty(queue)):
        parent = deQueue(queue)
        if is_full(parent):
            continue
        else:
            p_no = player_determiner(parent)
            possibilities = possible_combinations(parent, p_no)
            for i in possibilities:
                enQueue(queue, i)
                nodes.append(i)
                edges.append((parent, i, 1))
    addNodes(game_tree, nodes)
    addEdges(game_tree, edges, True)
    count = 0
    last_turn = 0

    interface = pygame.display.set_mode((640, 570))
    pygame.display.set_caption("Domineering")
    interface.fill((0, 0, 0))
    board = np.zeros((3, 4))
    font = pygame.font.Font('freesansbold.ttf', 40)
    left_scale = {0: 20, 1: 170, 2: 320, 3: 470}
    top_scale = {0: 100, 1: 250, 2: 400}
    turn = 0
    used_space = []
    lines()
    closed = False
    while not(closed):
        a = player_determiner(grid)
        if is_full(grid):
            winner = int()
            if a == 2:
                winner = 1
            else:
                winner = 2
            b = pygame.Rect(0, 0, 640, 97.5)
            pygame.draw.rect(interface, black, b)
            text = font.render('''Player ''' + str(winner) +
                            ''' Won !!''', True, (255, 255, 255))
            textrect = text.get_rect()
            textrect.center = (320, 40)
        else:
            text = font.render('''Player ''' + str(a) +
                            ''''s Turn''', True, (255, 255, 255))
            textrect = text.get_rect()
            textrect.center = (320, 40)
        interface.blit(text, textrect)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                closed = True
            if i.type == pygame.MOUSEBUTTONDOWN and is_full(grid):
                pass
            if i.type == pygame.MOUSEBUTTONDOWN and turn % 2 == 0 and int(count//0.5) % 2 == 0 and not(is_full(grid)):
                coord_1 = list_coordinates(i.pos)
                if not(coord_1 in used_space):
                    count += 0.5
                    used_space.append(coord_1)
            elif i.type == pygame.MOUSEBUTTONDOWN and turn % 2 == 0 and int(count//0.5) % 2 == 1 and not(is_full(grid)):
                coord_2 = list_coordinates(i.pos)
                if not(coord_2 in used_space):
                    if comes_after(coord_1, coord_2):
                        temp = coord_1
                        coord_1 = coord_2
                        coord_2 = temp
                    if is_adjacent(coord_1, coord_2):
                        used_space.append(coord_2)
                        update_grid(grid, coord_1, coord_2, a)
                        make_square(interface, a, coord_1, coord_2)
                        count += 0.5
                        turn += 1

            elif turn % 2 == 1 and not(is_full(grid)):
                x = bot(grid, player_determiner(test1), game_tree)
                coords = add_cods(grid, tuple_to_list(x))
                used_space.extend(coords)
                grid = tuple_to_list(x).copy()
                make_square(interface, a, coords[0], coords[1])
                turn += 1
        pygame.display.update()


""" Pick the brick code """
def Pick_The_Brick():
    """ GUI for the Game"""  # integrated with the bot
    # making the main screen
    screen = pygame.display.set_mode((640, 570))
    pygame.display.set_caption('Pick the Block')
    BG_COLOR = (100, 200, 160)
    black = (0, 0, 0)
    screen.fill(black)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)

    # a function for making buttons


    def button(screen, position, text):
        font = pygame.font.SysFont('timesnewroman', 50)
        text_render = font.render(text, 1, (150, 100, 100))
        x, y, width, height = text_render.get_rect()
        x, y = position
        pygame.draw.line(screen, (0, 0, 150), (x, y), (x + width, y), 5)
        pygame.draw.line(screen, (0, 0, 150), (x, y - 2), (x, y + height), 5)
        pygame.draw.line(screen, (0, 0, 150), (x, y + height),
                        (x + width, y + height), 5)
        pygame.draw.line(screen, (0, 0, 150), (x + width,
                                            y + height), [x + width, y], 5)
        pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))
        return screen.blit(text_render, (x, y))


    def menu(state):
        """ This is the main game GUI and bot function """
        header_font = pygame.font.SysFont('timesnewroman', 50)
        header_text = header_font.render("Your Turn", True, (255, 255, 255))
        header_textRect = header_text.get_rect()
        header_textRect.center = (320, 85)
        screen.blit(header_text, header_textRect)
        # initialising co=ordinates for the blocks and the buttons
        x = 100
        y = 200

        # making circular blocks numbered 1-10

        pygame.draw.circle(screen, (200, 200, 100), (x, y), 20)
        font = pygame.font.SysFont('timesnewroman', 20)
        text_1 = font.render("1", True, (150, 100, 100))
        textRect_1 = text_1.get_rect()
        textRect_1.center = (x, y)
        screen.blit(text_1, textRect_1)
        x += 50
        pygame.draw.circle(screen, (255, 255, 0), (x, y), 20)
        font = pygame.font.SysFont('timesnewroman', 20)
        text_2 = font.render("2", True, (150, 100, 100))
        textRect_2 = text_2.get_rect()
        textRect_2.center = (x, y)
        screen.blit(text_2, textRect_2)
        x += 50
        pygame.draw.circle(screen, (200, 200, 100), (x, y), 20)
        font = pygame.font.SysFont('timesnewroman', 20)
        text_3 = font.render("3", True, (150, 100, 100))
        textRect_3 = text_3.get_rect()
        textRect_3.center = (x, y)
        screen.blit(text_3, textRect_3)
        x += 50
        pygame.draw.circle(screen, (255, 255, 0), (x, y), 20)
        font = pygame.font.SysFont('timesnewroman', 20)
        text_4 = font.render("4", True, (150, 100, 100))
        textRect_4 = text_4.get_rect()
        textRect_4.center = (x, y)
        screen.blit(text_4, textRect_4)
        x += 50
        pygame.draw.circle(screen, (170, 200, 230), (x, y), 20)
        font = pygame.font.SysFont('timesnewroman', 20)
        text_5 = font.render("5", True, (150, 100, 100))
        textRect_5 = text_5.get_rect()
        textRect_5.center = (x, y)
        screen.blit(text_5, textRect_5)
        x += 50
        pygame.draw.circle(screen, (170, 200, 230), (x, y), 20)
        font = pygame.font.SysFont('timesnewroman', 20)
        text_6 = font.render("6", True, (150, 100, 100))
        textRect_6 = text_6.get_rect()
        textRect_6.center = (x, y)
        screen.blit(text_6, textRect_6)
        x += 50
        pygame.draw.circle(screen, (255, 255, 0), (x, y), 20)
        font = pygame.font.SysFont('timesnewroman', 20)
        text_7 = font.render("7", True, (150, 100, 100))
        textRect_7 = text_7.get_rect()
        textRect_7.center = (x, y)
        screen.blit(text_7, textRect_7)
        x += 50
        pygame.draw.circle(screen, (200, 200, 100), (x, y), 20)
        font = pygame.font.SysFont('timesnewroman', 20)
        text_8 = font.render("8", True, (150, 100, 100))
        textRect_8 = text_8.get_rect()
        textRect_8.center = (x, y)
        screen.blit(text_8, textRect_8)
        x += 50
        pygame.draw.circle(screen, (255, 255, 0), (x, y), 20)
        font = pygame.font.SysFont('timesnewroman', 20)
        text_9 = font.render("9", True, (150, 100, 100))
        textRect_9 = text_9.get_rect()
        textRect_9.center = (x, y)
        screen.blit(text_9, textRect_9)
        x += 50
        pygame.draw.circle(screen, (200, 200, 100), (x, y), 20)
        font = pygame.font.SysFont('timesnewroman', 20)
        text_10 = font.render("10", True, (150, 100, 100))
        textRect_10 = text_10.get_rect()
        textRect_10.center = (x, y)
        screen.blit(text_10, textRect_10)

        x = 100

        # making the buttons for picking either 1 or 2 blocks
        b1 = button(screen, (185, 300), "Pick 1 Block")
        b2 = button(screen, (175, 450), "Pick 2 Blocks")

        # main game loop
        start = True
        while start:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    start = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                if is_ended(state):
                    continue
                # checks if the mouse has been clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # checks if 1 block has to be picked or 2 according to the move.
                    # Makes the bot unravel its algorithm, and make the move accordingly.
                    # To be updated with the bot, changes to be made as the bot will not click the mouse
                    # so the blocks still have to be removed when the bot makes a move.
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        pygame.draw.circle(screen, black, (x, y), 20)
                        x += 50
                        state = result(state, (1, 2))
                        if x >= 600:
                            rectangle = pygame.Rect(0, 0, 640, 180)
                            pygame.draw.rect(screen, black, rectangle)
                            header_font = pygame.font.SysFont('timesnewroman', 50)
                            header_text = header_font.render(
                                "You Won", True, (255, 255, 255))
                            header_textRect = header_text.get_rect()
                            header_textRect.center = (320, 85)
                            screen.blit(header_text, header_textRect)
                        else:
                            rectangle = pygame.Rect(0, 0, 640, 180)
                            pygame.draw.rect(screen, black, rectangle)
                            header_font = pygame.font.SysFont('timesnewroman', 50)
                            header_text = header_font.render(
                                "Demon's Turn", True, (255, 255, 255))
                            header_textRect = header_text.get_rect()
                            header_textRect.center = (320, 85)
                            screen.blit(header_text, header_textRect)
                    elif b2.collidepoint(pygame.mouse.get_pos()):
                        pygame.draw.circle(screen, black, (x, y), 20)
                        x += 50
                        pygame.draw.circle(screen, black, (x, y), 20)
                        x += 50
                        state = result(state, (2, 2))
                        if x >= 600:
                            rectangle = pygame.Rect(0, 0, 640, 180)
                            pygame.draw.rect(screen, black, rectangle)
                            header_font = pygame.font.SysFont('timesnewroman', 50)
                            header_text = header_font.render(
                                "You Won", True, (255, 255, 255))
                            header_textRect = header_text.get_rect()
                            header_textRect.center = (320, 85)
                            screen.blit(header_text, header_textRect)
                        else:
                            rectangle = pygame.Rect(0, 0, 640, 180)
                            pygame.draw.rect(screen, black, rectangle)
                            header_font = pygame.font.SysFont('timesnewroman', 50)
                            header_text = header_font.render(
                                "Demon's Turn", True, (255, 255, 255))
                            header_textRect = header_text.get_rect()
                            header_textRect.center = (320, 85)
                            screen.blit(header_text, header_textRect)

                    pygame.display.update()
                    if is_ended(state) == True:
                        break
                    time.sleep(1)
                    move = minimax(state)
                    state = result(state, move)
                    if move[0] == 1:
                        pygame.draw.circle(screen, black, (x, y), 20)
                        x += 50
                        if x >= 600:
                            rectangle = pygame.Rect(0, 0, 640, 180)
                            pygame.draw.rect(screen, black, rectangle)
                            header_font = pygame.font.SysFont('timesnewroman', 50)
                            header_text = header_font.render(
                                "Demon Won", True, (255, 255, 255))
                            header_textRect = header_text.get_rect()
                            header_textRect.center = (320, 85)
                            screen.blit(header_text, header_textRect)
                        else:
                            rectangle = pygame.Rect(0, 0, 640, 180)
                            pygame.draw.rect(screen, black, rectangle)
                            header_font = pygame.font.SysFont('timesnewroman', 50)
                            header_text = header_font.render(
                                "Your Turn", True, (255, 255, 255))
                            header_textRect = header_text.get_rect()
                            header_textRect.center = (320, 85)
                            screen.blit(header_text, header_textRect)
                    elif move[0] == 2:
                        pygame.draw.circle(screen, black, (x, y), 20)
                        x += 50
                        pygame.draw.circle(screen, black, (x, y), 20)
                        x += 50
                        if x >= 600:
                            rectangle = pygame.Rect(0, 0, 640, 180)
                            pygame.draw.rect(screen, black, rectangle)
                            header_font = pygame.font.SysFont('timesnewroman', 50)
                            header_text = header_font.render(
                                "Demon Won", True, (255, 255, 255))
                            header_textRect = header_text.get_rect()
                            header_textRect.center = (320, 85)
                            screen.blit(header_text, header_textRect)
                        else:
                            rectangle = pygame.Rect(0, 0, 640, 180)
                            pygame.draw.rect(screen, black, rectangle)
                            header_font = pygame.font.SysFont('timesnewroman', 50)
                            header_text = header_font.render(
                                "Your Turn", True, (255, 255, 255))
                            header_textRect = header_text.get_rect()
                            header_textRect.center = (320, 85)
                            screen.blit(header_text, header_textRect)

                pygame.display.update()


    ####### BOT #######
    bricks = 10
    turn = 1
    board = [bricks, turn]


    def is_ended(state):
        if state[0] > 0:
            return False
        else:
            return True


    def utility(state):
        if (state[0] == 0) and (state[1] == 1):  # turn being 2 means that player 2 did the last move
            return -1
        # turn being 2 means that player 1 did the last move
        elif (state[0] == 0) and (state[1] == 2):
            return 1


    def action(state):
        if state[1] == 1:  # If we are looking at player 1's move then set the next move to player 2
            next = 2
        else:  # If we are looking at player 2's move then set the next move to player 1
            next = 1
        out = []
        # you can alway pick 1 brick, so we add that as a possible move
        out.append((1, next))
        # if more than 1 brick is left, then you can also pick 2 bricks, thus we add that as a move.
        if state[0] > 1:
            out.append((2, next))
        return out


    def result(state, move):
        temp = state.copy()  # make a copy of the board so the og board isnt effected
        # remove the pbricks that the move tells to remove
        temp[0] = temp[0] - move[0]
        temp[1] = move[1]  # set the turn to the next player
        return temp


    def display(state):
        print("Blocks left: ", state[0])
        print("Next move is of player " + str(state[1]) + "\n")


    def max_value(state):
        if is_ended(state) == True:
            return utility(state)
        v = -9999999
        for a in action(state):
            v = max(v, min_value(result(state, a)))
        return v


    def min_value(state):
        if is_ended(state) == True:
            return utility(state)
        v = 9999999
        for a in action(state):
            v = min(v, max_value(result(state, a)))
        return v


    def MAX(state):
        val = -9999999
        for a in action(state):
            check = state.copy()
            w = min_value(result(check, a))
            if w > val:
                val = w
                best = a
        return best


    def MIN(state):
        val = 9999999
        for a in action(state):
            check = state.copy()
            z = max_value(result(check, a))
            if z < val:
                val = z
                best = a
        return best


    def minimax(state):
        if state[1] == 2:
            return MIN(state)
        elif state[1] == 1:
            return MAX(state)
    ####### END #######


    menu(board)

""" Tic Tac Toe code """

def Tic_Tac_Toe():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    def is_ended(state):
        # check if draw
        end = True
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    end = False
        if end == True:
            return True
        # check if a win condition is met
        # for horizontal win
        for k in range(len(state)):
            if (state[k][0] == state[k][1]) and (state[k][1] == state[k][2]) and (state[k][0] != 0):
                return True
        # for vertical win
        for l in range(len(state[0])):
            if (state[0][l] == state[1][l]) and (state[1][l] == state[2][l]) and (state[0][l] != 0):
                return True
        # for daignol win
        if (state[0][0] == state[1][1]) and (state[1][1] == state[2][2]) and (state[1][1] != 0):
            return True
        if (state[0][2] == state[1][1]) and (state[1][1] == state[2][0]) and (state[1][1] != 0):
            return True
        # if game not ended
        return False


    def utility(state):
        # For O
        # for horizontal win
        for k in range(len(state)):
            if state[k][0] == "O" and (state[k][0] == state[k][1]) and (state[k][1] == state[k][2]):
                return -1
        # for vertical win
        for l in range(len(state[0])):
            if state[0][l] == "O" and (state[0][l] == state[1][l]) and (state[1][l] == state[2][l]):
                return -1
        # for daignol win
        if state[0][0] == "O" and (state[0][0] == state[1][1]) and (state[1][1] == state[2][2]):
            return -1
        if state[0][2] == "O" and (state[0][2] == state[1][1]) and (state[1][1] == state[2][0]):
            return -1
        # For X
        # for horizontal win
        for k in range(len(state)):
            if state[k][0] == "X" and (state[k][0] == state[k][1]) and (state[k][1] == state[k][2]):
                return 1
        # for vertical win
        for l in range(len(state[0])):
            if state[0][l] == "X" and (state[0][l] == state[1][l]) and (state[1][l] == state[2][l]):
                return 1
        # for daignol win
        if state[0][0] == "X" and (state[0][0] == state[1][1]) and (state[1][1] == state[2][2]):
            return 1
        if state[0][2] == "X" and (state[0][2] == state[1][1]) and (state[1][1] == state[2][0]):
            return 1
        # For draw
        end = True
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    end = False
        if end == True:
            return 0
        return False


    def action(state, turn):  # outputs the list of all the possible moves
        out = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    move = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
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


    def draw_win_line(state):
        infinity = float('inf')
        start = (infinity, infinity)
        line_type = None
        # For O
        # for horizontal win
        for k in range(len(state)):
            if state[k][0] == "O" and (state[k][0] == state[k][1]) and (state[k][1] == state[k][2]):
                start = k, 0
                line_type = "horizontalo"
        # for vertical win
        for l in range(len(state[0])):
            if state[0][l] == "O" and (state[0][l] == state[1][l]) and (state[1][l] == state[2][l]):
                start = 0, l
                line_type = "verticalo"
        # for daignol win
        if state[0][0] == "O" and (state[0][0] == state[1][1]) and (state[1][1] == state[2][2]):
            start = 0, 0
            end = 2, 2
            line_type = "diagonalo"
        if state[0][2] == "O" and (state[0][2] == state[1][1]) and (state[1][1] == state[2][0]):
            start = 0, 2
            end = 2, 0
            line_type = "diagonalo"
        # For X
        # for horizontal win
        for k in range(len(state)):
            if state[k][0] == "X" and (state[k][0] == state[k][1]) and (state[k][1] == state[k][2]):
                start = k, 0
                line_type = "horizontalx"
        # for vertical win
        for l in range(len(state[0])):
            if state[0][l] == "X" and (state[0][l] == state[1][l]) and (state[1][l] == state[2][l]):
                start = 0, l
                line_type = "verticalx"
        # for daignol win
        if state[0][0] == "X" and (state[0][0] == state[1][1]) and (state[1][1] == state[2][2]):
            start = 0, 0
            end = 2, 2
            line_type = "diagonalx"
        if state[0][2] == "X" and (state[0][2] == state[1][1]) and (state[1][1] == state[2][0]):
            start = 0, 2
            end = 2, 0
            line_type = "diagonalx"
        if line_type == "horizontalo":
            pygame.draw.line(
                screen, red, (left_scale[start[1]], top_scale[start[0]]+75), (545, top_scale[start[0]]+75))
        elif line_type == "verticalo":
            pygame.draw.line(
                screen, red, (left_scale[start[1]]+75, top_scale[start[0]]), (left_scale[start[1]]+75, 550))
        elif line_type == "horizontalx":
            pygame.draw.line(
                screen, blue, (left_scale[start[1]], top_scale[start[0]]+75), (545, top_scale[start[0]]+75))
        elif line_type == "verticalx":
            pygame.draw.line(
                screen, blue, (left_scale[start[1]]+75, top_scale[start[0]]), (left_scale[start[1]]+75, 550))
        elif line_type == "diagonalo":
            if start == (0, 0):
                pygame.draw.line(
                    screen, red, (left_scale[start[1]], top_scale[start[0]]), (left_scale[end[1]]+150, 550))
            else:
                pygame.draw.line(
                    screen, red, (left_scale[start[1]]+150, top_scale[start[0]]), (left_scale[end[1]], 550))
        elif line_type == "diagonalx":
            if start == (0, 0):
                pygame.draw.line(
                    screen, blue, (left_scale[start[1]], top_scale[start[0]]), (left_scale[end[1]]+150, 550))
            else:
                pygame.draw.line(
                    screen, blue, (left_scale[start[1]]+150, top_scale[start[0]]), (left_scale[end[1]], 550))


    def display(state):
        for i in state:
            print(i)


    def max_value(state):
        if is_ended(state) == True:
            return utility(state)
        v = -9999999
        for a in action(state, check_turn(state)):
            v = max(v, min_value(result(state, a)))
        return v


    def min_value(state):
        if is_ended(state) == True:
            return utility(state)
        v = 9999999
        for a in action(state, check_turn(state)):
            v = min(v, max_value(result(state, a)))
        return v


    def MAX(state):
        val = -9999999
        for a in action(state, check_turn(state)):
            check = state.copy()
            y = min_value(result(check, a))
            if y > val:
                val = y
                best = a
        return best


    def MIN(state):
        val = 9999999
        for a in action(state, check_turn(state)):
            check = state.copy()
            x = max_value(result(check, a))
            if x < val:
                val = x
                best = a
        return best


    def minimax(state):
        if check_turn(state) == "O":
            return MIN(state)
        elif check_turn(state) == "X":
            return MAX(state)


    pygame.init()

    # designing the tic tac toe game board
    red = (255, 0, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)
    WIDTH = 640
    HEIGHT = 570
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
    BG_COLOR = (100, 200, 160)
    LINE_COLOR = (75, 145, 135)
    CIRCLE_COLOR = (239, 231, 200)
    CROSS_COLOR = (66, 66, 66)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('TIC TAC TOE')
    screen.fill(black)
    font = pygame.font.Font('freesansbold.ttf', 40)
    large_font = pygame.font.Font('freesansbold.ttf', 150)


    game_board = np.zeros((ROWS, COLUMNS))

    # drawslines on the game board


    def lines():
        pygame.draw.line(screen, white, (95, 100), (545, 100), 5)
        pygame.draw.line(screen, white, (95, 250), (545, 250), 5)
        pygame.draw.line(screen, white, (95, 400), (545, 400), 5)
        pygame.draw.line(screen, white, (95, 550), (545, 550), 5)
        pygame.draw.line(screen, white, (95, 100), (95, 550), 5)
        pygame.draw.line(screen, white, (245, 100), (245, 550), 5)
        pygame.draw.line(screen, white, (395, 100), (395, 550), 5)
        pygame.draw.line(screen, white, (545, 100), (545, 550), 5)

        return True


    def list_coordinates(a, b):
        x = float('inf')
        y = float('inf')
        if a in range(95, 246):
            y = 0
        elif a in range(246, 396):
            y = 1
        elif a in range(396, 546):
            y = 2
        if b in range(100, 251):
            x = 0
        elif b in range(251, 401):
            x = 1
        elif b in range(401, 551):
            x = 2
        return (x, y)


    def make_x(coord):
        text = large_font.render("×", True, red)
        textrect = text.get_rect()
        textrect.center = (left_scale[coord[1]]+75, top_scale[coord[0]]+75)
        screen.blit(text, textrect)


    def make_o(coord):
        text = large_font.render("o", True, blue)
        textrect = text.get_rect()
        textrect.center = (left_scale[coord[1]]+75, top_scale[coord[0]]+75)
        screen.blit(text, textrect)


    def change_made(initial, final):
        for i in range(len(initial)):
            for j in range(len(final)):
                if initial[i][j] != final[i][j]:
                    return (i, j)


    # the defined game functions above are used to construct the interface below this line
    left_scale = {0: 95, 1: 245, 2: 395}
    top_scale = {0: 100, 1: 250, 2: 400}
    lines()
    turn = 0
    player = 1
    exited = False
    done_spaces = []
    while not(exited):
        a = check_turn(board)
        b = pygame.Rect(0, 0, 640, 97.5)
        pygame.draw.rect(screen, black, b)
        if is_ended(board):
            if utility(board) == 1:
                text = font.render('''You Won !!''', True, (255, 255, 255))
                draw_win_line(board)
            elif utility(board) == -1:
                text = font.render('''You Lost !!''', True, (255, 255, 255))
                draw_win_line(board)
            elif utility(board) == 0:
                text = font.render('''Draw !!''', True, (255, 255, 255))
            textrect = text.get_rect()
            textrect.center = (320, 40)
        elif a == "X":
            text = font.render('Your Turn', True, (255, 255, 255))
            textrect = text.get_rect()
            textrect.center = (320, 40)
        elif a == "O":
            text = font.render("Demon's Turn", True, (255, 255, 255))
            textrect = text.get_rect()
            textrect.center = (320, 40)
        screen.blit(text, textrect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exited = True
            if is_ended(board):
                pass
            if event.type == pygame.MOUSEBUTTONDOWN and not(is_ended(board)) and turn % 2 == 0:
                if not(list_coordinates(event.pos[0], event.pos[1]) in done_spaces):
                    X = event.pos[0]
                    Y = event.pos[1]
                    coord = list_coordinates(X, Y)
                    done_spaces.append(coord)
                    board[coord[0]][coord[1]] = "X"
                    make_x(coord)
                    turn += 1
            elif turn % 2 == 1 and not(is_ended(board)):
                temp = result(board, minimax(board))
                cods = change_made(board, temp)
                done_spaces.append(cods)
                make_o(cods)
                board = temp
                turn += 1

        pygame.display.update()

""" Hex code """
# TBA

""" Main Screen Code """
import pygame

pygame.init()

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
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width , height))
    return screen.blit(text_render, (x, y))

# making the main screen back ground
main_screen = pygame.display.set_mode((640, 570))
pygame.display.set_caption( 'Pick the Block' )
BG_COLOR = (0, 0, 0)
main_screen.fill( BG_COLOR )

# main function for the screen
def mainmenu():

    pygame.draw.ellipse(main_screen, (180, 255, 180), [70, 20, 500, 150], 0)
    font = pygame.font.SysFont('timesnewroman', 50)
    text = font.render("John Nash's Demon",True,(150, 100, 100))
    textRect = text.get_rect()
    textRect.center = (320, 85)
    main_screen.blit(text,textRect)
    hex = button(main_screen,(280,200), "Hex")
    tic_tac_toe = button(main_screen, (205, 300), "Tic Tac Toe")
    domineering = button(main_screen, (193, 400), "Domineering")
    pick_the_brick = button(main_screen,(180,500), "Pick the Brick")


    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            # checks if the mouse has been clicked 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tic_tac_toe.collidepoint(pygame.mouse.get_pos()):
                    Tic_Tac_Toe()
                elif domineering.collidepoint(pygame.mouse.get_pos()):
                    Domineering()
                elif pick_the_brick.collidepoint(pygame.mouse.get_pos()):
                    Pick_The_Brick()
                elif hex.collidepoint(pygame.mouse.get_pos()):
                    pass
        pygame.display.update()


mainmenu()
