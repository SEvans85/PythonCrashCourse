from random import randint

class Dice:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        return randint(1,self.sides)

d6 = Dice()

results = []
for i in range(10):
    result = d6.roll_dice()
    results.append(result)
print(f'10 Rolls of a 6-sided dice: ')
print(f'\t{results}')


d10 = Dice(10)
results = []
for i in range(10):
    result = d10.roll_dice()
    results.append(result)
print(f'10 Rolls of a 10-sided dice: ')
print(f'\t{results}')


d20 = Dice(20)
results = []
for i in range(10):
    result = d20.roll_dice()
    results.append(result)
print(f'10 Rolls of a a 20-sided dice: ')
print(f'\t{results}')



