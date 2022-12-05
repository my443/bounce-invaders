# Simple pygame program
# https://realpython.com/pygame-a-primer/

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

## l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
## a = list(map(lambda x: [x[0], x[1] + 5, x[1]], l))
## a.assert.equals([[1, 7, 2], [4, 10, 5], [7, 13, 8]])

# Import and initialize the pygame library
import pygame
from update_ball import *
from operator import mul
import time
from pygame import Rect
from move_enemies import *


# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
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
## DONE - Start the ball in a random place, or in a random **direction** every time.
##      (Started it from the middle of the paddle, going up.)
ball_x_y = (SCREEN_WIDTH / 2, 499)

## DONE - Set a gamespeed. So that the ball will go slower and faster, but the paddle speed doesn't change at all.
## Gamespeed is a number between 1 and 10.
## 1    - is the fastest speed
## 10   - is the slowest speed.
gamespeed = 5

## Ball movement is determined by the x, y movement.
## Numbers in this tuple can be positive or negative integers of any size.
ball_direction = (1, -1)

## Each time the level increases, the speed can increase also by some factor.
level = 1
speed_increase_factor = .95

font = pygame.font.Font('freesansbold.ttf', 32)

# create a text surface object,
# on which text is drawn on it.
text = font.render('Level', True, (0,0,0))

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# Run until the user asks to quit
running = True
runloop = 0

# r = Rect(55, 55, 55, 25)
# enemies = [Rect(55 + (i * 150), 55, 55, 25) for i in range(5)]
def generate_enemies():

    enemies = []
    for j in range(5):
        for i in range(5):
            top = 55 + (i * 150)
            left = 25 + (j * 50)
            enemies.append(Rect(top, left, 55, 25))

    return enemies

enemies = generate_enemies()


# Add the enemies
generate_enemies()

current_enemy_position = 0
enemy_direction = 1
# b = move_enemies(enemies, current_enemy_position, 1)
# print (enemies)
# print (b)
counter = 0
score   = 0
lifes = 3
while running:
    counter += 1
    if counter % 10-level == 0:
        enemies = move_enemies(enemies, current_enemy_position, enemy_direction)

    # change the enemy direction if it hits the right side (6) or the left side (0)
    if current_enemy_position >= 250:
        enemies = move_enemies_down(enemies)
        enemy_direction = -1
        # running = False
    elif current_enemy_position <= 0:
        enemies = move_enemies_down(enemies)
        enemy_direction = 1

    current_enemy_position += enemy_direction
    # print (current_enemy_position, enemy_direction)

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
        # print (index_of_hit_enemy)
        del enemies[index_of_hit_enemy]
        ball_direction = tuple(map(mul, ball_direction, (1, -1)))
        update_ball = update_ball_info(ball_x_y, ball_direction, SCREEN_WIDTH, SCREEN_HEIGHT)
        ball = pygame.draw.circle(screen, (242, 91, 80), ball_x_y, 10)
        score += level + 1

        # If you finish the level
        if len(enemies) == 0:
            level += 1
            enemies = generate_enemies()
            # running = False

    # Flip the display after adding all of thet text
    level_text = font.render('Level:  '+str(level), True, (0, 0, 0))
    score_text = font.render('Score:  ' + str(score), True, (0, 0, 0))
    lifes_text = font.render('Life:  ' + str(lifes), True, (0, 0, 0))
    screen.blit(level_text, (0, 550))
    screen.blit(score_text, (550, 550))
    screen.blit(lifes_text, (300, 550))
    pygame.display.flip()

    update_ball = update_ball_info(ball_x_y, ball_direction, SCREEN_WIDTH, SCREEN_HEIGHT)

    ## Set the x and y and the ball direction at each iteration
    ball_x_y = update_ball[0]
    ball_direction = update_ball[1]

    # print (ball_x_y[1])
    if ball[1] >= 580:
        lifes += -1
        ball_x_y = (SCREEN_WIDTH / 2, 499)
        ball_direction = (1, -1)

    if lifes == 0:
        game_over_text = font.render('GAME OVER!!', True, (0, 0, 0))
        screen.blit(game_over_text, (300, 250))
        pygame.display.flip()
        time.sleep(5)
        running = False

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

