import pygame, os, sys
from Window import *




#player draw
def Draw_Player(player, DISPLAYSURF):
    pygame.draw.rect(DISPLAYSURF, (255, 0, 0), player) #draw player



#player movement
#player movement
def Player_Move_Left(player, player_speed, player_Postion, bg_position, key): #player move left
    player.x -= player_speed
    if player_Postion.x < 500:  # player position start Bg move
        player.x = 500  # player stop move
        bg_position['x'] += player_speed  # update background X position
    return bg_position

def Player_Move_Right(player, player_speed, player_Postion, bg_position, key): #player move right
    player.x += player_speed
    if player_Postion.x > 500:  # player position start Bg move
        player.x = 500  # player stop move
        bg_position['x'] -= player_speed  # update background X position
    return bg_position


