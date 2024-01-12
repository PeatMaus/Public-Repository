#Connect Four 2
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

SCREEN_HEIGHT = 450
SCREEN_WIDTH = 355
MARGIN = 10
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
MAUVE = (234, 212, 252)
BLUE = (61,89,171)
RED = (220,20,60)
GREEN = (0,100,0)
#change
running = True
reset_game = False
winner = False
player = 1
played_column = 0
column_counter0 = 0
column_counter1 = 0
column_counter2 = 0
column_counter3 = 0
column_counter4 = 0
column_counter5 = 0
column_counter6 = 0
max_row = 6
row5 = [9,9,9,9,9,9,9]
row4 = [9,9,9,9,9,9,9]
row3 = [9,9,9,9,9,9,9]
row2 = [9,9,9,9,9,9,9]
row1 = [9,9,9,9,9,9,9]
row0 = [9,9,9,9,9,9,9]

pygame.init()
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bryan's Connect Four")
surface.fill(WHITE)
pygame.display.flip()

"""
For tokens on pygame screen, these are the center coordinates for 
each square. Columns first then Rows

                    Columns
            0   1    2   3   4   5   6
        0   125  75  125 175 225 275 325 
        1   175  
Rows    2   225
        3   275        x,y
        4   325
        5   375

"""

def red_token(column, row):
    pygame.draw.circle(surface, RED, (column, row), 20, 0)
    pygame.display.update()

def black_token(column, row): 
    pygame.draw.circle(surface, BLACK,(column, row),20, 0)
    pygame.display.update()

def small_token(player):
    small_col = 145
    small_row = 75
    if player == 1:
        color = RED
    else:
        color = BLACK

    pygame.draw.circle(surface, color, (small_col, small_row), 10, 0)
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render("'s turn ", False, color)
    textRect = text.get_rect()
    textRect.center = (small_col + 50, small_row)
    surface.blit(text, textRect)
    pygame.display.update()

def grid():
    for line in range(100, SCREEN_WIDTH + 100, 50):
        pygame.draw.line(surface,BLACK,(1,line),(SCREEN_WIDTH - 3, line), 2)
        pygame.draw.line(surface,BLACK,(line-99, 102),(line - 99, SCREEN_HEIGHT-50), 2)
        font = pygame.font.Font('freesansbold.ttf', 12)
        col = 45
        for x in range(1,8):
            text = font.render(str(x), False, BLACK)
            textRect = text.get_rect()
            textRect.center = (col, 110)
            surface.blit(text, textRect)
            col +=50
        pygame.display.update()
    
def player_turn(played_column, column, player):
    if row0[played_column] == 9:
        row0[played_column] = player
        row = 375
    elif row1[played_column] == 9:
        row1[played_column] = player
        row = 325
    elif row2[played_column] == 9:
        row2[played_column] = player
        row = 275
    elif row3[played_column] == 9:
        row3[played_column] = player
        row = 225
    elif row4[played_column] == 9:
        row4[played_column] = player
        row = 175
    elif row5[played_column] == 9:
        row5[played_column] = player
        row = 125
    if player == 1:
        red_token(column, row)
        return 1
    else:
        black_token(column, row)
        return 2

def check_for_winning_move(played_column, winner):
#Vertical
    if row0[played_column] + row1[played_column] + row2[played_column] + row3[played_column] == 4 or row0[played_column] + row1[played_column] + row2[played_column] + row3[played_column] == 8:
        winner = True
        return winner
    if row1[played_column] + row2[played_column] + row3[played_column] + row4[played_column] == 4 or row1[played_column] + row2[played_column] + row3[played_column] + row4[played_column] == 8:
        winner = True
        return winner
    if row2[played_column] + row3[played_column] + row4[played_column] + row5[played_column] == 4 or row2[played_column] + row3[played_column] + row4[played_column] + row5[played_column] == 8:
        winner = True
        return winner 

