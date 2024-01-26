# Functions are blocks of code that you "pre-write" to use later.
"""
There are three main reasons why we use functions:
1) Readability: If you're rewriting the same block of code multiple times,
    the rest of your code might become difficult to parse. By putting that 
    rewritten code in a function, you can condense it down to a simple phrase
    like "calculate_mean." It's much easier to read that than it would be to
    identify the formula for a mean every time.
    
2) Generalization: Functions make code reusable. For example, if I write a
    "calculate mean" function, then I can use it whenever I need to, no matter
    what inputs I have. Using the formula would require it to change every time.
    
3) Maintenance: With a function, all the necessary code is in one place, even
    if it's used in multiple places in code. Without functions, if you had to debug
    a block you used 5 times, you would need to make the same changes 5 times, rather
    than just once. 
"""


# Here's the most basic form of a function.
def function_name(parameter1, parameter2):
    print(parameter1 + " is definitely a " + parameter2)


# Note the most important parts:
"""
1) "def" keyword: This lets Python know that you're creating a function,
    just like how "if" tells Python that you're writing a conditional.
    
2) Function name: Follows the same naming conventions as variables. Like variables,
    (and people) you "call" functions to run by their name.
    
3) Parameters: Inside the parentheses are the names for your inputs. Think of it like
    initiating variables you'll need to complete the task. Note that, when you call the
    function, the inputs do not need to have the same name as the parameter names given
    here; in fact, it's better if they don't so that you don't get confused as to which
    is which. Technically you can have as many parameters as you want, but be reasonable.
"""

# If you want to get an output for the function, use the "return" keyword.
"""
Be VERY careful about this point! Again: If you want a function to output a value that
the rest of the code can use, use the RETURN keyword.

Print does not do the same thing as return. It's only useful to peek at what's
happening inside the function.

One more time: USE RETURN. Print shows you a value, but DOES NOT save it for later use.
"""


# Calculates the mean of a list of numbers.
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


random_list = [9, 5, 1, 4, 1, 9]
# Here's how you call a function. Remember: use the name, and give it the parameters
## that it needs.
avg1 = calculate_mean(random_list)
print(avg1)
# Alternatively, just give it a direct value: no extra variables needed.
avg2 = calculate_mean([8, 10, 7, 2, 7, 1])
print(avg2)


# Lastly, here's a showcase of some other fun quirks of functions.
## Multiple Inputs / Parameters
def is_multiple(num, factor):
    print("Called is_multiple on " + str(num) + " and " + str(factor))
    return num % factor == 0


## Multiple Outputs
def double_and_halve(num):
    return num * 2, num / 2


## Functions can be put inside functions. This gets kinda crazy later on.
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
