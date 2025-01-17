def Draw_Griffith(DISPLAYSURF, griffith_image, bg_pf_position, griffith_posY):
    griffith_position_X = bg_pf_position['griffith_position_X']
    DISPLAYSURF.blit(griffith_image, (griffith_position_X, griffith_posY))

def Update_Griffith(bg_pf_position, griffith_start_bg_position_X, griffith_speed, griffith_direction, griffith_move_range):
    bg_pf_position['griffith_position_X'] += griffith_speed * griffith_direction
    if (
        bg_pf_position['griffith_position_X'] >= griffith_start_bg_position_X + griffith_move_range or
        bg_pf_position['griffith_position_X'] <= griffith_start_bg_position_X
    ):
        griffith_direction *= -1
    return bg_pf_position, griffith_direction