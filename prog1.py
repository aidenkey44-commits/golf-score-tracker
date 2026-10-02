choice = ""

rounds = []

file = open("rounds.txt", "r")
for line in file:
    course, score = line.strip().split(" - ")
    rounds.append([course, int(score)])
file.close()

while choice != "6":
    print("=== Golf Round Tracker ===")
    print("1. Add Round")
    print("2. View Rounds")
    print("3. Average Score")
    print("4. Best Round")
    print("5. Worst Round")
    print("6. Exit")

    choice = input("Choose an Option: ")

    if choice == "1":
        course = input("What course did you play today? ")
        score = int(input("What did you shoot/score at " + course + " today? "))
        rounds.append([course, score])
        file = open("rounds.txt", "a")
        file.write(f"{course} - {score}\n")
        file.close()

        print("Thank you for confirming your score with us, if you would like to double-check your scoring history, please see option 2 in the menu.")

    elif choice == "2":
        print("Here are your previous rounds: ")
        for round_data in rounds:
            print(f"{round_data[0]} - {round_data[1]}")

    elif choice == "3":
        if len(rounds) == 0:
            print("there are no rounds in your records.")
        else:
            total = 0
            for round_data in rounds:
                total = total + round_data[1]

            avg = total / len(rounds)

            print(f"Your average score is {avg}")
    elif choice == "4":
        if len(rounds) == 0:
            print("there are no rounds in your records.")
        else:
            best = rounds[0][1]
            for round_data in rounds:
                if round_data[1] < best:
                    best = round_data[1]
        print(f"Your best score is {best}")
    elif choice == "5":
        if len(rounds) == 0:
            print("there are no rounds in your records.")
        else:
            worst = rounds[0][1]
            for round_data in rounds:
                if round_data[1] > worst:
                    worst = round_data[1]
        print(f"Your worst score is {worst}")

    elif choice == "6":
        print("Have a good one!")
    else:
        print("That is not an option, please try again.")
