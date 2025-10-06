import random
GREEN="\033[92m"
RED="\033[91m"
YELLOW="\033[93m"
RESET="\033[0m"
def play_game():
    number_to_guess = random.randint(1,100)
    attempts=0
    score=100
    print("\n Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    while True:
        try:
            guess=int(input("Enter your guess:"))
            attempts+=1

            if guess==number_to_guess:
                print(GREEN + f"correct! you guessed it in {attempts} attempts."+RESET)
                print(GREEN + f" You scored {score} points this round!"+RESET)
                return score
            elif abs(guess - number_to_guess) <=5:
                print(YELLOW + "Very close! Try again."+RESET)
                score-=5
            elif guess < number_to_guess:
                print(YELLOW + "Too Low! Try again."+RESET)   
                score-=10
            else:
                print(RED + "Too High! Try again." +RESET)  
                score-=10
            if score <=0:
                print(RED + "No points left! The correct number was"+str(number_to_guess)+RESET)  
                return 0
        except ValueError:
            print(RED + "please enter a valid number!"+RESET)         
def main():
    total_score=0
    while True:
        round_score=play_game()
        total_score+=round_score
        print(f"\n Your total score so far:{total_score}")
        play_again=input("Do you want to play again? (yes/no):").strip().lower()
        if play_again!="yes":
            print(GREEN + f"\n Game Over! Your final score: {total_score}"+ RESET)
            print("Thanks for playing!")
            break
if __name__=="__main__":
    main()        