# Multiple Inputs / Parameters
def is_multiple(num, factor):
    print("Called is_multiple on " + str(num) + " and " + str(factor))
    return num % factor == 0


# Notice how short this is!


# Multiple Outputs
def double_and_halve(num):
    return num * 2, num / 2


# Functions in Functions, and nested conditionals
def is_kind_of_prime(num):
    if is_multiple(num, 2):
        print(False)
    elif is_multiple(num, 3):
        print(False)
    elif is_multiple(num, 5):
        print(False)
    else:
        print(True)


print(is_kind_of_prime(9))
