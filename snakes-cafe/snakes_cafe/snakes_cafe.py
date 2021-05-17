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

total_order_list = []
order = input("> ")

while order != "exit":
    total_order_list.append(order)
    order = input("> ")
    if order == "exit":
        print(f"Your complete order is {total_order_list}")
        