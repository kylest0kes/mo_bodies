import numpy as np

class Sim:
    def __init__(self, center):
        self.center = center
        self.bodies = []
        self.G = 350 

    def add_body(self, body):
        self.bodies.append(body)

    def calculate_accelerations(self):
        for i, body1 in enumerate(self.bodies):
            body1.acc = np.array([0.0, 0.0], dtype=float)
            
            direction = self.center.pos - body1.pos
            distance = np.linalg.norm(direction)
            if distance > 1:
                body1.acc += self.G * self.center.mass * direction / (distance ** 3)
            
            for j, body2 in enumerate(self.bodies):
                if i != j:
                    direction = body2.pos - body1.pos
                    distance = np.linalg.norm(direction)
                    if distance > 1:
                        body1.acc += self.G * body2.mass * direction / (distance ** 3)
    
    def update(self, dt):
        self.calculate_accelerations()
        for body in self.bodies:
            body.vel[0] += body.acc[0] * dt
            body.vel[1] += body.acc[1] * dt

            body.pos[0] += body.vel[0] * dt
            body.pos[1] += body.vel[1] * dt
    