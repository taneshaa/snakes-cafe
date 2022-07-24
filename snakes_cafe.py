def welcome():
    print("""
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **

    ** To quit at any time, type "quit" **
    **************************************
    """)


def menu():
    print(""" Appetizers
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
    """)


def orders():
    print("""***********************************
    ** What would you like to order? **
    ***********************************
    """)


if __name__ == '__main__':

    order = input(">")

# create data structure that menu items and quantity
    num_item = 1
    report = f" {num_item} order of {order} have been added to your meal "
    print(report)
