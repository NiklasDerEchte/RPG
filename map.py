import pygame
import pytmx
from settings import *

class TileMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))

    def make_map(self):
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

class Camera:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, target):
        x = -target.rect.centerx + int(WINDOW_WIDTH / 2)
        y = -target.rect.centery + int(WINDOW_HEIGHT / 2)

        if target.rect.centery + int(WINDOW_HEIGHT / 2) >= MAX_HEIGHT:
            y = self.rect.y
        if target.rect.centery - int(WINDOW_HEIGHT / 2) <= 0:
            y = self.rect.y
        if target.rect.centerx + int(WINDOW_WIDTH / 2) >= MAX_WIDTH:
            x = self.rect.x
        if target.rect.centerx - int(WINDOW_WIDTH / 2) <= 0:
            x = self.rect.x

        self.rect.x, self.rect.y = x, y

    def apply(self, rect):
        return rect.move(self.rect.topleft)

    def apply_coord(self, x, y):
        rect = pygame.Rect(x, y, 0, 0)
        rect = self.apply(rect)
        return (rect.x, rect.y)