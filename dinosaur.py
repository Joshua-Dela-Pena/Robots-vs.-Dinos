import robots
import fleet

class Dinosaurs:
    def __init__(self, name, attack_power, health):
       self.name = name
       self.attack_power = attack_power
       self.health = 100

    def attack(self,robots):
        robots.health = robots.health - self.attack_power
        return robots.health

    def str(self):
        return self.name