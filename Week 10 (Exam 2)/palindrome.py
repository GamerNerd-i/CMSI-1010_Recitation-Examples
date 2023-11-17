# A palindrome is a sequence that can be read the same
# both forwards and backwards:

# A Toyota
# racecar
# @$#%%#$@

# Create a recursive function that determines whether or not
# a given string is a palindrome and returns True if it is.


def palindrome(string):
    # base cases
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False

    # recursive case
    return string[1:-1]


assert palindrome("atoyota")
assert not palindrome("I am not a palindrome")
assert palindrome("100202001")
assert palindrome("a")
assert palindrome("")
