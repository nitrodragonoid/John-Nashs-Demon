# Importing required libraries
import pygame
import pygame.gfxdraw
import time
pygame.init()
# Different colors used in GUI
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
# Initializing Tic-tac-toe board and determining several helping data
board_ttt = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
left_scale_ttt = {0: 95, 1: 245, 2: 395}
top_scale_ttt = {0: 100, 1: 250, 2: 400}
# Determining UI size
width = 640
height = 570
# Initializing the fonts used throoughout
font = pygame.font.Font('freesansbold.ttf', 40)
large_font = pygame.font.Font('freesansbold.ttf', 150)
small_font = pygame.font.Font('freesansbold.ttf', 20)
# Initializing Game Tree, board and determinig several other helping data for Domineering
game_tree_dm = dict()
grid_dm = [[0 for _ in range(4)] for __ in range(3)]
left_scale_dm = {0: 20, 1: 170, 2: 320, 3: 470}
top_scale_dm = {0: 100, 1: 250, 2: 400}
# Initializing board for Pick the block game
bricks = 10
turn = 1
board = [bricks, turn]


''' Tic Tac Toe '''
# Tictactoe main/helper functions
# Function that determines whether the state has ended or not


def is_ended_ttt(state):
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

# assigns a utility to a ended game board


def utility_ttt(state):
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


def action_ttt(state, turn):  # outputs the list of all the possible moves
    out = []
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                move = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                move[i][j] = turn
                out.append(move)
    return out

# Combines the move with the state


def result_ttt(state, move):
    temp = []
    for i in state:
        temp.append(i.copy())
    for i in range(len(move)):
        for j in range(len(move[i])):
            if move[i][j] != 0:
                temp[i][j] = move[i][j]
    return temp

# Determines which player will play next


def check_turn_ttt(state):
    Xs = 0
    Os = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            Xs += state[i][j] == "X"
            Os += state[i][j] == "O"
    return "O" * ( Xs != Os ) + "X" * (Xs == Os)

# Draws a line where a player ends up in winning a match


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
            screen, red, (left_scale_ttt[start[1]], top_scale_ttt[start[0]]+75), (545, top_scale_ttt[start[0]]+75))
    elif line_type == "verticalo":
        pygame.draw.line(
            screen, red, (left_scale_ttt[start[1]]+75, top_scale_ttt[start[0]]), (left_scale_ttt[start[1]]+75, 550))
    elif line_type == "horizontalx":
        pygame.draw.line(
            screen, blue, (left_scale_ttt[start[1]], top_scale_ttt[start[0]]+75), (545, top_scale_ttt[start[0]]+75))
    elif line_type == "verticalx":
        pygame.draw.line(
            screen, blue, (left_scale_ttt[start[1]]+75, top_scale_ttt[start[0]]), (left_scale_ttt[start[1]]+75, 550))
    elif line_type == "diagonalo":
        if start == (0, 0):
            pygame.draw.line(
                screen, red, (left_scale_ttt[start[1]], top_scale_ttt[start[0]]), (left_scale_ttt[end[1]]+150, 550))
        else:
            pygame.draw.line(
                screen, red, (left_scale_ttt[start[1]]+150, top_scale_ttt[start[0]]), (left_scale_ttt[end[1]], 550))
    elif line_type == "diagonalx":
        if start == (0, 0):
            pygame.draw.line(
                screen, blue, (left_scale_ttt[start[1]], top_scale_ttt[start[0]]), (left_scale_ttt[end[1]]+150, 550))
        else:
            pygame.draw.line(
                screen, blue, (left_scale_ttt[start[1]]+150, top_scale_ttt[start[0]]), (left_scale_ttt[end[1]], 550))

# returns maximum value


def max_value_ttt(state):
    if is_ended_ttt(state) == True:
        return utility_ttt(state)
    v = -float('inf')
    for a in action_ttt(state, check_turn_ttt(state)):
        v = max(v, min_value_ttt(result_ttt(state, a)))
    return v

# returns minimum value


def min_value_ttt(state):
    if is_ended_ttt(state) == True:
        return utility_ttt(state)
    v = float('inf')
    for a in action_ttt(state, check_turn_ttt(state)):
        v = min(v, max_value_ttt(result_ttt(state, a)))
    return v

# Max function of minimax


def MAX_ttt(state):
    val = -float('inf')
    for a in action_ttt(state, check_turn_ttt(state)):
        check = state.copy()
        y = min_value_ttt(result_ttt(check, a))
        if y > val:
            val = y
            best = a
    return best

# Min function of minimax


def MIN_ttt(state):
    val = float('inf')
    for a in action_ttt(state, check_turn_ttt(state)):
        check = state.copy()
        x = max_value_ttt(result_ttt(check, a))
        if x < val:
            val = x
            best = a
    return best

# minimax algorithm main_call


def minimax_ttt(state):
    if check_turn_ttt(state) == "O":
        return MIN_ttt(state)
    elif check_turn_ttt(state) == "X":
        return MAX_ttt(state)

