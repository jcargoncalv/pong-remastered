import pygame
import random
from datetime import datetime
from classes.game_object import GameObject

BALL_SPEED = 500

class Ball(GameObject):

    def __init__(self, x, y):
        super().__init__(x,y)
        self.height = 20
        self.width = 20
        self.start_position = pygame.math.Vector2(x,y)
        self.acc = 1.0


    def process(self, delta):
        super().process(delta)
        
        if self.velocity != pygame.math.Vector2(0,0):
            self.position += self.velocity * BALL_SPEED * delta * self.acc
            if self.position.y < self.min_y or self.position.y > self.max_y:
                self.bounce_y()


    def direction_shuffle(self):
        random.seed(datetime.now().timestamp())
        options = [[1,1], [1,-1], [-1,1], [-1,-1]]
        #options = [[0.5, 1], [1, 0.5], [0.5, -1], [-1, 0.5], [-0.5, 1], [1, -0.5], [-1, -0.5], [-0.5, -1],
        #           [0.5, 0.5], [-0.5, -0.5], 
        #           [1,1], [1,-1], [-1,1], [-1,-1]]
        return options[random.randint(0, 3)]
    

    def start(self):
        self.position.x = self.start_position.x
        self.position.y = self.start_position.y
        
        temp = self.direction_shuffle()
        self.velocity.x = temp[0]
        self.velocity.y = temp[1]
        self.velocity = self.velocity.normalize()

        self.acc = 1.0


    def stop(self):
        self.position.x = self.start_position.x
        self.position.y = self.start_position.y
        self.velocity = pygame.math.Vector2(0,0)


    def bounce_x(self):
        self.velocity.x *= -1
        self.acc = self.acc + 0.03


    def bounce_y(self):
        self.velocity.y *= -1
        self.acc = self.acc + 0.03


    def scored(self):
        if self.position.x < self.min_x:
            return 'p2'
        elif self.position.x > self.max_x:
            return 'p1'
        return 'none'