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