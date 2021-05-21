import pygame
import pygame.gfxdraw
from time import time
##### Queue helper functions #####


def enQueue(queue, item):
    queue.append(item)
    return queue


def deQueue(queue):
    c = queue[0]
    queue.pop(0)
    return c


def getFront(queue):
    return queue[0]


def displayQueue(queue):
    print(queue)


def is_emptyQueue(queue):
    if len(queue) == 0:
        return True
    else:
        return False
##### end #####

# Helper functions for the graph


def addNodes(G, nodes):
    for i in nodes:
        G[i] = []
    return G


def addEdges(G, edges, directed=False):
    if directed == True:
        for i in range(len(edges)):
            G[edges[i][0]].append((edges[i][1], edges[i][2]))
    elif directed == False:
        for i in range(len(edges)):
            G[edges[i][0]].append((edges[i][1], edges[i][2]))
            G[edges[i][1]].append((edges[i][0], edges[i][2]))
    return G


def listOfNodes(G):
    nodeslist = []
    for i in G:
        nodeslist.append(i)
    return nodeslist


def getNeighbors(G, node):
    out = []
    for j in G[node]:
        out.append(j[0])
    return out


def displayGraph(G):
    for i in G:
        print(i, ":", G[i])

####### END #######


def makes_node(board):
    nodes = [("start 1"), ("start 2"), ("end 1"), ("end 2")]
    for i in range(len(board)):
        for j in range(len(board)):
            nodes.append((i, j))
    return nodes


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


def check_player_1(state, G):
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
    while is_emptyQueue(queue) == False:  # loop untill all nodes are visited
        f = getFront(queue)  # get the front of the queue
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
        if is_emptyQueue(queue) == False:
            deQueue(queue)
    return False


def check_player_2(state, G):
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
    while is_emptyQueue(queue) == False:  # loop untill all nodes are visited
        f = getFront(queue)  # get the front of the queue
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
        if is_emptyQueue(queue) == False:
            deQueue(queue)
    return False


def is_ended(state, connections):
    if (check_player_1(state, connections) == True) or (check_player_2(state, connections) == True):
        return True
    return False


def utility(state, connections):
    if check_player_1(state, connections) == True:
        return 1
    if check_player_2(state, connections) == True:
        return -1


def action(state):
    moves = []
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == 0:
                moves.append((i, j))
    return moves


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


def result(state, move):
    temp = []
    for i in state:
        temp.append(i.copy())
    temp[move[0]][move[1]] = check_turn(state)
    return temp


def display(state):
    for i in state:
        print(i)
    print("\n")

####### alpha beta pruning #######


def max_value(state, connections):
    if is_ended(state, connections) == True:
        return utility(state, connections)
    v = -9999999
    for a in action(state):
        v = max(v, min_value(result(state, a), connections))
        if v == 1:
            break
    return v


def min_value(state, connections):
    if is_ended(state, connections) == True:
        return utility(state, connections)
    v = 9999999
    for a in action(state):
        v = min(v, max_value(result(state, a), connections))
        if v == -1:
            break
    return v


def max_pruning(state, connections, beta):
    if is_ended(state, connections) == True:
        return utility(state, connections)
    v = -9999999
    for a in action(state):
        check = min_pruning(result(state, a), connections, beta)
        if v < check:
            v = check
        if check >= beta:
            break
        if v == 1:
            break
    return v


def min_pruning(state, connections, alpha):
    if is_ended(state, connections) == True:
        return utility(state, connections)
    v = 9999999
    for a in action(state):
        check = max_pruning(result(state, a), connections, alpha)
        if v > check:
            v = check
        if check <= alpha:
            break
        if v == -1:
            break
    return v


def MAX(state, connections):
    val = -9999999
    moves = action(state)
    for a in moves:
        if a == moves[0]:
            x = min_value(result(state, a), connections)
            if x > val:
                val = x
                best = a
        else:
            x = min_pruning(result(state, a), connections, val)
            if x > val:
                val = x
                best = a
        if val == 1:
            break
    return best


def MIN(state, connections):
    val = 9999999
    moves = action(state)
    for a in moves:
        if a == moves[0]:
            x = max_value(result(state, a), connections)
            if x < val:
                val = x
                best = a
        else:
            x = max_pruning(result(state, a), connections, val)
            if x < val:
                val = x
                best = a
        if val == -1:
            break
    return best


def minimax(state, connections):
    if check_turn(state) == "O":
        return MIN(state, connections)
    elif check_turn(state) == "X":
        return MAX(state, connections)
