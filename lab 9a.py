#Surya Hardiansyah

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']

#p1 = input('Pick one of rock, paper or scissors: ')
#p2 = random.choice(choices)

import random

class RockPaperScissors:
    def __init__(self, human_players=1):
        self.choices = ['rock', 'paper', 'scissors']
        self.beats = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
        self.score = [0, 0]  # [P1, P2]
        self.loss = [0, 0]
        self.rounds = 1
        self.human_players = human_players
    
    def get_player_choice(self):
        while True:
            choice = input('Pick one of rock, paper, or scissors: ').lower()
            if choice in self.choices:
                return choice
            print("Invalid choice. Please choose again.")
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def decide_winner(self, p1, p2):
        if p1 == p2:
            self.rounds += 1
            return "It's a tie!"
        elif self.beats[p1] == p2:
            self.rounds += 1
            self.score[0] += 1
            self.loss[1] += 1
            return "P1 wins!"
        else:
            self.rounds += 1
            self.score[1] += 1
            self.loss[0] += 1
            return "P2 wins!"
    
    def final_result(self):
        if self.score[0] > self.score[1]:
            return "P1 is the overall winner!"
        elif self.score[0] < self.score[1]:
            return "P2 is the overall winner!"
        else:
            return "It's a tie overall!"
    
    def final_score(self):
        self.tie = self.rounds-1 - sum(self.score)
        print(f"\nRounds played: {self.rounds-1}")
        print(f"P1: {self.score[0]} wins, {self.loss[0]} losses, and {self.tie} ties.")
        print(f"P2: {self.score[1]} wins, {self.loss[1]} losses, and {self.tie} ties.")        
        print(f"{self.final_result()}")
    
    def play_round(self):
        if self.human_players == 2:
            p1 = self.get_player_choice()
            p2 = self.get_player_choice()
        elif self.human_players == 1:
            p1 = self.get_player_choice()
            p2 = self.get_computer_choice()
        else:
            p1 = self.get_computer_choice()
            p2 = self.get_computer_choice()
        print(f"\nRound {self.rounds}!")
        print(f"\nP1: {p1}\nP2: {p2}")
        print(self.decide_winner(p1, p2))
    
    def play(self):
        while True:
            self.play_round()
            rematch = input('Enter Y to play again: ').lower()
            if rematch != 'y':
                self.final_score()
                break
        
print("Welcome to Rock-Paper-Scissors Game!")
human_players = int(input("Enter the number of human players (0, 1, or 2): "))
if human_players not in [0, 1, 2]:
    print("Invalid number of players. Defaulting to 1 human player.")
    human_players = 1
game = RockPaperScissors(human_players)
game.play()
