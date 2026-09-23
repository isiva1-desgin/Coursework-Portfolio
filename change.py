

cents = input("Please enter a number of cents: ")
num_cents = int(cents)

num_quarters = num_cents//25 
num_cents = num_cents%25

num_dimes = num_cents//10 
num_cents = num_cents%10

num_nickels = num_cents//5
num_cents = num_cents%5

pennies = num_cents

print(f" {num_quarters} quarters, {num_dimes} dimes, {num_nickels} nickels, {pennies} pennies")