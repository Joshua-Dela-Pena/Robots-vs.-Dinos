from robots import Robots
import weapons

class Fleet:
    def __init__(self):
        self.fleet_list = []
        self.create_fleet()
        
    def create_fleet(self):
        robo_one = Robots("lamo", 100, weapons)
        robo_two = Robots("amol", 100, weapons)
        robo_three = Robots("lmao", 100, weapons)
        
        self.fleet_list.append(robo_one)
        self.fleet_list.append(robo_two)
        self.fleet_list.append(robo_three)