


def Draw_Griffith(DISPLAYSURF, griffith_image, bg_pf_position, griffith_posY, Griffith_live):
    if Griffith_live == True:
        griffith_position_X = bg_pf_position['griffith_position_X']
        DISPLAYSURF.blit(griffith_image, (griffith_position_X, griffith_posY))



def Update_Griffith(bg_pf_position, griffith_start_bg_position_X, griffith_speed, griffith_direction, griffith_move_range, griffith_active, screen_width, griffith_initialized, level_length):
    # Activate Griffith if he comes into view
    if bg_pf_position['x'] <= - (level_length - screen_width):
        griffith_active = True

        # Set Griffith's start position only once when he's activated
        griffith_start_bg_position_X = bg_pf_position['griffith_position_X']


    # Move Griffith if active
    if griffith_active:
        bg_pf_position['griffith_position_X'] += griffith_speed * griffith_direction

        # Reverse direction when reaching the movement range
        if bg_pf_position['griffith_position_X'] <= screen_width / 100 * 10:
            griffith_direction = 1

        if bg_pf_position['griffith_position_X'] >= screen_width / 100 * 90:
            griffith_direction = -1

    return bg_pf_position, griffith_direction, griffith_active, griffith_start_bg_position_X, griffith_initialized


def check_griffith_collision(player_rect, player_mask, bg_pf_position, griffith_mask, griffith_posY, Griffith_live):
    if not Griffith_live:
        return False
    # Calculate the offset between the player and Griffith
    offset = (bg_pf_position['griffith_position_X'] - player_rect.x, griffith_posY - player_rect.y)

    top_20_end = int(player_rect.height * 0.2)

    player_dead_mask = player_mask.copy()
    for y in range(player_rect.height):
        if y > top_20_end:  # Clear all but the bottom 15% of the mask
            for x in range(player_rect.width):
                player_dead_mask.set_at((x, y), 0)

    # Check for mask overlap (collision)
    if player_dead_mask.overlap(griffith_mask, offset):
        return True  # Collision detected

    return False  # No collision






def check_kill_with_feet(player_rect, player_mask, bg_pf_position, griffith_mask, griffith_rect):
    # Calculate the offset between the player and Griffith
    offset = (bg_pf_position['griffith_position_X'] - player_rect.x, griffith_rect.y - player_rect.y)

    # Calculate the height of the bottom 15% of the player
    bottom_15_start = int(player_rect.height * 0.85)

    # Create a mask for just the bottom 15% of the player
    feet_mask = player_mask.copy()
    for y in range(player_rect.height):
        if y < bottom_15_start:  # Clear all but the bottom 15% of the mask
            for x in range(player_rect.width):
                feet_mask.set_at((x, y), 0)

    # Calculate the height of the top 20% of Griffith
    top_20_end = int(griffith_rect.height * 0.2)

    # Create a mask for just the top 20% of Griffith
    head_mask = griffith_mask.copy()
    for y in range(griffith_rect.height):
        if y >= top_20_end:  # Clear everything except the top 20% of the mask
            for x in range(griffith_rect.width):
                head_mask.set_at((x, y), 0)

    # Check for mask overlap (collision) between the player's feet and Griffith's head
    if feet_mask.overlap(head_mask, offset):
        return True  # Collision detected with feet (killing Griffith)

    return False  # No collision


