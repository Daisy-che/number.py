#main.py
Import random
#define range and max-attempts
lower_bound =1
uppper_bound=1000
max_attempts=10
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