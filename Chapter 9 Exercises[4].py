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
        print(f'Last Name: {self.last_name.title()}')
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
        self.privileges = Privileges()


    def show_privileges(self):
        print(f'The privileges an Admin has are detailed bellow: ')
        for i in self.privileges:
            print(f'\t{i}')




#9.8 Privileges

class Privileges:

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print(f'Privileges: ')
        if self.privileges:
            for i in self.privileges:
                print(f'- {i}')
        else:
            print(f'- this user has no privileges.')



scott = Admin('Scotty', 'evansy', 30, 'black', 'earth')
scott.describe_user()

scott_privileges = ['can reset passwords', 'can delete accounts', 'can register accounts']
scott.privileges.privileges = scott_privileges
scott.privileges.show_privileges()

#9.9 Battery Upgrade

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f'This car has a {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cant roll the clock back.')


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f'This car can go about {range} on a full charge.')

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100




#my_tesla = ElectricCar('telsa', 'model s', 2019)
#print(my_tesla.get_descriptive_name())
#my_tesla.battery.describe_battery()
#my_tesla.battery.get_range()

new_car = ElectricCar('ford', 'focus', 2022)
new_car.battery.get_range()
new_car.battery.upgrade_battery()
new_car.battery.get_range()








