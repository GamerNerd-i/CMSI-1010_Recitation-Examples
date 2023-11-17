# Create a function that returns the nth Fibonacci number.

# The Fibonacci sequence creates its next value by adding the previous
# two values together. For example, the first few values are:
# 1 1 2 3 5 8 13 21...


def fibonacci(index):
    # base case
    if index <= 0:
        return None
    if index == 1 or index == 2:
        return 1

    return fibonacci(index - 1) + fibonacci(index - 2)


# fibonacci(3) = fibonacci(2) + fibonacci(1)
# fibonacci(2) = fibonacci(1) + fibonacci(0)
# fibonacci(1) = 1


assert fibonacci(3) == 2
assert fibonacci(9) == 34
assert fibonacci(1) == 1

# lmucs.slack.com
# Join channel: 1010-recitations-2023
