#!/usr/bin/env python3.9
# -*- coding:utf-8 -*-
from random import randint


class RouletteGame:

    def __init__(self):
        self.random_number = 0
        self.choice_number = 0
        self.bet_value = 0
        self.winnings = 0

    def spin_roulette(self):
        self.random_number = randint(0, 49)

    def select_a_number(self):
        bad_value = True
        while bad_value:
            self.choice_number = input("Choisir un nombre entre 0 et 49 : ")
            try:
                self.choice_number = int(self.choice_number)
                bad_value = False
            except ValueError as err:
                bad_value = True
                print(err)

    def bet(self):
        bad_value = True
        while bad_value:
            self.bet_value = input("Votre mise : ")
            try:
                self.bet_value = int(self.bet_value)
                bad_value = False
            except ValueError as err:
                bad_value = True
                print(err)

    def resolve_game(self):
        if self.random_number == self.choice_number:
            self.winnings = self.bet_value + (self.bet_value * 3)
        elif self.random_number % 2 == self.choice_number % 2:
            self.winnings = self.bet_value + (self.bet_value / 2)
        else:
            self.winnings -= self.bet_value

        print(f"\nVous avez misé {self.bet_value} sur {self.choice_number}.")
        print(f"La roulette a donné le nombre {self.random_number}.")
        print(f"Vos gains sont donc: {self.winnings}.")
        print("Tour suivant...\n")

    def reset_game(self):
        self.random_number = 0
        self.choice_number = 0
        self.bet_value = 0
        self.winnings = 0

    def play(self):
        is_running = True
        while is_running:
            self.spin_roulette()
            self.select_a_number()
            self.bet()
            self.resolve_game()
            self.reset_game()

            check_if_running = input("Voulez-vous continuer ? (O/n) ")
            if check_if_running == 'O' or check_if_running == 'o':
                is_running = True
            else:
                is_running = False


game = RouletteGame()
game.play()
        
