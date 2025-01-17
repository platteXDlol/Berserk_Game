


def Draw_Griffith(DISPLAYSURF, griffith_image, bg_pf_position, griffith_posY):
    griffith_position_X = bg_pf_position['griffith_position_X']
    DISPLAYSURF.blit(griffith_image, (griffith_position_X, griffith_posY))

def Update_Griffith(bg_pf_position, griffith_start_bg_position_X, griffith_speed, griffith_direction, griffith_move_range, griffith_active, screen_width, griffith_initialized, level_length):
    # Activate Griffith if he comes into view
    if bg_pf_position['x'] <= -level_length:
        griffith_active = True

        # Set Griffith's start position only once when he's activated
        if not griffith_initialized:
            griffith_start_bg_position_X = bg_pf_position['griffith_position_X']
            griffith_initialized = True

    # Move Griffith if active
    if griffith_active:
        bg_pf_position['griffith_position_X'] += griffith_speed * griffith_direction

        # Reverse direction when reaching the movement range
        if (
            bg_pf_position['griffith_position_X'] >= griffith_start_bg_position_X + griffith_move_range or
            bg_pf_position['griffith_position_X'] <= griffith_start_bg_position_X
        ):
            griffith_direction *= -1

    return bg_pf_position, griffith_direction, griffith_active, griffith_start_bg_position_X, griffith_initialized