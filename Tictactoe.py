import sys

from numpy.core.fromnumeric import diagonal
import pygame
import numpy as np
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