####### END #######


def MAX_second(state, connections):
    val = -9999999
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == "X":
                connected = getNeighbors(connections, (i, j))
                for a in connected:
                    if state[a[0]][a[1]] == 0:
                        if a == connected[0]:
                            x = min_value(result(state, a), connections)
                            if x > val:
                                val = x
                                best = a
                        else:
                            x = min_pruning(result(state, a), connections, val)
                            if x > val:
                                val = x
                                best = a
                        if val == 1:
                            break
    return best


def MIN_second(state, connections):
    val = 9999999
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == "O":
                connected = getNeighbors(connections, (i, j))
                for a in connected:
                    if state[a[0]][a[1]] == 0:
                        if a == connected[0]:
                            x = max_value(result(state, a), connections)
                            if x < val:
                                val = x
                                best = a
                        else:
                            x = max_pruning(result(state, a), connections, val)
                            if x < val:
                                val = x
                                best = a
                        if val == -1:
                            break
    return best


def minimax_second(state, connections):
    if check_turn(state) == "O":
        return MIN_second(state, connections)
    elif check_turn(state) == "X":
        return MAX_second(state, connections)


def first_move_4(state):
    turn = check_turn(state)
    if turn == "X":
        state = result(state, (2, 2))
    else:
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == "X":
                    if i == 2 and j == 2:
                        state = result(state, (1, 1))
                    else:
                        state = result(state, (2, 2))
    return state


def game_playing_x_4(initial, connections):
    state = initial
    no_turns = 1
    while is_ended(state, connections) == False:
        display(state)
        command = str(input("Enter move as ij: "))
        state = result(state, (int(command[0]), int(command[1])))
        display(state)
        if is_ended(state, connections) == True:
            break
        if no_turns > 1:
            state = result(state, minimax(state, connections))
        else:
            state = first_move_4(state)
        no_turns += 1
    display(state)
    if utility(state, connections) == 1:
        print("You won the game")
    elif utility(state, connections) == -1:
        print("You lost the game")
    else:
        print("Error")


def game_playing_o_4(initial, connections):
    state = initial
    no_turns = 1
    while is_ended(state, connections) == False:
        display(state)
        if no_turns == 1:
            state = first_move_4(state)
        elif no_turns == 2:
            state = result(state, MAX_second(state, connections))
        else:
            state = result(state, minimax(state, connections))
        display(state)
        if is_ended(state, connections) == True:
            break
        command = str(input("Enter move as ij: "))
        state = result(state, (int(command[0]), int(command[1])))
        no_turns += 1
    display(state)
    if utility(state, connections) == 1:
        print("You lost the game")
    elif utility(state, connections) == -1:
        print("You won the game")
    else:
        print("Error")


board4 = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

graph = {}
addNodes(graph, makes_node(board4))
addEdges(graph, make_edges(board4))
# game_playing_x_4(board4, graph)
# game_playing_o_4(board4, graph)


l = 51.96152423
h = 25.98076211


def lines():
    x = 45
    for i in range(5):
        a = 0
        b = 0
        c = 0
        for j in range(5):
            if i <= 3:
                pygame.draw.line(screen, white, (x+a+h, 150+h+b+c),
                                 (x+45+h+a, 150+c+b))
                if j != 4 or i != 3:
                    pygame.draw.line(
                        screen, white, (x+45+h+a, 150+c+b), (x+90+h+a, 150+h+b+c))
            if j == 4:
                continue
            pygame.draw.line(screen, white, (x+h+a, 150+c+b+h),
                             (x+h+a, 150+c+b+l+h))
            a += 45
            b += l
            c += h
        x += 90
    x = 45
    a = 0
    b = 0
    c = 0
    # lst = [(45+h+1, 150+h), (90+h, 151), (135+h-1, 150+h),
    #        (135+h-1, 150+h+l), (90+h, 150+h+l+h-1), (45+h+1, 150+h+l)]
    # pygame.gfxdraw.filled_polygon(screen, lst, red)
    for i in range(4):
        pygame.draw.line(screen, white, (x+h+a, 150+c+b+h+l),
                         (x+45+h+a, 150+c+b+h+l+h))
        a += 45
        b += l
        c += h


hex_vertices = list()
row1 = []
x = 0
for i in range(4):
    hex1 = [(45+h+1+x, 150+h), (90+h+x, 151), (135+h-1+x, 150+h),
            (135+h-1+x, 150+h+l), (90+h+x, 150+h+l+h-1), (45+h+1+x, 150+h+l)]
    row1.append(hex1.copy())
    x += 90
