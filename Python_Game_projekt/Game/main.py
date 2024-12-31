import pygame, os, sys
from Window import *
from Player import *
from Level import *
from Retry_Lose_Screen import *
from End_Screen import *

pygame.init()


os.environ['SDL_VIDEO_CENTERED'] = '1' # Center the window
info = pygame.display.Info() # Get screen info
screen_width, screen_height = info.current_w, info.current_h # set screen width and height

# Background position
# Platform position
bg_pf_position = {'x': 0, 'y': 0, 'platform_position_X': 0, 'triangle_position_X' : 0, 'end_rect_position_X' : 0}  # Background and Platform position dictionary

# Window setup
DISPLAYSURF = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # fullscreen
Main_Bg_Path = os.path.join("Python_Game_projekt", "Images", "Backgrounds", "MainBackground.png")  # Background Img
Main_Bg = pygame.image.load(Main_Bg_Path)  # Background load
Main_Bg = pygame.transform.scale(Main_Bg, (screen_width, screen_height)) # Background scale fullscreen

# Level End setup
End_Bg_Path = os.path.join("Python_Game_projekt", "Images", "Backgrounds", "MainBackground_End.png")  # End Background Img
End_Bg = pygame.image.load(End_Bg_Path)  # End Background load
End_Bg = pygame.transform.scale(End_Bg, (screen_width, screen_height)) # End Background scale fullscreen

level_length = Main_Bg.get_width() * 14  # Level length


# Player setup
player_live = 1 # player live
player_posY = screen_height# player position Y
scaling_factor = 2.5  # Increase player size by 50%
player_width = int(screen_height * 0.0463 * scaling_factor)  # Player width
player_height = int(screen_height * 0.0463 * scaling_factor)  # Player height


# Player image
player_image = pygame.image.load(os.path.join("Python_Game_projekt", "Images", "Charakters", "Guts.png"))  # player Img
player_image = pygame.transform.scale(player_image, (int(player_width), int(player_height))) # player scale

player_rect = player_image.get_rect(topleft=(100, player_posY))  # player position
player_mask = pygame.mask.from_surface(player_image)  # player mask
mask_image = player_mask.to_surface()  # mask image

player_position = player_rect  # player position
player_speed = 5  # player speed
dash_speed = 15
player_jump_count = 0 # player jump count


player_gravity = 0   # player gravity
increase_gravity = screen_height / 1080 * 0.4  # increase gravity
jumpheight = screen_height / 1080 * -12.65 # jump height



# Ground setup
ground_posY = screen_height * 0.9583 # ground position Y
ground_height = player_posY + player_height # ground height

# Platform setup
platform = []
triangles = []

# Spickes
Spickes_path = os.path.join("Python_Game_projekt", "Images", "World", "Spike2.png")  # Spickes Img
Spickes_img = pygame.image.load(Spickes_path)  # Spickes load
Spickes_img = pygame.transform.scale(Spickes_img, (screen_width * (50 / 1920), screen_height *(50 / 1080))) # Spickes scale






# Clock and Start Timer

clock = pygame.time.Clock() # clock for timer and fps
start_time = pygame.time.get_ticks() # start time





# Game loop --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
GameRun = True
while GameRun:

    # Calculate elapsed time
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # seconds

    # Draw ground
    Draw_Ground(DISPLAYSURF, ground_posY, ground_height)

    # Draw window
    Draw_Window(DISPLAYSURF, bg_pf_position['x'], bg_pf_position['y'], Main_Bg, End_Bg)

    # Draw player
    Draw_Player(player_rect, player_image, DISPLAYSURF, player_mask, mask_image)





    #Player wall collision
    player_gravity += increase_gravity  # Gravity
    player_gravity, player_jump_count = Player_Gravity(player_gravity, player_rect, ground_posY, player_height, player_jump_count)


    #player platform collision
    platforms = Draw_Platforms(DISPLAYSURF, screen_height, screen_width, bg_pf_position['platform_position_X'])
    player_gravity, player_jump_count = Player_Platform_Collision(player_rect, player_height, platforms, player_gravity, player_jump_count)

    #player triangle collision
    triangle_mask_positions = Draw_Triangle(DISPLAYSURF, ground_posY, screen_width, screen_height, bg_pf_position['triangle_position_X'], Spickes_img)
    player_live = check_triangle_collision(player_rect, player_mask, player_live, triangle_mask_positions, player_width)



    #player dead
    if player_live == 0:
        Retry(DISPLAYSURF, Main_Bg, screen_width, screen_height, clock)
        player_live = 1
        player_rect = player_image.get_rect(topleft=(100, player_posY))
        player_position = player_rect
        player_gravity = 0
        player_jump_count = 0
        bg_pf_position = {'x': 0, 'y': 0, 'platform_position_X': 0, 'triangle_position_X': 0, 'end_rect_position_X': 0}
        start_time = pygame.time.get_ticks()  # Reset start time






    # Draw End Block
    end_rect_position = End_Block_Draw(DISPLAYSURF, screen_width, screen_height, level_length, bg_pf_position['end_rect_position_X'])
    if player_rect.colliderect(end_rect_position): # Check if player collides with the end block
        End_Screen(DISPLAYSURF, screen_width, screen_height, clock, elapsed_time)  # Display the end screen
        player_live = 1
        player_rect = player_image.get_rect(topleft=(100, player_posY))
        player_position = player_rect
        player_gravity = 0
        player_jump_count = 0
        bg_pf_position = {'x': 0, 'y': 0, 'platform_position_X': 0, 'triangle_position_X': 0, 'end_rect_position_X': 0}
        start_time = pygame.time.get_ticks()  # Reset start time




    #player input
    # Player move
    key = pygame.key.get_pressed()


    if key[pygame.K_a] or key[pygame.K_LEFT]:
        if player_position.x > screen_width / 100 * 50:
            player_speed = 5 # end of game
        bg_pf_position = Player_Move_Left(player_rect, player_speed, player_position, bg_pf_position, level_length)
        if key[pygame.K_LSHIFT]:  # Sprint
            player_speed = 50
        else:
            player_speed = 5

      
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        if player_position.x > screen_width / 100 * 50: # end of game
            player_speed = 5
        bg_pf_position = Player_Move_Right(player_rect, player_speed, player_position, bg_pf_position, level_length, screen_width, player_width)
        if key[pygame.K_LSHIFT]:  # Sprint
            player_speed = 50
        else:
            player_speed = 5


    if key[pygame.K_SPACE]:      #or key[pygame.K_UP]:
        if player_position.x > screen_width / 100 * 50: # end of game
            player_jump_count = 1
        if player_jump_count == 0:  # If player is on the ground
            player_gravity = jumpheight  # Jump height
            player_jump_count = 1  # Increase jump count























# JUST FOR TESTING ------------------------------------------------------------------------------------------------------------------------------
    if key[pygame.K_s] or key[pygame.K_UP]:
        player_rect.y -= 100



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
