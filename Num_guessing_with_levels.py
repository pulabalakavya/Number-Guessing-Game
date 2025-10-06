import random

print("Choose difficulty level:")
print("1.Easy(1-10)")
print("2.Medium(1-50)")
print("3.Hard(1-100)")

choice = input("Enter 1,2, or 3:")

if choice=='1':
    max_num=10
elif choice=='2':
    max_num=50
else:
    max_num=100

number_to_guess=random.randint(1,max_num)
attempts=0
print(f"\n i am thinking of a number between 1 and {max_num}....")
while True:
    try:
        guess = int(input('Your guess:'))  
        attempts+=1
        if guess < number_to_guess:
            print('Too Low..!')  
        elif guess > number_to_guess:
            print("Too High..!")  
        else:
            print(f' Correct! You found it in {attempts} attempts.')   
            break
    except ValueError:
        print('Please enter a valid number.')       


