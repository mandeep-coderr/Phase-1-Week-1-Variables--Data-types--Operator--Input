# 1. Data Input
API_limit = int(input("Monthly Rate Limit of API ? "))       # input() , int()
API_days_limit = int(input("Days in Current Month ? "))      # input() , int()
safety_threshold = 100

# 2. Math Calculations
daily_limit = API_limit // API_days_limit           # Floor Division
leftover_requests = API_limit % API_days_limit      # Modulo
safe_zone = daily_limit >= safety_threshold         # greater than / equal to
# print(safe_zone)

# 3. Output result
print("    ====== API RATE LIMIT REPORT ======")
print(f"Monthly Rate Limit of API: {API_limit}")
print(f"Days in Current Month: {API_days_limit}")
print(f"Safe Requests Per Day: {daily_limit}")
print(f"Leftover Requests: {leftover_requests}")
print(f"Is API in Safe Mode? {safe_zone}")



