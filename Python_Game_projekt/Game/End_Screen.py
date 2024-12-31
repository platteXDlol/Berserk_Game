import pygame




# Block for End detection
def End_Block_Draw():
    pass




# End screen
def End_Screen(DISPLAYSURF, screen_width, screen_height, clock, elapsed_time):
    End = True
    while End:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_RETURN:
                    End = False

        # Calculate and format elapsed time
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        formatted_time = f"{minutes}:{seconds:02}"

        # Fill the screen
        DISPLAYSURF.fill((0, 0, 0))

        # Load font
        font = pygame.font.Font(None, 74)

        # Render text
        text = font.render("You Won!", True, (255, 255, 255))
        time_text = font.render(f"Time: {formatted_time}", True, (255, 255, 255))
        exit_text = font.render("Press 'Enter' to exit", True, (255, 255, 255))

        # Center text
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
        time_text_rect = time_text.get_rect(center=(screen_width // 2, screen_height // 2))
        exit_text_rect = exit_text.get_rect(center=(screen_width // 2, screen_height // 2 + 100))

        # Draw text
        DISPLAYSURF.blit(text, text_rect)
        DISPLAYSURF.blit(time_text, time_text_rect)
        DISPLAYSURF.blit(exit_text, exit_text_rect)

        # Update the display
        pygame.display.update()
        clock.tick(60)
