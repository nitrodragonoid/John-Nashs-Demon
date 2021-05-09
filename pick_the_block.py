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
