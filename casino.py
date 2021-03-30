#!/usr/bin/env python3.9
# -*- coding:utf-8 -*-
from random import randint


class RouletteGame:

    def __init__(self):
        self.pot = 1000
        self.random_number = 0
        self.choice_number = 0
        self.bet_value = 0
        self.winnings = 0
        print("Jeu de la Roulette")
        print("Vous disposez de 1000 euros pour jouer.")
        print("Bonne chance!\n")
        want_help = input("Voulez-vous afficher l'aide ? (O/n) ")
        if want_help == 'O' or want_help == 'o':
            self.help()

    def help(self):
        print("\n==========> JEU DE LA ROULETTE <==========")
        print("Ce programme est une implémentation simplifiée du jeu de la roulette.")
        print("Vous disposez d'une cagnote de 1000 euros en début de partie.")
        print("À chaque tour, vous devrez :")
        print("\t- Choisir un nombre entre 0 et 49")
        print("\t- Miser la somme de votre choix")
        print("Une fois la roulette lancé :")
        print("\t- Si votre nombre est le nombre tiré, vous remportez 3 fois la mise.")
        print("\t- Si votre nombre est de la même couleur que le nombre tiré, vous remporté la moitié de la mise.")
        print("\t- Sinon vous perdez votre mise.")
        print("Vous pouvez jouer autant de fois que vous voulez.")
        print("=========================================\n")

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

        self.pot += self.winnings

        print(f"\nVous avez misé {self.bet_value} sur {self.choice_number}.")
        print(f"La roulette a donné le nombre {self.random_number}.")
        print(f"Vos gains sont donc: {self.winnings}.")
        print(f"Votre cagnote est actuellement de {self.pot}")
        print("Tour suivant...\n")

    def reset_game(self):
        self.random_number = 0
        self.choice_number = 0
        self.bet_value = 0
        self.winnings = 0

    def finish(self):
        if self.pot > 0:
            print(f"Bien joué! Vous avez gagné {self.pot} euro(s).")
        else:
            print(f"Pas de chance! Vous devez {self.pot} euro(s).")

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

        self.finish()


game = RouletteGame()
game.play()
        
