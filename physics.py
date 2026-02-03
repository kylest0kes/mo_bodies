import pygame
import numpy as np

class Body: 
    def __init__(self, x, y, vx, vy, mass, trail_color):
        self.pos = np.array([x, y], dtype=float) 
        self.vel = np.array([vx, vy], dtype=float) 
        self.mass = mass
        self.acc = np.array([0.0, 0.0], dtype=float)
        self.trail_color = trail_color 

    def draw(self, screen, radius=5):
        pygame.draw.circle(screen, "white", (int(self.pos[0]), int(self.pos[1])), radius)

    def update(self, dt):
        self.vel += self.acc * dt
        self.pos += self.vel * dt

    @classmethod
    def generate_starting_pos(cls, width, height):
        angle = np.random.uniform(0, 2*np.pi)
        distance = np.random.uniform(80, 200)
        
        x = 400 + distance * np.cos(angle)
        y = 300 + distance * np.sin(angle)
        
        orbital_speed = np.sqrt(200 * 1000 / distance) * 1.5  
        vx = -orbital_speed * np.sin(angle)  
        vy =  orbital_speed * np.cos(angle)
        
        mass = np.random.choice([12.3, 5.0, 2.0, 1.0, 0.5])

        r = np.random.uniform(30, 255)
        g = np.random.uniform(30, 255)
        b = np.random.uniform(30, 255)
        trail_color = [r, g, b] 
        return cls(x, y, vx, vy, mass, trail_color)