# Horizontal
    for played_column_loop in range(0,4):
        if row0[played_column_loop] + row0[played_column_loop + 1] + row0[played_column_loop + 2] + row0[played_column_loop + 3] == 4 or row0[played_column_loop] + row0[played_column_loop + 1] + row0[played_column_loop + 2] + row0[played_column_loop + 3] == 8:
            winner = True
            return winner 
        if row1[played_column_loop] + row1[played_column_loop + 1] + row1[played_column_loop + 2] + row1[played_column_loop + 3] == 4 or row1[played_column_loop] + row1[played_column_loop + 1] + row1[played_column_loop + 2] + row1[played_column_loop + 3] == 8:
            winner = True
            return winner 
        if row2[played_column_loop] + row2[played_column_loop + 1] + row2[played_column_loop + 2] + row2[played_column_loop + 3] == 4 or row2[played_column_loop] + row2[played_column_loop + 1] + row2[played_column_loop + 2] + row2[played_column_loop + 3] == 8:
            winner = True
            return winner 
        if row3[played_column_loop] + row3[played_column_loop + 1] + row3[played_column_loop + 2] + row3[played_column_loop + 3] == 4 or row3[played_column_loop] + row3[played_column_loop + 1] + row3[played_column_loop + 2] + row3[played_column_loop + 3] == 8:
            winner = True
            return winner 
        if row4[played_column_loop] + row4[played_column_loop + 1] + row4[played_column_loop + 2] + row4[played_column_loop + 3] == 4 or row4[played_column_loop] + row4[played_column_loop + 1] + row4[played_column_loop + 2] + row4[played_column_loop + 3] == 8:
            winner = True
            return winner 
        if row5[played_column_loop] + row5[played_column_loop + 1] + row5[played_column_loop + 2] + row5[played_column_loop + 3] == 4 or row5[played_column_loop] + row5[played_column_loop + 1] + row5[played_column_loop + 2] + row5[played_column_loop + 3] == 8:
            winner = True
            return winner 

#Diagonal Right
    for played_column_loop in range(0,4):
        if row0[played_column_loop] + row1[played_column_loop + 1] + row2[played_column_loop + 2] + row3[played_column_loop + 3] == 4 or row0[played_column_loop] + row1[played_column_loop + 1] + row2[played_column_loop + 2] + row3[played_column_loop + 3] == 8:
            winner = True
            return winner 
        if row1[played_column_loop] + row2[played_column_loop + 1] + row3[played_column_loop + 2] + row4[played_column_loop + 3] == 4 or row1[played_column_loop] + row2[played_column_loop + 1] + row3[played_column_loop + 2] + row4[played_column_loop + 3] == 8:
            winner = True
            return winner 
        if row2[played_column_loop] + row3[played_column_loop + 1] + row4[played_column_loop + 2] + row5[played_column_loop + 3] == 4 or row2[played_column_loop] + row3[played_column_loop + 1] + row4[played_column_loop + 2] + row5[played_column_loop + 3] == 8:
            winner = True
            return winner 

# Diagonal Left
    for played_column_loop in range(6,2,-1):
        if row0[played_column_loop] + row1[played_column_loop - 1] + row2[played_column_loop - 2] + row3[played_column_loop - 3] == 4 or row0[played_column_loop] + row1[played_column_loop - 1] + row2[played_column_loop - 2] + row3[played_column_loop - 3] == 8:
            winner = True
            return winner 
        if row1[played_column_loop] + row2[played_column_loop - 1] + row3[played_column_loop - 2] + row4[played_column_loop - 3] == 4 or row1[played_column_loop] + row2[played_column_loop - 1] + row3[played_column_loop - 2] + row4[played_column_loop - 3] == 8:
            winner = True
            return winner 
        if row2[played_column_loop] + row3[played_column_loop - 1] + row4[played_column_loop - 2] + row5[played_column_loop - 3] == 4 or row2[played_column_loop] + row3[played_column_loop - 1] + row4[played_column_loop - 2] + row5[played_column_loop - 3] == 8:
            winner = True
            return winner 

