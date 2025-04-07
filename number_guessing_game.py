import random
N = (random.randint(1,100))
attempts= 5

print("Welcome to the Number Guessing Game!")
print("You have 5 attempts to guess the number between 1 and 100.\n")

for i in range(attempts):
    
    n = int(input(f" Attempt {i +1} : Guess the number  "))
    
    if N == n:
        print("Awesome! Your Guess  right") 
    elif N > n :
        print("It's wrong..\n Hint : Number is greater than this")
    elif N < n:
        print("It's wrong..\n Hint : Number is smaller than this")

    else :
        print("Well tried !But you have reached maximum attempts")
    

print(f"Actual number was : {N}")

    

