from function import play_game
from function import get_top_scores

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit?")

    if selection.upper() == "A":
        play_game(level=input("Choose the level of difficulty: "))
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    elif selection.upper() == "C":
        break
    else:
        print("Wrong input, try again")