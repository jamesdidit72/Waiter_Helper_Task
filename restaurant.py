# restaurant and order form
from typing import List, Any


class Restaurant:
    def __init__(self):
        self.menu_starter = ['0 - Nachos', '1 - Chicken wings', '2 - Mac and Cheese']
        self.menu_main = ['3 - Steak', '4 - Burger', '5 - Pasta']
        self.menu_dessert = ['6 - Ice cream', '7 - Cheesecake', '8 - Fruit bowl']
        # lists that were printed for the menu
        self.starter = ['Nachos', 'Chicken wings', 'Mac and Cheese']
        self.main = ['Steak', 'Burger', 'Pasta']
        self.dessert = ['Ice cream', 'Cheesecake', 'Fruit bowl']
        # lists that were appended to the order form
        self.order_form = [

        ]  # the list that holds the users order


restaurant_features = Restaurant()  # object
