import pygame

import time

import sys

eng_board = [['  ' for i in range(8)] for i in range(8)]

class eng_Piece:
    def __init__(self, team, type, image, killable=False):
        self.team = team
        self.type = type
        self.killable = killable
        self.image = image


## Creates instances of chess pieces, so far we got: pawn, king, rook and bishop
## The first parameter defines what team its on and the second, what type of piece it is
bp = eng_Piece('b', 'p', 'b_pawn.png')
wp = eng_Piece('w', 'p', 'w_pawn.png')
bk = eng_Piece('b', 'k', 'b_king.png')
wk = eng_Piece('w', 'k', 'w_king.png')
br = eng_Piece('b', 'r', 'b_rook.png')
wr = eng_Piece('w', 'r', 'w_rook.png')
bb = eng_Piece('b', 'b', 'b_bishop.png')
wb = eng_Piece('w', 'b', 'w_bishop.png')
bq = eng_Piece('b', 'q', 'b_queen.png')
wq = eng_Piece('w', 'q', 'w_queen.png')
bkn = eng_Piece('b', 'kn', 'b_knight.png')
wkn = eng_Piece('w', 'kn', 'w_knight.png')


starting_order = {(0, 0): pygame.image.load(br.image), (1, 0): pygame.image.load(bkn.image),
                  (2, 0): pygame.image.load(bb.image), (3, 0): pygame.image.load(bq.image),
                  (4, 0): pygame.image.load(bk.image), (5, 0): pygame.image.load(bb.image),
                  (6, 0): pygame.image.load(bkn.image), (7, 0): pygame.image.load(br.image),
                  (0, 1): pygame.image.load(bp.image), (1, 1): pygame.image.load(bp.image),
                  (2, 1): pygame.image.load(bp.image), (3, 1): pygame.image.load(bp.image),
                  (4, 1): pygame.image.load(bp.image), (5, 1): pygame.image.load(bp.image),
                  (6, 1): pygame.image.load(bp.image), (7, 1): pygame.image.load(bp.image),

                  (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
                  (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,
                  (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
                  (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,
                  (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
                  (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,
                  (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
                  (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

                  (0, 6): pygame.image.load(wp.image), (1, 6): pygame.image.load(wp.image),
                  (2, 6): pygame.image.load(wp.image), (3, 6): pygame.image.load(wp.image),
                  (4, 6): pygame.image.load(wp.image), (5, 6): pygame.image.load(wp.image),
                  (6, 6): pygame.image.load(wp.image), (7, 6): pygame.image.load(wp.image),
                  (0, 7): pygame.image.load(wr.image), (1, 7): pygame.image.load(wkn.image),
                  (2, 7): pygame.image.load(wb.image), (3, 7): pygame.image.load(wq.image),
                  (4, 7): pygame.image.load(wk.image), (5, 7): pygame.image.load(wb.image),
                  (6, 7): pygame.image.load(wkn.image), (7, 7): pygame.image.load(wr.image),}


def create_board(eng_board):
    eng_board[0] = [eng_Piece('b', 'r', 'b_rook.png'), eng_Piece('b', 'kn', 'b_knight.png'), eng_Piece('b', 'b', 'b_bishop.png'), \
               eng_Piece('b', 'q', 'b_queen.png'), eng_Piece('b', 'k', 'b_king.png'), eng_Piece('b', 'b', 'b_bishop.png'), \
               eng_Piece('b', 'kn', 'b_knight.png'), eng_Piece('b', 'r', 'b_rook.png')]

    eng_board[7] = [eng_Piece('w', 'r', 'w_rook.png'), eng_Piece('w', 'kn', 'w_knight.png'), eng_Piece('w', 'b', 'w_bishop.png'), \
               eng_Piece('w', 'q', 'w_queen.png'), eng_Piece('w', 'k', 'w_king.png'), eng_Piece('w', 'b', 'w_bishop.png'), \
               eng_Piece('w', 'kn', 'w_knight.png'), eng_Piece('w', 'r', 'w_rook.png')]

    for i in range(8):
        eng_board[1][i] = eng_Piece('b', 'p', 'b_pawn.png')
        eng_board[6][i] = eng_Piece('w', 'p', 'w_pawn.png')
    return eng_board

WIDTH = 800
eng_WIN = pygame.display.set_mode((WIDTH, WIDTH))

""" This is creating the eng_window that we are playing on, it takes a tuple argument which is the dimensions of the eng_window so in this case 800 x 800px
"""

pygame.display.set_caption("Chess Engine")
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)

class eng_Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = int(row * width)
        self.y = int(col * width)
        self.colour = WHITE
        self.occupied = None

    def draw(self, eng_WIN):
        pygame.draw.rect(eng_WIN, self.colour, (self.x, self.y, WIDTH / 8, WIDTH / 8))

    def setup(self, eng_WIN):
        if starting_order[(self.row, self.col)]:
            if starting_order[(self.row, self.col)] == None:
                pass
            else:
                eng_WIN.blit(starting_order[(self.row, self.col)], (self.x, self.y))

        """
        For now it is draeng_wing a rectangle but eventually we are going to need it
        to use blit to draw the chess pieces instead
        """

def make_grid(rows, width):
    eng_grid = []
    gap = WIDTH // rows
    print(gap)
    for i in range(rows):
        eng_grid.append([])
        for j in range(rows):
            eng_node = eng_Node(j, i, gap)
            eng_grid[i].append(eng_node)
            if (i+j)%2 ==1:
                eng_grid[i][j].colour = GREY
    return eng_grid
"""
This is creating the nodes thats are on the eng_board(so the chess tiles)
I've put them into a 2d array which is identical to the dimesions of the chessboard
"""


def draw_grid(eng_win, rows, width):
    gap = width // 8
    for i in range(rows):
        pygame.draw.line(eng_win, BLACK, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(eng_win, BLACK, (j * gap, 0), (j * gap, width))

    """
    The nodes are all white so this we need to draw the grey lines that separate all the chess tiles
    from each other and that is what this function does"""


def update_display(eng_win, eng_grid, rows, width):
    for row in eng_grid:
        for spot in row:
            spot.draw(eng_win)
            spot.setup(eng_win)
    draw_grid(eng_win, rows, width)
    pygame.display.update()

def Find_eng_Node(pos, WIDTH):
    interval = WIDTH / 8
    y, x = pos
    rows = y // interval
    columns = x // interval
    return int(rows), int(columns)

def remove_highlight(eng_grid):
    for i in range(len(eng_grid)):
        for j in range(len(eng_grid[0])):
            if (i+j)%2 == 0:
                eng_grid[i][j].colour = WHITE
            else:
                eng_grid[i][j].colour = GREY
    return eng_grid




create_board(eng_board)

def eng_blue(x,y,team):
    blue_list = []
    red_list = []
    if team == 'w':
        blue_list.append[(x,y)] 
        return blue_list
    else: 
        red_list.append[(x,y)]
        return red_list

def window_main(eng_WIN, WIDTH, eng_grid):
    while True:
        pygame.time.delay(50) ##stops cpu dying
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            """This quits the program if the player closes the eng_window"""

            update_display(eng_WIN, eng_grid, 8, WIDTH)


def engine_main(eng_WIN, WIDTH):
    eng_grid = make_grid(8, WIDTH)
    while True: 
        damn = time.time()


        


def eng_window():
    window_main(eng_WIN, WIDTH)

engine_main(eng_WIN, WIDTH)