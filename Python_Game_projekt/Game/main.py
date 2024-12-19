import pygame, os, sys
from Window import *
from Player import *

pygame.init()

# clock for timer and fps
clock = pygame.time.Clock()

os.environ['SDL_VIDEO_CENTERED'] = '1' # Center the window
info = pygame.display.Info() # Get screen info
screen_width, screen_height = info.current_w, info.current_h # set screen width and height

# Background position
bg_position = {'x': 0, 'y': 0}  # Background position dictionary

# Window setup
DISPLAYSURF = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # fullscreen
Main_Bg_Path = os.path.join("Python_Game_projekt", "Images", "Backgrounds", "Main_Bg.jpg")  # Background Img
Main_Bg = pygame.image.load(Main_Bg_Path)  # Background load
Main_Bg = pygame.transform.scale(Main_Bg, (screen_width, screen_height)) # Background scale fullscreen





# Player setup
player_posY = screen_height * 0.862 - 500 # player position Y
player_width = screen_height * 0.0463 # player width
player_height = screen_height * 0.0463 # player height


player = pygame.Rect((100, player_posY, player_height, player_width))  # player position and size
player_position = player
player_speed = 5  # player speed
player_jump_count = 0 # player jump count


player_gravity = 0   # player gravity
increase_gravity = 0.25  # increase gravity
jumpheight = -10 # jump height


# Ground setup
ground_posY = screen_height * 0.862 + 55 # ground position Y
ground_height = player_posY + player_height # ground height











# Game loop --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
GameRun = True
while GameRun:


    # Draw ground
    Draw_Ground(DISPLAYSURF, ground_posY, ground_height)

    # Draw window
    Draw_Window(DISPLAYSURF, bg_position['x'], bg_position['y'], Main_Bg)

    # Draw player
    Draw_Player(player, DISPLAYSURF)




    #Player wall collision
    player_gravity += increase_gravity  # Gravity
    player_jump_count = Player_Wall_Collision(player, ground_posY, player_height, player_jump_count)
    player_gravity, player_jump_count = Player_Gravity(player_gravity, player, ground_posY, player_height, player_jump_count)



    Draw_Level(DISPLAYSURF)

















    #player input
    # Player move
    key = pygame.key.get_pressed()

    if key[pygame.K_a] or key[pygame.K_LEFT]:
        bg_position = Player_Move_Left(player, player_speed, player_position, bg_position, key)

    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        bg_position = Player_Move_Right(player, player_speed, player_position, bg_position, key)

    if key[pygame.K_SPACE] or key[pygame.K_UP]:
        if player_jump_count == 0:
            player_gravity = jumpheight  # Jump height
            player_jump_count = 1  # Increase jump count
        print(f"Player Y: {player.y}, Gravity: {player_gravity}")














    # JUST FOR TESTING ------------------------------------------------------------------------------------------------------------------------------
    if key[pygame.K_s] or key[pygame.K_DOWN]:
        player.y += player_speed

# JUST FOR TESTING ------------------------------------------------------------------------------------------------------------------------------


























    # Quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If the close button is pressed
            GameRun = False # Stop the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # If the escape key is pressed
                GameRun = False # Stop the game



    pygame.display.update() # Update the display
    clock.tick(60)  # Wait until next frame (at 60 FPS)

pygame.quit() # Quit the game
