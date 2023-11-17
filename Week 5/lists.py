# Lists are like strings! And tuples are like lists, but unchanging.
# Rather, strings are lists of characters...

# Creating
# list_name = [item, item, item]
empty_list = []
string_list = ["yarn", "thread", "rope", "cord"]
mixed_list = [100.0, "rope", ["Yo", "what", "the"]]
list_list = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]  # [5, 6, 7] is list_list[2]
# List access -- look familiar?
# Indexing
# print(string_list[2])

## Slicing
# print(string_list[1:3])
# print(string_list[:2])
# print(string_list[2:])
# print(list_list[2][2])
# print()

# List operations
# ## Addition
not_string_list = ["point", "line"]
# print(string_list + not_string_list)

# ## Multiplication
# print(not_string_list * 3)
# print()

# Modifying Lists
## Individual indexing
print(string_list)
string_list[2] = "string"
# print(string_list)
## Adding items
string_list.append("rope")
# print(string_list)
string_list.extend(not_string_list)  # Note that this is the same as adding!
# print(string_list)
## Removing items
string_list.remove("point")
# print(string_list)
del string_list[-1]
# print(string_list)
## Sorting
print(string_list.sort())
# print(string_list)

# print()

# Other Methods
# print(len(string_list))
# print(len(list_list))
# print(len(list_list[0]))

# for i in range(len(string_list))

# if "rope" in string_list:
#     print("I have a rope!")
# if "line" not in string_list:
#     print("There's no line.")

# print()

# You might hear other people call Lists "Arrays".
## Most other languages have Arrays -- they work similarly to Python's Lists.
## For now, think of them as the same thing.
## (They're not, but you don't need to know that yet.)

tuple = (1, 8, 3, 4, 5)
print(tuple)
tuple = ("cat", "dog", False)
print(tuple)
# tuple[0] = 10

# print(sorted(string_list))
# string_list.sort()
