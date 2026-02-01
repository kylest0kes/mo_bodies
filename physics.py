import pygame
import numpy as np

class Body: 
    def __init__(self, x, y, vx, vy, mass):
        self.pos = np.array([x, y], dtype=float) 
        self.vel = np.array([vx, vy], dtype=float) 
        self.mass = mass

    def draw(self, screen, radius=10):
        pygame.draw.circle(screen, "white", (int(self.pos[0]), int(self.pos[1])), radius)

    @classmethod
    def generate_starting_pos(cls, w, h):
        x = np.random.uniform(20, 790)
        y = np.random.uniform(20, 590)
        return cls(x, y, 0, 0, 1.0)