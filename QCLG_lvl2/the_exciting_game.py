from random import randint

import numpy as np
from qiskit import execute, BasicAer
from qiskit.circuit.quantumcircuit import QuantumCircuit


class Game:

    @classmethod
    def run(cls, circuit: QuantumCircuit):
        # use local simulator
        backend = BasicAer.get_backend('qasm_simulator')
        results = execute(circuit, backend=backend, shots=1024).result()
        answer = results.get_counts()
        max_value = 0
        max_key = ""
        for key, value in answer.items():
            if value > max_value:
                max_value = value
                max_key = key
        print(answer)
        if max_key == "00":
            print("Both players stay grounded :(")
            return 0
        elif max_key == "01":
            print("Player 1 is excited!")
            return 1
        elif max_key == "10":
            print("Player 2 is excited!")
            return 2
        elif max_key == "11":
            print("Both players are excited!")
            return 3
        return

    @classmethod
    def place_gate(cls, player, field, qubit):
        card = player.pop()
        print(f"now inserting card {card} from player {qubit + 1}")
        if card == "H":
            field.h(qubit)
        elif card == "X":
            field.x(qubit)
        elif card == "RX":
            field.rx(np.pi / 2, qubit)
        elif card == "CX":
            if qubit == 0:
                field.cx(qubit, qubit + 1)
            else:
                field.cx(qubit, qubit - 1)
        return

    @classmethod
    def create_playing_field(cls, player1: list, player2: list) -> QuantumCircuit:
        field = QuantumCircuit(2, 2)
        player1.reverse()
        player2.reverse()
        while len(player1) > 0:
            cls.place_gate(player1, field, 0)
        while len(player2) > 0:
            cls.place_gate(player2, field, 1)
        field.measure(0, 0)
        field.measure(1, 1)
        return field

    @classmethod
    def generate_deck(cls) -> list:
        cards = ["H", "H", "X", "X", "CX", "RX", "RX"]
        deck = []
        for j in range(4):
            for i in range(len(cards)):
                deck.append(cards[i])
        return deck

    @classmethod
    def shuffle_deck(cls, deck: list):
        for i in range(len(deck) * 5):
            j = randint(0, len(deck) - 1)
            k = randint(0, len(deck) - 1)
            temp = deck[j]
            deck[j] = deck[k]
            deck[k] = temp
        return

    @classmethod
    def deal_starting_hands(cls, player1: list, player2: list, deck: list):
        for i in range(0, 4, 2):
            player1.append(deck.pop())
            player2.append(deck.pop())
        return

    @classmethod
    def draw_from_deck(cls, deck: list) -> str:
        return deck.pop()

    @classmethod
    def replace(cls, replacement_choice, card, player):
        player.remove(replacement_choice)
        player.append(card)
        return

    @classmethod
    def draw(cls, player: list, deck: list):
        card = cls.draw_from_deck(deck)
        print("Card drawn from deck is:" + card)
        user_choice = "?"
        while user_choice != "y" and user_choice != "n":
            user_choice = input("Do you want this card? (y/n)")
        if user_choice == "y":
            player.append(card)
        else:
            deck.insert(0, card)  # put the card on the bottom of the deck
        return

    @classmethod
    def fix_hand(cls, player: list) -> list:
        new_hand = []
        print("Your current hand is setup like this:")
        print(player)
        i = 0
        while len(player) > 0:
            replacement_choice = input(f"Choose one of your cards to be on position {i} :")
            while replacement_choice not in player:
                replacement_choice = input(f"Choose one of your cards to be on position {i} :")
            new_hand.insert(len(new_hand), replacement_choice)
            player.remove(replacement_choice)
            print("Cards remaining in previous hands")
            print(player)
            i = i + 1

        print("New hand")
        print(new_hand)
        print()
        return new_hand

    @classmethod
    def play_the_exciting_game(cls):
        deck = cls.generate_deck()
        cls.shuffle_deck(deck)
        player1 = []
        player1_wins = 0
        player2 = []
        player2_wins = 0
        rounds = int(input("Enter number of rounds: "))

        print("The exciting game begins!")
        current_round = 0
        while current_round <= rounds:
            countdown = 4
            print("#" * (current_round + 1), end="")
            print(f"ROUND {current_round}", end="")
            print("#" * (current_round + 1))
            print()
            cls.deal_starting_hands(player1, player2, deck)
            while countdown != 0:
                print("\nPlayer 1")
                print(player1)
                cls.draw(player1, deck)
                print("\nPlayer 2")
                print(player2)
                cls.draw(player2, deck)
                countdown = countdown - 1
                print(f"{countdown} dealings remain before the players have to see who's Excited!")
                if countdown == 0:
                    print("Next turn is going to be Exciting!!!")

            print("Both players get to fix their hands in the order they desire!")
            player1 = cls.fix_hand(player1)
            player2 = cls.fix_hand(player2)
            playing_field = cls.create_playing_field(player1, player2)
            print(playing_field.draw())
            round_result = cls.run(playing_field)
            if round_result == "1":
                player1_wins = player1_wins + 1
            elif round_result == "2":
                player2_wins = player2_wins + 1
            current_round = current_round + 1

        if player1_wins > player2_wins:
            print("PLAYER ONE WAS MOST EXCITED!")
        elif player2_wins > player1_wins:
            print("PLAYER TWO WAS MOST EXCITED!")
        else:
            print("PLAYERS WERE EQUALLY EXCITED!")
