##### Queue helper functions #####
def enQueue(queue,item):
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

#Helper functions for the graph
def addNodes(G,nodes):
    for i in nodes:
        G[i] = []
    return G

def addEdges(G,edges, directed = False):
    if directed == True:
        for i in range(len(edges)):
            G[edges[i][0]].append((edges[i][1],edges[i][2]))
    elif directed == False:
        for i in range(len(edges)):
            G[edges[i][0]].append((edges[i][1],edges[i][2]))
            G[edges[i][1]].append((edges[i][0],edges[i][2]))
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
        print(i,":",G[i])

####### END #######

def makes_node(board):
    nodes = [("start 1"), ("start 2"), ("end 1"), ("end 2")]
    for i in range(len(board)):
        for j in range(len(board)):
            nodes.append((i,j))
    return nodes

def make_edges(board):
    edges = []
    for i in range(len(board)):
        for j in range(len(board)):
            if i == 0:
                edges.append(((i,j),"end 1",1))
            if i == len(board)-1:
                edges.append(((i,j),"start 1",1))
            if j == 0:
                edges.append(((i,j),"start 2",1))
            if j == len(board)-1:
                edges.append(((i,j),"end 2",1))
            if i != 0:
                edges.append(((i,j),(i-1,j),1)) #connect to the node above
                if j != 0:
                    edges.append(((i,j),(i-1,j-1),1)) #connect to the node above and to the left 
            if i != len(board)-1:
                edges.append(((i,j),(i+1,j),1)) #connect to the node below
                if j != len(board)-1:
                    edges.append(((i,j),(i+1,j+1),1)) #connect to the node below and to the right
            if j != 0:
                edges.append(((i,j),(i,j-1),1)) #connect to the node on the left
            if j != len(board[i])-1:
                edges.append(((i,j),(i,j+1),1)) #connect to the node on the right
    return edges

def check_player_1(state,G):
    queue = [] #Declare a queue for keeping track of nodes
    visited = [] #to keep track a node is visited
    nodes = listOfNodes(G)
    enQueue(queue,"start 1") 
    while is_emptyQueue(queue) == False: #loop untill all nodes are visited
          f = getFront(queue) #get the front of the queue
          if f not in visited:
             visited.append(f) #make sure to mark the first node as visited
          next = getNeighbors(G, f) #get all the nodes connested to the node on the front of the queue
          for i in next:
              if i == "end 1":
                 return True
              if (i != "start 1") and (i != "end 1") and (i != "start 2") and (i != "end 2"):
                 if (i not in visited) and (state[int(i[0])][int(i[1])] == "X"): #enQueue all the nodes connected to f that are not yet visited
                    enQueue(queue,i) 
                    visited.append(i) #mark them as visited
          if is_emptyQueue(queue) == False: #if queue is not empty remove the front of the queue
             deQueue(queue)
    return False

def check_player_2(state,G):
    queue = [] #Declare a queue for keeping track of nodes
    visited = [] #to keep track a node is visited
    nodes = listOfNodes(G)
    enQueue(queue,"start 2") 
    while is_emptyQueue(queue) == False: #loop untill all nodes are visited
          f = getFront(queue) #get the front of the queue
          if f not in visited:
             visited.append(f) #make sure to mark the first node as visited
          next = getNeighbors(G, f) #get all the nodes connested to the node on the front of the queue
          for i in next:
              if i == "end 2":
                 return True
              if (i != "start 1") and (i != "end 1") and (i != "start 2") and (i != "end 2"):
                 if (i not in visited) and (state[int(i[0])][int(i[1])] == "O"): #enQueue all the nodes connected to f that are not yet visited
                    enQueue(queue,i) 
                    visited.append(i) #mark them as visited
          if is_emptyQueue(queue) == False: #if queue is not empty remove the front of the queue
             deQueue(queue)
    return False

def is_ended(state,connections):
    if (check_player_1(state,connections) == True) or (check_player_2(state,connections) == True):
        return True
    return False

def utility(state,connections):
    if check_player_1(state,connections) == True:
        return 1
    if check_player_2(state,connections) == True:
        return -1

def action(state):
    moves = []
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == 0:
                moves.append((i,j))
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

def result(state,move):
    temp = []
    for i in state:
        temp.append(i.copy())
    temp[move[0]][move[1]] = check_turn(state)
    return temp

def display(state):
    for i in state:
        print(i)
    print("\n")

def max_value(state,connections):
    if is_ended(state,connections) == True:
        return utility(state,connections)
    v = -9999999
    for a in action(state):
        v = max(v,min_value(result(state,a),connections))
    return v

def min_value(state,connections):
    if is_ended(state,connections) == True:
        return utility(state,connections)
    v = 9999999
    for a in action(state):
        v = min(v,max_value(result(state,a),connections))
    return v

def MAX(state,connections):
    val = -9999999
    for a in action(state):
        check = state.copy()
        y = min_value(result(check,a),connections)
        if y > val:
            val = y
            best = a
    return best

def MIN(state,connections):
    val = 9999999
    for a in action(state):
        check = state.copy()     
        x = max_value(result(check,a),connections)
        if x < val:
            val = x
            best = a
    return best

def minimax(state,connections):
    if check_turn(state) == "O":
        return MIN(state,connections)
    elif check_turn(state) == "X":
        return MAX(state,connections)

def game_playing_x(initial,connections):    
    state = initial
    while is_ended(state,connections) == False:
        display(state)
        command = str(input("Enter move as ij: "))
        state = result(state,(int(command[0]),int(command[1])))
        display(state)
        if is_ended(state,connections) == True:
            break	
        state = result(state,minimax(state,connections))
    display(state)
    if utility(state,connections) == 1:
        print("You won the game")
    elif utility(state,connections) == -1:
        print("You lost the game")
    else:
        print("Error")
        
board3 = [[0,0,0],
          [0,0,0],
          [0,0,0]]

board5 = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]

board7 = [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],]

board9 = [[0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]

board11 = [[0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0]]

graph = {}
addNodes(graph,makes_node(board5))
addEdges(graph,make_edges(board5))
game_playing_x(board5,graph)
