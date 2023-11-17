# Ordering at a restaurant

# In this exercise you will implement a function, get_order_total, that will calculate the cost of
# the food in an order before tax or tip given a menu as a dictionary of items with price and an
# order as a list of lists where each list within the list contains the food from the menu and the
# quantity that has been ordered. If an item requested in order is not on menu, do not add it to
# the total. This function should return the total cost of the food in the order ordering at a
# restaurant.

# We have given you a sample menu, sample order, and sample function call. You can use this to test
# your function and modify to test further.

# ordering at a restaurant
sample_menu = {
    "burger": 4.50,
    "ramen": 10.00,
    "hummus": 2.00,
    "salad": 5.00,
    "water": 1.50,
    "tea": 2.00,
    "horchata": 2.50,
}

sample_order = [["burger", 2], ["soda", 2], ["fries", 2]]


def get_order_total(menu, order):
    """Given a dictionary for the menu containing food with
    price per item and an order as a list of lists where each
    sublist contains the food and quantity, get_order_total
    returns total cost for food before tax and tip."""
    pass


order_total = get_order_total(sample_menu, sample_order)

print("Order total:", order_total)