def state_winner(player):
    color = RED
    if player == 2:
        color = BLACK
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(f'Congratulations Player {player}, you are a Winner!!', False, color)
    text1 = font.render(f"Restart game, press the 'esc' key", False, color)
    textRect = text.get_rect()
    textRect1 = text1.get_rect()
    textRect.center = ((SCREEN_WIDTH)/2, SCREEN_HEIGHT - 435)
    textRect1.center = ((SCREEN_WIDTH)/2, SCREEN_HEIGHT -415)
    pygame.display.set_caption("Winner's circle")
    surface.blit(text, textRect)
    surface.blit(text1, textRect1)
    pygame.display.update(textRect)
    pygame.display.update(textRect1)
    pygame.event.clear()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return
  
def change_player(player):
    if player == 1:
        player = 2
    else:
        player = 1
    return player
while running:
    grid()
    small_token(player)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                reset_game = True

            elif event.key == pygame.K_KP1:
                column_counter0 += 1
                if column_counter0 > max_row:
                    break
                played_column = 0
                player = player_turn(0,25, player)
                winner = check_for_winning_move(played_column, winner)
                if winner == True:
                    state_winner(player)
                    reset_game = True
                player = change_player(player)

            elif event.key == pygame.K_KP2:
                column_counter1 += 1
                if column_counter1 > max_row:
                    break
                played_column = 1
                player = player_turn(1,75, player)
                winner = check_for_winning_move(played_column, winner)
                if winner == True:
                    state_winner(player)
                    reset_game = True                
                player = change_player(player)

            elif event.key == pygame.K_KP3:
                column_counter2 += 1
                if column_counter2 > max_row:
                    break
                played_column = 2
                player = player_turn(2,125, player)
                winner = check_for_winning_move(played_column, winner)
                if winner == True:
                    state_winner(player)
                    reset_game = True
                player = change_player(player)

            elif event.key == pygame.K_KP4:
                column_counter3 += 1
                if column_counter3 > max_row:
                    break
                played_column = 3
                player = player_turn(3,175, player)
                winner = check_for_winning_move(played_column, winner)
                if winner == True:
                    state_winner(player)
                    reset_game = True
                player = change_player(player)
        
            elif event.key == pygame.K_KP5:
                column_counter4 += 1
                if column_counter4 > max_row:
                    break
                played_column = 4
                player = player_turn(4,225, player) 
                winner = check_for_winning_move(played_column, winner)
                if winner == True:
                    state_winner(player)
                    reset_game = True
                player = change_player(player)
        
            elif event.key == pygame.K_KP6:
                column_counter5 += 1
                if column_counter5 > max_row:
                    break
                played_column = 5
                player = player_turn(5,275, player)
                winner = check_for_winning_move(played_column, winner)
                if winner == True:
                    state_winner(player)
                    reset_game = True
                player = change_player(player)

            elif event.key == pygame.K_KP7:
                column_counter6 += 1
                if column_counter6 > max_row:
                    break
                played_column = 6
                player = player_turn(6,325, player)
                winner = check_for_winning_move(played_column, winner)
                if winner == True:
                    state_winner(player)
                    reset_game = True
                player = change_player(player)
    if reset_game == True:
        winner = False
        player = 1
        played_column = 0
        column_counter0 = 0
        column_counter1 = 0
        column_counter2 = 0
        column_counter3 = 0
        column_counter4 = 0
        column_counter5 = 0
        column_counter6 = 0
        row5 = [9,9,9,9,9,9,9]
        row4 = [9,9,9,9,9,9,9]
        row3 = [9,9,9,9,9,9,9]
        row2 = [9,9,9,9,9,9,9]
        row1 = [9,9,9,9,9,9,9]
        row0 = [9,9,9,9,9,9,9]
        surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Bryan's Connect Four")
        surface.fill(WHITE)
        pygame.display.flip()
        player = 1
        reset_game = False