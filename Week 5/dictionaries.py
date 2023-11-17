# Dictionaries are like real dictionaries in that you can
# find a definition (value) by looking up a word (key).

dictionary = {}
dictionary = {"josh": 100, "peter": 52, "alice": 200}

# print(dictionary["alice"])
dictionary["peter"] += 20  # dictionary["peter"] = dictionary["peter"] + 20
# print(dictionary["peter"])

dictionary["clarisee"] = 90
# print(dictionary)
dictionary["clarisee"] += 10
# print(dictionary)

dict_of_lists = {1: True, 2: [1, 2, 3], 3: {"a": 1, "b": 2}}
# print(dict_of_lists[2])
# print(dict_of_lists[3]["b"])

# del dict_of_lists[1]
# print(dict_of_lists)

for name in dictionary:
    print(name)  # this is the KEY
    print(dictionary[name])  # this is the VALUE
    print()
