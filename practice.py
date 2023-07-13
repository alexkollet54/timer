class Human:
    def __init__(self, height, weight, race):
        self.height = height
        self.weight = weight
        self.race = race
    
    def growth_spurt(self, spurt):
        self.height += spurt


Alex = Human(510,175,"Black")
Alex.growth_spurt(6)
print(Alex.height)

