from robots import Robots
import weapons

class Fleet:
    def __init__(self):
        self.fleet_list = []
        self.create_fleet()
        
    def create_fleet(self):
        robot_one = Robots("lamo", 100, weapons)
        robot_two = Robots("amol", 100, weapons)
        robot_three = Robots("lmao", 100, weapons)
        
        self.fleet_list.append(robot_one)
        self.fleet_list.append(robot_two)
        self.fleet_list.append(robot_three)


