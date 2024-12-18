import pygame, os, sys



#Window Draw
def Draw_Window(DISPLAYSURF, Bg_Move_X, Bg_Move_Y, Main_Bg):
    DISPLAYSURF.fill((0, 0, 0))  # background color
    for x in range(0, 10):  # background repeat 10 times
        DISPLAYSURF.blit(Main_Bg, (Bg_Move_X + Main_Bg.get_width() * x, Bg_Move_Y))

def Draw_Ground(DisplaySurf, ground_posY, ground_height):
    pygame.draw.rect(DisplaySurf, (255, 255, 0), (0, ground_posY, 1980, 200))



color = (255, 255, 0)
rect = pygame.Rect(200, 875, 50, 100)
def Draw_Rect(DISPLAYSURF):
    pygame.draw.rect(DISPLAYSURF, color, rect)

