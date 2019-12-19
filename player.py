import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 0, width, height)
        self.posX = self.rect.x
        self.posY = self.rect.y
        self.isMoving = False
        self.canMove = True
        self.direction = 0

    def update(self):
        keys = pygame.key.get_pressed()
        self.posX = self.rect.x
        self.posY = self.rect.y
        self.isMoving = False
        if keys[pygame.K_a] and self.canMove:
            self.rect.x += -playerSpeed
            self.isMoving = True
            self.direction = 1
        if keys[pygame.K_d] and self.canMove:
            self.rect.x += playerSpeed
            self.isMoving = True
            self.direction = 2
        if keys[pygame.K_w] and self.canMove:
            self.rect.y += -playerSpeed
            self.isMoving = True
            self.direction = 3
        if keys[pygame.K_s] and self.canMove:
            self.rect.y += playerSpeed
            self.isMoving = True
            self.direction = 0