#input()
name = input("What is your name")
print(name)

color = input("What is your favorite color?")
print(color)

#Type conversion- int() , float() , string() , bool() , type()
user_age_text = input("How old are you? ")
user_age_math = int(user_age_text)                      #int() - 10 , 20, 25 integer
print(user_age_text) 

weight = input("What is your exact weight? ")
convert_to_decimal = float(weight)                      #float() - 14.5 , 999.9 decimal
print(convert_to_decimal) 

score = 100
convert_to_string = str(score)                          #str()- Change int to "string"

print("Your total score is" , (convert_to_string))     #BEST METHOD
print("My game score is" + convert_to_string)           #Get 3 different way to write print
print("My game score is" +" "+ convert_to_string)

points = 0
has_points = bool(points)        #bool() is used to covert a value in boolean in True or False

#type()- is used to check the data type of a value or variable
age_in_text = input("How old are you? ")
age_numbers = int(age_in_text)
print(type(age_in_text))
print(type(age_numbers))

#Why you must convert: input("Age: ") returns "25" not 25.
age = "25" 
convert = int(age)    #I used int to convert text age value to math value
next_year = convert + 1
print(next_year)

#Implicit (automatic) vs Explicit (forced) Conversion
whole_number = 10      
decimal_number = 2.5   
total = whole_number + decimal_number   #(Implicit Automatic work)
print(total)

age_text = "25"                         #(Explicit conversion)
age_math = int(age_text)                 #Because we need to change string number to pure number

#What happens when conversion fails — ValueError
 #answer is ValueError come when Python receives the correct type of data "25" , "30"
  # but the value is invalid for conversion like "Hello"
age = input ("What is your age")
integer = int(age)  #if I enter age something like (20) output will be 20
print(integer)      #But if I enter something like (Twenty) then show Error

#Round() function — round(3.7) = 4, round(3.14159, 2) = 3.14
ugly_number = 3.457845114557855
clean_number = round(ugly_number , 2)      #round() to make clean numbers
print(clean_number)