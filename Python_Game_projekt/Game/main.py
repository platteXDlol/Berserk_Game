import pygame


pygame.init()

#Window fullscreen
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#clock for timer and fps
clock = pygame.time.Clock()

#player
#player = pygame.image.load('player.png')
player = pygame.Rect((300, 250, 50, 50))

player_speed = 5 #player speed
player_gravity = 0 #player gravity


#window loop
#make the game in it
GameRun = True
while GameRun:

    DISPLAYSURF.fill((0, 0, 0)) #background color

    pygame.draw.rect(DISPLAYSURF, (255, 0, 0), player) #draw player

    #player movement
    key = pygame.key.get_pressed()
    if key[pygame.K_a]: #left with a
        player.x -= player_speed
    if key[pygame.K_d]: #right with d
        player.x += player_speed





















    # quit the game
    for event in pygame.event.get():
        #quit with close button
        if event.type == pygame.QUIT:
            pygame.quit()
        #quit with escape button
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GameRun = False

    pygame.display.update()
    clock.tick(60)  # wait until next frame (at 60 FPS)
pygame.quit()