#String Indexing / Negative Indexing
Fruit = "APPLE"
print(Fruit[1])          #string indexing / compartment number

Fruit = "BANANA"
print(Fruit[0])           # String indexing
print(Fruit[-1])          # Negative indexing / pick character from end

#String Slicing
Fruit = "BANANA"
print(Fruit[0:4])         # String Slicing 

Vegetable = "Artichoke"
print(Vegetable[0:4])     # String Slicing
print(Vegetable[4:])

Word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(Word[1:26:3])       # String slicing- Start:End:Step means how much words inbetween leave.

word = "APPLE"
print(word[::-1])         #String slicing- Magic Reverse Trick ([::-1]) to reverse word (ART TO TRA)

#len()
Message = "HI BOB you are a nice person"
print(len(Message))       #len() It counts everything spaces, letter, number, symbols

word = "Apple , Store"
container = len(word)
Box = container           #learnt new way to write code to using variables
print(Box)

#String Method
Game = "BASKETBALL"       # String methods
print(Game.lower())       # lower()

Game = "cricket"          # Upper
print(Game.upper())

name = "mandeep SINGH"
print(name.title())        # Every word 1st letter to change in capital 

name = "mandeep SINGH"
print(name.capitalize())   # Every 1st word 1st letter to change in capital

sweet_fruit = "                    Apple         "                         
print(sweet_fruit.strip())                  #strip(): Removes spaces from both sides.

sweet_fruit = "                    Orange"
print(sweet_fruit.lstrip())                 #lstrip(): Removes spaces only from the left side.
                          
sweet_fruit = "                    Litchi          "                          
print(sweet_fruit.rstrip())                 #rstrip(): Removes spaces only from the right side.

sentence = "I really like Apples"
print(sentence.replace("Apples" , "to play football"))  #replace(Replace the words)

message = "Do you like it"
print(message.split())                      #split() line of word splits / break into different words

my_list = ["Batman", "and", "Robin"]
print(" ".join(my_list))                    #join() It work as a glue to join many words

#String concatenation with + and repetition with *
word1 = "Spider"
word2 = "man"                               #string concatenation with +
print(word1 + " " + word2)

laugh = "ha"
print(laugh * 20)                           #Repetition (The * Copy-Paste)

Group_1 = "My Code is cool"  
Group_2 = "your code is cool"               # Use both tool to add + or multiple * to make a line
Group_3 = "Wahh"                            #It is complicated to write as compared to f-string
print(Group_1 +" "+ Group_2 +" "+ (Group_3 + " ") *5)

# f-string(This string is used to join varible and text with clean and easy way)
player_name = "Alex"
level = 100                                 # f-string This is a Modern way to combine variables and text in a cleaner way.
print(f"Congratulations {player_name}! You have reached level {level}.")

# in operator
grocery_bag = "Apples, Bread, milk, cheese"  # (in) operator- check if any word exist in variable or not 
print("Milk" in grocery_bag)                  # and give response within True or False values
