            # File Size Converter
user_file = input("What is your File size in MB ")
change_format = float(user_file)
total_calculate = (change_format * 1024 * 1024)
print(f"Your file is {total_calculate} bytes") 

            # fully functional Bandwidth Calculator
total_data_GB = float(input("Enter total data in GB "))
time_seconds = float(input("Enter total seconds taken "))
speed_calculate = total_data_GB / time_seconds
fix_values = round(speed_calculate , 2)
print(f"Your download speed was {fix_values} GB/s")

# Fix the Debugging
age = input("Age: ")
age_convert_into_int = int(age)
print(f"Your age will be Next year {age_convert_into_int + 1}") 


# The Taxi Ride Bill Project

# Part 1: Getting the distance
km_text = input("How many kilometers did you travel? ")
km_math = float(km_text)

# Part 2: Take the price
price_for_kilometer = input("What is the price for one kilometer? ")
price_math = int(price_for_kilometer)

# Part 3: Calculation math
total_bill = price_math * km_math
clean_bill = round(total_bill, 1)

# Part 4: receive the receipt
bill_into_text = str(clean_bill)
total_message = "Your total bill is " + bill_into_text
print(total_message)

