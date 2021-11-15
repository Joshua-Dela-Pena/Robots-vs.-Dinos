from dinosaur import Dinosaurs

class Herd:
    def __init__(self):
        self.dinosaur_herd = []
        self.create_herd()
        
    def create_herd(self):
            dinosaur_one = Dinosaurs("oll", 50, 100)
            dinosaur_two = Dinosaurs("llo", 50, 100)
            dinosaur_three = Dinosaurs("lol", 50, 100)
            
            self.dinosaur_herd(dinosaur_one)
            self.dinosaur_herd(dinosaur_two)
            self.dinosaur_herd(dinosaur_three)