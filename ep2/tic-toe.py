# coding: utf-8

# In[1]:

import pygame
from pygame.locals import *

# Constants

SIZE = WIDTH, HEIGHT = 440, 300
print(SIZE)
CELL_SIZE = CELL_WIDTH, CELL_HEIGHT = WIDTH // 3, HEIGHT // 3
COLOR = (255, 255, 255)  # white line


def draw_line(screen):
    # (object, color_code, start point, end point, thickness of line)
    for i in range(1, 3):  # draw 2 row lines
        pygame.draw.line(screen, COLOR, (0, CELL_HEIGHT * i), (WIDTH, CELL_HEIGHT * i), (1))
    for i in range(1, 3):  # draw 2 column lines
        pygame.draw.line(screen, COLOR, (CELL_WIDTH * i, 0), (CELL_WIDTH * i, HEIGHT), (1))
    pygame.display.update()

    return screen


def getInput(map, type):
    while True:

        pos = ()

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                break

        if pos == ():  # If got nothing, get the input again

            continue

        now_width, now_height = pos

        x, y = now_width // CELL_WIDTH, now_height // CELL_HEIGHT

        # for x=3 or y=3 where the end of the screen

        if x > 2:
            x -= 1

        if y > 2:
            y -= 1

        if map[x][y] != " ":

            continue

        else:

            map[x][y] = type

            return map


def printMap(map, screen):
    for i in range(3):
        for j in range(3):
            if map[i][j] == " ":
                continue
            elif map[i][j] == 'X':
                # Need 2 lines that cross each other for drawing 'X'
                # left diagonal line
                start = (CELL_WIDTH * i + CELL_WIDTH // 4, CELL_HEIGHT * j + CELL_HEIGHT // 4)
                end = (CELL_WIDTH * (i + 1) - CELL_WIDTH // 4, CELL_HEIGHT * (j + 1) - CELL_HEIGHT // 4)
                pygame.draw.line(screen, COLOR, start, end)
                # right diagonal line
                start = (CELL_WIDTH * (i + 1) - CELL_WIDTH // 4, CELL_HEIGHT * j + CELL_HEIGHT // 4)
                end = (CELL_WIDTH * i + CELL_WIDTH // 4, CELL_HEIGHT * (j + 1) - CELL_HEIGHT // 4)
                pygame.draw.line(screen, COLOR, start, end)
            elif map[i][j] == 'O':
                center = (CELL_WIDTH * i + CELL_WIDTH // 2, CELL_HEIGHT * j + CELL_HEIGHT // 2)
                radius = CELL_HEIGHT // 3
                thickness = 1
                pygame.draw.circle(screen, COLOR, center, radius, thickness)
    pygame.display.update()

def isFull(map):
    for i in range(3):
        for j in range(3):
            if map[i][j] == " ":
                return False
    # If there is no " ", the map is full
    return True


def isEnd(map, type, screen):
    myfont = pygame.font.SysFont(None, 48)  # None will load System default font
    end_message = ""
    # Check rows and columns
    for i in range(3):
        if map[i][0] == map[i][1] == map[i][2] == type or map[0][i] == map[1][i] == map[2][i] == type:
            end_message = "Player " + type + " WINS!"
            end_text = myfont.render(end_message, True, COLOR)
            text_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(end_text, text_rect)
            return True
# Check left diagonal line
    if map[0][0] == map[1][1] == map[2][2] == type:
        end_message = "Player " + type + " WINS!"
        end_text = myfont.render(end_message, True, COLOR)
        text_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(end_text, text_rect)
        return True
# Check right diagonal line
    if map[0][2] == map[1][1] == map[2][0] == type:
        end_message = "Player " + type + " WINS!"
        end_text = myfont.render(end_message, True, COLOR)
        text_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(end_text, text_rect)
        return True
# If the map is full but no one wins, draw
    if isFull(map) == True:
        end_message = "DRAW!"
        end_text = myfont.render(end_message, True, COLOR)
        text_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(end_text, text_rect)
        return True
    return False


def wait():
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                pygame.quit()



def setup():
    #os.putenv('SDL_FBDEV', '/dev/fb1')  # Set on the touch screen
    pygame.init()  # Initialize pygame
    screen = pygame.display.set_mode(SIZE)  # Set screen with size
    return screen

def start_game():
    # Initialize map by 3x3 matrix with a blank(" ")
    map = []
    for i in range(3):
        map.append([" ", " ", " "])
    screen = setup()  # Set up the screen
    screen = draw_line(screen)  # Draw 4 dividing lines.
    # Play the game until the game is ended
    while isEnd(map, 'X', screen) == False:
        map = getInput(map, 'O')  # Player O starts first
        printMap(map, screen)
        if isEnd(map, 'O', screen):
            break
        map = getInput(map, 'X')
        printMap(map, screen)
    pygame.display.update()
    wait()  # Wait for touch and close this program
# If this program is not imported by other program, start the game automatically

if __name__ == '__main__':
    start_game()