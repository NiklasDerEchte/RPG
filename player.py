import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, width, height, matrix):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 0, width, height)
        self.is_moving = False
        self.canMove = True
        self.direction = 0

        self.move_direction = pygame.math.Vector2()
        self.cur_tile_pos = pygame.math.Vector2()

        self.matrix = matrix

    def update_pos(self, new_pos):
        self.cur_tile_pos = new_pos
        self.rect.x, self.rect.y = self.matrix.get_coord(self.cur_tile_pos)

    def update_world_pos(self, new_world_pos):
        self.cur_tile_pos = self.matrix.get_tile_pos(new_world_pos)
        self.rect.x, self.rect.y = new_world_pos

    def set_world_pos(self, coord):
        self.rect.x, self.rect.y = self.matrix.position_reset(coord) # setzt die rect position auf 0
        self.cur_tile_pos.x, self.cur_tile_pos.y = self.matrix.get_tile_pos((self.rect.x, self.rect.y))


    def update(self):
        keys = pygame.key.get_pressed()
        self.move_direction.x = 0
        self.move_direction.y = 0
        self.is_moving = False
        if keys[pygame.K_a] and self.canMove:
            self.move_direction.x = -1
            self.direction = 1
        if keys[pygame.K_d] and self.canMove:
            self.move_direction.x = 1
            self.direction = 2
        if keys[pygame.K_w] and self.canMove:
            self.move_direction.y = -1
            self.direction = 3
        if keys[pygame.K_s] and self.canMove:
            self.move_direction.y = 1
            self.direction = 0

        if not self.is_moving and (self.move_direction.x != 0 or self.move_direction.y != 0):
            self.is_moving = True