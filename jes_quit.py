import pygame

class QUIT:
    def __init__():
        gamerunning = True

        while gamerunning == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gamerunning = False
                else:
                    gamerunning = True
                    
        pygame.quit