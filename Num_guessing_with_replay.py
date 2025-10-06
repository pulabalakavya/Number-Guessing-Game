import random
while True:
    number_to_guess=random.randint(1,100)
    attempts =0
    print("\n i am thinking of a number between 1 and 100....")

    while True:
        try:
            guess=int(input('Your guess:'))
            attempts +=1
            if guess < number_to_guess:
                print('Too Low..!')
            elif guess > number_to_guess:
                print('Too High..!')    
            else:
                print(f'You got it in {attempts} attempts!')   
                break
        except ValueError:
            print('please enter a valid number.!')  
    play_again=input('play again? (yes/no):').lower()  
    if play_again !='yes':
        print('Thanks for playing!!')    
        break     