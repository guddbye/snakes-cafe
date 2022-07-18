print("""
***********************************
** What would you like to order? **
***********************************
> Wings

** 1 order of Wings have been added to your meal **

> Wings

** 2 orders of Wings have been added to your meal **
""")

# Initialize an empty meal dictionary

# Start loop here until user enters quit

# Create a variable to store the user's order
order = input('> ')

# Print the order in some way

num_items = 1 # TODO: properly tally items that have been ordered
report = f"** {num_items} order of {order} have been added to your meal **"

print(report)
