import random
from datetime import datetime

print("Welcome to Smart ChatBot")
print("Type 'help' to see commands.")
print("Type 'bye' to exit.\n")

#Random jokes
Jokes = [
    "Python is smarter than many snakes",
    "Coding without coffee is impossible"
]

#Motivational qotes
quotes = [
    "Sucess start with self belief",
    "Practice makes man perfect"
]

#Fun facts
facts = [
    "Python was created by Guido van Rossum",
    "AI is changing the future"
]

while True:
    user = input("you:").lower()
    if user in["hi","hello","hey"]:
        print("Bot: Hello!")

     elif"how are you" in user:
         print("Bot: I'm fine, thanks for asking!")

     elif"your name" in user:
         print("Bot: My name is SmartBot")

     elif user =="creator":
         print("Bot: I was created by Priya Mahar")

     elif user == "time":
         current_time = datetime.now().strftime("%:%M%P")
         print("Bot: Current Time is", current_time)
     elif user =="date":
         current_date = datetime.now().strftime("%d-%m-%y")
         print("Bot: Today's Date is", current_date)
         
     elif user == "joke":
         print("Bot:" , random.choice(jokes))
         
     elif user == "quote":
         print("Bot:" , random.choice(quotes))

     elif user == "fact":
         print("Bot:" , random choice(facts))

     elif user =="roll dice":
         print("Bot: you got",random.randint(1,6))
         
     elif user == "flip coin":
         print("Bot:" , random.choice(["Heads", "Tails"]))

     elif user == "good morning":
         print("Bot: Good Morning!")

     elif user == "good night":
         print("Bot: Good Night!")

     elif user == "calculator":
         expression = input("Enter calculation: ")

         try:
             result = eval(expression)
             print("Bot: Result =", result)
         except:
             print("Bot: Invalid Calculation")
     elif user == "help":
         print(""" ====== COMMANDS ======
hello /hi / hey
how are you
your name
creator
time
date
joke
quote
fact
roll dice
flip coin
calculator
good morning
good night
bye
===========================================""")
     elif user in ["bye" , "exit"]:
         print("Bot: Goodbye! Have a nice day")

     else:
         print("Bot: soory, I don't understand that")

             

         
         
         
         
