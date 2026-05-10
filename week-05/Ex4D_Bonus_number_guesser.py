numbers = {'1', '2', '3', '4', '5', '6'}

ran = numbers.pop()
random_num = int(ran)

user_guesses = []

input_prompt = "Guess integer number between 1 and 6: "

check = True

while check:

    try:
        user_num = int(input(input_prompt))

    except ValueError:
        print("Error: Please enter a valid integer.")
        continue

    user_guesses.append(user_num)

    if random_num == user_num:
        print("You win!")
        check = False

    elif random_num > user_num:
        input_prompt = "Guess higher: "

    else:
        input_prompt = "Guess lower: "


print(f"Your guesses: {user_guesses}")

if len(user_guesses) < 5:
    print("You are awesome!")