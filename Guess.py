def guess_the_num():
    min_num = 1
    max_num = 25
    cpu_num = random.randint(min_num, max_num)
    score = 0

guessing = True

while not guessing:
    guess = int(input(f"Guess the number between {min_num} and {max_num}: " ))
    score += 1

    if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
    else:
            guessing = False
            print(f"Congratulations! You guessed the number in {score} attempts.")
            break

guess_the_number()

