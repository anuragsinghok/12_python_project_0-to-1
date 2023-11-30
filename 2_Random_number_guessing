import random

def guess(user,rand):
    if user ==rand :
        print(f"congrants you guess it right : you guess was {user} ")
    elif user > rand: 
        print(f" you guess is high choose a lower number then {user}")
    elif user < rand: 
        print(f" you guess is low choose a higher number then {user}")
    else:
        print("invalid input")
   
    

rand = random.randint(0,100) # it will guess the random interger from 1 to 100
print(rand)
user = int(input("Enter a number to guess between 0 to 100 : "))
print(guess(user,rand))
