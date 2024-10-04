# Recursion is kind of a weird idea.
# Intuitively you shouldn't be able to call a function in itself,
## but that's exactly what we do sometimes.

# As you saw in class, recursion and iteration *can* be used
## in similar ways.
# We'll soon see why you *shouldn't* treat them interchangably,
## but I'll be making constant comparisons to get the ideas
## of recursion across.

# We'll start with these two functions that were shown in class.
# They should look familiar, but also a little different.
# Notice that we use a while loop instead of a for loop.
# Notice also the annotated bits -- these parts serve the same purpose
## in both functions!


def countdown_iterative(n):
    i = n
    while i > 0:  # Base case condition / "Recursive call"
        print(i)  # Recursive case execution
        i -= 1  # "Recursive alteration"
    print("Blast off!")  # Base case execution


def countdown_recursive(n):
    if n == 0:  # Base case condition -- Recursion stops
        print("Blast off!")
    else:  # Recursive case -- Recursion continues
        print(n)  # Recursive case execution
        countdown_recursive(n - 1)  # Recursive call


# Make sure both your base case and recursive call are written carefully!
# As you know from loops, either one can end in an infinite loop.
# With recursion, you would have infinite recursion -- the "stack frames"
## in your computer would "overflow," and you'd get an error
## with a name that might be familiar... StackOverflow!

# More examples!


def factorial(n):
    # n! = n * n-1 * n-2... 1
    # base: n == 1
    if n == 1:
        return 1

    # recursive: n !=
    else:
        return n * factorial(n - 1)


# print(factorial(4))

# factorial(4) = 4 * (3 * (2 * 1))
# 4 * 3 * 2 * 1 = 4!

# factorial(3) = 3 * (2 * 1)
# factorial(2) = 2 * 1
# factorial(1) = 1
