import pygame
import random

from reel import Reel
from player import Player
from settings import *
from creditor import Creditor

class Machine:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.reel_index = 0
        self.reel_list = {}
        self.can_toggle = True
        self.spinning = False
        self.win_animation_ongoing = False
        
        # Results
        self.prev_result = {0: None, 1: None, 2: None}
        self.spin_result = {0: None, 1: None, 2: None}

        # load mask images
        self.top_mask =   pygame.image.load(TOP_MASK).convert_alpha()
        self.bottom_mask = pygame.image.load(BOTTOM_MASK).convert_alpha()

        self.spawn_reels()

        # configure pot and player
        self.creditor = Creditor()

        self.currPlayer = Player()

    def cooldowns(self):
        # Only lets player spin if all reels are NOT spinning
        for reel in self.reel_list:
            if self.reel_list[reel].reel_is_spinning:
                self.can_toggle = False
                self.spinning = True

        if not self.can_toggle and [self.reel_list[reel].reel_is_spinning for reel in self.reel_list].count(False) == 3:
            
            # Results
            results = list(self.get_result().values())
            win = all(x == results[0] for x in results)
            print(results[0]) if win else print(False)
            self.can_toggle = True

            if win:
                # Play the win sound
                # self.play_win_sound(self.win_data)
                self.pay_player(win, self.currPlayer)
                print(self.currPlayer.get_data())
                self.creditor.set_win_condition()
                # self.win_animation_ongoing = True
                # self.ui.win_text_angle = random.randint(-4, 4)

    def handle_player(self):
        self.currPlayer.can_spin = self.creditor.check_credit()
        self.currPlayer.credit_spins = self.creditor.credits * CREDIT_VALUE_SPINS
        self.currPlayer.balance = self.currPlayer.credit_spins - self.currPlayer.debit_spins

        print(self.currPlayer.balance)

    def input(self):
        keys = pygame.key.get_pressed()

        # checks for space key, ability to togggle spin, and balance to cover bet
        #if keys[pygame.K_SPACE] and self.can_toggle and self.currPlayer.balance >= self.currPlayer.bet_size:
        if keys[pygame.K_SPACE]:
            self.toggle_spinning()
            self.spin_time = pygame.time.get_ticks()
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
        if self.can_toggle and self.currPlayer.balance > 0 and self.currPlayer.can_spin:
            self.spin_time = pygame.time.get_ticks()
            self.spinning = not self.spinning
            self.can_toggle = False

            self.currPlayer.place_bet()
            for reel in self.reel_list:
                self.reel_list[reel].start_spin(int(reel) * 200)
                # self.spin_sound.play()

    def get_result(self):
        for reel in self.reel_list:
            self.spin_result[reel] = self.reel_list[reel].reel_spin_result()
        return self.spin_result
    
    def pay_player(self, win_data, curr_player):
        # This will refernce the creditor
        pass

    def update(self, delta_time, screen):
        if not self.creditor.check_device_status:
            return
        self.cooldowns()
        self.handle_player()
        self.input()
        self.draw_reels(delta_time)
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            screen.blit(self.top_mask, (0,0))
            screen.blit(self.bottom_mask, (0,0))
            self.reel_list[reel].symbol_list.update()

        # debug_player_data = self.currPlayer.get_data()
        # machine_balance = 