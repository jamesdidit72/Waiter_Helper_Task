from restaurant import Restaurant


class User_Order(Restaurant):
    def __init__(self, item_ordered, keep_ordering):  # function that sets the values
        # a keyword called SUPER which inherits everything from parent class (Animal) at the time of initialisation of this class
        super().__init__()
        self.item_ordered = item_ordered
        self.keep_ordering = keep_ordering

    def display_menu(self):
        print('\nStarters:')  # prints statement, \n starts a new line
        for food in food_ordered.menu_starter:  # loops through the starter list
            print(food)
        print('\nMains:')  # prints statement, \n starts a new line
        for food in food_ordered.menu_main:  # loops through the starter list
            print(food)
        print('\nDesserts:')  # prints statement, \n starts a new line
        for food in food_ordered.menu_dessert:  # loops through the dessert list
            print(food)
        food_ordered.take_order()  # calls the function

    def take_order(self):
        self.item_ordered = input('\nPlease enter the number of the item you would like to order: ')  # generates an input
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
