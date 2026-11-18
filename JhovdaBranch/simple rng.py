while True:
    userGuess = int(input("What's your guess? "))
    attempts += 1

    if userGuess < number:
        print("Too low, Try again.") 
    elif userGuess > number:
        print("Too high, Try again.")
    else:
        print(f"You got it in {attempts} guesses. Nice!") #what would be a funny message to put here
        break

