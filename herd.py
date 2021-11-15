from dinosaur import Dinosaurs

class Herd:
    def __init__(self):
        self.dinosaur_herd = []
        self.create_herd()
        
    def create_herd(self):
            dino_one = Dinosaurs("oll", 50, 100)
            dino_two = Dinosaurs("llo", 50, 100)
            dino_three = Dinosaurs("lol", 50, 100)
            
            self.dinosaur_herd(dino_one)
            self.dinosaur_herd(dino_two)
            self.dinosaur_herd(dino_three)