import pygame

from reel import Reel
from settings import *

class Machine:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.reel_index = 0
        self.reel_list = {}

        self.spawn_reels()

    def spawn_reels(self):
        if not self.reel_list:
            x_topleft, y_topleft = 470, 100
        while self.reel_index < 3:
            if self.reel_index > 0:
                x_topleft, y_topleft = x_topleft + (260 + X_OFFSET), y_topleft

            self.reel_list[self.reel_index] = Reel((x_topleft, y_topleft))
            self.reel_index += 1

    def update(self, delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            self.reel_list[reel].symbol_list.update()