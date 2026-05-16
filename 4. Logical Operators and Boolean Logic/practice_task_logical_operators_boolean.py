# 1st Task from the Practice list              
is_admin = False  
is_active = True  
is_banned = False  
user_detail =(is_admin or is_active) and not is_banned      # System Access Granted - If three conditions matched True
print(user_detail) 

# 2nd Task from the Practice list
port_input = "8080"
change_to_integer = int(port_input)                    # Network Port Validation: Define a port variable (e.g. port = 8080)
port_check = 0 < change_to_integer <= 65535             #Use chained comparisons to print True if the port is valid (0 < port <= 65535).
print(port_check) 

# 3rd Task from the Practice list
my_box = ""
entire_box = bool(my_box)         #answer is False
print(entire_box)

my_box = 0
entire_box = bool(my_box)         #answer is false       # Verify truthy/falsy behavior: Convert an empty string "", a zero 0, 
print(entire_box)                                         # and a non-empty string "config" to booleans using bool()

my_box = "config"
box_size = bool(my_box)           #answer is True
print(box_size) 












