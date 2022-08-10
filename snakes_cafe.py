def welcomeMessage():
    print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
        """)
def displayMenu():
    print("""
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
CoffeeWing
Tea
Unicorn Tears
          """)
def submitPrompt():
    print("""
************************************
** What would you like to order?  **
** To submit order, type "Submit" **
************************************
        """)
def menuCounter():
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
"CoffeeWing": 0,
"Tea": 0,
"Unicorn Tears": 0
}
    status = True
    displayTheOrder = "** {} order of {} have been added to your meal **"
    while status == True:
        orderedItem = input("> ")
        if orderedItem in list:
            list[orderedItem] += 1
            print(displayTheOrder.format(list[orderedItem], orderedItem))
        elif orderedItem == "quit":
            exit()
        elif orderedItem == "Submit":
            print("**           Your order:           **")
            for item in list:
                if list[item] > 0:
                    print(f'Total {item}: {list[item]}')
        else:
            print("Item not on Menu")
if __name__=="__main__":
  welcomeMessage()
  displayMenu()
  submitPrompt()
  menuCounter()