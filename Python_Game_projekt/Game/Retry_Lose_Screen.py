import pygame

def Retry(DISPLAYSURF, Main_Bg, screen_width, screen_height, clock):
    GameOver = True
    player_live = 1
    while GameOver == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_r:
                    GameOver = False

        DISPLAYSURF.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render("You Lose, press 'R' to retry", True, (255, 255, 255))
        textRect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        DISPLAYSURF.blit(text, textRect)

        pygame.display.update()
        clock.tick(60)
