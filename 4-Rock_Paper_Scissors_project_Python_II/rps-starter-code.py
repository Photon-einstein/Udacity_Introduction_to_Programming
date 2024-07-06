#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self):
        self.movements = ['rock', 'paper', 'scissors']
        self.last_opponent_move = ""

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.last_opponent_move = their_move


class RandomPlayer(Player):

    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(self.movements)


class HumanPlayer(Player):

    def move(self):
        while True:
            move = input("Rock, Paper or Scissors?\n")
            if move.lower() not in self.movements:
                print("Please type in Rock, Paper or Scissors.")
            else:
                return move.lower()


class ReflectPlayer(Player):

    def move(self):
        if self.last_opponent_move not in self.movements:
            return random.choice(self.movements)
        else:
            return self.last_opponent_move


class CyclePlayer(Player):

    def __init__(self):
        super().__init__()
        self.next_move_index = 0

    def move(self):
        next_move = self.movements[self.next_move_index]
        self.next_move_index = (self.next_move_index+1) % len(self.movements)
        return next_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0
        self.number_of_games = 5

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        # update score
        if beats(move1, move2) is True:
            self.score_p1 = self.score_p1 + 1
        if beats(move2, move1) is True:
            self.score_p2 = self.score_p2 + 1

    def play_game(self):
        print("Game start!")
        for round in range(self.number_of_games):
            print(f"Round {round+1}:")
            self.play_round()
            print(f"""Score end of Round {round+1} |
                  Player 1: {self.score_p1} W
                  Player 2: {self.score_p2} W\n""")
        self.print_final_score()
        print("Game over!")

    def print_final_score(self):
        print(f"""Final score |
              Player 1: {self.score_p1} W
              Player 2: {self.score_p2} W\n""")
        if self.score_p1 > self.score_p2:
            print("Player 1 won!")
        elif self.score_p1 < self.score_p2:
            print("Player 2 won!")
        else:
            print("Draw!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
