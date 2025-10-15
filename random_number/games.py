from random_utils import random_number

def guess_number():
    secret = random_number(1, 100)
    print("I have picked a number between 1 and 100. Try to guess it")
    
    while True:
        try:
            guess = int(input("Enter your guess:"))
        except ValueError:
            print("Please enter a valid integer")
            continue
        
        if guess < secret:
            print("Higher")
        elif guess > secret:
            print("Lower")
        else:
            print("Ypu guess the number", secret)            
            break

if __name__ == "__main__":
    guess_number()       