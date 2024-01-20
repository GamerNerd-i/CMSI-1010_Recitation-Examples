# Variables allow you to save data for use later in your program,
"""My analogy here is labeling boxes. Suppose you put 5 balls in a box,
then give it to your friend. They might have the box, but they don't know
what's inside. They might even throw it out! If label the box "balls,"
they know exactly what you gave them and know (hopefully) what to do with it.

The same thing can be said for your data. Your data goes in boxes -- but
you need to label that box in order for the computer to use it, and so
that you and your collaborators know what's in the box later!
"""

# Variables, no matter what they contain, use "name = data."
# That data can also be a variable for now, using a varaible uses it's value.
dog = "Fido"
lucky_number = 7
have_homework = True
pet = dog

# Once you've declared a variable, you can use it like any other value.
# Just call its name!
print("This dog's name is ", dog)
print(str(7) + " * 2 = " + str(7 * 2))
if have_homework:
    print("I have work, but I'm lazy...")
print("My pet's name is " + dog)

# You can change what is stored in the variable's "box" by using the same syntax.
"""Think carefully about when you need to create a new variable, and when you
would be able to just reassign an old one.
"""
lucky_number = 21
have_homework = False

# Variables are absolutely crucial to creating meaningful and readable code.
"""Any data you store for later will be given a variable label, which makes
it VERY important to give them good names.

If you return to code later, or if someone else has to look at your
code, the reader's understanding of what's happening is heavily
influenced by the names you give your variables -- and later, your functions.
"""

# Python has a few naming rules you should be aware of.
"""Even if you don't follow most of them, your program will still work, but your
code will be much less readable to yourself and others.
"""

# Variable names are *case sensitive*.
Dog = "Spot"
print(dog)
print(Dog)

# Variable names can only use letters, numbers, and underscores.
# However, they *cannot* begin with a number.
letters = "a"
_underscore = "_"
numbers_123 = 123

# Variables can NOT be the same as a keyword. For now, these include if, elif, and else.
# If you really *must* use a keyword as a variable name, put an underscore before it.
_if = "if and only if"
_break = "oh nooooo its brooooken"

# "Snake case" is the "capitalization" you use while in Python.
# There are other "cases" such as "camel case," but don't worry about them now.
variable_in_snake_case = True
variableInCamelCase = False

"""Otherwise, the names are up to you. To reduce headaches later, practice
writing names that are *short and to the point but descriptive.*
"""
# Suppose we want to write a variable to track the number of red blocks in a box.

number = 0
# This is not a good variable name. It doesn't tell me anything. Number of what?

number_of_blocks = 0
# This is better, but if I have different kinds of blocks then it can still be unclear.

number_of_red_blocks_in_box = 0
# Very descriptive, but it's getting a little bit long now.

red_blocks_in_box = 0
# This is probably the best mix.
# You don't need to point out that it's a number - you can tell that from its assigned value!
