import random

# Step 1: Define the Weapon class
class Weapon:
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

# Step 2: Define the Player class
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = None

    def take_damage(self):
        self.health -= damage

    def equip_weapon(self, weapon):
        pass

    def shoot(self):
        pass

