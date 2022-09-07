from car import Car as C
from electric_car import ElectricCar as EC

my_beetle = C('volkwagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_telsa = EC('tesla', 'roadster', 2022)
print(my_telsa.get_descriptive_name())