# creates a full black screen


def blank():
    pygame.gfxdraw.filled_polygon(
        screen, [(0, 0), (640, 0), (640, 570), (0, 570)], black)

# Draws the board for tictactoe


def lines_ttt():
    pygame.draw.line(screen, white, (95, 100), (545, 100), 5)
    pygame.draw.line(screen, white, (95, 250), (545, 250), 5)
    pygame.draw.line(screen, white, (95, 400), (545, 400), 5)
    pygame.draw.line(screen, white, (95, 550), (545, 550), 5)
    pygame.draw.line(screen, white, (95, 100), (95, 550), 5)
    pygame.draw.line(screen, white, (245, 100), (245, 550), 5)
    pygame.draw.line(screen, white, (395, 100), (395, 550), 5)
    pygame.draw.line(screen, white, (545, 100), (545, 550), 5)

    return True

# Converts the coordinates of clicked point into the corresponding indices of nested lists (board)


def list_coordinates_ttt(a, b):
    x = float('inf')
    y = float('inf')
    x = (b in range(251, 401)) + 2 * (b in range(401, 551))
    y = (a in range(246, 396)) + 2 * (a in range(396, 546))
    return (x, y)

# Draws X


def make_x(coord):
    text = large_font.render("×", True, red)
    textrect = text.get_rect()
    textrect.center = (left_scale_ttt[coord[1]]+75, top_scale_ttt[coord[0]]+75)
    screen.blit(text, textrect)

# Draws O


def make_o(coord):
    text = large_font.render("o", True, blue)
    textrect = text.get_rect()
    textrect.center = (left_scale_ttt[coord[1]]+75, top_scale_ttt[coord[0]]+75)
    screen.blit(text, textrect)

# Detects a change made from current state to next state


def change_made_ttt(initial, final):
    for i in range(len(initial)):
        for j in range(len(final)):
            if initial[i][j] != final[i][j]:
                return (i, j)

# tic-tac-toe driver code


