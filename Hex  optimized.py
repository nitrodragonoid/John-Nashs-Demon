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
    #checking is a path can exist
    check = False
    for j in getNeighbors(G, "start 1"):
        if state[int(j[0])][int(j[1])] == "X":
            check = True
    for j in getNeighbors(G, "end 1"):
        if state[int(j[0])][int(j[1])] == "X":
            check = True
    if check == False:
        return False
    #if a path can exists we check if it does exist
    queue = [] #Declare a queue for keeping track of nodes
    visited = [] #to keep track a node is visited
    nodes = listOfNodes(G)
    enQueue(queue,"start 1") #start searching from the start
    while is_emptyQueue(queue) == False: #loop untill all nodes are visited
          f = getFront(queue) #get the front of the queue
          if f not in visited:
             visited.append(f) #make sure to mark the first node as visited
          next = getNeighbors(G, f) #get all the nodes connested to the node on the front of the queue
          for i in next:
              if i == "end 1": #if end is reached the game is ended
                 return True
              if (i != "start 1") and (i != "end 1") and (i != "start 2") and (i != "end 2"):
                 if (i not in visited) and (state[int(i[0])][int(i[1])] == "X"): #enQueue all the nodes connected to f that are not yet visited and contains X
                    enQueue(queue,i) 
                    visited.append(i) #mark them as visited
          if is_emptyQueue(queue) == False: #if queue is not empty remove the front of the queue
             deQueue(queue)
    return False

def check_player_2(state,G):
    #checking is a path can exist
    check = False
    for j in getNeighbors(G, "start 2"):
        if state[int(j[0])][int(j[1])] == "O":
            check = True
    for j in getNeighbors(G, "end 2"):
        if state[int(j[0])][int(j[1])] == "O":
            check = True
    if check == False:
        return False
    #if a path can exists we check if it does exist
    queue = [] #Declare a queue for keeping track of nodes
    visited = [] #to keep track a node is visited
    nodes = listOfNodes(G)
    enQueue(queue,"start 2") #start searching from the start
    while is_emptyQueue(queue) == False: #loop untill all nodes are visited
          f = getFront(queue) #get the front of the queue
          if f not in visited:
             visited.append(f) #make sure to mark the first node as visited
          next = getNeighbors(G, f) #get all the nodes connested to the node on the front of the queue
          for i in next:
              if i == "end 2": #if end is reached the game is ended
                 return True
              if (i != "start 1") and (i != "end 1") and (i != "start 2") and (i != "end 2"):
                 if (i not in visited) and (state[int(i[0])][int(i[1])] == "O"): #enQueue all the nodes connected to f that are not yet visited and contains X
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

####### alpha beta pruning #######
def max_value(state,connections):
    if is_ended(state,connections) == True:
        return utility(state,connections)
    v = -9999999
    for a in action(state):
        v = max(v,min_value(result(state,a),connections))
        if v == 1:
            break
    return v

def min_value(state,connections):
    if is_ended(state,connections) == True:
        return utility(state,connections)
    v = 9999999
    for a in action(state):
        v = min(v,max_value(result(state,a),connections))
        if v == -1:
            break
    return v

def max_pruning(state,connections,beta):
    if is_ended(state,connections) == True:
        return utility(state,connections)
    v = -9999999
    for a in action(state):
        check = min_pruning(result(state,a),connections,beta)
        if v < check:
            v = check
        if check >= beta:
            break
        if v == 1:
            break
    return v

def min_pruning(state,connections,alpha):
    if is_ended(state,connections) == True:
        return utility(state,connections)
    v = 9999999
    for a in action(state):
        check = max_pruning(result(state,a),connections,alpha)
        if v > check:
            v = check
        if check <= alpha:
            break
        if v == -1:
            break
    return v


def MAX(state,connections):
    val = -9999999
    moves = action(state)
    for a in moves:     
        if a == moves[0]:
            x = min_value(result(state,a),connections)
            if x > val:
                val = x
                best = a
        else:
            x = min_pruning(result(state,a),connections,val)
            if x > val:
                val = x
                best = a
        if val == 1:
            break
    return best

def MIN(state,connections):
    val = 9999999
    moves = action(state)
    for a in moves:     
        if a == moves[0]:
            x = max_value(result(state,a),connections)
            if x < val:
                val = x
                best = a
        else:
            x = max_pruning(result(state,a),connections,val)
            if x < val:
                val = x
                best = a
        if val == -1:
            break
    return best

def minimax(state,connections):
    if check_turn(state) == "O":
        return MIN(state,connections)
    elif check_turn(state) == "X":
        return MAX(state,connections)
####### END #######

def first_move(state):
    turn = check_turn(state)
    if turn == "X":
        state = result(state,(0,0))
    else:
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == "X":
                    if i != len(state)-1:
                        state = result(state,(i+1,j))
                    else:
                        state = result(state,(i-1,j))
    return state


def game_playing_x(initial,connections):    
    state = initial
    while is_ended(state,connections) == False:
        display(state)
        command = str(input("Enter move as ij: "))
        state = result(state,(int(command[0]),int(command[1])))
        display(state)
        if is_ended(state,connections) == True:
            break	
        start = time.time()
        state = result(state,minimax(state,connections))
        end = time.time()
        print(end - start)
    display(state)
    if utility(state,connections) == 1:
        print("You won the game")
    elif utility(state,connections) == -1:
        print("You lost the game")
    else:
        print("Error")
        
def game_playing_x_4(initial,connections): #For 4x4, by fixing the first move to decrease the time complexity 
    state = initial
    no_turns = 1
    while is_ended(state,connections) == False:
        display(state)
        command = str(input("Enter move as ij: "))
        state = result(state,(int(command[0]),int(command[1])))
        display(state)
        if is_ended(state,connections) == True:
            break	
        if no_turns > 1:
            start = time.time()
            state = result(state,minimax(state,connections))
            end = time.time()
            print(end - start)
        else:
            state = first_move(state)
        no_turns += 1
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

board4 = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]


graph = {}
addNodes(graph,makes_node(board4))
addEdges(graph,make_edges(board4))
#game_playing_x(board,graph)
game_playing_x_4(board4,graph)





