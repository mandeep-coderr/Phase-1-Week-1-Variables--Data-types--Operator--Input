               # False True False
is_admin = False  
is_active = True  
is_banned = False  
user_detail =(is_admin or is_active) and not is_banned      # System Access Granted - If three conditions matched True
print(user_detail) 

port_input = "8080"
change_to_integer = int(port_input)
port_check = 0 < change_to_integer <= 65535
print(port_check) 