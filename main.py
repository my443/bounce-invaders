# Simple pygame program
# https://realpython.com/pygame-a-primer/

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Import and initialize the pygame library
import pygame
from update_ball import *
from operator import mul
import time
from pygame import Rect


# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH    = 800
SCREEN_HEIGHT   = 600
PADDLE_WIDTH    = 100
pygame.init()
# Set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT ))

## Set the repeat level for they keyboard input.
pygame.key.set_repeat(1, 0)

## Start the paddle in the middle of the screen.
paddle_left = (SCREEN_WIDTH / 2) - (PADDLE_WIDTH / 2)
paddle_top  = 500

## Set up the ball
## TODO - Start the ball in a random place, or in a random **direction** every time.
ball_x_y = (250, 250)

## DONE - Set a gamespeed. So that the ball will go slower and faster, but the paddle speed doesn't change at all.
## Gamespeed is a number between 1 and 10.
## 1    - is the fastest speed
## 10   - is the slowest speed.
gamespeed = 5

## Ball movement is determined by the x, y movement.
## Numbers in this tuple can be positive or negative integers of any size.
ball_direction = (1, 1)

# Run until the user asks to quit
running = True
runloop = 0

# r = Rect(55, 55, 55, 25)
# enemies = [Rect(55 + (i * 150), 55, 55, 25) for i in range(5)]
enemies = []
for j in range(5):
    for i in range(5):
        enemies.append(Rect(55 + (i * 150), 55+(j*50), 55, 25))


while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_RIGHT:
                if paddle_left <= (SCREEN_WIDTH - PADDLE_WIDTH):
                    paddle_left = paddle_left + 1
            if event.key == K_LEFT:
                if paddle_left >= 0:
                    paddle_left = paddle_left - 1
        elif event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    ball = pygame.draw.circle(screen, (242, 91, 80), ball_x_y, 10)

    paddle = pygame.draw.rect(screen, (0, 0, 255), (paddle_left, paddle_top, PADDLE_WIDTH, 25))

    for item in enemies:
        pygame.draw.rect(screen, (255,0,0) , item)

    # if runloop == 0:
    #     enemies = [pygame.draw.rect(screen, (255, 0, 0), (55+(i*150), 55, 55, 25)) for i in range(5)]
    #     runloop = 1
    # else:
    #     enemies = enemies

    if ball.collidelist(enemies) != -1:
        index_of_hit_enemy = ball.collidelist(enemies)
        print (index_of_hit_enemy)
        del enemies[index_of_hit_enemy]
        ball_direction = tuple(map(mul, ball_direction, (1, -1)))
        update_ball = update_ball_info(ball_x_y, ball_direction, SCREEN_WIDTH, SCREEN_HEIGHT)
        ball = pygame.draw.circle(screen, (242, 91, 80), ball_x_y, 10)

        # If you finish the level, the game ends.
        if len(enemies) == 0:
            running = False

    # Flip the display
    pygame.display.flip()

    update_ball = update_ball_info(ball_x_y, ball_direction, SCREEN_WIDTH, SCREEN_HEIGHT)

    ## Set the x and y and the ball direction at each iteration
    ball_x_y = update_ball[0]
    ball_direction = update_ball[1]

    if ball.colliderect(paddle):
        if ball_direction[1] == 1 and ball_x_y[1] == 500:
            ball_direction = tuple(map(mul, ball_direction, (1, -1)))           ## Change the Y direction only.
            ball_x_y = (ball_x_y[0], 498)                                       ## Put the ball back above the paddle
        elif ball_direction[1] == -1 and ball_x_y[1] == 525:
            ball_direction = tuple(map(mul, ball_direction, (1, -1)))
            ball_x_y = (ball_x_y[0], 526)                                       ## Put the ball below the paddle

        update_ball = update_ball_info(ball_x_y, ball_direction, SCREEN_WIDTH, SCREEN_HEIGHT)
        ball = pygame.draw.circle(screen, (242, 91, 80), ball_x_y, 10)
        # running = False

    time.sleep(gamespeed * 0.0005)


# Done! Time to quit.
pygame.quit()

