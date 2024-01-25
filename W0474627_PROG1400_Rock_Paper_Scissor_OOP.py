import random

# Step 1: Define the base class
class Player:
    def __init__(self, name):
        self.name = name
    
    def choose_move(self):
        pass

# Step 2: Createaa derived class (human player) that imherits from the base class (Player)
class HumanPlayer(Player):
    def choose_move(self):
        move  = input(f"{self.name} Please eneter  you move (rock, paper, scisssor):").lower()
        while move not in ["rock", "paper", "scissor"]:
            print ("Invalid move.")
            move  = input(f"{self.name} Please eneter  you move (rock, paper, scisssor):").lower()
        return move
    
class ComputerPlayear(Player):
    def choose_move(self):
        return random.choice(["rock", "paper", "scissor"])