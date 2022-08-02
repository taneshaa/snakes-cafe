# def = define function, then calling the welcome function
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


def menu_counter():
    list = {
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


order = input(">")
if order in list:
    list[order] += 1
elif order == "quit":
    exit()
elif order == "submit":
    for item in list:
        if list[item] > 0:
            print(f'{item}:{list[item]}')
else:
    print("item is not on the menu")

def orders():
    print("""***********************************
    ** What would you like to order? **
    ***********************************
    """)


# only execute code below when this file is directly executed from command line
if __name__ == '__main__':
    # what do I want to have show up on screen first? welcome
    welcome()

    # what I want to show up on the screen next is menu
    menu()

    # what I want to show up next
    orders()

#
# # create data structure that menu items and quantity
#     num_item = 1
#     report = f" {num_item} order of {order} have been added to your meal "
#     print(report)
