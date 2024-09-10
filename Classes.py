class Animals():
    def __init__(self, type="Horse", name="Henry", number_of_feet=4):
        self.type = type
        self.name = name
        self.number_of_feet = number_of_feet
        self.number_of_eyes = 2

    def tail(self, tail):
        self.tail = tail
        
    def type_of_feet(self, feet="paws"):
        self.feet = feet
        
    def description(self):
        print(f"{self.name}, is a {self.type}, who has {self.number_of_feet} {self.feet}.")
        print(f"This animal has {self.number_of_eyes} eyes.\n")


george = Animals("Dog", "George", 4)
george.tail("Yes")
john = Animals("Bird", "John", 2)
john.type_of_feet("Claws")
alex = Animals()
alex.type_of_feet("hooves")
george.type_of_feet()
john.number_of_eyes=4
Abigal = Animals("Spider", "Abigal", 8)
Abigal.number_of_eyes=10
Abigal.type_of_feet("legs")
Andi = Animals("Human", "Andrea", 2)
Andi.type_of_feet("feet")

john.description()
alex.description()
george.description()
Abigal.description()
Andi.description()


