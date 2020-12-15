class car:
    def __init__(self, name, numberOfDoors, color):
        self.name = name
        self.numberOfDoors = numberOfDoors
        self.color = color

    def showCarFullInfo(self):
        return f"car name is {self.name} & car color is {self.color}"


benz = car("sls", 2, "red")

print(benz.showCarFullInfo())
