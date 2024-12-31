import pygame, os, sys


from Window import *




#player draw
def Draw_Player(player, player_image, DISPLAYSURF, player_mask, mask_image):
    DISPLAYSURF.blit(player_image, (player.x, player.y))  # Draw player



#player move
def Player_Move_Right(player, player_speed, player_Postion, bg_position, level_length, screen_width, player_width): #player move right
    player.x += player_speed
    if player_Postion.x > 500 and bg_position['x'] > -level_length:  # player position start Bg move
        player.x = 500  # player stop move
        bg_position['x'] -= player_speed  # background move
        bg_position['platform_position_X'] -= player_speed  # platform move
        bg_position['triangle_position_X'] -= player_speed  # triangle move
        bg_position['end_rect_position_X'] -= player_speed  # end block move
    if player_Postion.x > screen_width - player_width - 5:  # dont move out screen
        player.x = screen_width - player_width - 5
    return bg_position


def Player_Move_Left(player, player_speed, player_Postion, bg_position, level_length): #player move left
    player.x -= player_speed
    if bg_position['x'] < 0 and bg_position['x'] > -level_length or player.x < 500 and  bg_position['x'] <0: # if Bg position is less than 0 (player is far right) -->  if greater than 0 player can move left
        player.x = 500  # player dont move
        bg_position['x'] += player_speed # background move
        bg_position['platform_position_X'] += player_speed # platform move
        bg_position['triangle_position_X'] += player_speed # triangle move
        bg_position['end_rect_position_X'] += player_speed # end block move
    if player_Postion.x < 5: #dont move out screen
        player.x = 5
    return bg_position






# player wall collision
def Player_Wall_Collision(player, ground_posY, player_height, player_jump_count):
    if player.y >= ground_posY - player_height:
        player.y = ground_posY - player_height
        player_jump_count = 0  # Reset jump count when player hits the ground
    return player_jump_count


# player platform collision
def Player_Platform_Collision(player, player_height, platforms, player_gravity, player_jump_count):
    for i, plat in enumerate(platforms):
        if plat.colliderect(player): # If player collides with a platform
            if player_gravity > 0:  # only if falling
                player_jump_count = 0 # Reset jump count
                player_gravity = 0 # Reset Gravity
                player.y = plat.y - player_height # Teleport player to top of platform
    return player_gravity, player_jump_count # Return both gravity and jump count




# player triangle collision
#ChatGPT __________
def check_triangle_collision(player, player_mask, player_live, triangle_mask_positions, player_width):
    for triangle in triangle_mask_positions:
        triangle_mask = triangle['mask']  # Get the mask for the triangle
        triangle_pos = triangle['pos']   # Get the position of the triangle

        # Calculate the relative offset between the player and the triangle
        offset = (player.x + (player_width/2) - triangle_pos[0], player.y + (player_width/2) - triangle_pos[1])

        # Check if the player's mask overlaps with the triangle's mask
        if player_mask.overlap(triangle_mask, offset):
            player_live -= 1  # Decrease player's lives
            # Reset player position (modify based on your reset logic)
    return player_live


# player gravity
def Player_Gravity(player_gravity, player, ground_posY, player_height, player_jump_count):
    player.y += player_gravity
    if player.y >= ground_posY - player_height:  # Collision with ground
        player.y = ground_posY - player_height  # Teleport to ground
        player_gravity = 0  # Gravity stops when on the ground
        player_jump_count = 0  # Reset jump count when on the ground
    else:
        player_jump_count = 1  # Player is in the air
    return player_gravity, player_jump_count  # Return both gravity and jump count
