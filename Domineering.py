game_tree = dict()
grid = [[0 for _ in range(4)] for __ in range(3)]


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
    while True:
        a = idx1.split()
        a = [int(i) for i in a]
        b = idx2.split()
        b = [int(i) for i in b]
        if (a[0]+1 == b[0] and a[1] == b[1]):
            break
        elif (a[0] == b[0] and a[1]+1 == b[1]):
            break
        idx1 = int(input("Enter Valid Index 1: "))
        idx2 = int(input("Enter Valid Index 2: "))
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
    for i in visited:
        if len(graph[i]) == 0:
            a = i
            break
    sequence = list()
    while a != temp:
        sequence.append(a)
        a = parent[a]
    sequence.append(temp)
    return sequence[-2]


def tuple_to_list(grid):
    lst = []
    for i in grid:
        lst.append(list(i))
    return lst


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

while not(is_full(grid)):
    p_no = player_determiner(grid)
    display_grid(grid)
    print(f"Player {p_no} turn.")
    if count % 2 == 0:
        idx1 = input("Enter Index 1: ")
        idx2 = input("Enter Index 2: ")
        update_grid(grid, idx1, idx2, p_no)
    elif count % 2 != 0:
        x = bot(grid, player_determiner(test1), game_tree)
        grid = tuple_to_list(x).copy()
    last_turn = p_no
    count += 1
display_grid(grid)
print(f"Game Over! Player {p_no} Won !!")
