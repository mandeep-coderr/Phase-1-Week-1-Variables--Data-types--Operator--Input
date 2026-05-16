#Logical operators (and, or, not)
Correct_pin = True
Enough_balance = False
withdraw_balance = Correct_pin and Enough_balance         # and - all conditions check - if one condition is fail Result- Error / False 
print(withdraw_balance)

has_sugar = False
has_honey = True
is_tea_sweet = has_sugar or has_honey                     # or - opposite of (and) if all of them only one condtion is True - Result (TRUE)
print(is_tea_sweet)

cart_is_empty = True
show_payment_button = not cart_is_empty                   # not -this operator is very simple. It just flips the answer to the exact opposite
print(show_payment_button)

# Truth tables for and / or / not — understand every combination
 #Chart sheet for Truth table
True and True = True
True and False = False    #If even one thing is false, then everything becomes false
False and True = False
False and False = False

True and True =  True
True and False = True
False and True = True     #If even one thing is True, then everything will be becomes True
False and False = False

is_holiday = True
ring_alarm = not is_holiday
print(ring_alarm) 

#Short-circuit evaluation-- Python stops early when result is guaranted / for example
has_ticket = False
has_passport = True
can_fly = has_ticket and has_passport   #(and) condition need only one false it will consider all False 

#Truthy and falsy values — 0, "", None, [], {} are all falsy
 #falsy = False , Truthy = True

my_name = ""  # , None , [] , 0 , {}
is_name_filled = bool(my_name)           #bool() To check variable data what is inside empty or full
print(is_name)                            # then we use bool. It also give response in True / False

# Boolean arithmetic — True(1) + True (1) = 2, True (1) * 5 = 5
room_price = 1000
breakfast_price = 200
pool_pass_price = 50

wants_breakfast = True
wants_pool_pass = True
total_payment = room_price + (wants_breakfast * breakfast_price) + (wants_pool_pass * pool_pass_price)
print(total_payment)

#Chained comparisons — 1 < x < 10
score = 81
is_b_grade = 80 <= score <= 89
print(is_b_grade)

current_hour = 14
open_vault = 9 <= current_hour <= 17
print(open_vault) 

#Final Beginner Project: The Smart Theme Park Gate
# Step 1: Check age
age = 65
is_senior = 60 <= age <= 100

# Step 2: Check fast lane access
has_vip = False
paid_extra = True
is_banned = False
fast_lane = (has_vip or paid_extra) and not is_banned

# Step 3: Check if name is filled
user_name = ""
has_valid_name = bool(user_name)

# Step 4: Calculate final price
base_price = 100
discount = 30
final_price = base_price - (is_senior * discount)

# Step 5: Output to the screen
print(is_senior)        
print(fast_lane)        
print(has_valid_name)   
print(final_price)      