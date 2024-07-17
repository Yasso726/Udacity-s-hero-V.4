import random

# Define constants for better code readability
SUCCESS = "You win!"
FAILURE = "You lose!"
OPTIONS = {
    "mainframe": {
        "1": "Use a brute force attack",
        "2": "Use a stealth approach"
    },
    "hideout": {
        "1": "Take out the guards silently",
        "2": "Create a distraction"
    }
}

def play_game():
    print("Welcome, Udacity Hero!")
    while True:
        print("\nHackers have captured hostages and are threatening to corrupt Udacity's files.")
        print("Do you:")
        choice = get_choice(["1. Hack into the hacker's mainframe", "2. Infiltrate the hacker's hideout", "3. Exit"])

        if choice == "1":
            hack_mainframe()
        elif choice == "2":
            infiltrate_hideout()
        elif choice == "3":
            print("\nThanks for playing!")
            break
        else:
            print("Invalid choice. You lose!")

        if input("\nPlay again? (yes/no) ").strip().lower() != "yes":
            print("\nThanks for playing!")
            break

def get_choice(options):
    while True:
        print("\n".join(options))
        choice = input("> ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def hack_mainframe():
    print("\nYou try to hack into the mainframe. Do you:")
    choice = get_choice([f"1. {OPTIONS['mainframe']['1']}", f"2. {OPTIONS['mainframe']['2']}"])

    if choice == "1":
        outcome = random.choice([
            "successfully bypass the security and rescue the hostages",
            "trigger an alarm and get caught by the hackers"
        ])
        print(f"\nYou {outcome}.", SUCCESS if "rescue" in outcome else FAILURE)
    elif choice == "2":
        outcome = random.choice([
            "infiltrate the system unnoticed and save the files",
            "get detected and locked out"
        ])
        print(f"\nYou {outcome}.", SUCCESS if "save the files" in outcome else FAILURE)
    else:
        print("Invalid choice. You lose!")

def infiltrate_hideout():
    print("\nYou infiltrate the hacker's hideout. Do you:")
    choice = get_choice([f"1. {OPTIONS['hideout']['1']}", f"2. {OPTIONS['hideout']['2']}"])

    if choice == "1":
        outcome = random.choice([
            "neutralize the guards and free the hostages",
            "get overpowered by the guards"
        ])
        print(f"\nYou {outcome}.", SUCCESS if "free the hostages" in outcome else FAILURE)
    elif choice == "2":
        outcome = random.choice([
            "cause chaos and rescue the hostages in the confusion",
            "get captured in the attempt"
        ])
        print(f"\nYou {outcome}.", SUCCESS if "rescue the hostages" in outcome else FAILURE)
    else:
        print("Invalid choice. You lose!")

play_game()
