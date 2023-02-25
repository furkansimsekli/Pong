import pygame
from Constants import *
from random import choice

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = pygame.math.Vector2(MIN_BALL_SPEED * choice([-1,1]), MIN_BALL_SPEED * choice([-1,1]))
        self.speed = MIN_BALL_SPEED
        # if custom_rect == None:
        self.rect = pygame.Rect(SCREEN_WIDTH/2 - BALL_SIZE/2, SCREEN_HEIGHT/2 - BALL_SIZE/2, BALL_SIZE, BALL_SIZE)
        # else: self.rect = custom_rect

    def reflect_ball(self):
        # if self.rect.left <= 0:
        #     return True
        # if self.rect.right >= SCREEN_WIDTH:
        #     return False
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.velocity.y *= -1
    
    def update(self, player_win):
        player_win = self.reflect_ball()
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
    
    def reset(self):
        self.velocity = pygame.math.Vector2(MIN_BALL_SPEED * choice([-1,1]), MIN_BALL_SPEED * choice([-1,1]))
        self.speed = MIN_BALL_SPEED
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


