import numpy as np
Num=np.random.randint(1,100)
attempt=0
while True:
    guess=int(input("Enter your guess:"))
    attempt+=1
    if guess<Num:
        print("too low!")
    elif guess>Num:
        print("too high!")
    else:
        print(f"Correct! you guessed it in {attempt} attempts")
        break
        
