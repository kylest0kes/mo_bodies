import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from sim import Sim
from body import Body
from button import Button

def add_mo_bodies(sim, bodies_count):
    bodies_count[0] += 1
    sim.clear_bodies()
    for _ in range(bodies_count[0]):
        body = Body.generate_starting_pos(1000, 800)
        sim.add_body(body)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("mo bodies")
    clock = pygame.time.Clock()
    running = True
    zoom = 1.0

    bodies_count = [3] 
    
    center = Body(500, 400, 0, 0, 2500.0)        

    sim = Sim(center)
    for i in range(bodies_count[0]):
        body = Body.generate_starting_pos(1000, 800)
        sim.add_body(body)

    buttons = [
        Button(940, 740, 20, "+", lambda: add_mo_bodies(sim, bodies_count), (150, 150, 150), (0, 255, 0), pygame.font.Font(None, 32))
    ]

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
            if e.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for button in buttons:
                    if button.check_hover((m_x, m_y)):
                        button.cb()
                    
    
        dt = clock.tick(60) / 1000.0 * 3.5

        if sim.paused == False:    
            sim.update(dt)

        screen.fill("black")
        sim.draw_trails(screen, zoom)

        center.draw(screen, zoom)
        for body in sim.bodies: 
            body.draw(screen, zoom)

        for button in buttons:
            if button.check_hover(pygame.mouse.get_pos()):
                button.current_color = button.hover_color
            else:
                button.current_color = button.color
            button.draw(screen)
        
        pygame.display.flip()

    pygame.quit()