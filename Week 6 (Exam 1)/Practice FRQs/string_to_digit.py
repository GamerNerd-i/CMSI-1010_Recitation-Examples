# Given three word numbers separated by spaces, convert them into digit numbers.

user_input = input("Give me numbers as words: ")

number_words = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

words_list = user_input.split(" ")

output = ""

for word in words_list:
    if word.lower() not in number_words:
        continue
    else:
        output += str(number_words[word.lower()])

print(output)


AYODQ

"ANSWER YOUR OWN DAMN QUESTION"
