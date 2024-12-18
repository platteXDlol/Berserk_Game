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
player = pygame.Rect((100, screen_height * 0.862, screen_height * 0.0465, screen_height * 0.0465))  # player position and size
player_position = player
player_speed = 5  # player speed











# Game loop --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
GameRun = True
while GameRun:


    # Draw window
    Draw_Window(DISPLAYSURF, bg_position['x'], bg_position['y'], Main_Bg)

    # Draw player
    Draw_Player(player, DISPLAYSURF)




#player input
    # Player move
    key = pygame.key.get_pressed()
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        bg_position = Player_Move_Left(player, player_speed, player_position, bg_position, key)

    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        bg_position = Player_Move_Right(player, player_speed, player_position, bg_position, key)



    # player collision
    if player.colliderect(200, 875, 50, 100):
        print('collision')




















    # Quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GameRun = False

    pygame.display.update()
    clock.tick(60)  # Wait until next frame (at 60 FPS)

pygame.quit()
