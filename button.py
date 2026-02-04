import pygame, math

class Button:
    def __init__(self, x, y, radius, text, cb, color, hover_color, font):
        self.x = x
        self.y = y
        self.radius = radius
        self.text_str = text
        self.cb = cb
        self.color = color
        self.hover_color = hover_color
        self.font = font 
        self.text_surf = font.render(text, True, (0, 0, 0))
        self.current_color = color
        self.hovered = False
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.current_color, (self.x, self.y), self.radius)
        text_rect = self.text_surf.get_rect(center=(self.x, self.y))
        screen.blit(self.text_surf, text_rect)
    
    def check_hover(self, mouse_pos):
        dist = math.sqrt((self.x - mouse_pos[0])**2 + (self.y - mouse_pos[1])**2) 
        self.hovered = dist < self.radius
        return self.hovered