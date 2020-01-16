import pygame
from settings import *
class Matrix:

    def __init__(self, window_width, window_height, block_size):
        self.window_width = window_width
        self.window_height = window_height
        self.block_size = block_size
        self.x_amount = int (window_width / block_size)
        self.y_amount = int (window_height / block_size)

    def debug(self, window, camera):
        for y in range(self.y_amount):
            pygame.draw.line(window, green, camera.apply_coord(0, self.block_size*y), camera.apply_coord(self.window_height, self.block_size*y))
        for x in range(self.x_amount):
            pygame.draw.line(window, green, camera.apply_coord(self.block_size*x, 0), camera.apply_coord(self.block_size*x, self.window_width))

    def get_coord(self, x, y):
        x_pos = 0
        y_pos = 0
        if(x < self.x_amount):
            x_pos = self.block_size * x
        if(y < self.y_amount):
            y_pos = self.block_size * y
        return (x_pos, y_pos)

    def get_tile_position(self, cur_x, cur_y):
        x_pos = 0
        y_pos = 0
        for y in range(self.y_amount):
            if(cur_y < y*self.block_size):
                break
            else:
                y_pos = y
        for x in range(self.x_amount):
            if(cur_x < x*self.block_size):
                break
            else:
                x_pos = x
        return (x_pos, y_pos)

    def position_reset(self, x, y):
        x,y = self.get_tile_position(x,y)
        return self.get_coord(x,y)