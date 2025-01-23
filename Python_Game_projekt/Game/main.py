import pygame, os, sys

from Griffith import *
from Window import *
from Player import *
from Level import *
from Retry_Lose_Screen import *
from End_Screen import *

pygame.init()


os.environ['SDL_VIDEO_CENTERED'] = '1' # Center the window
info = pygame.display.Info() # Get screen info
screen_width, screen_height = info.current_w, info.current_h # set screen width and height




#--------------------------------------------------------------------
# Determine if the game is running from a bundled executable
if getattr(sys, 'frozen', False):
    # The app is running as a bundled executable
    base_path = sys._MEIPASS
else:
    # The app is running in a normal Python environment
    #base_path = os.path.abspath("Berserk_Game.\Python_Game_projekt")
    base_path = os.path.abspath("..")
#--------------------------------------------------------------------




# Background position
# Platform position
bg_pf_position = {'x': 0, 'y': 0, 'platform_position_X': 0, 'triangle_position_X' : 0, 'end_rect_position_X' : 0, 'griffith_position_X' : 0}  # Background and Platform position dictionary

# Window setup
DISPLAYSURF = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # fullscreen
Main_Bg_Path = os.path.join(base_path, "Images", "Backgrounds", "MainBackground.png")  # Background Img
Main_Bg = pygame.image.load(Main_Bg_Path)  # Background load
Main_Bg = pygame.transform.scale(Main_Bg, (screen_width, screen_height)) # Background scale fullscreen

# Level End setup
End_Bg_Path = os.path.join(base_path, "Images", "Backgrounds", "MainBackground_End.png")  # End Background Img
End_Bg = pygame.image.load(End_Bg_Path)  # End Background load
End_Bg = pygame.transform.scale(End_Bg, (screen_width, screen_height)) # End Background scale fullscreen

level_length = Main_Bg.get_width() * 15  # Level length


# Player setup
player_live = 1 # player live
player_posY = screen_height# player position Y
scaling_factor = 2.5  # Increase player size by 50%
player_width = int(screen_height * 0.0463 * scaling_factor)  # Player width
player_height = int(screen_height * 0.0463 * scaling_factor)  # Player height


# Player image
player_image_path = os.path.join(base_path, "Images", "Charakters", "Guts.png")  # player Img
player_image = pygame.image.load(player_image_path)  # player Img
player_image = pygame.transform.scale(player_image, (int(player_width), int(player_height)))  # player scale

player_rect = player_image.get_rect(topleft=(100, player_posY))  # player position
player_mask = pygame.mask.from_surface(player_image)  # player mask
mask_image = player_mask.to_surface()  # mask image

player_position = player_rect  # player position
player_speed = (screen_width / 100 * 0,63)  # player speed
player_jump_count = 0 # player jump count


player_gravity = 0   # player gravity
increase_gravity = screen_height / screen_height * 0.4  # increase gravity
jumpheight = screen_height / screen_height * -12.65 # jump height



# Ground setup
ground_posY = screen_height * 0.9583 # ground position Y
ground_height = player_posY + player_height # ground height

# Platform setup
platform = []
triangles = []

# Spickes
Spickes_path = os.path.join(base_path, "Images", "World", "Spike2.png")  # Spickes Img
Spickes_img = pygame.image.load(Spickes_path)  # Spickes load
Spickes_img = pygame.transform.scale(Spickes_img, (screen_width * (50 / 1920), screen_height * (50 / 1080)))  # Spickes scale



coyote_timer = 0
coyote_time_limit = 5  # Adjust based on desired forgiveness (e.g., 5 frames)




# GRIFFITH!!!!!!!!!!------------------------------------------------------------------------------------------------------------------------------------------------------------------

griffith_image_path = os.path.join(base_path, "Images", "Charakters", "Griffith.png")  # griffith Img
griffith_image = pygame.image.load(griffith_image_path)  # griffith Img
griffith_image = pygame.transform.scale(griffith_image, (int(player_width), int(player_height)))  # griffith scale


griffith_posY =   ground_posY - player_height
bg_pf_position['griffith_position_X'] = level_length - screen_width + (screen_width / 100 * 51)  # griffith position X
griffith_posX = bg_pf_position['griffith_position_X']
griffith_width = griffith_image.get_width()  # griffith width

griffith_rect = griffith_image.get_rect(topleft=(griffith_posX, griffith_posY))  # griffith position
griffith_mask = pygame.mask.from_surface(griffith_image)  # griffith mask
griffith_mask_image = griffith_mask.to_surface()  # griffith mask image


# Griffith movement parameters
griffith_speed = 2  # Adjust speed as needed
griffith_direction = 1  # 1 for right, -1 for left
griffith_move_range = 200  # Range of movement

