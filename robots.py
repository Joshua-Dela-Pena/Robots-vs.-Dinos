from weapons import Weapons
from dinosaur import Dinosaurs


class Robots:
    def __init__(self,name,health,weapon):
        self.name = name
        self.health = health
        self.weapon = Weapons()

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
        return dinosaur.health

    
