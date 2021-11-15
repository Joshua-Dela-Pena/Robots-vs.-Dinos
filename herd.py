from dinosaur import Dinosaurs




class Herd: 
    def __init__(self):
        self.dinosaur_herd = [] 
        self.create_herd()
    def create_herd(self):
        dinosaur_one = Dinosaurs("oll", 50, 500)
        dinosaur_two = Dinosaurs("llo", 50, 500)
        dinosaur_three = Dinosaurs("lol", 50, 500)

        self.dinosaur_herd.append(dinosaur_one)
        self.dinosaur_herd.append(dinosaur_two)
        self.dinosaur_herd.append(dinosaur_three)

    
   