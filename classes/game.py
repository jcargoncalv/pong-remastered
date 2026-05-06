import pygame
import sys
from classes.paddle import Paddle
#from classes.auto_paddle import AutoPaddle as Paddle2
from classes.ball import Ball

#Screen size tuple (width x height)
SCREEN_SIZE = (1280, 620)
#FPS rate
FPS = 60
WIN_SCORE = 10

class Game:
    
    def __init__(self, screen_size = (800, 600), fps = 60, win_score = 10):
        #Pygame initialization method
        pygame.init()

        pygame.font.init()
        
        #self.score_font = pygame.font.Font('assets/bit5x3.ttf', size = 60)
        self.score_font = pygame.font.Font(None, size = 60)
        self.text_font = pygame.font.Font(None, size = 35)

        self.fps = fps
        self.win_score = win_score
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Pong Remastered')

        #Pygame clock, needed to force the game loop to an specific FPS rate
        self.clock = pygame.time.Clock()

        #Initial Game State
        self.game_state = 'main_menu'

        #Game Colors as tuples
        self.bg_color = (24,45,52)        #"Arcade screen" green
        self.line_color = (255,255,255)   #White
        self.paddle_color = (255,255,255) #White
        self.ball_color = (255,255,255)   #White
        self.text_color = (255,255,255)   #White

        #Player Paddles
        self.paddle1 = Paddle(20, self.screen_size[1] // 2 - 60)
        self.paddle2 = Paddle(self.screen_size[0] - 40, self.screen_size[1] // 2 - 60)

        #Clamp paddle movement
        self.paddle1.set_bounds_y(0, self.screen_size[1] - 80)
        self.paddle2.set_bounds_y(0, self.screen_size[1] - 80)

        #Define ball and set score and bouncing boundaries
        self.ball = Ball(self.screen_size[0]/2 - 10, self.screen_size[1]/2 - 20)
        self.ball.set_bounds_x(0, self.screen_size[0] - 20)
        self.ball.set_bounds_y(0, self.screen_size[1] - 20)

        #Initialize scores
        self.p1_score = 0
        self.p2_score = 0
        
        # Initialize Delta Time between frames, in miliseconds
        self.delta = 0.0


    def ready(self):
        # Fill screen with background color, enable animation "flipping"
        self.screen.fill(self.bg_color)

        # Clock for FPS frames per second
        # Delta between frames, in miliseconds
        self.delta = self.clock.tick(self.fps) / 1000
        self.delta = max(0.001, min(0.1, self.delta))

        if self.game_state == 'start':
            self.ball.start()
            self.game_state = 'play'
        elif self.game_state == 'main_menu':
            #Ball stays put
            self.ball.stop()
        elif self.p1_score == self.win_score or self.p2_score == self.win_score:
            self.game_state = 'game_over'
            self.ball.stop()
            pass

    def process(self, delta):
        self.paddle1.process(delta)
        self.paddle2.process(delta)
        self.ball.process(delta)

        if self.paddle1.check_collision(self.ball.get_rect()):
            self.ball.bounce_x()
            #Small fix for ball rect going inside paddle and bouncing forever.
            self.ball.position.x += 5
        elif self.paddle2.check_collision(self.ball.get_rect()):
            self.ball.bounce_x()
            #Small fix for ball rect going inside paddle and bouncing forever.
            self.ball.position.x -= 5

        #Ball Tracker
        #if self.ball.position.x <= self.screen_size[0] / 2:
        #    self.paddle1.track_ball(self.ball.position.y)
        #else:
        #    self.paddle1.track_ball(self.screen_size[1]/ 2)

        scored = self.ball.scored()
        if scored != 'none':

            if scored == 'p1':
                self.p1_score = self.p1_score + 1
            elif scored == 'p2':
                self.p2_score = self.p2_score + 1
        
            self.ball.stop()
            if self.p1_score == self.win_score or self.p2_score == self.win_score:
                self.game_state = 'game_over'
            else:
                self.game_state = 'main_menu'

    def render(self, screen):
        #Draw Line in the middle of the game area
        pygame.draw.line(screen, self.line_color, (self.screen_size[0] // 2, 0), (self.screen_size[0] // 2, self.screen_size[1]))
        
        self.paddle1.render(screen, self.paddle_color)
        self.paddle2.render(screen, self.paddle_color)
        self.ball.render(screen, self.ball_color)

        # Score Text Rendering
        score1 = self.score_font.render(str(self.p1_score), True, self.text_color)
        screen.blit(score1, (self.screen_size[0] // 2 - 50, self.screen_size[1] // 12))
        score2 = self.score_font.render(str(self.p2_score), True, self.text_color)
        screen.blit(score2, (self.screen_size[0] // 2 + 30, self.screen_size[1] // 12))

        if self.game_state == 'game_over':
            self.screen.fill(self.bg_color)
            print("Player1: ", self.p1_score)
            print("Player2: ", self.p2_score)
            msg_gameover = self.text_font.render("Game Over", True, self.text_color)
            if self.p1_score == self.win_score:
                winner = 'Player 1'
            elif self.p2_score == self.win_score:
                winner = 'Player 2'    
            msg_gameover = self.text_font.render("Game Over", True, self.text_color)
            msg_playerwin = self.text_font.render(winner + " is the winner!", True, self.text_color)

            screen.blit(msg_gameover, (self.screen_size[0] // 2 - 110, self.screen_size[1] // 4))
            screen.blit(msg_playerwin, (self.screen_size[0] // 2 - 120, self.screen_size[1] // 3))

        # Message Text rendering
        elif self.game_state == 'main_menu':
            msg_welcome = self.text_font.render("Welcome to Pong!", True, self.text_color)
            msg_pressenter = self.text_font.render("Press Enter to draw", True, self.text_color)
            screen.blit(msg_welcome, (self.screen_size[0] // 2 - 110, self.screen_size[1] // 4))
            screen.blit(msg_pressenter, (self.screen_size[0] // 2 - 120, self.screen_size[1] // 3))
        
        pygame.display.flip()

    def handle_input(self, events):
        # Get the events that are on the queue for the game loop
        for event in events:
            # Clicking in the X of the window. Necessary to code in pygame, surprisingly
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    if self.game_state == 'main_menu':
                        self.game_state = 'start'
                    elif self.game_state == 'start':
                        self.game_state = 'main_menu'
                    elif self.game_state == 'game_over':
                        self.p1_score = 0
                        self.p2_score = 0
                        self.game_state = 'main_menu'

                if event.key == pygame.K_w:
                    self.paddle1.change_state('move_up')
                elif event.key == pygame.K_s:
                    self.paddle1.change_state('move_down')

                if event.key == pygame.K_UP:
                    self.paddle2.change_state('move_up')
                elif event.key == pygame.K_DOWN:
                    self.paddle2.change_state('move_down')
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.paddle1.change_state('idle')
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.paddle2.change_state('idle')

    def run(self):

        while True:
            self.ready()
            self.process(self.delta)
            self.render(self.screen)
            self.handle_input(pygame.event.get())