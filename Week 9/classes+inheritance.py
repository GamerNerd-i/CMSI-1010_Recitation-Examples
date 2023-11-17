class Furniture:  # class ClassName
    def __init__(self, kind, room, material):  # Constructor
        self.kind = kind
        self.room = room
        self.material = material
        self.dirt = 0

    def clean_furniture(self):
        self.dirt = 0
        print("All cleaned up!")

    def sit_and_eat(self, food):
        print("Oh no! I got some crumbs on it...")
        self.dirt += food

    def move(self, new_room):
        if self.room is new_room:
            print("It's already in this room!")
        else:
            print(
                "Moving " + self.kind + " from " + self.room + " to " + new_room + "!"
            )
            self.room = new_room


# Inheritance!
class SofaBed(Furniture):  # class Subclass(Superclass)
    def __init__(self, room):
        # super() lets you access the superclass' methods
        super().__init__("sofa", room, "fabric")
        self.softness = 20

    def change_layout(self):
        if self.kind == "sofa":
            print("Turning the sofa into a bed!")
            self.kind = "bed"
        else:
            print("Turning the bed into a sofa!")
            self.kind = "sofa"

    # override
    def sit_and_eat(self, food):
        self.softness -= 1
        super().sit_and_eat(food)


# print("I have a new desk!")
my_desk = Furniture("desk", "office", "wood")

# print("I'm going to eat at my desk.")
# my_desk.sit_and_eat(5)
# print(my_desk.dirt)
# print("I should clean up.")
# my_desk.clean_furniture()
# print(my_desk.dirt)
# print("My desk is in the " + my_desk.room)
# my_desk.move("bedroom")
# print("My desk is now in the " + my_desk.room)


my_sofa = SofaBed("living room")
# print(my_sofa.room)
my_sofa.move("family room")
# print(my_sofa.room)

# print(my_sofa.dirt)
# print(my_sofa.softness)
my_sofa.sit_and_eat(5)
# print(my_sofa.dirt)
# print(my_sofa.softness)

print(my_sofa.kind)
my_sofa.change_layout()
print(my_sofa.kind)
my_sofa.change_layout()
print(my_sofa.kind)

# object_name.attribute
# object_name.method()
