server_name = input("Enter a server name: ")

clean_server = server_name.replace(" ", "").strip().upper()

total_RAM = float(input("Total RAM in Computer (GB): "))
used_RAM = float(input("Used RAM in Computer (GB): "))

calculate_RAM = total_RAM - used_RAM

used_RAM_in_percentage = (used_RAM / total_RAM) * 100

used_RAM_in_percentage = round(used_RAM_in_percentage, 1)

is_worst_system = used_RAM_in_percentage > 85.0

#output - Biggest learning- " " This is used for just single line """ """ we use to print many lines
print(f"""SERVER NAME : {clean_server} 
        TOTAL RAM   : {total_RAM} GB  
        USED RAM    : {used_RAM} GB 
        FREE RAM    : {calculate_RAM} GB  
        RAM USED %  : {used_RAM_in_percentage}%  
        Worst       : {is_worst_system}""")