import pygame
import numpy as np

class Body: 
    def __init__(self, x, y, vx, vy, mass):
        self.pos = np.array([x, y], dtype=float) 
        self.vel = np.array([vx, vy], dtype=float) 
        self.mass = mass
        pass

    def draw(self, screen, radius=13):
        pygame.draw(screen, "white", self.pos, radius)