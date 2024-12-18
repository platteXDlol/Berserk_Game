import pygame, os, sys
from Window import *




#player draw
def Draw_Player(player, DISPLAYSURF):
    pygame.draw.rect(DISPLAYSURF, (255, 0, 0), player) #draw player



#player move
def Player_Move_Right(player, player_speed, player_Postion, bg_position, key): #player move right
    player.x += player_speed
    if player_Postion.x > 500:  # player position start Bg move
        player.x = 500  # player stop move
        bg_position['x'] -= player_speed  # background move
    return bg_position # return background position


def Player_Move_Left(player, player_speed, player_Postion, bg_position, key): #player move left
    player.x -= player_speed
    if bg_position['x'] < 0: # if Bg position is less than 0 (player is far right) -->  if greater than 0 player can move left
        player.x = 500  # player dont move
        bg_position['x'] += player_speed # background move
    if player_Postion.x < 5: # player dont move out screen
        player.x = 5
    return bg_position # return background position




# player wall collision
def Player_Wall_Collision(player, ground_posY, player_height):
    if player.colliderect(0, ground_posY, 1980, 200):
        print('collision')
        player.y = ground_posY - player_height



