# the computer generates a secret number and the user tries to guess it
import random 

#define a function 
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Guess is too low")
        elif guess > random_number:
            print("Guess is too high")
    
    print(f"Congratulations!!!! You have guessed corrently. It is definitely {random_number}. \n Okay it's my turn now.")
guess(10) #this sets the range

#let the computer guess this time and the user has the secret number
def comp_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
           guess = random.randint(low, high)
        else:
            guess = high #could be either low or high because low = high in this case
        feedback = input(f"Is {guess} to high (H), too low (L) or correct (C)?").lower()
        #the lower() changes the input to lowercase
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    print(f"Yay!! Congratulations to me. My {guess} is correct")
comp_guess(12) #this sets the range
