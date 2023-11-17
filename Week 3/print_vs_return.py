def greeter1(name):
    print("Hello " + name + " from greeter1")


def greeter2(name):
    return "Hello " + name + " from greeter2"


# greeter1("Bob")
# greeter2("Bob")

# print(greeter1("Anna"))
# print(print("Hello Anna"))

# print(greeter2("Anna"))
# print("Hello Anna")

# greetings = greeter1("Carla")

greetings = greeter2("Carla")
print(greetings)
greetings = greetings + ". It's nice to meet you!"
print(greetings)
