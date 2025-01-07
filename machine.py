import pygame
import random
import time

import usb.core

from reel import Reel
from player import Player
from settings import *
from creditor import Creditor
from messages import Messages
from joystick import Joystick



class Machine:
    def __init__(self, starting_pot):
        self.display_surface = pygame.display.get_surface()
        self.reel_index = 0
        self.reel_list = {}
        self.can_toggle = True
        self.spinning = False
        self.win_reset = False

        # init joystick
        self.joystick = Joystick()
        
        # Results
        self.prev_result = {0: None, 1: None, 2: None}
        self.spin_result = {0: None, 1: None, 2: None}

        # load mask images
        self.top_mask =   pygame.image.load(TOP_MASK).convert_alpha()
        self.bottom_mask = pygame.image.load(BOTTOM_MASK).convert_alpha()
        self.spawn_reels()

        # configure pot and player
        self.creditor = Creditor(starting_pot)

        self.currPlayer = Player()

        self.message_handler = Messages()

    def cooldowns(self):
        # Only lets player spin if all reels are NOT spinning
        for reel in self.reel_list:
            if self.reel_list[reel].reel_is_spinning:
                self.can_toggle = False
                self.spinning = True

        if not self.can_toggle and [self.reel_list[reel].reel_is_spinning for reel in self.reel_list].count(False) == 3:
            self.can_toggle = True

    def check_win(self):
        # Only lets player spin if all reels are NOT spinning
        for reel in self.reel_list:
            if self.reel_list[reel].reel_is_spinning:
                self.can_toggle = False
                self.spinning = True

        if not self.can_toggle and [self.reel_list[reel].reel_is_spinning for reel in self.reel_list].count(False) == 3:
            # self.can_toggle = True
        
            # Results
            results = list(self.get_result().values())
            win = all(x == results[0] for x in results)

            if win:
                win_type = results[0].split('/')[-1]
                time.sleep(1)
                if win_type in ['skis','seven']:
                    self.message_handler.display_jackpot()
                if win_type in ['chicken']:
                    self.message_handler.display_chicken()
                if win_type in ['chance']:
                    self.message_handler.display_chance()
                if win_type in ['beer']:
                    self.message_handler.display_beer()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE] or self.joystick.check_joystick_pull_back():
                    self.message_handler.sound_playing = False
                    if win_type in ['skis','seven']:
                        self.creditor.jackpot_reset()
                    self.currPlayer.jackpot_reset()
                    self.win_reset = True
                    self.can_toggle = True
                    return False

                return True
            else:
                return False

    def handle_player(self):
        self.currPlayer.can_spin = self.creditor.check_credit()
        self.currPlayer.credit_spins = self.creditor.credits * CREDIT_VALUE_SPINS
        self.currPlayer.balance = self.currPlayer.credit_spins - self.currPlayer.debit_spins

    def input(self):
        keys = pygame.key.get_pressed()

        # checks for space key, ability to togggle spin, and balance to cover bet
        #if keys[pygame.K_SPACE] and self.can_toggle and self.currPlayer.balance >= self.currPlayer.bet_size:
        if keys[pygame.K_SPACE] or self.joystick.check_joystick_pull_back():
            self.toggle_spinning()
            self.spin_time = pygame.time.get_ticks()
            self.win_reset = False

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
        try:
            # Win condition
            if self.check_win() == True and not self.win_reset:
                return
            
            # Play
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

            self.message_handler.check_creditor(creditor=self.creditor)
            if self.creditor.device_status == False:
                self.message_handler.display_scale_error()

            debug_player_data = self.currPlayer.get_data()
            self.message_handler.display_spin_count(f"Spins Remaining: {debug_player_data['spins']} | Estimated Pot: {self.creditor.ref_chips}")
            
        # Handle Auto-Shutoff from Scale
        except usb.core.USBError as e:
            self.message_handler.display_scale_error()