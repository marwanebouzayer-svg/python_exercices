import random


class Game:

    def get_user_item(self):
        while True:
            user_item = input("Choose rock, paper or scissors: ").lower()

            if user_item in ["rock", "paper", "scissors"]:
                return user_item
            else:
                print("Invalid choice! Try again.")

    def get_computer_item(self):
        items = ["rock", "paper", "scissors"]
        return random.choice(items)

    def get_game_result(self, user_item, computer_item):

        if user_item == computer_item:
            return "draw"

        elif user_item == "rock" and computer_item == "scissors":
            return "win"

        elif user_item == "paper" and computer_item == "rock":
            return "win"

        elif user_item == "scissors" and computer_item == "paper":
            return "win"

        else:
            return "loss"

    def play(self):

        user_item = self.get_user_item()

        computer_item = self.get_computer_item()

        result = self.get_game_result(user_item, computer_item)

        print(f"\nYou selected {user_item}.")
        print(f"The computer selected {computer_item}.")

        if result == "win":
            print("You win!")

        elif result == "draw":
            print("You drew!")

        else:
            print("You lose!")

        return result