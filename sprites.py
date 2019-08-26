import pygame
from learner import *

class Player(pygame.sprite.Sprite):

    def __init__(self,image,size,start):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,size)
        self.rect = self.image.get_rect()
        self.rect.x  = start[0]
        self.rect.y = start[1]

    def get_rect(self):
        return self.rect

    def get_position(self):
        position = [self.rect.x,self.rect.y]
        return position

    def rotate(self,angle):
        self.image = pygame.transform.rotate(self.image,angle)

    def update_pos(self, key):
        new_position = move_sprite(key, self.get_position())
        self.rect.x = new_position[0]
        self.rect.y = new_position[1]

    def update(self):
        new_position = sprite_down(self.get_position())
        if new_position is not None:
            self.rect.y = new_position[1]

class Enemy(pygame.sprite.Sprite):

    def __init__(self,image,size,start):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,size)
        self.rect = self.image.get_rect()
        self.rect.x  = start[0]
        self.rect.y = start[1]

    def get_rect(self):
        return self.rect

    def get_position(self):
        position = [self.rect.x,self.rect.y]
        return position

    def update(self,pipe_speed):
        new_position = move_pipe(self.get_position(),pipe_speed)
        self.rect.x = new_position[0]
