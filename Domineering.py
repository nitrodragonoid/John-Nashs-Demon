game_tree = dict()
grid = [[0 for _ in range(3)] for __ in range(3)]
def node_grid_maker(grid, p_no, x1, y1, x2, y2):
    tmp = grid.copy()
    tmp[x1][y1] = p_no
    tmp[x2][y2] = p_no
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
