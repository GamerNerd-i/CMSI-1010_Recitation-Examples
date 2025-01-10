# Furniture is a superclass or parent class
from typing import override


class Furniture:
    def __init__(self, color, location, dimensions, num_legs):
        self.color = color
        self.location = location
        self.dimensions = dimensions
        self.num_legs = num_legs
        self.dirt = 0

    def recolor(self, new_color):
        print("Changing color to " + new_color)
        self.color = new_color

    def move(self, new_location):
        print("Moving from " + self.location + " to " + new_location)
        self.location = new_location

    def sit_and_eat(self, food):
        print("Oh no! I got some crumbs on it...")
        self.dirt += food

    def clean(self):
        self.dirt = 0
        print("All cleaned up!")


# SofaBed is a subclass or child class of Furniture
class SofaBed(Furniture):
    def __init__(self, color, location, dimensions, num_legs):
        super().__init__(color, location, dimensions, num_legs)
        self.is_sofa = True

    def switch(self):
        if self.is_sofa:
            print("Changing to a bed")
        else:
            print("Changing to a sofa")
        self.is_sofa = not self.is_sofa

    @override
    def move(self, new_location):
        if not self.is_sofa:
            print("This is hard to move as a bed! We'll change it to a sofa first.")
            self.is_sofa = True

        super().move(new_location)


print("Creating a Keck Annex table")
table = Furniture("white", "Keck Annex", {"H": 3.0, "W": 8.0, "L": 1.5}, 4)

print("Painting it black")
table.recolor("black")

print(table.color)

print("Making a sofabed")
sofabed = SofaBed("brown", "Keck Lab", {"H": 3.0, "W": 8.0, "L": 1.5}, 4)

sofabed.recolor("blue")
print(sofabed.color)
print()

sofabed.switch()
print(sofabed.is_sofa)

print(sofabed.location)
sofabed.move("Keck Annex")
print(sofabed.location)
print(sofabed.is_sofa)
