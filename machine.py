import pygame

from reel import Reel
from settings import *

class Machine:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.reel_index = 0
        self.reel_list = {}
        self.can_toggle = True
        self.spinning = False

        # load mask images

        self.top_mask =   pygame.image.load(TOP_MASK).convert_alpha()
        self.bottom_mask = pygame.image.load(BOTTOM_MASK).convert_alpha()

        self.spawn_reels()

    def cooldowns(self):
        # Only lets player spin if all reels are NOT spinning
        for reel in self.reel_list:
            if self.reel_list[reel].reel_is_spinning:
                self.can_toggle = False
                self.spinning = True

        if not self.can_toggle and [self.reel_list[reel].reel_is_spinning for reel in self.reel_list].count(False) == 3:
            self.can_toggle = True


    def input(self):
        keys = pygame.key.get_pressed()

        # checks for space key, ability to togggle spin, and balance to cover bet
        #if keys[pygame.K_SPACE] and self.can_toggle and self.currPlayer.balance >= self.currPlayer.bet_size:
        if keys[pygame.K_SPACE]:
            self.toggle_spinning()
            self.spin_time = pygame.time.get_ticks()
            # self.currPlaer.place_bet()
            # self.machine_balance += self.currPlayer.bet_size()
            # self.currPlayer.last_payout = None

    def draw_reels(self, delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].animate(delta_time)
 
    def spawn_reels(self):
        if not self.reel_list:
            x_topleft, y_topleft = 470, 100
        while self.reel_index < 3:
            if self.reel_index > 0:
                x_topleft, y_topleft = x_topleft + (260 + X_OFFSET), y_topleft

            self.reel_list[self.reel_index] = Reel((x_topleft, y_topleft))
            self.reel_index += 1

    def toggle_spinning(self):
        if self.can_toggle:
            self.spin_time = pygame.time.get_ticks()
            self.spinning = not self.spinning
            self.can_toggle = False

            for reel in self.reel_list:
                self.reel_list[reel].start_spin(int(reel) * 200)
                # self.spin_sound.play()

    def update(self, delta_time, screen):
        self.cooldowns()
        self.input()
        self.draw_reels(delta_time)
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            screen.blit(self.top_mask, (0,0))
            screen.blit(self.bottom_mask, (0,0))
            self.reel_list[reel].symbol_list.update()