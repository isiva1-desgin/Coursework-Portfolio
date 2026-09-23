
import math 
import random
num_radius = int(input("Please enter the raidus of the sphere: "))
num_volume = num_radius**3 * math.pi *4/3

num_rand = random.randint(1,10)
num_fact = math.factorial(num_rand)

print(f"The volume of a sphere with raidus of {num_radius} is {num_volume:.2f}")
print()
print(f"The factorial of {num_rand} is {num_fact}")
