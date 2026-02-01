import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from physics import Body

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True
    
    center = Body(400, 300, 0, 0, 1.0)        
    body1 = Body.generate_starting_pos(800, 600)

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
            
        screen.fill("black")

        center.draw(screen)
        body1.draw(screen)

        pygame.display.flip()
        
        clock.tick(60)
        
    pygame.quit()