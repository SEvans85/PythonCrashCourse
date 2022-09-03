#9.6 Ice Cream Stand

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.resaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'The Restaurant name is {self.resaurant_name}')
        print(f'The Restaurant serves {self.cuisine_type} food.')

    def restaurant_open(self):
        print(f'{self.resaurant_name} is open for service.')

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['chocolate', 'strawberry', 'vanilla']

    def list_flavours(self):
        print(f'The flavours we have on offer are: ')
        for i in self.flavours:
            print(f'\t{i}')

my_icecream_stand = IceCreamStand('Mr Whippy', 'Ice Cream')
my_icecream_stand.list_flavours()

#9.7 Admin

class User:

    def __init__(self, first_name, last_name, age, eye_colour, town):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.eye_colour = eye_colour
        self.town = town
        self.login_attempts = 0

    def describe_user(self):
        print(f'First Name: {self.first_name.title()}')
        print(f'Last Name: {self.last_name.title * ()}')
        print(f'Age: {self.age}')
        print(f'Eye Colour: {self.eye_colour}')
        print(f'Town: {self.town}')

    def greet_user(self):
        print(f'Greetings {self.first_name} {self.last_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):

    def __init__(self, first_name, last_name, age, eye_colour, town):
        super().__init__(first_name, last_name, age, eye_colour, town)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f'The privileges an Admin has are detailed bellow: ')
        for i in self.privileges:
            print(f'\t{i}')

my_admin = Admin('scott', 'evans', 36, 'blue', 'manchester')
my_admin.show_privileges()






