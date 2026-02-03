import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from sim import Sim
from body import Body

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("mo bodies")
    clock = pygame.time.Clock()
    running = True
    zoom = 1.0
    
    center = Body(500, 400, 0, 0, 2500.0)        

    sim = Sim(center)
    for i in range(3):
        body = Body.generate_starting_pos(1000, 800)
        sim.add_body(body)

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                if e.key == pygame.K_SPACE:
                    sim.paused = not sim.paused
            if e.type == pygame.MOUSEWHEEL:
                if e.y > 0: 
                    zoom *= 1.1
                else: 
                    zoom *= 0.9
                
                zoom = max(0.3, min(9.0, zoom))
                    
    
        dt = clock.tick(60) / 1000.0 * 4.5

        if sim.paused == False:    
            sim.update(dt)

        screen.fill("black")
        sim.draw_trails(screen, zoom)

        center.draw(screen, zoom)
        for body in sim.bodies: 
            body.draw(screen, zoom)
        
        pygame.display.flip()

    pygame.quit()