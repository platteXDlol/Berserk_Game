import pygame
from Level import Platform_Draw




#Window Draw
def Draw_Window(DISPLAYSURF, Bg_Move_X, Bg_Move_Y, Main_Bg):
    DISPLAYSURF.fill((0, 0, 0))  # background color
    for x in range(0, 10):  # background repeat 10 times
        DISPLAYSURF.blit(Main_Bg, (Bg_Move_X + Main_Bg.get_width() * x, Bg_Move_Y))



# Ground Draw
def Draw_Ground(DisplaySurf, ground_posY, ground_height):
    pygame.draw.rect(DisplaySurf, (255, 255, 0), (0, ground_posY, 1980, 200))



# Level Draw
def Draw_Level(DISPLAYSURF):

    platform = [
        pygame.Rect(200, 500, 200, 20),
        pygame.Rect(500, 400, 200, 20),
        pygame.Rect(800, 300, 200, 20),
        pygame.Rect(1100, 200, 200, 20)
    ]

    for i in range(1, 4):
        Platform_Draw(DISPLAYSURF, platform[i])





