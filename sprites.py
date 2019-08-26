import pygame
from learner import *

class Player(pygame.sprite.Sprite):
    """Class for the main character which is controlled by the player """

    def __init__(self,image,size,start):
        """Constructor for player sprite. Inherits from pygame Sprite class"""
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,size)
        self.rect = self.image.get_rect()
        self.rect.x  = start[0]
        self.rect.y = start[1]

    def get_rect(self):
        """Returns the coordinates for the rectangle bounding box around
         sprite object"""
        return self.rect

    def get_position(self):
        """Return the x,y coordinates for the top left corner of the sprite"""
        position = [self.rect.x,self.rect.y]
        return position

    def rotate(self,angle):
        """Updates sprites orientations by rotating the image by angle"""
        self.image = pygame.transform.rotate(self.image,angle)

    def update_pos(self, key):
        """Update the position of the sprite based on whether the up or down
        key is pressed"""
        position = self.get_position()
        new_position = move_sprite(key, position)
        self.rect.x = new_position[0]
        self.rect.y = new_position[1]

    def update(self):
        """Update the sprites position on the screen"""
        new_position = sprite_down(self.get_position())
        if new_position is not None:
            self.rect.y = new_position[1]

class Enemy(pygame.sprite.Sprite):
    """Class for the enemy character or object which is controlled by the player """

    def __init__(self,image,size,start):
        """Constructor for player sprite. Inherits from pygame Sprite class"""

        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,size)
        self.rect = self.image.get_rect()
        self.rect.x  = start[0]
        self.rect.y = start[1]

    def get_rect(self):
        """Returns the coordinates for the rectangle bounding box around sprite
        object"""

        return self.rect

    def get_position(self):
        """Return the x,y coordinates for the top left corner of the sprite"""

        position = [self.rect.x,self.rect.y]
        return position

    def update(self,pipe_speed):
        """Update the sprites position on the screen. Makes the enemy scroll
        across the screen"""

        new_position = move_pipe(self.get_position(),pipe_speed)
        self.rect.x = new_position[0]
