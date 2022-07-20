print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Drinks
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************
""")
#intialize empty meal dictionary
items = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0
}

# print the order
num_items = 1 #TODO: properly tally items that have been ordered

order = input("> ")

while order != "quit":
    if order not in items:
        print("Please order from the menu.")
        order = input("> ")
        continue
    if items[order] == 0:
        items[order] = 1
        report = f"** 1 order of {order} has been added to your meal **"
        print(report)
    else:
        items[order] += 1
        report = f"** {items[order]} orders of {order} have been added to your meal **"
        print(report)

    order = input("> ")