hex_vertices.append(row1.copy())
row1 = []
x = 0
for i in range(4):
    hex1 = [(90+h+1+x, 150+h+h+l), (135+h+x, 151+h+l), (180+h-1+x, 150+h+h+l),
            (180+h-1+x, 150+h+l+h+l), (135+h+x, 150+h+l+h-1+h+l), (90+h+1+x, 150+h+l+h+l)]
    row1.append(hex1.copy())
    x += 90
hex_vertices.append(row1.copy())
row1 = []
x = 0
for i in range(4):
    hex1 = [(135+h+1+x, 150+h+h+h+l+l), (180+h+x, 151+h+h+l+l), (225+h-1+x, 150+h+l+h+h+l),
            (225+h-1+x, 150+h+h+l+l+h+l), (180+h+x, 150+h+h+l+l+h-1+h+l), (135+h+1+x, 150+h+h+l+l+h+l)]
    row1.append(hex1.copy())
    x += 90
hex_vertices.append(row1.copy())
row1 = []
x = 0
for i in range(4):
    hex1 = [(180+h+1+x, 150+h+h+l+h+h+l+l), (225+h+x, 151+h+h+l+h+l+l), (270+h-1+x, 150+h+h+l+l+h+h+l),
            (270+h-1+x, 150+h+h+l+h+l+l+h+l), (225+h+x, 150+h+h+l+h+l+l+h-1+h+l), (180+h+1+x, 150+h+h+l+h+l+l+h+l)]
    row1.append(hex1.copy())
    x += 90
hex_vertices.append(row1.copy())


def lst_cord(coord):
    x1 = 0
    for i in range(4):
        if 45+h+x1 <= coord[0] <= 135+h+x1 and 150+h <= coord[1] <= 150+h+l:
            return (0, i)
        x1 += 90
    x1 = 0
    for i in range(4):
        if 90+h+x1 <= coord[0] <= 180+h+x1 and 150+h+h+l <= coord[1] <= 150+h+h+l+l:
            return (1, i)
        x1 += 90
    x1 = 0
    for i in range(4):
        if 135+h+x1 <= coord[0] <= 225+h+x1 and 150+(3*h)+(2*l) <= coord[1] <= 150+(3*h)+(3*l):
            return (2, i)
        x1 += 90
    x1 = 0
    for i in range(4):
        if 180+h+x1 <= coord[0] <= 270+h+x1 and 150+4*h+3*l <= coord[1] <= 150+4*h+4*l:
            return (3, i)
        x1 += 90


def make_hex(p_no, coord):
    color = blue
    if p_no == 0:
        color = red
    pygame.gfxdraw.filled_polygon(
        screen, hex_vertices[coord[0]][coord[1]], color)


def change_in_states(initial, final):
    for i in range(len(initial)):
        for j in range(len(initial[i])):
            if initial[i][j] != final[i][j]:
                return (i, j)


pygame.init()
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
screen = pygame.display.set_mode((640, 570))
pygame.display.set_caption('Hex')
screen.fill(black)
font = pygame.font.Font('freesansbold.ttf', 40)
large_font = pygame.font.Font('freesansbold.ttf', 150)
lines()
turn = 0
player = 1
exited = False
done_spaces = []

turn_of = 0
while not(exited):
    if turn_of % 2 == 0:
        text = font.render("Demon's Turn", True, white)
        textrect = text.get_rect()
        textrect.center = (320, 40)
    elif turn_of % 2 != 0:
        text = font.render("Your Turn", True, white)
        textrect = text.get_rect()
        textrect.center = (320, 40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exited = True
        if event.type == pygame.MOUSEBUTTONDOWN and turn_of % 2 == 1 and not(is_ended(board4, graph)):
            a = lst_cord(event.pos)
            if a == None:
                pass
            elif not(a in done_spaces):
                board4 = result(board4, a)
                make_hex(turn_of % 2, a)
                done_spaces.append(a)
                turn_of += 1
        elif turn_of % 2 == 0 and not(is_ended(board4, graph)):

            temp = board4.copy()
            if turn_of == 0:
                board4 = first_move_4(board4)
            elif turn_of in [2, 4]:
                board4 = result(board4, MAX_second(board4, graph))
            else:
                board4 = result(board4, minimax(board4, graph))
            d = change_in_states(temp, board4)
            done_spaces.append(d)
            make_hex(turn_of % 2, d)
            turn_of += 1

    pygame.display.update()
