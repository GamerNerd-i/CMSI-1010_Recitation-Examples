import random

def get_card():
    card = random.randint(2, 11)
    return card


sum = 0
while sum < 21:
    user_response = input('Would you like a card? Y or N')
    if user_response == 'N':
        break

    card = get_card()
    if card == 11 and sum + card > 21:
        card = 1

    print('Your card:', card)

    sum += card
    print('Your hand:', sum)


if sum == 21:
    print('You win!')
elif sum > 21:
    print('Broke!')
else:
    print('Good try!')