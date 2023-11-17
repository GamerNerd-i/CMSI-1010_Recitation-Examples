# ordering at a restaurant
sample_menu = {
    "curry": 4.50,
    "ramen": 10.00,
    "hummus": 2.00,
    "salad": 5.00,
    "water": 1.50,
    "tea": 2.00,
    "horchata": 2.50,
}

sample_order = [["curry", 2], ["tea", 2], ["hummus", 2]]


def get_order_total(menu, order):
    """Given a dictionary for the menu containing food with
    price per item and an order as a list of lists where each
    sublist contains the food and quantity, get_order_total
    returns total cost for food before tax and tip."""
    total = 0
    for item in order:
        if item[0] in menu:
            total += item[1] * menu[item[0]]

    return total


order_total = get_order_total(sample_menu, sample_order)

print("Order total:", order_total)
