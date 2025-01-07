from settings import *

class Player():
    def __init__(self):
        self.balance = 0
        self.bet_size = 1
        self.can_spin = False
        self.credit_spins = 0
        self.debit_spins = 0

    def get_data(self):
        player_data = {}
        player_data['balance'] = str(int(self.balance))
        player_data['spins'] = str(int(self.credit_spins - self.debit_spins))
        player_data['can_spin'] = str(self.can_spin)
        return player_data
    
    def place_bet(self):
        self.debit_spins += 1
        
    def jackpot_reset(self):
        self.balance = 0
        self.credit_spins = 0
        self.debit_spins = 0