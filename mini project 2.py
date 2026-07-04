# guess the no


import random
num = random.randint(1 , 100)
attempts = 0

print("lets , start the game!")
print(" I  am thinking of no between 1 and 100")

while True:
    guess = int(input("enter a no."))
    attempts +=1

    if guess<num:
        print("too low! try again")
    elif guess>num:
        print("too high! try again")
    else:
        print(f"congrats! you guessed right in {attempts}attempts")
    
           