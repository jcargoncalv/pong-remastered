import pygame
from classes.game_object import GameObject

PADDLE_SPEED = 400

class AutoPaddle(GameObject):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.height = 80
        self.width = 20

    def process(self, delta):
        super().process(delta)

        self.position += self.velocity * delta
        self.clamp_y()


    def track_ball(self, ball_pos):
        dead_zone = 5

        paddle_center = self.position.y + self.height / 2

        if abs(paddle_center - ball_pos) < dead_zone:
            self.velocity.y = 0
        if (paddle_center < ball_pos):
            self.velocity.y = PADDLE_SPEED
        elif (paddle_center > ball_pos):
            self.velocity.y = -PADDLE_SPEED
