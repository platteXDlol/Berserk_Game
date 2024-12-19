import pygame, os, sys

from Window import *




#player draw
def Draw_Player(player, DISPLAYSURF):
    pygame.draw.rect(DISPLAYSURF, (255, 0, 0), player) #draw player



#player move
def Player_Move_Right(player, player_speed, player_Postion, bg_position, platform_position_X): #player move right
    player.x += player_speed
    if player_Postion.x > 500:  # player position start Bg move
        player.x = 500  # player stop move
        bg_position['x'] -= player_speed  # background move
        platform_position_X -= player_speed  # platform move
    return bg_position # return background position
    return platform_position_X # return platform position


def Player_Move_Left(player, player_speed, player_Postion, bg_position, platform_position_X): #player move left
    player.x -= player_speed
    if bg_position['x'] < 0: # if Bg position is less than 0 (player is far right) -->  if greater than 0 player can move left
        player.x = 500  # player dont move
        bg_position['x'] += player_speed # background move
        platform_position_X -= player_speed  # platform move
    if player_Postion.x < 5: # player dont move out screen
        player.x = 5
    return bg_position # return background position
    return platform_position_X # return platform position




# player wall collision
def Player_Wall_Collision(player, ground_posY, player_height, player_jump_count):
    if player.y >= ground_posY - player_height:
        player.y = ground_posY - player_height
        player_jump_count = 0  # Reset jump count when player hits the ground
    return player_jump_count







# player gravity
def Player_Gravity(player_gravity, player, ground_posY, player_height, player_jump_count):
    player.y += player_gravity
    if player.y >= ground_posY - player_height:  # Collision with ground
        player.y = ground_posY - player_height  # Teleport to ground
        player_gravity = 0  # Gravity stops when on the ground
        player_jump_count = 0  # Reset jump count when on the ground
    return player_gravity, player_jump_count  # Return both gravity and jump count






