import pygame
from classes.game_object import GameObject

PADDLE_SPEED = 150

class Paddle(GameObject):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.height = 80
        self.width = 20


    def process(self, delta):
        super().process(delta)

        if self.state == 'move_up':
            self.velocity.y -= PADDLE_SPEED
        elif self.state == 'move_down':
            self.velocity.y += PADDLE_SPEED
        else:
            self.velocity.y = 0.0
        
        self.position += self.velocity * delta
        self.clamp_y()