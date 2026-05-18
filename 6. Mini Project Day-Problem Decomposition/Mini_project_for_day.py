#write a small program that asks a user for their birth year, calculates their current age, and prints it out.
birth_year = input("What is your Birth year? ")
birth_year_time = int(birth_year)
current_year = "2026"
current_year_time = int(current_year)
calculate_age = (current_year_time - birth_year_time)
print(f"Your age is {calculate_age}") 

# Write a Program That Calculates Tax, Total Price of item, Checks Expensive Items, and Prints a Final Receipt
blue_berries_price = 1100
tax_amount = 18 * (blue_berries_price / 100)
total_price = blue_berries_price + tax_amount
print(total_price)
is_expensive = total_price >= 1200
print(f"{is_expensive}, This fruit is expensive")