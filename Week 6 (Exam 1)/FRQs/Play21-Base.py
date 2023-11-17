import random

# In this exercise you will need to implement a simplified version of the game 21 with a singular
# player asking for cards from a dealer. We have provided a function that deals cards for you. The
# function get_card returns a value between 1 and 11. Your script will need to ask a single user to
# see if the user would like another card until one of the following conditions is met:
## the value of the user's hand is 21 or greater
## the user requests not to have another card

# Your script will need to keep track of the current value of the cards the user has in hand. There
# is one exception: an ace, which would initially have a value of 11. If the value of 11 makes the
# dealt cards exceed the limit of 21, then the value of an ace becomes 1. After each card is dealt
# to the user, print to the user the value of the current card and the value of the hand.

# We have also provided you with code to print the final results of the game to the user.

import random

def get_card():
    card = random.randint(2, 11)
    return card


sum = 0
# Start here: keep asking for cards until
# one of the two given conditions is met.
# Add to the following code to finish up
# your script.
    user_response = input('Would you like a card? Y or N')

    card = get_card()

    print('Your card:', card)

    print('Your hand:', sum)


if sum == 21:
    print('You win!')
elif sum > 21:
    print('Broke!')
else:
    print('Good try!')