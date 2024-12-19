import pygame, os, sys



def Platform_Draw(DISPLAYSURF, platform):
    pygame.draw.rect(DISPLAYSURF, (255, 0, 255), platform)