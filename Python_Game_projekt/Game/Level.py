import pygame


def Draw_Platforms(DISPLAYSURF, screen_height, screen_width, platform_position_X):
    # Platform X positions: extended to 28000 pixels
    platform_X = [
        platform_position_X + 1000,
        platform_position_X + 2000,
        platform_position_X + 3000,
        platform_position_X + 4000,
        platform_position_X + 5000,
        platform_position_X + 6000,
        platform_position_X + 7000,
        platform_position_X + 8000,
        platform_position_X + 9000,
        platform_position_X + 10000,
        platform_position_X + 11000,
        platform_position_X + 12000,
        platform_position_X + 13000,
        platform_position_X + 14000,
        platform_position_X + 15000,
        platform_position_X + 16000,
        platform_position_X + 17000,
        platform_position_X + 18000,
        platform_position_X + 19000,
        platform_position_X + 20000,
        platform_position_X + 21000,
        platform_position_X + 22000,
        platform_position_X + 23000,
        platform_position_X + 24000,
        platform_position_X + 25000,
        platform_position_X + 26000,
        platform_position_X + 27000,
    ]

    # Platform Y positions: mixed heights for varying difficulty
    platform_Y = [
        screen_height / 100 * 75,  # Lower platform for easy walking
        screen_height / 100 * 60,  # Medium height
        screen_height / 100 * 80,  # High platform
        screen_height / 100 * 65,  # Mid height for jump
        screen_height / 100 * 55,  # Lower platform
        screen_height / 100 * 60,  # Mid-high platform for jump
        screen_height / 100 * 45,  # Low enough for easy jump
        screen_height / 100 * 50,  # Mid platform, easy jump
        screen_height / 100 * 40,  # High platform, but reachable
        screen_height / 100 * 50,  # Low platform
        screen_height / 100 * 55,  # Mid height
        screen_height / 100 * 60,  # Platform at medium height
        screen_height / 100 * 45,  # Lower platform for walking
        screen_height / 100 * 50,  # Mid height platform
        screen_height / 100 * 55,  # Slightly higher platform
        screen_height / 100 * 65,  # Higher platform for jump
        screen_height / 100 * 50,  # Lower platform
        screen_height / 100 * 45,  # Another low platform for walking
        screen_height / 100 * 50,  # Mid platform
        screen_height / 100 * 40,  # Slightly higher platform, requiring a jump
        screen_height / 100 * 45,  # Mid platform
        screen_height / 100 * 50,  # Last platform, mid height
        screen_height / 100 * 55,  # Mid height
        screen_height / 100 * 60,  # Slightly higher platform
        screen_height / 100 * 65,  # Higher platform
        screen_height / 100 * 50,  # Last reachable platform
        screen_height / 100 * 60,  # Slightly higher platform
    ]

    # Platform length: balanced length for each platform
    platform_length = [
        screen_width / 100 * 15,  # Small platform
        screen_width / 100 * 18,  # Longer platform
        screen_width / 100 * 10,  # Short platform for fast timing
        screen_width / 100 * 14,  # Medium platform
        screen_width / 100 * 20,  # Longer platform for stability
        screen_width / 100 * 16,  # Medium platform
        screen_width / 100 * 18,  # Medium platform
        screen_width / 100 * 12,  # Shorter platform for precision
        screen_width / 100 * 14,  # Medium-sized platform
        screen_width / 100 * 15,  # Medium platform
        screen_width / 100 * 16,  # Medium platform
        screen_width / 100 * 18,  # Larger platform
        screen_width / 100 * 14,  # Medium-sized platform
        screen_width / 100 * 20,  # Larger platform
        screen_width / 100 * 14,  # Medium platform
        screen_width / 100 * 12,  # Short platform
        screen_width / 100 * 18,  # Larger platform
        screen_width / 100 * 15,  # Medium platform
        screen_width / 100 * 10,  # Shorter platform for timing
        screen_width / 100 * 14,  # Medium platform
        screen_width / 100 * 16,  # Medium platform
        screen_width / 100 * 20,  # Final larger platform
        screen_width / 100 * 18,  # Larger platform
        screen_width / 100 * 15,  # Medium platform
        screen_width / 100 * 12,  # Shorter platform
        screen_width / 100 * 18,  # Final platform
        screen_width / 100 * 15,  # Medium platform
    ]

    # Ensure all lists are the same length (27 platforms each)
    assert len(platform_X) == len(platform_Y) == len(platform_length)

    # Platform width remains constant
    platform_width = screen_height / 100 * 2

    # Create the platforms as rectangles
    platforms = [
        pygame.Rect(platform_X[i], platform_Y[i], platform_length[i], platform_width)
        for i in range(len(platform_X))
    ]

    # Draw all the platforms
    for platform in platforms:
        pygame.draw.rect(DISPLAYSURF, (0, 255, 100), platform)

    return platforms


def Draw_Spikes(DISPLAYSURF, ground_posY, screen_width, screen_height, triangle_position_X, Spikes_img):
    triangle_X = [
        triangle_position_X + 1200,
    ]

    triangle_Y = [
        ground_posY - Spikes_img.get_height(),
    ]

    triangles = [
        pygame.Rect(triangle_X[i], triangle_Y[i], Spikes_img.get_width(), Spikes_img.get_height())
        for i in range(len(triangle_X))
    ]

    for triangle in triangles:
        DISPLAYSURF.blit(Spikes_img, (triangle.x, triangle.y))

    triangle_masks = [
        pygame.mask.from_surface(Spikes_img)
        for _ in range(len(triangle_X))
    ]

    triangle_mask_positions = [
        {'mask': triangle_masks[i], 'pos': (triangle_X[i], triangle_Y[i])}
        for i in range(len(triangles))
    ]

    return triangle_mask_positions
