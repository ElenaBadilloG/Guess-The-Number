import random

attempts = 0
secret_number = random.randint(0, 100)

while attempts < 10:
    print('Take a guess for the secret number:')
    guess = input()
    guess = int(guess)
    attempts = attempts + 1
    if guess < secret_number:
        print('Your guess is low.') 
    if guess > secret_number:
        print('Your guess is high.')
    
    if guess == secret_number:
        break
if guess == secret_number:
    attempts=str(attempts)
    print('You guessed right!')
if guess != secret_number:
    secret_number = str(secret_number)
    
    print('The maximum number of attempts was 10. End of the game!')
            
