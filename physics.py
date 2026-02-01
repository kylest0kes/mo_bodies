import pygame
import numpy as np

class Body: 
    def __init__(self, x, y, vx, vy, mass):
        self.pos = np.array([x, y], dtype=float) 
        self.vel = np.array([vx, vy], dtype=float) 
        self.mass = mass
        pass

    def draw(self, screen, radius=10):
        pygame.draw.circle(screen, "white", (int(self.pos[0]), int(self.pos[1])), radius)