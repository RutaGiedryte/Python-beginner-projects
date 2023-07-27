import random

# a computer comes up with a random name and a user tries to guess it
def user_guesses(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Guess again, too low :))")
        elif guess > random_number:
            print("Guess again, too high :))")
    
    print(f"Congratulations, you guessed it, it was {random_number}!")


# a user comes up with a random number and a computer tries to guess it
# user inputs 'correct' if it was guessed, 'lower' if the number is lower than the guess, otherwise 'higher' 
def computer_guesses(x):
    low = 1
    high = x
    feedback = ''

    while(feedback != 'correct'):
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} correct, lower or higher than your number? ")
        if feedback == 'lower':
            low = guess + 1
        elif feedback == 'higher':
            high = guess - 1

    print(f"The computer guessed correctly, it was {guess}")

#user_guesses(10)
computer_guesses(5000)