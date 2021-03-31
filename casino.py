#!/usr/bin/env python3.9
# -*- coding:utf-8 -*-
from random import randint
from os import system
from os.path import isfile
from pickle import Pickler, Unpickler


class RouletteGame:

    def __init__(self):
        # Lecture de la base de données
        want_load_data = input("Voulez-vous continuer la partie précédente ? (O/n) ")
        if want_load_data == 'O' or want_load_data == 'o':
            data = self.read_data()
        else:
            data = None

        # Définition des attributs de classe
        if data == None:
            self.pot = 1000
            self.random_number = 0
            self.choice_number = 0
            self.bet_value = 0
            self.winnings = 0
        else:
            self.pot = data["pot"]
            self.random_number = data["random_number"]
            self.choice_number = data["choice_number"]
            self.bet_value = data["bet_value"]
            self.winnings = data["winnings"]

        # Nettoyage de l'écran
        system('clear')

        # Initialisation de l'interface
        print("Jeu de la Roulette")
        print(f"Vous disposez de {self.pot} euros pour jouer.")
        print("Bonne chance!\n")

        # Demander à l'utilisateur d'afficher l'aide
        want_help = input("Voulez-vous afficher l'aide ? (O/n) ")
        if want_help == 'O' or want_help == 'o':
            self.help()

    def read_data(self):
        """
        Permet de lire la base de données data.dat, si elle existe.
        """
        if isfile("./data.dat"):
            with open("./data.dat", 'rb') as data_file:
                data_pickle = Unpickler(data_file)
                data = data_pickle.load()
            return data
        else:
            return None

    def save_data(self):
        """
        Sauvegarde les données à la fin de la partie.
        """
        data = {
            "pot": self.pot,
            "random_number": self.random_number,
            "choice_number": self.choice_number,
            "bet_value": self.bet_value,
            "winnings": self.winnings
        }
        with open("./data.dat", 'wb') as data_file:
            data_pickle = Pickler(data_file)
            data_pickle.dump(data)

    def help(self):
        print("\n==========> JEU DE LA ROULETTE <==========")
        print("Ce programme est une implémentation simplifiée du jeu de la roulette.")
        print("Vous disposez d'une cagnote de 1000 euros en début de partie.")
        print("À chaque tour, vous devrez :")
        print("\t- Choisir un nombre entre 0 et 49")
        print("\t- Miser la somme de votre choix")
        print("Une fois la roulette lancé :")
        print("\t- Si votre nombre est le nombre tiré, vous remportez 3 fois la mise.")
        print("\t- Si votre nombre est de la même couleur que le nombre tiré, vous remportez la moitié de la mise.")
        print("\t- Sinon vous perdez votre mise.")
        print("Vous pouvez jouer autant de fois que vous voulez.")
        print("=========================================\n")

    def spin_roulette(self):
        """
        Simulation d'un lancement de roulette.
        Cette fonction affecte un nombre aléatoire entre 0 et 49 à la
        variable self.random_number.
        """
        self.random_number = randint(0, 49)

    def select_a_number(self):
        """
        Fonction qui permet de demander un nombre à l'utilisateur.
        La boucle while effectue les vérifications nécessaires, en
        particulier que la valeur saisie est bien un entier compris
        entre 0 et 49.
        """
        bad_value = True
        while bad_value:
            self.choice_number = input("Choisir un nombre entre 0 et 49 : ")
            try:
                self.choice_number = int(self.choice_number)
                if self.choice_number not in range(50):
                    bad_value = True
                    print("Attention - Vous devez choisir un nombre entre 0 et 49.")
                else:
                    bad_value = False
            except ValueError as err:
                bad_value = True
                print("Attention - Vous devez choisir un nombre entier.")
                print("Error description: " + str(err))

    def bet(self):
        """
        Fonction qui permet de demander la mise de l'utilisateur.
        La boucle while effectue les vérifications nécessaires, en
        particulier que la valeur saisie est bien un entier supérieur
        à 10.
        """
        bad_value = True
        while bad_value:
            self.bet_value = input("Votre mise : ")
            try:
                self.bet_value = int(self.bet_value)
                if self.bet_value < 10:
                    bad_value = True
                    print("Attention - Vous devez miser au moins 10 euros.")
                else:
                    bad_value = False
            except ValueError as err:
                bad_value = True
                print("Attention - Vous devez choisir un nombre entier.")
                print("Error description: " + str(err))

    def resolve_game(self):
        """
        Résolution du tour.
        Permet de définir les gains de l'utilisateur pour chaque
        tour.
        """
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
        """
        Remise à 0 des attributs de classe.
        """
        self.random_number = 0
        self.choice_number = 0
        self.bet_value = 0
        self.winnings = 0

    def finish(self):
        """
        Affiche les gains de l'utilisateur à la fin de la partie.
        """
        if self.pot > 1000:
            print(f"Bien joué! Vous avez gagné {self.pot} euro(s).")
        elif self.pot > 0:
            print(f"Pas de chance! Vous avez perdu {1000-self.pot} euro(s).")
        else:
            print(f"Pas de chance! Vous devez {abs(self.pot)} euro(s).")

    def play(self):
        """
        Boucle principale du jeu.
        """
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

            system('clear')

        want_save = input("Voulez-vous sauvegarder les données de cette partie ? (O/n) ")
        if want_save == 'O' or want_save == 'o':
            self.save_data()
        else:
            self.finish()


if __name__ == "__main__":
    game = RouletteGame()
    game.play()
        