def tic_tac_toe(screen, board_ttt):

    blank()
    lines_ttt()
    turn = 0
    player = 1
    exited = False
    done_spaces = []
    while not(exited):
        a = check_turn_ttt(board_ttt)
        b = pygame.Rect(0, 0, 640, 97.5)
        pygame.draw.rect(screen, black, b)
        pygame.draw.line(screen, white, (20, 45), (80, 45), 1)
        pygame.draw.line(screen, white, (20, 15), (80, 15), 1)
        pygame.draw.line(screen, white, (20, 15), (20, 45), 1)
        pygame.draw.line(screen, white, (80, 15), (80, 45), 1)
        text = small_font.render('''Home''', True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.center = (50, 30)
        screen.blit(text, textrect)
        if is_ended_ttt(board_ttt):
            if utility_ttt(board_ttt) == 1:
                text = font.render('''You Won !!''', True, (255, 255, 255))
                draw_win_line(board_ttt)
            elif utility_ttt(board_ttt) == -1:
                text = font.render('''You Lost !!''', True, (255, 255, 255))
                draw_win_line(board_ttt)
            elif utility_ttt(board_ttt) == 0:
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
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 20 <= event.pos[0] < 80 and 15 <= event.pos[1] <= 45:
                    blank()
                    return False
            if is_ended_ttt(board_ttt):
                pass
            if event.type == pygame.MOUSEBUTTONDOWN and not(is_ended_ttt(board_ttt)) and turn % 2 == 0:
                if not(list_coordinates_ttt(event.pos[0], event.pos[1]) in done_spaces):
                    X = event.pos[0]
                    Y = event.pos[1]
                    coord = list_coordinates_ttt(X, Y)
                    done_spaces.append(coord)
                    board_ttt[coord[0]][coord[1]] = "X"
                    make_x(coord)
                    turn += 1
            elif turn % 2 == 1 and not(is_ended_ttt(board_ttt)):
                temp = result_ttt(board_ttt, minimax_ttt(board_ttt))
                cods = change_made_ttt(board_ttt, temp)
                done_spaces.append(cods)
                make_o(cods)
                board_ttt = temp
                turn += 1
        pygame.display.update()
    return False


''' Domineering '''

# Draws a domineering game board


def lines_dm():
    pygame.draw.line(screen, (255, 255, 255), (20, 100), (620, 100), 5)
    pygame.draw.line(screen, (255, 255, 255), (20, 250), (620, 250), 5)
    pygame.draw.line(screen, (255, 255, 255), (20, 400), (620, 400), 5)
    pygame.draw.line(screen, (255, 255, 255), (20, 550), (620, 550), 5)
    pygame.draw.line(screen, (255, 255, 255), (20, 100), (20, 550), 5)
    pygame.draw.line(screen, (255, 255, 255), (170, 100), (170, 550), 5)
    pygame.draw.line(screen, (255, 255, 255), (320, 100), (320, 550), 5)
    pygame.draw.line(screen, (255, 255, 255), (470, 100), (470, 550), 5)
    pygame.draw.line(screen, (255, 255, 255), (620, 100), (620, 550), 5)

# Stack Helper functions


def push(stack, item):
    stack.append(item)


def pop(stack):
    return stack.pop()


def top(stack):
    return stack[-1]

# adding nodes to a graph


def addNodes(G, nodes):
    for i in nodes:
        G[i] = list()
    return G

# adding edges to a graph


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

# Queue helper functions


def enQueue(queue, item):
    queue.append(item)


def deQueue(queue):
    return queue.pop(0)


def front(queue):
    return queue[0]


def is_empty(queue):
    return len(queue) == 0

# List representation of board to to tuple ( so that we can store the states as nodes(keys of dictionary)


def list_to_tuple(grid):
    tmp = grid.copy()
    req = tuple()
    for i in tmp:
        req += (tuple(i),)
    return req

# Determines which player to play next


def player_determiner(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            count += grid[i][j] != 0
    count = count//2
    return 2 * (count % 2 == 1) + (count % 2 == 0)

# Determines whether the grid is fully filled or not


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

# Returns all the possible next states from a certain state


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

# updates the grid given the coordinates of the move made


def update_grid(grid, idx1, idx2, p_no):
    a = idx1
    b = idx2
    if (a[0]+1 == b[0] and a[1] == b[1]):
        grid[a[0]][a[1]] = str(p_no)+"v"
        grid[b[0]][b[1]] = str(p_no)+"v"
    elif (a[0] == b[0] and a[1]+1 == b[1]):
        grid[a[0]][a[1]] = str(p_no)+"h"
        grid[b[0]][b[1]] = str(p_no)+"h"

# Depth first search algorithm


def dfs(graph, current_state, comp_no, visited, parent):
    visited.append(current_state)
    for i in graph[current_state]:
        if not(i[0] in visited):
            parent[i[0]] = current_state
            if len(graph[i[0]]) == 0 and player_determiner(current_state) != comp_no:
                return
            dfs(graph, i[0], comp_no, visited, parent)

# Bot that works using dfs


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
    if cd:
        return sequence[-2]
    for i in sequence:
        if i != temp:
            return i

# tuple form of grid to list converter


def tuple_to_list(grid):
    lst = []
    for i in grid:
        lst.append(list(i))
    return lst

# scaling the coordinates on the UI to the corespong one on the nested lists


def list_coordinates_dm(cod):
    x = float('inf')
    y = float('inf')
    x = (cod[1] in range(251, 401)) + 2 * (cod[1] in range(401, 551))
    y = (cod[0] in range(171, 321)) + 2 * (cod[0] in range(321, 471)) + 3 * (cod[0] in range(471, 621))
    return (x, y)

# checks if the two click oints corresponds to adjacent boxes or not


def is_adjacent(pos_1, pos_2):
    if pos_1[0]+1 == pos_2[0] and pos_1[1] == pos_2[1]:
        return True
    elif pos_1[0] == pos_2[0] and pos_1[1]+1 == pos_2[1]:
        return True
    return False

# checks if the rectangle to be placed is vertical or not


def is_vertical(st1, st2):
    if st1[0]+1 == st2[0]:
        return True

# Makes a rectangle where a move is made


def make_rec(interface, player_no, st1, st2):
    if player_no == 1:
        color = red
        color_1 = blue
    else:
        color = blue
        color_1 = red

    if st1[0]+1 == st2[0]:
        a = pygame.Rect(left_scale_dm[st1[1]]+2,
                        top_scale_dm[st1[0]]+2, 146, 296)
        text = font.render(str(player_no), True, color_1)
        textrect = text.get_rect()
        textrect.center = (
            (left_scale_dm[st1[1]]+75, (top_scale_dm[st1[0]]+150)))
    else:
        a = pygame.Rect(left_scale_dm[st1[1]]+2,
                        top_scale_dm[st1[0]]+2, 296, 146)
        text = font.render(str(player_no), True, color_1)
        textrect = text.get_rect()
        textrect.center = (
            (left_scale_dm[st1[1]]+150), (top_scale_dm[st1[0]]+75))
    pygame.draw.rect(interface, color, a)
    b = pygame.Rect(0, 0, 640, 97.5)
    pygame.draw.rect(interface, black, b)
    interface.blit(text, textrect)

# adds new coordinates in the nested list version of grid


def add_cods(previous, now):
    req = []
    for i in range(len(previous)):
        for j in range(len(previous[i])):
            if previous[i][j] != now[i][j]:
                req.append((i, j))
    return req

# checks if the first click point comes after the second


def comes_after(pos_1, pos_2):
    if pos_1[0] > pos_2[0]:
        return True
    elif pos_1[1] > pos_2[1]:
        return True
    return False


# completing/expanding the game tree
nodes = []
edges = []
queue = []
a = list_to_tuple(grid_dm)
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
addNodes(game_tree_dm, nodes)
addEdges(game_tree_dm, edges, True)

# Driver code for Domineering


def domineering_screen(screen):
    grid_t = [[0 for _ in range(4)] for __ in range(3)]
    blank()
    lines_dm()
    count = 0
    turn = 0
    used_space = []
    closed = False
    while not(closed):
        a = player_determiner(grid_t)
        if is_full(grid_t):
            winner = (a==2) + 2*(a!=2)
            b = pygame.Rect(0, 0, 640, 97.5)
            pygame.draw.rect(screen, black, b)
            text = font.render('''Player ''' + str(winner) +
                               ''' Won !!''', True, (255, 255, 255))
            textrect = text.get_rect()
            textrect.center = (320, 40)

        elif a % 2 == 0:
            text = font.render('''Demon's Turn''', True, (255, 255, 255))
            textrect = text.get_rect()
            textrect.center = (320, 40)
        elif a % 2 == 1:
            text = font.render('''Your Turn''', True, (255, 255, 255))
            textrect = text.get_rect()
            textrect.center = (320, 40)
        screen.blit(text, textrect)
        pygame.draw.line(screen, white, (20, 45), (80, 45), 1)
        pygame.draw.line(screen, white, (20, 15), (80, 15), 1)
        pygame.draw.line(screen, white, (20, 15), (20, 45), 1)
        pygame.draw.line(screen, white, (80, 15), (80, 45), 1)
        text = small_font.render('''Home''', True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.center = (50, 30)
        screen.blit(text, textrect)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                return True
            if i.type == pygame.MOUSEBUTTONDOWN and is_full(grid_t):
                pass
            if i.type == pygame.MOUSEBUTTONDOWN:
                if 20 <= i.pos[0] < 80 and 15 <= i.pos[1] <= 45:
                    blank()
                    grid_t = [[0 for _ in range(4)] for __ in range(3)]
                    return False
            if i.type == pygame.MOUSEBUTTONDOWN and turn % 2 == 0 and int(count//0.5) % 2 == 0 and not(is_full(grid_t)):
                coord_1 = list_coordinates_dm(i.pos)
                if not(coord_1 in used_space):
                    count += 0.5
                    used_space.append(coord_1)
            elif i.type == pygame.MOUSEBUTTONDOWN and turn % 2 == 0 and int(count//0.5) % 2 == 1 and not(is_full(grid_t)):
                coord_2 = list_coordinates_dm(i.pos)
                if not(coord_2 in used_space):
                    if comes_after(coord_1, coord_2):
                        temp = coord_1
                        coord_1 = coord_2
                        coord_2 = temp
                    if is_adjacent(coord_1, coord_2):
                        used_space.append(coord_2)
                        update_grid(grid_t, coord_1, coord_2, a)
                        make_rec(screen, a, coord_1, coord_2)
                        count += 0.5
                        turn += 1

            elif turn % 2 == 1 and not(is_full(grid_t)):
                x = bot(grid_t, player_determiner(grid_t), game_tree_dm)
                coords = add_cods(grid_t, tuple_to_list(x))
                used_space.extend(coords)
                grid_t = tuple_to_list(x).copy()
                make_rec(screen, a, coords[0], coords[1])
                turn += 1
        pygame.display.update()


# used to construct the interface
def button_pb(screen, position, text):
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

# create the menu for pick the block i.e the  driver code


def menu_pb(state):
    """ This is the main game GUI and bot function """
    blank()
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
    b1 = button_pb(screen, (185, 300), "Pick 1 Block")
    b2 = button_pb(screen, (175, 450), "Pick 2 Blocks")

    # main game loop
    start = True
    while start:
        pygame.draw.line(screen, white, (20, 45), (80, 45), 1)
        pygame.draw.line(screen, white, (20, 15), (80, 15), 1)
        pygame.draw.line(screen, white, (20, 15), (20, 45), 1)
        pygame.draw.line(screen, white, (80, 15), (80, 45), 1)
        text = small_font.render('''Home''', True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.center = (50, 30)
        screen.blit(text, textrect)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 20 <= event.pos[0] < 80 and 15 <= event.pos[1] <= 45:
                    blank()
                    return False
            if is_ended_pb(state):
                pass
            # checks if the mouse has been clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # checks if 1 block has to be picked or 2 according to the move.
                # Makes the bot unravel its algorithm, and make the move accordingly.
                # To be updated with the bot, changes to be made as the bot will not click the mouse
                # so the blocks still have to be removed when the bot makes a move.
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.circle(screen, black, (x, y), 20)
                    x += 50
                    state = result_pb(state, (1, 2))
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
                        pygame.draw.line(screen, white, (20, 45), (80, 45), 1)
                        pygame.draw.line(screen, white, (20, 15), (80, 15), 1)
                        pygame.draw.line(screen, white, (20, 15), (20, 45), 1)
                        pygame.draw.line(screen, white, (80, 15), (80, 45), 1)
                        text = small_font.render(
                            '''Home''', True, (255, 255, 255))
                        textrect = text.get_rect()
                        textrect.center = (50, 30)
                        screen.blit(text, textrect)

                elif b2.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.circle(screen, black, (x, y), 20)
                    x += 50
                    pygame.draw.circle(screen, black, (x, y), 20)
                    x += 50
                    state = result_pb(state, (2, 2))
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
                        pygame.draw.line(screen, white, (20, 45), (80, 45), 1)
                        pygame.draw.line(screen, white, (20, 15), (80, 15), 1)
                        pygame.draw.line(screen, white, (20, 15), (20, 45), 1)
                        pygame.draw.line(screen, white, (80, 15), (80, 45), 1)
                        text = small_font.render(
                            '''Home''', True, (255, 255, 255))
                        textrect = text.get_rect()
                        textrect.center = (50, 30)
                        screen.blit(text, textrect)

                pygame.display.update()
                if is_ended_pb(state) == True:
                    break
                time.sleep(1)

                move = minimax_pb(state)
                state = result_pb(state, move)
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


bricks = 10
turn = 1
board = [bricks, turn]

# checks if the state is ended or not


def is_ended_pb(state):
    return bool(state[0] <= 0)

# assigns a utility to a ended game board


def utility_pb(state):
    if (state[0] == 0) and (state[1] == 1):  # turn being 2 means that player 2 did the last move
        return -1
    # turn being 2 means that player 1 did the last move
    elif (state[0] == 0) and (state[1] == 2):
        return 1

# outputs the list of all the possible moves


def action_pb(state):
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

# combines the move with the state i.e. updates the state


def result_pb(state, move):
    temp = state.copy()  # make a copy of the board so the og board isnt effected
    # remove the pbricks that the move tells to remove
    temp[0] = temp[0] - move[0]
    temp[1] = move[1]  # set the turn to the next player
    return temp


# returns maximum
def max_value_pb(state):
    if is_ended_pb(state) == True:
        return utility_pb(state)
    v = -float('inf')
    for a in action_pb(state):
        v = max(v, min_value_pb(result_pb(state, a)))
    return v

# returns minimum


def min_value_pb(state):
    if is_ended_pb(state) == True:
        return utility_pb(state)
    v = float('inf')
    for a in action_pb(state):
        v = min(v, max_value_pb(result_pb(state, a)))
    return v

# Max function of the minimax algorithm


def MAX_pb(state):
    val = -float('inf')
    for a in action_pb(state):
        check = state.copy()
        w = min_value_pb(result_pb(check, a))
        if w > val:
            val = w
            best = a
    return best

# Min function of the minimax algorithm


def MIN_pb(state):
    val = float('inf')
    for a in action_pb(state):
        check = state.copy()
        z = max_value_pb(result_pb(check, a))
        if z < val:
            val = z
            best = a
    return best

# minimax algorithm main function


def minimax_pb(state):
    if state[1] == 2:
        return MIN_pb(state)
    elif state[1] == 1:
        return MAX_pb(state)

# returns list of all nodes in a graph


def listOfNodes(G):
    nodeslist = []
    for i in G:
        nodeslist.append(i)
    return nodeslist

# returns neigbours of a node in the graph


def getNeighbors(G, node):
    out = []
    for j in G[node]:
        out.append(j[0])
    return out

# returns a list of nodes to be added to the graph given the state


def makes_node(board):
    nodes = [("start 1"), ("start 2"), ("end 1"), ("end 2")]
    for i in range(len(board)):
        for j in range(len(board)):
            nodes.append((i, j))
    return nodes

# returns list of the edges to be added to the graph given the state


def make_edges(board):
    edges = []
    for i in range(len(board)):
        for j in range(len(board)):
            if i == 0:
                edges.append(((i, j), "end 1", 1))
            if i == len(board)-1:
                edges.append(((i, j), "start 1", 1))
            if j == 0:
                edges.append(((i, j), "start 2", 1))
            if j == len(board)-1:
                edges.append(((i, j), "end 2", 1))
            if i != 0:
                # connect to the node above
                edges.append(((i, j), (i-1, j), 1))
                if j != 0:
                    # connect to the node above and to the left
                    edges.append(((i, j), (i-1, j-1), 1))
            if i != len(board)-1:
                # connect to the node below
                edges.append(((i, j), (i+1, j), 1))
                if j != len(board)-1:
                    # connect to the node below and to the right
                    edges.append(((i, j), (i+1, j+1), 1))
            if j != 0:
                # connect to the node on the left
                edges.append(((i, j), (i, j-1), 1))
            if j != len(board[i])-1:
                # connect to the node on the right
                edges.append(((i, j), (i, j+1), 1))
    return edges

# checks if its player 1's turn


def check_player_1_hx(state, G):
    # checking is a path can exist
    check = False
    for j in getNeighbors(G, "start 1"):
        if state[int(j[0])][int(j[1])] == "X":
            check = True
    for j in getNeighbors(G, "end 1"):
        if state[int(j[0])][int(j[1])] == "X":
            check = True
    if check == False:
        return False
    # if a path can exists we check if it does exist
    queue = []  # Declare a queue for keeping track of nodes
    visited = []  # to keep track a node is visited
    nodes = listOfNodes(G)
    enQueue(queue, "start 1")  # start searching from the start
    while is_empty(queue) == False:  # loop untill all nodes are visited
        f = front(queue)  # get the front of the queue
        if f not in visited:
            visited.append(f)  # make sure to mark the first node as visited
        # get all the nodes connested to the node on the front of the queue
        next = getNeighbors(G, f)
        for i in next:
            if i == "end 1":  # if end is reached the game is ended
                return True
            if (i != "start 1") and (i != "end 1") and (i != "start 2") and (i != "end 2"):
                # enQueue all the nodes connected to f that are not yet visited and contains X
                if (i not in visited) and (state[int(i[0])][int(i[1])] == "X"):
                    enQueue(queue, i)
                    visited.append(i)  # mark them as visited
        # if queue is not empty remove the front of the queue
        if is_empty(queue) == False:
            deQueue(queue)
    return False

# checks if its player 2's turn


def check_player_2_hx(state, G):
    # checking is a path can exist
    check = False
    for j in getNeighbors(G, "start 2"):
        if state[int(j[0])][int(j[1])] == "O":
            check = True
    for j in getNeighbors(G, "end 2"):
        if state[int(j[0])][int(j[1])] == "O":
            check = True
    if check == False:
        return False
    # if a path can exists we check if it does exist
    queue = []  # Declare a queue for keeping track of nodes
    visited = []  # to keep track a node is visited
    nodes = listOfNodes(G)
    enQueue(queue, "start 2")  # start searching from the start
    while is_empty(queue) == False:  # loop untill all nodes are visited
        f = front(queue)  # get the front of the queue
        if f not in visited:
            visited.append(f)  # make sure to mark the first node as visited
        # get all the nodes connested to the node on the front of the queue
        next = getNeighbors(G, f)
        for i in next:
            if i == "end 2":  # if end is reached the game is ended
                return True
            if (i != "start 1") and (i != "end 1") and (i != "start 2") and (i != "end 2"):
                # enQueue all the nodes connected to f that are not yet visited and contains X
                if (i not in visited) and (state[int(i[0])][int(i[1])] == "O"):
                    enQueue(queue, i)
                    visited.append(i)  # mark them as visited
        # if queue is not empty remove the front of the queue
        if is_empty(queue) == False:
            deQueue(queue)
    return False

# checks if the game is ended or not


def is_ended_hx(state, connections):
    return (check_player_1_hx(state, connections) == True) or (check_player_2_hx(state, connections) == True)

# assigns a utility to a ended game board


def utility_hx(state, connections):
    return (check_player_1_hx(state, connections) == True) - (check_player_2_hx(state, connections) == True)

# returns all possible moves that can bbe made from a state


def action_hx(state):
    moves = []
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == 0:
                moves.append((i, j))
    return moves

# determines whoose turn is next


def check_turn_hx(state):
    Xs = 0
    Os = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            Xs += state[i][j] == "X"
            Os += state[i][j] == "O"
    return "O" * (Xs != Os) + "X" * (Xs == Os)

# combines the move made with the state i.e. updates the state


def result_hx(state, move):
    temp = []
    for i in state:
        temp.append(i.copy())
    temp[move[0]][move[1]] = check_turn_hx(state)
    return temp


# returns maximum value
def max_value_hx(state, connections):
    if is_ended_hx(state, connections) == True:
        return utility_hx(state, connections)
    v = -float('inf')
    for a in action_hx(state):
        v = max(v, min_value_hx(result_hx(state, a), connections))
    return v

# returns minimum value


def min_value_hx(state, connections):
    if is_ended_hx(state, connections) == True:
        return utility_hx(state, connections)
    v = float('inf')
    for a in action_hx(state):
        v = min(v, max_value_hx(result_hx(state, a), connections))
    return v

# max function of alpha beta pruning


def max_pruning_hx(state, connections, beta):
    if is_ended_hx(state, connections) == True:
        return utility_hx(state, connections)
    v = -float('inf')
    for a in action_hx(state):
        check = min_pruning_hx(result_hx(state, a), connections, beta)
        if v < check:
            v = check
        if check < beta:
            break
    return v

# min function of alpha beta pruning


def min_pruning_hx(state, connections, alpha):
    if is_ended_hx(state, connections) == True:
        return utility_hx(state, connections)
    v = float('inf')
    for a in action_hx(state):
        check = max_pruning_hx(result_hx(state, a), connections, alpha)
        if v > check:
            v = check
        if check > alpha:
            break
    return v

# max function of minimax


def MAX_hx(state, connections):
    val = -float('inf')
    moves = action_hx(state)
    for a in moves:
        if a == moves[0]:
            x = min_value_hx(result_hx(state, a), connections)
            if x > val:
                val = x
                best = a
        else:
            x = min_pruning_hx(result_hx(state, a), connections, val)
            if x > val:
                val = x
                best = a
    return best

# min function of minimax


def MIN_hx(state, connections):
    val = float('inf')
    moves = action_hx(state)
    for a in moves:
        if a == moves[0]:
            x = max_value_hx(result_hx(state, a), connections)
            if x < val:
                val = x
                best = a
        else:
            x = max_pruning_hx(result_hx(state, a), connections, val)
            if x < val:
                val = x
                best = a
    return best

# minimax algorithm (with alphe beta pruning)


def minimax_hx(state, connections):
    if check_turn_hx(state) == "O":
        return MIN_hx(state, connections)
    elif check_turn_hx(state) == "X":
        return MAX_hx(state, connections)

# first move the bot should


# board for hex (nested list version)
board3 = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]


# game tree for hex
graph = {}
addNodes(graph, makes_node(board3))
addEdges(graph, make_edges(board3))


l = 51.96152423
h = 25.98076211

# creates the grid for hex


def lines_hx():
    x = 200
    for i in range(4):
        a = 0
        b = 0
        c = 0
        for j in range(4):
            if i <= 2:
                pygame.draw.line(
                    screen, white, (x+45+h-a, 150+c+b), (x+90+h-a, 150+h+b+c))
                if j != 3 or i != 0:
                    pygame.draw.line(screen, white, (x-a+h, 150+h+b+c),
                                     (x+45+h-a, 150+c+b))

            if j == 3:
                continue
            pygame.draw.line(screen, white, (x+h-a, 150+c+b+h),
                             (x+h-a, 150+c+b+l+h))
            a += 45
            b += l
            c += h
        x += 90
        # break
    x = 200
    a = 0
    b = 0
    c = 0
    for i in range(3):
        pygame.draw.line(screen, white, (x+225+h-a, 150+h+l+h+c+b),
                         (x+270+h-a, 150+h+l+b+c))
        a += 45
        b += l
        c += h


# creation of a nested list data structure which updates the board of the hex in accordance with the position of the click
hex_vertices = list()
row1 = []
x = 0
for i in range(3):
    hex1 = [(200+h+1+x, 150+h), (245+h+x, 151), (290+h-1+x, 150+h),
            (290+h-1+x, 150+h+l), (245+h+x, 150+h+l+h-1), (200+h+1+x, 150+h+l)]
    row1.append(hex1.copy())
    x += 90
hex_vertices.append(row1.copy())
row1 = []
x = 0
for i in range(3):
    hex1 = [(155+h+1+x, 150+h+h+l), (200+h+x, 151+h+l), (245+h-1+x, 150+h+h+l),
            (245+h-1+x, 150+h+l+h+l), (200+h+x, 150+h+l+h-1+h+l), (155+h+1+x, 150+h+l+h+l)]
    row1.append(hex1.copy())
    x += 90
hex_vertices.append(row1.copy())
row1 = []
x = 0
for i in range(3):
    hex1 = [(110+h+1+x, 150+h+h+h+l+l), (155+h+x, 151+h+h+l+l), (200+h-1+x, 150+h+l+h+h+l),
            (200+h-1+x, 150+h+h+l+l+h+l), (155+h+x, 150+h+h+l+l+h-1+h+l), (110+h+1+x, 150+h+h+l+l+h+l)]
    row1.append(hex1.copy())
    x += 90
hex_vertices.append(row1.copy())


# converts the coordinates of click position into the corresponding coordinates of the board represented as nnested lists


def lst_cord(coord):
    x1 = 0
    for i in range(4):
        if 200+h+x1 <= coord[0] <= 290+h+x1 and 150+h <= coord[1] <= 150+h+l:
            return (0, i)
        x1 += 90
    x1 = 0
    for i in range(4):
        if 155+h+x1 <= coord[0] <= 245+h+x1 and 150+h+h+l <= coord[1] <= 150+h+h+l+l:
            return (1, i)
        x1 += 90
    x1 = 0
    for i in range(4):
        if 110+h+x1 <= coord[0] <= 200+h+x1 and 150+(3*h)+(2*l) <= coord[1] <= 150+(3*h)+(3*l):
            return (2, i)
        x1 += 90
    x1 = 0
    for i in range(4):
        if 180+h+x1 <= coord[0] <= 270+h+x1 and 150+4*h+3*l <= coord[1] <= 150+4*h+4*l:
            return (3, i)
        x1 += 90

# makes a hexagon


def make_hex(p_no, coord):
    color = blue
    if p_no == 0:
        color = red
    pygame.gfxdraw.filled_polygon(
        screen, hex_vertices[coord[0]][coord[1]], color)

# determines the move made by player/bot by comparing the states


def change_in_states(initial, final):
    for i in range(len(initial)):
        for j in range(len(initial[i])):
            if initial[i][j] != final[i][j]:
                return (i, j)

# driver code for hex


def hex_game(screen, board3):
    blank()
    lines_hx()
    exited = False
    done_spaces = []
    turn_of = 0
    while not(exited):
        b = pygame.Rect(0, 0, 640, 97.5)
        pygame.draw.rect(screen, black, b)
        if is_ended_hx(board3, graph):
            if utility_hx(board3, graph) == 1:
                text = font.render("Demon Won!", True, white)
                textrect = text.get_rect()
                textrect.center = (320, 40)
            else:
                text = font.render("You Won!", True, white)
                textrect = text.get_rect()
                textrect.center = (320, 40)
            screen.blit(text, textrect)
        elif turn_of % 2 == 0 and not(is_ended_hx(board3, graph)):
            text = font.render("Demon's Turn", True, white)
            textrect = text.get_rect()
            textrect.center = (320, 40)
            screen.blit(text, textrect)
        elif turn_of % 2 != 0 and not(is_ended_hx(board3, graph)):
            text = font.render("Your Turn", True, white)
            textrect = text.get_rect()
            textrect.center = (320, 40)
            screen.blit(text, textrect)
        pygame.draw.line(screen, white, (20, 45), (80, 45), 1)
        pygame.draw.line(screen, white, (20, 15), (80, 15), 1)
        pygame.draw.line(screen, white, (20, 15), (20, 45), 1)
        pygame.draw.line(screen, white, (80, 15), (80, 45), 1)
        text = small_font.render('''Home''', True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.center = (50, 30)
        screen.blit(text, textrect)
        for event in pygame.event.get():
            if is_ended_hx(board3, graph):
                if utility_hx(board3, graph) == 1:
                    text = font.render("Demon Won!", True, white)
                    textrect = text.get_rect()
                    textrect.center = (320, 40)
                else:
                    text = font.render("You Won!", True, white)
                    textrect = text.get_rect()
                    textrect.center = (320, 40)
                screen.blit(text, textrect)
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 20 <= event.pos[0] < 80 and 15 <= event.pos[1] <= 45:
                    blank()
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN and turn_of % 2 == 1 and not(is_ended_hx(board3, graph)):
                a = lst_cord(event.pos)
                if a == None:
                    pass
                elif not(a in done_spaces):
                    board3 = result_hx(board3, a)
                    make_hex(turn_of % 2, a)
                    done_spaces.append(a)
                    turn_of += 1
            elif turn_of % 2 == 0 and not(is_ended_hx(board3, graph)):
                temp = board3.copy()
                board3 = result_hx(board3, minimax_hx(board3, graph))
                d = change_in_states(temp, board3)
                done_spaces.append(d)
                make_hex(turn_of % 2, d)
                turn_of += 1

        pygame.display.update()

# 4 buttons that are made for each game in the main screen


def button(screen, position, text):
    font = pygame.font.SysFont('timesnewroman', 50)
    text_render = font.render(text, 1, red)
    x, y, width, height = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, blue, (x, y), (x + width, y), 5)
    pygame.draw.line(screen, blue, (x, y - 2), (x, y + height), 5)
    pygame.draw.line(screen, blue, (x, y + height),
                     (x + width, y + height), 5)
    pygame.draw.line(screen, blue, (x + width,
                                    y + height), [x + width, y], 5)
    pygame.draw.rect(screen, blue, (x, y, width, height))
    return screen.blit(text_render, (x, y))


# making the main screen back ground
screen = pygame.display.set_mode((640, 570))
pygame.display.set_caption("Game Bot")
screen.fill(black)


# main function for the screen


def mainmenu():
    closed = False
    while not(closed):
        pygame.draw.ellipse(screen, white, [70, 20, 500, 150], 1)
        font = pygame.font.SysFont('timesnewroman', 50)
        text = font.render("John Nash's Demon", True, white)
        textRect = text.get_rect()
        textRect.center = (320, 90)
        screen.blit(text, textRect)
        hex = button(screen, (282, 200), "Hex")
        ttt = button(screen, (207, 300), "Tic Tac Toe")
        domineering = button(screen, (193, 400), "Domineering")
        pick_the_brick = button(screen, (177, 500), "Pick the Block")
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                closed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            # checks if the mouse has been clicked
            if event.type == pygame.MOUSEBUTTONDOWN:

                if ttt.collidepoint(pygame.mouse.get_pos()):
                    closed = tic_tac_toe(screen, board_ttt)
                elif domineering.collidepoint(pygame.mouse.get_pos()):
                    closed = domineering_screen(screen)
                elif pick_the_brick.collidepoint(pygame.mouse.get_pos()):
                    closed = menu_pb(board)
                elif hex.collidepoint(pygame.mouse.get_pos()):
                    closed = hex_game(screen, board3)
        pygame.display.update()


mainmenu()
