import pygame, os, sys




def Draw_Platforms(DISPLAYSURF, screen_height, screen_width, platform_position_X):
    platform_X = [
        platform_position_X + 1000,
        platform_position_X + 1500,
        platform_position_X + 2100,
        platform_position_X + 2500,
        platform_position_X + 3100, # 5
        platform_position_X + 3500,
        platform_position_X + 5400,
        platform_position_X + 6200
    ]

    platform_Y = [
        screen_height / 100 * 78,
        screen_height / 100 * 59,
        screen_height / 100 * 63,
        screen_height / 100 * 48,
        screen_height / 100 * 70, # 5
        screen_height / 100 * 51,
        screen_height / 100 * 51,
        screen_height / 100 * 32
    ]

    platform_length = [
        screen_width / 100 * 15,
        screen_width / 100 * 15,
        screen_width / 100 * 20,
        screen_width / 100 * 10,
        screen_width / 100 * 12,
        screen_width / 100 * 20,
        screen_width / 100 * 15,
        screen_width / 100 * 15
    ]

    platform_width = [
        screen_height / 100 * 2,
        screen_height / 100 * 2,
        screen_height / 100 * 2,
        screen_height / 100 * 2,
        screen_height / 100 * 2,
        screen_height / 100 * 2,
        screen_height / 100 * 2,
        screen_height / 100 * 2
    ]


    platforms = [
        pygame.Rect(platform_X[i], platform_Y[i], platform_length[i], platform_width[i])
        for i in range(len(platform_X))
    ]

    # Draw each platform
    for platform in platforms:
        pygame.draw.rect(DISPLAYSURF, (0, 255, 100), platform)

    return platforms



import pygame

def Draw_Triangle(DISPLAYSURF, ground_posY, screen_width, screen_height, triangle_position_X, Spickes_img):
    # Adjust the triangle's X positions as a percentage of the screen width
    TriangleX = [
        triangle_position_X + screen_width * 0.3,  # 30% of screen width
        triangle_position_X + screen_width * 0.4,  # 40% of screen width
        triangle_position_X + screen_width * 0.5   # 50% of screen width
    ]

    TriangleY = ground_posY


    triangles = [
        ((TriangleX[i], TriangleY  * 0.978703703704))  # 97.8703703704% of screen height
        for i in range(len(TriangleX))
    ]

    # Blit the image at the triangle positions
    for triangle_top in triangles:
        DISPLAYSURF.blit(Spickes_img, (triangle_top[0] - Spickes_img.get_width() // 2, triangle_top[1] - Spickes_img.get_height() // 2))

    return triangles



