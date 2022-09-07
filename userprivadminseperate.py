from adminmodule import Admin

my_admin1 = Admin('scotty', 'evansy', 36, 'brown', 'manc')
my_admin1.privileges.privileges = ['a', 'b', 'c']
my_admin1.privileges.show_privileges()
