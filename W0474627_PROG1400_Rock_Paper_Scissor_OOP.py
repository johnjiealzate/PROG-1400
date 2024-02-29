import random
option_list = ["rock", "paper", "scissor"]

# Step 1: Define the base class
class Player:
    def __init__(self, name):
        self.name = name
    
    def choose_move(self):
        pass

# Step 2: Create derived class (human player) that imherits from the base class (Player)
class HumanPlayer(Player):
    def choose_move(self):
        move  = input(f"{self.name} Please eneter  you move (rock, paper, scisssor):").lower()
        while move not in ["rock", "paper", "scissor"]:
            print ("Invalid move.")
            move  = input(f"{self.name} Please enter  you move (rock, paper, scisssor):").lower()
        return move
    
# Step 3: Create another derived class (ComputerPlayer) that also inherits from the base class (Playear)
class ComputerPlayear(Player):
    def choose_move(self):
        return random.choice(option_list)
    
# Step 4: Craet a game class to manage the gameplay
class RockPaeperScissorGame:
    # Create the characters
    def __init__(self):
        self.player1 = HumanPlayer("Player 1")
        self.player2 = ComputerPlayear("Computer")
    def determine_winner(self, move1, move2):
        if move1 == move2:
            print
            return "It's a tie."
        elif (move1 == "rock" and move2 == "sciccor") or \
             (move1 == "scissor" and move2 == "paper") or \
             (move1 == "paper" and move2 == "rock"):
            return f"{self.player1.name} wins."
        else:
            return f"{self.player2.name} wins."
    def play_game(self):
        # Intro
        print ("Welcome to Rock Paper Scissor Game!")
        # Call the choose move  method on Player 1 and 2
        move1 = self.player1.choose_move()
        move2 = self.player2.choose_move()
        # Inform the player the moves
        print (f"{self.player1.name} chose {move1}")
        print (f"{self.player2.name} chose {move2}")

        result = self.determine_winner(move1, move2)
        print (result)

# Step 5: Instantiate the Game class and play athe game
if __name__ == "__main__":
    game = RockPaeperScissorGame()
    game.play_game()