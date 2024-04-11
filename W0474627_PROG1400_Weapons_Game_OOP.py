import random

# Step 1: Create a class to represent weapons available in the game
class Weapon:
    # Include attributes for the weapon's name, damage, and ammo capacity
    def __init__(self, name, damage, ammo_capacity):
        self.name = name
        self.damage = damage
        self.ammo_capacity = ammo_capacity
        # Local variable to account for the ammo_remaining
        self.ammo_remaining = ammo_capacity

    def shoot(self):
        if self.ammo_remaining > 0:
            print (f"{self.name} fire! -{self.damage}")
        else:
            print("Out of Ammo")

# Step 2: Define a class representing a player in the game
class Player:
    # Include attributes for the player's name, health, and equipped weapon.
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = None

    def take_damage(self, damage):
        self.health -= damage
        print (f"{self.name} took {damage}. Current health: {self.health}")

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equipped with {weapon.name}")

    def shoot(self):
        if self.weapon:
            self.weapon.shoot()
        else:
            print (f"{self.name} has no weapon!")

#Step 3: Develop a class to manage the gameplay, including rounds of combat between players
class FirstPersonShooterGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        print("New round!")
        self.player1.shoot()
        self.player2.take_damage(self.player1.weapon.damage)

        self.player2.shoot()
        self.player1.take_damage(self.player2.weapon.damage)

# Step 4: Instantiate the Game class and play the game
if __name__ == "__main__":
    # Create weapons
    assault_riffle = Weapon("Assault Riffle", damage=10, ammo_capacity=30)
    shotgun = Weapon("Shotgun", damage=20, ammo_capacity=8)

    # Create players
    player1 = Player("Player1", health=100)
    player2 = Player("Player2", health=100)

    # Equip weapons
    player1.equip_weapon(assault_riffle) 
    player2.equip_weapon(shotgun)

    # Create the game
    fps_game = FirstPersonShooterGame(player1, player2)

    # Play a round
    fps_game.play_round()