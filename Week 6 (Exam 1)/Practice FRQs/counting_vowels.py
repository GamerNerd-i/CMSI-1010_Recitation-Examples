# Counting Vowels
# Write a function count_vowels() that accepts a string input and returns the number
# of vowels (A, E, I, O, U) in the string, both upper and lowercase.
# Example:
## input 1: "hEllo"
## output 1: 2

## input 2: "I love Anacondas!"
## output 2: 7

vowels = ["A", "E", "I", "O", "U"]


def count_vowels(input):
    num_vowels = 0

    for letter in input:
        if letter.upper() in vowels:
            num_vowels += 1

    return num_vowels


assert count_vowels("hEllo") == 2
assert count_vowels("I love Anacondas!") == 7
assert (
    count_vowels(
        "This is an extremely long string with a lot of vowels in it, I hope it passes your tests though!"
    )
    == 27
)
print("Hooray! You passed all the tests!")
