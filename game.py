import pygame
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('juego')

#load background
bg_img = pygame.image.load('img/background.png')
bg_img = pygame.transform.scale(bg_img, (800, 600))

#player
player_img = pygame.image.load('img/player.png')
player_x = 400
player_y = 400
player_x_change = 0
player_y_change = 0


def player(x, y):
    screen.blit(player_img, (x, y))

run = True
while run:

    screen.blit(bg_img, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #key pressing
        if event.type == pygame.KEYDOWN:
            #any key pressed
            if event.key == pygame.K_LEFT:
                # certain key pressed
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                # certain key pressed
                player_x_change = 0.3
            if event.key == pygame.K_UP:
                # certain key pressed
                player_y_change = -0.3
            if event.key == pygame.K_DOWN:
                # certain key pressed
                player_y_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # certain key released
                player_x_change = -0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                # certain key released
                player_y_change = 0
            

    player_x += player_x_change
    player_y += player_y_change
    player(player_x, player_y)
    pygame.display.update()

pygame.quit()