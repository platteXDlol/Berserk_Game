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





def Draw_Triangle(DISPLAYSURF, ground_posY, screen_width, screen_height, triangle_position_X, Spickes_img):
    # Define triangle positions
    triangle_X = [
        triangle_position_X + 1000,
        triangle_position_X + 1500,
        triangle_position_X + 2100,
        triangle_position_X + 2500,
        triangle_position_X + 3100,  # 5
        triangle_position_X + 3500,
        triangle_position_X + 5400,
        triangle_position_X + 6200
    ]

    triangle_Y = [
        ground_posY - Spickes_img.get_height(),  # Place the spike top at ground level
        ground_posY - Spickes_img.get_height(),
        ground_posY - Spickes_img.get_height(),
        ground_posY - Spickes_img.get_height(),
        ground_posY - Spickes_img.get_height(),  # 5
        ground_posY - Spickes_img.get_height(),
        ground_posY - Spickes_img.get_height(),
        ground_posY - Spickes_img.get_height()
    ]

    # Create triangle Rects
    triangles = [
        pygame.Rect(triangle_X[i], triangle_Y[i], Spickes_img.get_width(), Spickes_img.get_height())
        for i in range(len(triangle_X))
    ]

    # Draw each triangle image
    for triangle in triangles:
        DISPLAYSURF.blit(Spickes_img, (triangle.x, triangle.y))

    # Create triangle masks
    triangle_masks = [
        pygame.mask.from_surface(Spickes_img)  # Generate a mask from the spike image
        for _ in range(len(triangle_X))
    ]

    # Adjust masks to triangle positions
    triangle_mask_positions = [
        {'mask': triangle_masks[i], 'pos': (triangle_X[i], triangle_Y[i])}
        for i in range(len(triangles))
    ]

    return triangle_mask_positions  # Return mask with positions



