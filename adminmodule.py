from usermodule import User

class Admin(User):

    def __init__(self, first_name, last_name, age, eye_colour, town):
        super().__init__(first_name, last_name, age, eye_colour, town)
        self.privileges = Privileges()

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