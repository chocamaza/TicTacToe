import pygame
import sys
import math

red = (255, 0, 0)
green = (0, 255, 0)
blue = (55, 55, 200)

Rows, Columns = 3, 3
square_size = 200
circle_radius = 60
offset = 55
circle_line_width = 15
x_line_width = 25

Width, Height = square_size * Columns, square_size * Rows

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]




def check_win(player):
    ver_win = Vertical(player)
    hor_win = Horizontal(player)
    dia_win = Diagonal(player)

    if ver_win:
        print("Gameover")
        return True
    elif hor_win:
        print("l1")
        return True
    elif dia_win:
        print('oo')
        return True
    else:
        return False


def Vertical(player):
    for i in range(Columns):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            WinVerticalLine(i, player)
            print("V_F")
            return True
    print("V")
    return False


def Horizontal(player):
    for i in range(Rows):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            WinHorizontalLine(i, player)
            print("H_F")
            return True
    print("H")
    return False


def Diagonal(player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        WinDiagonalLine()
        print("D_F")
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        WinDiagonalLine(False)
        print("dF")
        return True
    else:
        print("hhhb")
        return False


def WinVerticalLine(col, player):
    x_cor = col * square_size + square_size / 2

    if player == 1:
        pygame.draw.line(screen, red, (x_cor, 10), (x_cor, Height - 10), circle_line_width)
    else:
        pygame.draw.line(screen.red, (x_cor, 10), (x_cor, Height - 10), circle_line_width)


def WinHorizontalLine(row, player):
    y_cor = row * square_size + square_size / 2
    if player == 1:
        pygame.draw.line(screen, red, (10, y_cor), (y_cor, Width - 10), circle_line_width)
    else:
        pygame.draw.line(screen, red, (10, y_cor), (y_cor, Width - 10), circle_line_width)


def WinDiagonalLine(other=True):
    if other:
        pygame.draw.line(screen, red, (25, 25), (Width - 25, Height - 25), x_line_width)
    else:
        pygame.draw.line(screen, red, (25, Height - 25), (Width - 25, 25), x_line_width)


def avail_sqr(row, col):
    avail = board[row][col] == 0
    return avail


def mark_square(row, col, player):
    board[row][col] = player


def DrawFig():
    for col in range(Columns):
        for row in range(Rows):
            if board[row][col] == 1:
                pygame.draw.circle(screen, blue,
                                   (int(col * square_size + square_size / 2), int(row * square_size + square_size / 2)),
                                   circle_radius, circle_line_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, red, (col * square_size + offset, row * square_size + offset),
                                 (col * square_size+ square_size - offset, row * square_size + square_size - offset), x_line_width)
                pygame.draw.line(screen, red, (col * square_size + offset, row * square_size + square_size + offset),
                                 (col * square_size +square_size - offset, row * square_size + offset), x_line_width)


def FullBoard():
    for i in range(Columns):
        for j in range(Rows):
            if board[i][j] == 0:
                return False
    return True


def DrawLines():
    pygame.draw.line(screen, green, (0, 200), (600, 200), 5)
    pygame.draw.line(screen, green, (0, 400), (600, 400), 5)
    pygame.draw.line(screen, green, (200, 0), (200, 600), 5)
    pygame.draw.line(screen, green, (400, 0), (400, 600), 5)


# Graphic Board
pygame.init()
pygame.display.set_caption('Tic_Tac_Toe')
screen = pygame.display.set_mode((Width, Height))
screen.fill((55, 55, 55))
DrawLines()
pygame.display.update()

# Variables
player = 0
GameOver = False
in_menu = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not GameOver:
            y_pos = event.pos[1]
            row = int(math.floor(y_pos / square_size))
            x_pos = event.pos[0]
            col = int(math.floor(x_pos / square_size))

            if player % 2 == 0:
                if avail_sqr(row, col):
                    mark_square(row, col, 1)
                    if check_win(1):
                        GameOver = True
                    player += 1
            else:
                if avail_sqr(row, col):
                    mark_square(row, col, 2)
                    if check_win(2):
                        GameOver = True
                    player += 1

            if FullBoard():
                GameOver = True

    DrawFig()
    pygame.display.update()

print('Over')