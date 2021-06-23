import datetime
import json
import random


def get_score_list():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda x: (x["attempts"], x["date"]))
    return top_score_list[:3]


def play_game(level):
    secret = random.randint(1, 30)

    attempts = 0

    score_list = get_score_list()

    if level == "easy":

        while True:
            guess = int(input("Guess the secret number (between 1 and 30): "))
            attempts += 1

            if guess == secret:
                score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
                with open("score_list.json", "w") as score_file:
                    score_file.write(json.dumps(score_list))
                print("You've guessed it - congratulations! It's number " + str(secret))
                print("Attempts needed: " + str(attempts))
                break
            elif guess > secret:
                print("Your guess is not correct... try something smaller")
            elif guess < secret:
                print("Your guess is not correct... try something bigger")

    elif level == "hard":

        while True:
            guess = int(input("Guess the secret number (between 1 and 30): "))
            attempts += 1

            if guess == secret:
                score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
                with open("score_list.json", "w") as score_file:
                    score_file.write(json.dumps(score_list))
                print("You've guessed it - congratulations! It's number " + str(secret))
                print("Attempts needed: " + str(attempts))
                break
            else:
                print("Your guess is wrong")
    else:
        print(level + " is not the correct choice, try again")

