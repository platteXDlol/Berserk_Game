import pygame, os, sys
from Window import *
from Player import *

pygame.init()

# Window position
bg_position = {'x': 0, 'y': 0}  # Using a dictionary for background position

# Window setup
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # fullscreen
Main_Bg_Path = os.path.join("..", "Images", "Backgrounds", "Main_Bg.jpg")  # Background Img
Main_Bg = pygame.image.load(Main_Bg_Path)  # Background load

# clock for timer and fps
clock = pygame.time.Clock()

# Player setup
player = pygame.Rect((100, 800, 50, 50))  # player position and size
player_position = player
player_speed = 5  # player speed

# Game loop
GameRun = True
while GameRun:
    # Draw window
    Draw_Window(DISPLAYSURF, bg_position['x'], bg_position['y'], Main_Bg)

    # Draw player
    Draw_Player(player, DISPLAYSURF)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        bg_position = Player_Move_Left(player, player_speed, player_position, bg_position, key)

    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        bg_position = Player_Move_Right(player, player_speed, player_position, bg_position, key)

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
