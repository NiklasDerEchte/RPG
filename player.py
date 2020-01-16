import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, width, height, matrix):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 0, width, height)
        self.posX = self.rect.x
        self.posY = self.rect.y
        self.isMoving = False
        self.canMove = True
        self.direction = 0

        self.move_x = 0
        self.move_y = 0
        self.cur_tile_pos = 0, 0
        self.next_tile_pos = 0, 0
        self.matrix = matrix

    def update(self):
        keys = pygame.key.get_pressed()
        #self.posX = self.rect.x
        #self.posY = self.rect.y
        self.isMoving = False
        self.cur_tile_pos = self.next_tile_pos
        self.rect.x, self.rect.y = self.matrix.get_coord(self.cur_tile_pos[0],
                                                                       self.cur_tile_pos[1])
        self.move_x = 0
        self.move_y = 0
        if keys[pygame.K_a] and self.canMove:
            #self.rect.x += -playerSpeed
            self.isMoving = True
            self.direction = 1
            self.move_x = -1
        if keys[pygame.K_d] and self.canMove:
            #self.rect.x += playerSpeed
            self.isMoving = True
            self.direction = 2
            self.move_x = 1
        if keys[pygame.K_w] and self.canMove:
            #self.rect.y += -playerSpeed
            self.isMoving = True
            self.direction = 3
            self.move_y = -1
        if keys[pygame.K_s] and self.canMove:
            #self.rect.y += playerSpeed
            self.isMoving = True
            self.direction = 0
            self.move_y = 1
        self.next_tile_pos = self.cur_tile_pos[0] + self.move_x, self.cur_tile_pos[1] + self.move_y