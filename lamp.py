class Lamp:
    def __init__(self, wattage, color, luminosity, form):
        self.wattage = wattage
        self.color = color
        self.luminosity = luminosity
        self.form = form

lamp1 = Lamp(60, "blue", 8, "straight")
lamp2 = Lamp(50, "green", 8, "squiggly")