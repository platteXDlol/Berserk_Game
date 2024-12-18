import pygame, os, sys



#Window Draw
def Draw_Window(DISPLAYSURF, Bg_Move_X, Bg_Move_Y, Main_Bg):
    DISPLAYSURF.fill((0, 0, 0))  # background color
    for x in range(0, 10):  # background repeat 10 times
        DISPLAYSURF.blit(Main_Bg, (Bg_Move_X + Main_Bg.get_width() * x, Bg_Move_Y))


def Draw_Level():
    pass