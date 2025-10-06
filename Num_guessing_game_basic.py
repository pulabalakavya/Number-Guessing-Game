import random

number_to_guess=random.randint(1,100)
attempts =0
while True:
    try:
        guess=int(input('Guess the number between 1 to 100:'))
        attempts +=1

        if guess < number_to_guess:
            print('Too Low..!')
        elif guess > number_to_guess:
            print('Too High..!')
        else:
            print('Congratulations ! You guessed the number.')
            break
    except ValueError:
        print('Please enter a valid number')                
