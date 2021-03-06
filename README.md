# Restaurant Waiter Helper program
### Timings
- 60 Minutes

### Summary
- Now that we've created had some time to use our lists, time to make something more useful.
- You are going to make a program that helps a waiter with his menu and his orders.
### Tasks
#### User Stories
- AS a User I want to be able to see the menu in a formatted way, so that I can order my meal. 
- AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten
- As a user, I want to have my order read back to me in formatted way so I know what I ordered.
#### Acceptance Criteria
- implement OOP with most suitable pillars as per your understanding
- New repo f its own project on your laptop and Github
- be git tracked
- have 5 commits minimum!
- has documentation
- follows best practices

### First commit
- Uploading README and .gitignore
### second commit
- Initial start on menu
```python
class Restaurant:
    def __init__(self):
        self.menu = {
            'Starter': 'Chips' 'Nachos' 'Chicken wings' 'Mac and Cheese' 'Salad',
            'Main': 'Steak' 'Burger' 'Pasta' 'Fish' 'Wrap',
            'Dessert': 'Ice cream' 'Strawberries and cream' 'Cheesecake' 'Fruit bowl',}
        self.order_form = []
restaurant_features = Restaurant()
```
### User story 1 completed
#### AS a User I want to be able to see the menu in a formatted way, so that I can order my meal. 
```python
from restaurant import Restaurant
class User_Order(Restaurant):
    def __init__(self, item_ordered):  # function that sets the values
        # a keyword called SUPER which inherits everything from parent class (Animal) at the time of initialisation of this class
        super().__init__()
        self.item_ordered = item_ordered

    def display_menu(self):
        print('\nStarters:')
        for food in food_ordered.menu_starter:
            print(food)
        print('\nMains:')
        for food in food_ordered.menu_main:
            print(food)
        print('\nDesserts:')
        for food in food_ordered.menu_dessert:
            print(food)
        food_ordered.take_order()
    def take_order(self):
        self.item_ordered = input('\nPlease enter the number of the item you would like to order: ')
food_ordered = User_Order('')

food_ordered.display_menu()
```
### User story 2 completed
#### AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten
```python
from restaurant import Restaurant
class User_Order(Restaurant):
    def __init__(self, item_ordered):  # function that sets the values
        # a keyword called SUPER which inherits everything from parent class (Animal) at the time of initialisation of this class
        super().__init__()
        self.item_ordered = item_ordered

    def display_menu(self):
        print('\nStarters:')
        for food in food_ordered.menu_starter:
            print(food)
        print('\nMains:')
        for food in food_ordered.menu_main:
            print(food)
        print('\nDesserts:')
        for food in food_ordered.menu_dessert:
            print(food)
        food_ordered.take_order()

    def take_order(self):
        self.item_ordered = input('\nPlease enter the number of the item you would like to order: ')
        food_ordered.check_numbers(self.item_ordered)

    def check_numbers(self, item_ordered):
        user_prompt = True
        while user_prompt:
            if self.item_ordered.isdigit():
                food_ordered.continue_order()
                user_prompt = False
            else:
                return food_ordered.take_order()

    def continue_order(self):
        keep_ordering = input("Do you want to continue? Y/N:  ")  # collects value from user
        if keep_ordering.upper() == 'N':
             print('Enjoy your meal!')
        else:
            food_ordered.take_order()


food_ordered = User_Order('')

food_ordered.display_menu()

```
### User story 3 completed
#### As a user, I want to have my order read back to me in formatted way, so I know what I ordered.
```python
from restaurant import Restaurant


class User_Order(Restaurant):
    def __init__(self, item_ordered, keep_ordering):  # function that sets the values
        # a keyword called SUPER which inherits everything from parent class (Animal) at the time of initialisation of this class
        super().__init__()
        self.item_ordered = item_ordered
        self.keep_ordering = keep_ordering

    def display_menu(self):
        print('\nStarters:')
        for food in food_ordered.menu_starter:
            print(food)
        print('\nMains:')
        for food in food_ordered.menu_main:
            print(food)
        print('\nDesserts:')
        for food in food_ordered.menu_dessert:
            print(food)
        food_ordered.take_order()

    def take_order(self):
        self.item_ordered = input('\nPlease enter the number of the item you would like to order: ')
        food_ordered.check_numbers(self.item_ordered)

    def check_numbers(self, item_ordered):
        user_prompt = True
        while user_prompt:
            if self.item_ordered.isdigit():
                food_ordered.continue_order()
                user_prompt = False
            else:
                return food_ordered.take_order()

    def continue_order(self):
        if int(self.item_ordered) < 3:
            food_ordered.order_form.append(food_ordered.starter[int(self.item_ordered)])
            self.keep_ordering = input("Do you want to continue? Y/N:  ")  # collects value from user
        elif int(self.item_ordered) < 6:
            food_ordered.order_form.append(food_ordered.main[int(self.item_ordered) - 3])
            self.keep_ordering = input("Do you want to continue? Y/N:  ")  # collects value from user
        elif int(self.item_ordered) < 9:
            food_ordered.order_form.append(food_ordered.dessert[int(self.item_ordered) - 6])
            self.keep_ordering = input("Do you want to continue? Y/N:  ")  # collects value from user
        else:
            print('Please enter a valid number')
            self.keep_ordering = input("Do you want to continue? Y/N:  ")  # collects value from user
        if self.keep_ordering.upper() == 'N':
            print_order = ', '.join(food_ordered.order_form)
            print(f'Youve ordered: {print_order}, Enjoy your meal!')

        else:
            food_ordered.take_order()


food_ordered = User_Order('', '')

food_ordered.display_menu()

```