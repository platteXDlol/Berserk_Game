import pygame, os, sys




#Window Draw
def Draw_Window(DISPLAYSURF, Bg_Move_X, Bg_Move_Y, Main_Bg, End_Bg):
    DISPLAYSURF.fill((0, 0, 0))  # background color
    for x in range(0, 14):  # background repeat 15 times
        DISPLAYSURF.blit(Main_Bg, (Bg_Move_X + Main_Bg.get_width() * x, Bg_Move_Y))
    DISPLAYSURF.blit(End_Bg, (Bg_Move_X + Main_Bg.get_width() * 14, Bg_Move_Y))  # end background



# Ground Draw
def Draw_Ground(DisplaySurf, ground_posY, ground_height):
    pygame.draw.rect(DisplaySurf, (255, 255, 0), (0, ground_posY, 1980, 200))


def Draw_End():
    pass







