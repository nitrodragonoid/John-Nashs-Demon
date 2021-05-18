from numpy.lib.function_base import append
import pygame
import numpy as np
pygame.init()
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
