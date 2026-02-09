import pygame
import sys

pygame.init()
X_COLOR = (200, 0, 0)
O_COLOR = (0, 0, 200)
LINE_WIDTH = 10

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

CELL_SIZE = WIDTH // 3  
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

current_player = "X"
winner = None
game_over = False

def draw_x(row, col):
    padding = 40
    x1 = col * CELL_SIZE + padding
    y1 = row * CELL_SIZE + padding
    x2 = (col + 1) * CELL_SIZE - padding
    y2 = (row + 1) * CELL_SIZE - padding

    pygame.draw.line(screen, X_COLOR, (x1, y1), (x2, y2), LINE_WIDTH)
    pygame.draw.line(screen, X_COLOR, (x1, y2), (x2, y1), LINE_WIDTH)

def draw_o(row, col):
    center_x = col * CELL_SIZE + CELL_SIZE // 2
    center_y = row * CELL_SIZE + CELL_SIZE // 2
    radius = CELL_SIZE // 2 - 40

    pygame.draw.circle(
        screen,
        O_COLOR,
        (center_x, center_y),
        radius,
        LINE_WIDTH
    )
def check_winner(board):
    
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]

    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None
    
def check_draw(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                return False
    return True


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(WHITE)

    
    
    pygame.draw.line(screen, BLACK, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), 5)
    pygame.draw.line(screen, BLACK, (CELL_SIZE * 2, 0), (CELL_SIZE * 2, HEIGHT), 5)

    
    pygame.draw.line(screen, BLACK, (0, CELL_SIZE), (WIDTH, CELL_SIZE), 5)
    pygame.draw.line(screen, BLACK, (0, CELL_SIZE * 2), (WIDTH, CELL_SIZE * 2), 5)
    

    if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
     mouse_x, mouse_y = pygame.mouse.get_pos()
     row = mouse_y // CELL_SIZE
     col = mouse_x // CELL_SIZE

     if row < 3 and col < 3:
         if board[row][col] is None:
            board[row][col] = current_player

            winner = check_winner(board)
            if winner:
                print("Winner:", winner)
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"

    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                draw_x(row, col)
            elif board[row][col] == "O":
                draw_o(row, col)            

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
