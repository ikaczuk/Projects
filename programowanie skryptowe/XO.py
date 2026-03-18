import pygame as pg
import sys

pg.init()

screen_size = 750,750
screen= pg.display.set_mode(screen_size)
pg.display.set_caption("Kółko i krzyżyk")

X = pg.image.load("Users\ikawa\PycharmProjects\pythonProject1/X.png")
O = pg.image.load("Users\ikawa\PycharmProjects\pythonProject1/O.png")
tło = "white"

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
graphical_board = [[[None, None], [None, None], [None, None]],
                   [[None, None], [None, None], [None, None]],
                   [[None, None], [None, None], [None, None]]]

to_move = 'X'

SCREEN.fill(BG_COLOR)
SCREEN.blit(BOARD, (64, 64))

pygame.display.update()

def rys_tlo():  #rysowanie planszy
    screen.fill(pg.Color("grey"))
    i = 1
    while i * 80 < 720:
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(i * 245 + 15, 15), pg.Vector2(i * 245 + 15, 735), 5)  # rysowanie pionowych pasków
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(15, i * 245 + 15), pg.Vector2(735, i * 245 + 15), 5)  # rysowanie poziomych pasków
        i += 1


def rys_XO():


def render_board(board, ximg, oimg):
    global graphical_board
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                # Create an X image and rect
                graphical_board[i][j][0] = ximg
                graphical_board[i][j][1] = ximg.get_rect(center=(j * 300 + 150, i * 300 + 150))
            elif board[i][j] == 'O':
                graphical_board[i][j][0] = oimg
                graphical_board[i][j][1] = oimg.get_rect(center=(j * 300 + 150, i * 300 + 150))


def add_XO(board, graphical_board, tura):
    current_pos = pg.mouse.get_pos()
    x = pozycja[0]//245
    y = pozycja[1]//245
    if board[y][x] != 'O' and board[y][x] != 'X':
        board[y][x] = tura
        if tura == 'O':
            tura = 'X'
        else:
            tura = 'O'

    render_board(board, X, O)

    for i in range(3):
        for j in range(3):
            if graphical_board[i][j][0] is not None:
                SCREEN.blit(graphical_board[i][j][0], graphical_board[i][j][1])

    return board, tura


game_finished = False


def check_win(board):
    winner = None
    for row in range(0, 3):
        if ((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            winner = board[row][0]
            for i in range(0, 3):
                graphical_board[row][i][0] = pygame.image.load(f"assets/Winning {winner}.png")
                SCREEN.blit(graphical_board[row][i][0], graphical_board[row][i][1])
            pygame.display.update()
            return winner

    for kolumna in range(0, 3):
        if ((board[0][kolumna] == board[1][kolumna] == board[2][kolumna]) and (board[0][kolumna] is not None)):
            winner = board[0][kolumna]
            for i in range(0, 3):
                graphical_board[i][kolumna][0] = pygame.image.load(f"assets/Winning {winner}.png")
                SCREEN.blit(graphical_board[i][kolumna][0], graphical_board[i][kolumna][1])
            pg.display.update()
            return winner

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner = board[0][0]
        graphical_board[0][0][0] = pg.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[0][0][0], graphical_board[0][0][1])
        graphical_board[1][1][0] = pg.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[1][1][0], graphical_board[1][1][1])
        graphical_board[2][2][0] = pg.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[2][2][0], graphical_board[2][2][1])
        pg.display.update()
        return winner

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner = board[0][2]
        graphical_board[0][2][0] = pg.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[0][2][0], graphical_board[0][2][1])
        graphical_board[1][1][0] = pg.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[1][1][0], graphical_board[1][1][1])
        graphical_board[2][0][0] = pg.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[2][0][0], graphical_board[2][0][1])
        pg.display.update()
        return winner

    if winner is None:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    return None
        return "DRAW"


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board, to_move = add_XO(board, graphical_board, to_move)

            if game_finished:
                board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                graphical_board = [[[None, None], [None, None], [None, None]],
                                   [[None, None], [None, None], [None, None]],
                                   [[None, None], [None, None], [None, None]]]

                to_move = 'X'

                SCREEN.fill(BG_COLOR)
                SCREEN.blit(BOARD, (64, 64))

                game_finished = False

                pg.display.update()

            if check_win(board) is not None:
                game_finished = True

            pg.display.update()
    rys_tlo()