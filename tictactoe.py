import pygame,sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BG_COLOR = (28,170,156)
LINE_COLOR = (23,145,135)
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_COLOR = (239, 251, 200)
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_COLOR = (66,66,66)
CROSS_WIDTH = 22
SPACE = 40

font = pygame.font.Font(None, 50)
pvp_button = pygame.Rect(150, 180, 300, 80)
cpu_button = pygame.Rect(150, 340, 300, 80)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')


#board
board=np.zeros((BOARD_ROWS,BOARD_COLS))
#print(board)

def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0,200), (600,200), LINE_WIDTH)    #1st horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0,400), (600,400), LINE_WIDTH)    #2nd horizontal line
    
    pygame.draw.line(screen, LINE_COLOR, (200,0), (200,600), LINE_WIDTH)    #1st vertical line
    pygame.draw.line(screen, LINE_COLOR, (400,0), (400,600), LINE_WIDTH)    #2nd vertical Line

def draw_figure():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col*200 + SPACE, row *200+200-SPACE), (col*200+200-SPACE, row*200+SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col*200 + SPACE, row *200+SPACE), (col*200+200-SPACE, row*200+200-SPACE), CROSS_WIDTH)


def mark_square(row,col,player):
    board[row][col] = player

def available_square(row,col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def check_win(player, draw=True):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            if draw:
                draw_vertical_win_line(col, player)
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            if draw:
                draw_horizontal_win_line(row, player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        if draw:
            draw_asc_win_line(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        if draw:
            draw_desc_win_line(player)
        return True

    return False


def draw_vertical_win_line(col,player):
    posX=col*200+100
    if player == 1:
        color= CIRCLE_COLOR
    elif player == 2:
        color= CROSS_COLOR

    pygame.draw.line(screen, color, (posX,15),(posX, HEIGHT-15), 15)

def draw_horizontal_win_line(row,player):
    posY=row*200+100
    if player == 1:
        color= CIRCLE_COLOR
    elif player == 2:
        color= CROSS_COLOR

    pygame.draw.line(screen, color, (15,posY),(WIDTH-15, posY), 15)


def draw_asc_win_line(player):
    if player == 1:
        color= CIRCLE_COLOR
    elif player == 2:
        color= CROSS_COLOR

    pygame.draw.line(screen, color, (15,HEIGHT-15), (WIDTH-15, 15), 15)

def draw_desc_win_line(player):
    if player == 1:
        color= CIRCLE_COLOR
    elif player == 2:
        color= CROSS_COLOR

    pygame.draw.line(screen, color, (15,15), (WIDTH-15, HEIGHT-15), 15)

def draw_menu():
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, LINE_COLOR, pvp_button)
    pygame.draw.rect(screen, LINE_COLOR, cpu_button)

    pvp_text = font.render("Player vs Player", True, CIRCLE_COLOR)
    cpu_text = font.render("Player vs Computer", True, CIRCLE_COLOR)
    screen.blit(pvp_text, pvp_text.get_rect(center=pvp_button.center))
    screen.blit(cpu_text, cpu_text.get_rect(center=cpu_button.center))

def make_move(row, col):
    global player, game_over
    mark_square(row, col, player)
    draw_figure()
    if check_win(player):
        game_over = True
    elif is_board_full():
        game_over = True
    player = 2 if player == 1 else 1

def minimax(is_computer_turn):
    # Stopping points: someone won, or it's a draw
    if check_win(2, False):
        return 1
    if check_win(1, False):
        return -1
    if is_board_full():
        return 0

    if is_computer_turn:
        best = -100
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    board[row][col] = 2                # try the move
                    score = minimax(False)             # human's turn next
                    board[row][col] = 0                # undo the move
                    best = max(best, score)
        return best
    else:
        best = 100
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    board[row][col] = 1
                    score = minimax(True)
                    board[row][col] = 0
                    best = min(best, score)
        return best

def best_move():
    best_score = -100
    move = None
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

def computer_move():
    row, col = best_move()
    make_move(row, col)

def restart():
    main()

def main():
    draw_menu()
    
    global player, game_over, state
    state="menu"
    mode=None
    player = 1
    game_over=False

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col]= 0

    #mainloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if state == "menu":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pvp_button.collidepoint(event.pos):
                        mode = "pvp"
                        state = "playing"
                    elif cpu_button.collidepoint(event.pos):
                        mode = "computer"
                        state = "playing"
                    if state == "playing":
                        screen.fill(BG_COLOR)
                        draw_lines()

            else:  # state == "playing"
                human_turn = (mode == "pvp") or (player == 1)

                if event.type == pygame.MOUSEBUTTONDOWN and not game_over and human_turn:
                    clicked_row = int(event.pos[1] // 200)
                    clicked_col = int(event.pos[0] // 200)

                    if available_square(clicked_row, clicked_col):
                        make_move(clicked_row, clicked_col)

                        if mode == "computer" and not game_over:
                            computer_move()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        restart()

        if state == "menu":
            draw_menu()

        pygame.display.update()


if __name__=="__main__":
    main()
