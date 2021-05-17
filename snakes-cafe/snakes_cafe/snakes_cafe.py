# **************************************
# **    Welcome to the Snakes Cafe!   **
# **    Please see our menu below.    **
# **
# ** To quit at any time, type "quit" **
# **************************************

print("*" * 38)
print("""**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **""")
print("*" * 38)

# Appetizers
# ----------
# Wings
# Cookies
# Spring Rolls

print(""" """)

print("""Appetizers
----------
Wings
Cookies
Spring Rolls""")

# Entrees
# -------
# Salmon
# Steak
# Meat Tornado
# A Literal Garden

print(""" """)

print("""Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden""")

# Desserts
# --------
# Ice Cream
# Cake
# Pie

print(""" """)

print("""Desserts
--------
Ice Cream
Cake
Pie""")

# Drinks
# ------
# Coffee
# Tea
# Unicorn Tears

print(""" """)

print("""Drinks
------
Coffee
Tea
Unicorn Tears""")

# ***********************************
# ** What would you like to order? **
# ***********************************
# >

print(""" """)

print("""***********************************
** What would you like to order? **
** 'exit' to end order           **
***********************************""")

items_in_stock = ["wings", "cookies", "spring rolls", "salmon", "steak", "meat tornado", "a literal garden", "ice cream", "cake", "pie", "coffee", "tea", "unicorn tears"]

total_order_list = []
order = input("> ")

while True:
    if order == "exit":
        print(f"** Your complete order is:
        for item in total_order_list:
            print(f"** {item}")
        break
    elif order == "done":
        print(f"** Your complete order is:
        for item in total_order_list:
            print(f"** {item}")
        break
    elif order not in items_in_stock: 
        print(f"** {order} isn't available **")
        order = input("> ")
    else:
        total_order_list.append(order)
        print(f"** your order of {order} have been added to your meal **")
        order = input("> ")
