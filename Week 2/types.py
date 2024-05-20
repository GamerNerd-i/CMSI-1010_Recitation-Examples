# Types define what kind of information is stored in a variable.
"""Not all data is the same. For example. it wouldn't make sense to make some text
negative, as if it were a number. These different kinds of data are called "types."

You should be familiar with these four types.
"""

# Integers and floats are both numbers.
"""Ints are whole numbers and are either positive or negative.
Floats are decimals. They can also be positive or negative.
"""
lucky_number = 7
tax_rate = 0.05

# Strings represent text.
"""Text doesn't just mean letters and numbers and punctuation. It includes
things like emoji and symbols too! Although you'll mostly be using letters,
numbers, and punctuation.
"""
dog = "Fido"
smiley = "Today's a great day! 😀"
pi = "π"

# Booleans have only two values: True and False.
"""Understanding booleans is very important! They're a "new" kind of data
if you're new to programming but are used everywhere. Think of them like
a lightswitch: a switch can only be either ON or OFF; not both, and not neither.
Booleans are the same.
"""
have_homework = True

# Types define what you can do with data and how Python treats them.
"""Most of these are pretty intuitive. For example, it makes sense that you can only make
numbers negative (-). Because Python stores booleans as 0 (False) or 1 (True), you can even
make them negative, although they'll change from booleans to integers.
"""
print(-lucky_number)
print(-True)
# This throws a TypeError!
print(-"Hello!")

"""We'll get into this later, but the math symbols aren't just for numbers. Strings
will also use some of them in ways that make sense if you think about it.
"""
