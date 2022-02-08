
class Shape:
    def __init__(self):
        pass

    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 33



















class Lamp:
    def __init__(self, wattage, color, luminosity, form):
        self.wattage = wattage
        self.color = color
        self.luminosity = luminosity
        self.form = form

lamp1 = Lamp(60, "blue", 8, "straight")
lamp2 = Lamp(50, "green", 8, "squiggly")