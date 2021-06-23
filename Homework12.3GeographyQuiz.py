import json
import random


def list_countries():
    with open("countries.json", "r") as countries_file:
        countries_list = json.loads(countries_file.read())
        return countries_list


def random_country_number():
    secret = random.randint(0, len(list_countries())-1)
    return secret


def game():
    countries_lists = list_countries()
    number = random_country_number()

    capital = input("What is the capital of " + countries_lists[number]["country"] + " :")

    if capital.lower() == countries_lists[number]["city"].lower():
        print("This is correct ! " + countries_lists[number]["city"] + " is the capital.")
    else:
        print("You are wrong my friend. the correct answer is " + countries_lists[number]["city"])


while True:
    a = input("If you want to play the game select A, if not press anything else: ")
    if a.lower() == "A".lower():
        game()
    else:
        break
