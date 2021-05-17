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
***********************************""")

is_True = True

while is_True:
    order_list = []
    order = input("> ")
    order = order.split(",")

    if order == "exit":
        print(f"Thank you for shopping with us!")
        break
    elif order == "done":
        print(f"Thank you for shopping with us!")
        break
    else:
        print(f"{order} added to your order!")