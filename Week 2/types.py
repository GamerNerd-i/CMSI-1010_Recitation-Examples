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
dog = "Fido"

# Booleans have only two values: True and False.
have_homework = True


integer = -2
float = 0.5

# Types define what you can do with data and how Python treats them.
"""Most of these are pretty intuitive. For example, it makes sense that you can only make
numbers negative (-). Because Python stores booleans as 0 (False) or 1 (True), you can even
make them negative, although they'll come back as integers.
"""

print(-lucky_number)
print(-True)
# Throws a TypeError!
# print(-"Hello " + " world!")
