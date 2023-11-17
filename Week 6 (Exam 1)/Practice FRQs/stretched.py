# Stretched
# Write a function stretched() that accepts a string to_stretch. The function should return a string with all the same characters in the original, but doubled.
# BONUS CHALLENGE: Give stretched another input, length, an integer representing how many times each character is repeated. Call this version of the function extra_stretched().

# Example:
## input 1: "hello"
## output 1: "hheelllloo"

## input 2: "abc"
## output 2: "aabbcc"


def stretched(to_stretch):
    stretched_string = ""

    for character in to_stretch:
        stretched_string += character * 2

    return stretched_string


def extra_stretched(to_stretch, length):
    stretched_string = ""

    for character in to_stretch:
        stretched_string += character * length

    return stretched_string


# Normal tests
assert stretched("hello") == "hheelllloo"
assert stretched("abc") == "aabbcc"
assert stretched("I AM YELLING") == "II  AAMM  YYEELLLLIINNGG"
assert stretched("12345") == "1122334455"
assert stretched("Punctuation? Wow...!") == "PPuunnccttuuaattiioonn??  WWooww......!!"

# Extra tests - comment these out if you didn't do the bonus part!
assert extra_stretched("hello", 2) == "hheelllloo"
assert extra_stretched("abc", 4) == "aaaabbbbcccc"
assert extra_stretched("12345", 3) == "111222333444555"
assert extra_stretched("!", 20) == "!!!!!!!!!!!!!!!!!!!!"
assert extra_stretched("But nothing's different...", 1) == "But nothing's different..."
assert extra_stretched("Mr. Programmer I don't feel so good...", 0) == ""