# Store Griffith's original position to calculate movement range
Griffith_live = True
griffith_initialized = False  # Track if starting position has been set
griffith_active = False  # Initially inactive
griffith_start_bg_position_X = bg_pf_position['griffith_position_X']  # Placeholder for initialization



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




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

    bg_pf_position, griffith_direction, griffith_active, griffith_start_bg_position_X, griffith_initialized = Update_Griffith(
        bg_pf_position, griffith_start_bg_position_X, griffith_speed, griffith_direction, griffith_move_range,
        griffith_active, screen_width, griffith_initialized, level_length
    )

    if check_kill_with_feet(player_rect, player_mask, bg_pf_position, griffith_mask, griffith_rect):
        Griffith_live = False

    Draw_Griffith(DISPLAYSURF, griffith_image, bg_pf_position, griffith_posY, Griffith_live)

    if check_griffith_collision(player_rect, player_mask, bg_pf_position, griffith_mask, griffith_posY, Griffith_live):
        player_live = 0







    # player triangle collision
    spike_positions = Draw_Spikes(DISPLAYSURF, ground_posY, screen_width, screen_height, bg_pf_position['triangle_position_X'], Spickes_img)
    # Check if player collides with any spike
    if check_spike_collision(player_rect, player_mask, spike_positions):
        player_live = 0  # Handle player death or reset



    #Player wall collision
    player_gravity += increase_gravity  # Gravity
    player_gravity, player_jump_count = Player_Gravity(player_gravity, player_rect, ground_posY, player_height, player_jump_count)



    #player platform collision
    platforms = Draw_Platforms(DISPLAYSURF, screen_height, screen_width, bg_pf_position['platform_position_X'])
    player_gravity, player_jump_count, coyote_timer = Player_Platform_Collisions(player_rect, player_mask, player_height, platforms, player_gravity, player_jump_count, coyote_timer, coyote_time_limit)






    #player dead
    if player_live == 0:
        Retry(DISPLAYSURF, screen_width, screen_height, clock)
        player_live = 1
        player_rect = player_image.get_rect(topleft=(100, player_posY))
        player_position = player_rect
        player_gravity = 0
        player_jump_count = 0
        bg_pf_position = {'x': 0, 'y': 0, 'platform_position_X': 0, 'triangle_position_X': 0, 'end_rect_position_X': 0, 'griffith_position_X': level_length - screen_width + (screen_width / 100 * 51)}
        Griffith_live = True






    # Draw End Block
    end_rect_position = End_Block_Draw(DISPLAYSURF, screen_width, screen_height, level_length, bg_pf_position['end_rect_position_X'])
    if player_rect.colliderect(end_rect_position): # Check if player collides with the end block
        End_Screen(DISPLAYSURF, screen_width, screen_height, clock, elapsed_time)  # Display the end screen
        player_live = 1
        player_rect = player_image.get_rect(topleft=(100, player_posY))
        player_position = player_rect
        player_gravity = 0
        player_jump_count = 0
        bg_pf_position = {'x': 0, 'y': 0, 'platform_position_X': 0, 'triangle_position_X': 0, 'end_rect_position_X': 0, 'griffith_position_X': level_length - screen_width + (screen_width / 100 * 51)}
        Griffith_live = True
        start_time = pygame.time.get_ticks()  # Reset start time




    #player input
    # Player move
    key = pygame.key.get_pressed()


    if key[pygame.K_a] or key[pygame.K_LEFT]:
        if player_position.x > screen_width / 100 * 50:
            player_speed = screen_width / 100 * 0.26 # end of game
        else:
            player_speed = screen_width / 100 * 0.63
        bg_pf_position = Player_Move_Left(player_rect, player_speed, player_position, bg_pf_position, level_length)



      
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        if player_position.x > screen_width / 100 * 50: # end of game
            player_speed = screen_width / 100 * 0.26
        else:
            player_speed = screen_width / 100 * 0.63
        bg_pf_position = Player_Move_Right(player_rect, player_speed, player_position, bg_pf_position, level_length, screen_width, player_width)




    if key[pygame.K_SPACE]:      #or key[pygame.K_UP]:
        if player_position.x > screen_width / 100 * 50: # end of game
            player_jump_count = 1
        if coyote_timer > 0 or player_jump_count == 0:  # On ground or within coyote time
            player_gravity = jumpheight  # Apply jump
            player_jump_count = 1  # Reset jump count
            coyote_timer = 0  # Disable coyote time once used




    if key[pygame.K_r]:
        player_rect = player_image.get_rect(topleft=(100, player_posY))
        player_position = player_rect
        player_gravity = 0
        player_jump_count = 0
        bg_pf_position = {'x': 0, 'y': 0, 'platform_position_X': 0, 'triangle_position_X': 0, 'end_rect_position_X': 0, 'griffith_position_X': level_length - screen_width + (screen_width / 100 * 51)}
        Griffith_live = True











































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
