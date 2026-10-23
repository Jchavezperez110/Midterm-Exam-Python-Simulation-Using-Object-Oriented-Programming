# JJBA Character Roster Simulator
# Introduction to Programming Midterm

# Class 1: Represents a JJBA character
class Character:

    def __init__(self, name, stand, power):
        self.name = name
        self.stand = stand
        self.power = power

    def display_info(self):
        print("\nCharacter:", self.name)
        print("Stand:", self.stand)
        print("Power:", self.power)

    def battle(self):
        print(self.name, "uses", self.stand + "!")


# Class 2: Manages the game
class Game:

    def __init__(self):
        self.characters = [
            Character("Jotaro Kujo", "Star Platinum", 95),
            Character("Johnny Joestar", " Tusk", 100),
            Character("Jolyne Cujoh", "Stone Free", 80),
            Character("Josuke Higashikata", "Crazy Diamond", 90),
            Character("Giorno Giovanna", "Gold Experience", 95)
        ]

    # Display the main menu with character names
    def show_menu(self):
        print("\n===== JJBA CHARACTER SIMULATOR =====")
        print("1. Jotaro Kujo")
        print("2. Johnny Joestar")
        print("3. Jolyne Cujoh")
        print("4. Josuke Higashikata")
        print("5. Giorno Giovanna")
        print("6. Exit")

    # Run the game
    def run(self):
        while True:
            self.show_menu()
            choice = input("\nChoose a character (1-5) or exit (6): ")

            if choice.isdigit() and 1 <= int(choice) <= 5:
                character = self.characters[int(choice) - 1]

                print("\nYou selected", character.name)
                print("1. View Character Information")
                print("2. Use Stand Ability")

                action = input("Choose an action (1-2): ")

                if action == "1":
                    character.display_info()
                elif action == "2":
                    character.battle()
                else:
                    print("Invalid action.")

            elif choice == "6":
                print("Thanks for playing!")
                break

            else:
                print("Invalid choice. Please try again.")


# Start the program
game = Game()
game.run()
