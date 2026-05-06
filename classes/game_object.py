import pygame

class GameObject:

    def __init__(self, pos_x, pos_y):
        self.position = pygame.Vector2(pos_x, pos_y)
        self.velocity = pygame.Vector2(0.0, 0.0)  # pixels per second
        self.height = 0
        self.width = 0
        self.min_x = 0
        self.min_x = 0
        self.min_y = 0
        self.max_y = 100
        self.state = 'main_menu'


    def ready(self):
        pass


    def process(self, delta):
        pass


    def render(self, screen, color=(255,255,255)):
        return pygame.draw.rect(screen, color, self.get_rect())


    def handle_input():
        pass


    def set_bounds_x(self, min, max):
        self.min_x = min
        self.max_x = max


    def set_bounds_y(self, min, max):
        self.min_y = min
        self.max_y = max


    def clamp_x(self):
        self.position.x = max(self.min_x,
                              min(self.max_x, self.position.x))
        

    def clamp_y(self):
        self.position.y = max(self.min_y,
                              min(self.max_y, self.position.y))

    def check_collision(self, rect):
        return pygame.Rect.colliderect(
                            pygame.Rect(self.position.x,self.position.y,self.width,self.height), rect)
    

    def change_state(self, state='main_menu'):
        self.state = state


    def get_rect(self):
        return pygame.Rect(self.position.x,self.position.y,self.width,self.height)


 