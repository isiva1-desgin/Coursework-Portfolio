

menu = {"Hot Dog":1.50, "Slice of Pizza":1.99, "Whole Pizza":9.95, "Soft Drink":0.59}
numDogs = int(input("Please enter the number of Hot Dogs: "))
numSlice = int(input("Please enter the number of Pizza Slices: "))
numWhole = int(input("Please enter the number of Whole Pizzas: "))
numSoft = int(input("Please enter the number of Soft Drinks: "))

TotalCost = menu["Hot Dog"]*numDogs + menu["Slice of Pizza"]*numSlice + menu["Whole Pizza"]*numWhole + menu["Soft Drink"]*numSoft
print(f"The total cost of the order is {TotalCost:.2f}")