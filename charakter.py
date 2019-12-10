import pygame
from sprite import *
class Charakter(pygame.sprite.Sprite):
    def __init__(self, dialogArray, name, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.dialog = Dialog(dialogArray)
        self.rect = pygame.Rect(x, y, width, height)
        self.name = name

    def load_img(self, sprite):
        self.sprite = sprite

class Dialog:
    def __init__(self, dialogArray):
        self.dialog_array = dialogArray
        self.dialog_pos = 0

    def has_dialog(self):
        return self.dialog_pos < len(self.dialog_array)

    def get_next_dialog(self):
        if self.has_dialog():
            dialog = self.dialog_array[self.dialog_pos]
            self.dialog_pos = self.dialog_pos+1
            return dialog
        else:
            return -1


allCharakter = pygame.sprite.Group()

def parse_charakter(array):
    return Charakter(array['m'], array['name'], array['rect'][0], array['rect'][1], array['rect'][2], array['rect'][3])

def get_colliding_charakter(player):
    hits = pygame.sprite.spritecollide(player, allCharakter, False)
    if hits:
        return hits[0]
    else:
        return False


mann = {
    "name": "Mann",
    "m": ["Hey", "Wie gehts"],
    "rect": [350, 300, 50, 50]
}
