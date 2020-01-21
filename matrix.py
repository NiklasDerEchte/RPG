import pygame
from settings import *

class Matrix():
    def __init__(self, window_width, window_height, tile_size):
        self.window_width = window_width
        self.window_height = window_height
        self.tile_size = tile_size
        self.tile_x_amount = int(window_width / tile_size)
        self.tile_y_amount = int(window_height / tile_size)

    def get_coord(self, tile_pos):
        return (self.tile_size * tile_pos[0], self.tile_size * tile_pos[1])

    def get_tile_pos(self, coord_pos):
        cur_x = 0
        cur_y = 0

        for y in range(self.tile_y_amount):
            if y*self.tile_size == coord_pos[1]:
                cur_y = y

        for x in range(self.tile_x_amount):
            if x * self.tile_size == coord_pos[0]:
                cur_x = x

        if cur_y != 0 or cur_x != 0:
            return cur_x, cur_y

        for x in range(self.tile_x_amount):
            if (coord_pos[0] < x * self.tile_size):
                break
            else:
                cur_x = x
        for y in range(self.tile_y_amount):
            if (coord_pos[1] < y * self.tile_size):
                break
            else:
                cur_y = y
        return (cur_x, cur_y)

    def draw(self, window):
        for x in range(self.tile_x_amount):
            pygame.draw.line(window, (0, 0, 0), (x * self.tile_size, 0), (x * self.tile_size, self.window_height))

        for y in range(self.tile_y_amount):
            pygame.draw.line(window, (0, 0, 0), (0, y * self.tile_size), (self.window_width, y * self.tile_size))

    def position_reset(self, coord_pos):
        return self.get_coord(self.get_tile_pos(coord_pos))

    def debug(self, window, camera):
        for y in range(self.tile_y_amount):
            pygame.draw.line(window, green, camera.apply_coord(0, self.tile_size*y), camera.apply_coord(self.window_height, self.tile_size*y))
        for x in range(self.tile_x_amount):
            pygame.draw.line(window, green, camera.apply_coord(self.tile_size*x, 0), camera.apply_coord(self.tile_size*x, self.window_width))

