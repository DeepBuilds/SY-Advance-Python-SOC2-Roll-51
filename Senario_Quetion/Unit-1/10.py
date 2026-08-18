#10. Cricket Team Management System
class Player:
    def __init__(self, name, jersey, runs):
        self.name = name
        self.jersey = jersey
        self.runs = runs

        if runs >= 1000:
            self.category = "Excellent"
        elif runs >= 500:
            self.category = "Good"
        else:
            self.category = "Average"

    def display(self):
        print("Player Name:", self.name)
        print("Jersey Number:", self.jersey)
        print("Runs:", self.runs)
        print("Category:", self.category)
        print("------------------------")


class Team:
    def __init__(self):
        self.players = []

    def add_player(self):
        name = input("Enter Player Name: ")
        jersey = int(input("Enter Jersey Number: "))
        runs = int(input("Enter Runs: "))

        player = Player(name, jersey, runs)
        self.players.append(player)
        print("Player added successfully.")

    def display_all(self):
        if not self.players:
            print("No players available.")
        else:
            print("\n--- All Player Details ---")
            for player in self.players:
                player.display()


# Main program
team = Team()

while True:
    print("\n1. Add Player")
    print("2. Display All Players")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        team.add_player()
    elif choice == "2":
        team.display_all()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")

'''

1. Add Player
2. Display All Players
3. Exit
Enter your choice: 1
Enter Player Name: Karan 
Enter Jersey Number: 4
Enter Runs: 50
Player added successfully.

1. Add Player
2. Display All Players
3. Exit
Enter your choice: 1
Enter Player Name: Sachin 
Enter Jersey Number: 7
Enter Runs: 100
Player added successfully.

1. Add Player
2. Display All Players
3. Exit
Enter your choice: 2

--- All Player Details ---
Player Name: Karan
Jersey Number: 4
Runs: 50
Category: Average
------------------------
Player Name: Sachin
Jersey Number: 7
Runs: 100
Category: Average
------------------------
1. Add Player
2. Display All Players
3. Exit
Enter your choice: 4
Invalid choice.

1. Add Player
2. Display All Players
3. Exit
Enter your choice: 3
'''