import pygame
import numpy as np

class Body: 
    def __init__(self, x, y, vx, vy, mass, acc):
        self.pos = np.array([x, y], dtype=float) 
        self.vel = np.array([vx, vy], dtype=float) 
        self.mass = mass
        self.acc = np.array([0.0, 0.0], dtype=float)

    def draw(self, screen, radius=5):
        pygame.draw.circle(screen, "white", (int(self.pos[0]), int(self.pos[1])), radius)

    def update(self, dt):
        self.vel += self.acc * dt
        self.pos += self.vel * dt

    @classmethod
    def generate_starting_pos(cls, width, height):
        x = np.random.uniform(20, width-20)
        y = np.random.uniform(20, height-20)
        vx = np.random.uniform(-50, 50)
        vy = np.random.uniform(-50, 50)
        return cls(x, y, vx, vy, 1.0)