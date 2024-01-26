# Scope refers to what the program can "see" at a given point.
"""
Think of your program like a factory. What parts you can see on the workfloor
depends on where you're standing, or at what point of the manufacturing you are
currently overseeing.

For example, say your factory makes cars. If you're in the part of the factory
where the engine goes into the chassis, there's a good chance that you didn't see
the chassis get built -- it was just given to you, already complete. If you're on
the walkways above the workfloor, you can see everything at once. If you're in a
conference room going over financial reports, presumably, you won't see anything
of the factory at all -- just your financial reports!

Your position in the factory -- what you can see -- is your scope. Your program has
the same idea: some code takes place in different "rooms." In those rooms, you can only
see what's in the room, including what you brought into it. Here are some examples.
"""

# Global code can be seen by everything. You'll usually hear this in terms of variables.
# Any completely unindented code is considered global.

from tokenize import triple_quoted


word = "dog"


def print_word():
    print(word)


print(word)
print_word()

# Functions each have their own "local" scope.
"""
Local variables can only be seen inside its own function. This means that once the
function finishes, those local variables cease to exist. By default, any parameters
of the function are local.

Here, I demonstrate that, if a global and a local variable share a name, the local
variable (the one with a smaller scope) takes precedence.
"""

value = 5


# Notice here that our parameter has the same name as a global variable.
def print_different_number(value):
    value = value + 5
    print(value)


print_different_number(value)
# Even though we altered the local "value" in the function, the global "value"
## remains unchanged.
print(value)

# This next example is meant to crash. Once a function is finished, all its local
## variables cease to exist.


def a_lot_of_math():
    start = 1 + 3
    triple_sum = start * 3
    half_triple = triple_sum / 2


# Even without running the code, Python should be getting very mad at you for trying
## to access names that don't exist anymore.
print(start)
print(triple_sum)
print(half_triple)
