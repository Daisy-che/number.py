#main.py
Import random
#define range and maximum attempts

lower_bound =1
uppper_bound=100
maximum-attempts=10

#generate the secret number
secret-number= random.randint(lower_bound)
#Get the user's guess
def get-guess():
    while True
    try
    guess=int(input(f"Guess a number between{lower_bound}"))
    if lower-bound<=guess <=uppper_bound:
        return guess
        else:
     print("Invalid input.Please enter a valid number.")
    #validate guess
    def check-guess(guess,secret_number):
    if guess==secret_number:
    return"correct"
    elif guess<secret_number:
     return "Too low"
    else:return"Too high"
    #track the number,detect if the game is over
    def play-game():
    attempts=0
     won=false
     while attempts <max-attempts:
    attempts+-=1
    guess=get-gues()
    result=check-guess(guess,secret-number)

 if result=="correct":
 print(f"Congratulation!You guessed the secret number{secret_number}in{attempts3}attempts.")
won=True
break
 else
 print(f"Sorry,you ran outof attempts!The secret number is {secret_number}in")

 if_____name____=="_____main______":
print("Welcome to the Number Guessing Game!")
play_game()

