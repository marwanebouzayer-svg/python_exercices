import random


def get_random_temp(season):
    if season == "winter":
        return random.randint(-10, 16)
    elif season == "spring":
        return random.randint(0, 23)
    elif season == "summer":
        return random.randint(16, 40)
    elif season == "autumn" or season == "fall":
        return random.randint(5, 25)
    else:
        return None


def main():
    season = input(
        "Enter a season (summer, autumn, winter, spring): "
    ).lower()

    temperature = get_random_temp(season)

    if temperature is None:
        print("Invalid season")
    else:
        print("The temperature right now is",
              temperature, "degrees Celsius.")

        if temperature < 0:
            print("Brrr, that's freezing! Wear extra layers.")
        elif temperature < 16:
            print("Quite chilly! Don't forget your coat.")
        elif temperature < 24:
            print("The weather is mild. Enjoy your day!")
        elif temperature <= 32:
            print("It's warm outside. Stay hydrated!")
        else:
            print("It's very hot! Drink plenty of water.")


main()