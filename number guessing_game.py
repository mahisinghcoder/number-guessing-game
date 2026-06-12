# NUMBER GUESSING GAME

winning_number = 43
guess = 1

number = int(input("Guess a number between 1 and 100: "))
game_over = False

while not game_over:
    if number == winning_number:
        print(f"You win! You guessed the number in {guess} tries.")
        game_over = True
    else:
        if number < winning_number:
            print("Too low")
        else:
            print("Too high")

        guess += 1
        number = int(input("Guess again: "))