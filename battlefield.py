from fleet import Fleet
from herd import Herd
from dinosaur import Dinosaurs
from robots import Robots
from weapons import Weapons

# Steps before the last user story 
# 1. Pass in dinosaur and robots.
# 2. Call/create fleet and herd functions.
# 3. When it's the dinosaurs turn make it deal damage to set hp for robots.
# 4. when it's the robots turn make it deal damage to set hp for dinosaurs.
# 5. Repeat 3 and 4 until all robots or dinosaurs have been defeated by either side.
# 6. Display who won the battle!
# 7. Give the user a choice to play again or not.

class Battlefield:


    def __init__(self):
            self.dino_herd = Herd()
            self.robo_fleet = Fleet()
            
            
            
    
    def run_game(self):
        self.display_welcome()
        self.start = input("Would you like to start the game? ").lower()
        if self.start == 'yes':
            self.battle()
        else:
            self.start == 'no'
            pass
            
        

    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs! The rules are simple, beat every oponent to win the battle. Enjoy!")

    def battle(self):
        # 
        loop = True
        selected_dinosaur = self.dino_herd.dinosaur_herd[0]    
        selected_robot = self.robo_fleet.fleet_list[0]
        while loop == True:
                if len(self.robo_fleet.fleet_list) == 0 or len(self.dino_herd.dinosaur_herd) == 0:
                        loop = False
                        break
                
                self.dino_turn(selected_dinosaur)
                if len(self.robo_fleet.fleet_list) == 0 or len(self.dino_herd.dinosaur_herd) == 0:
                        loop = False
                        break
                
                self.robo_turn(selected_robot)
        self.display_winners()

    def dino_turn(self, dinosaur):
        # Which dino is going to attack ? - get passed in
         # Which Robo will it attack ?
        defending_robo = self.show_dino_opponent_options()
        # Using the selected dino . attack it passing the robo as an argument.
        dinosaur.attack(defending_robo)
        # Check for health - Is he dead?
        print(f"{defending_robo.name}'s remaining health: {defending_robo.health}")
        if self.robo_fleet.fleet_list[0].health <= 0:
                self.robo_fleet.fleet_list.pop(0)

                
    def robo_turn(self, robot):
        
        defending_dino = self.show_robo_opponent_options()
        robot.attack(defending_dino)
        print(f"{defending_dino.name}'s remaining health: {defending_dino.health}")
        if self.dino_herd.dinosaur_herd[0].health <= 0:
                self.dino_herd.dinosaur_herd.pop(0)

    def show_dino_opponent_options(self):
        # List available dinos for attack/hit
        for robo in self.robo_fleet.fleet_list:
                print(f'Here are your robots: {robo.name}')
        # Choose one and return it
        user_input = int(input("Would you like to attack robo: 1, 2, or 3? "))
        if user_input == 1:
                return self.robo_fleet.fleet_list[0]

        elif user_input == 2:
                return self.robo_fleet.fleet_list[1]

        elif user_input == 3:
                return self.robo_fleet.fleet_list[2]


    def show_robo_opponent_options(self):
        for dino in self.dino_herd.dinosaur_herd:
                print(f'Here are your dinos: {dino.name}')

        user_input = int(input("Would you like to attack dino: 1, 2, or 3? "))
        if user_input == 1:
                return self.dino_herd.dinosaur_herd[0]

        elif user_input == 2:
                return self.dino_herd.dinosaur_herd[1]

        elif user_input == 3:
                return self.dino_herd.dinosaur_herd[2]


    def display_winners(self):
            
        if len(self.robo_fleet.fleet_list) == 0:
                print("Battles over! The Dinosaurs win the match!")

        elif len(self.dino_herd.dinosaur_herd) == 0:
                print("Battles over! The Robots win the match!")


def str(self):
        return self.name