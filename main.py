import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from sim import Sim
from physics import Body

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("mo bodies")
    clock = pygame.time.Clock()
    running = True
    
    center = Body(400, 300, 0, 0, 1000.0)        

    sim = Sim(center)
    for i in range(3):
        body = Body.generate_starting_pos(800, 600)
        sim.add_body(body)

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
            
        dt = clock.tick(60) / 1000.0 * 4.5
        sim.update(dt)

        screen.fill("black")

        center.draw(screen)
        for body in sim.bodies: 
            body.draw(screen)
        
        pygame.display.flip()

    pygame.quit()