import random

random_numbers = [random.randint(0,49) for x in range(0,20)]

print(random_numbers)

squared_randoms = [number**2 for number in random_numbers]

print(squared_randoms)