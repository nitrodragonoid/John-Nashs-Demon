game_tree = dict()
grid = [[0 for _ in range(4)] for __ in range(3)]


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
                    new_comb[i][j] = p_no
                    new_comb[i+1][j] = p_no
                    b = list_to_tuple(new_comb.copy())
                    req.append(b)
                if j+1 < len(a[i]) and a[i][j+1] == 0:
                    new_comb = []
                    for x in a:
                        new_comb.append(x.copy())
                    new_comb[i][j] = p_no
                    new_comb[i][j+1] = p_no
                    b = list_to_tuple(new_comb.copy())
                    req.append(b)
    return req


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
# Prinitng all possiblities i.e. Nodes
for i in game_tree:
    for j in i:
        print(j)
    print()
