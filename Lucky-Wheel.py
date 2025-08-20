
import random

def Lucky_Wheel():
    # initialisation
    balance = 10000 # player's initial balance
    print()
    print("-----------------------------------------------------------------------------")
    print("*******************| | welcome to the Lucky Wheel Game | |*******************".upper())
    print("-----------------------------------------------------------------------------\n")

    print(f"your initial balance is : $ {balance}.")

    while balance > 0:
        # ask for bet and choice
        try:
            print()
            bet = int(input("How much do you bet ?...: "))
            if bet > balance:
                print()
                print("Bet too high ! you don't have enough.\n")
                continue
            print()
            choice = int(input("choose a number between 1 and 6: "))
            if choice < 1 or choice > 6:
                print()
                print("Invalid number. Choose between 1 and 6.\n")
                continue
        except ValueError:
            print()
            print("please enter a valid number.")
            continue

        # Spin the wheel
        wheel = random.randint(1, 6)
        print()
        print(f"the wheel spins... and stops on {wheel} !.\n")

        # check result
        if choice == wheel:
            winnings = bet * choice
            print(f"congratulation ! you win $ {winnings}.🥳🥳\n")
            balance += winnings
        else:
            print("Sorry, you lose your bet.😥😥\n")
            balance -= bet

        # Show balance
        print(f"your new balance: $ {balance}.\n")

        # ask if player wants to continue
        continue_playing = input("Do you want to continue ?...(y/n): ")
        if continue_playing != 'y':
            print()
            print("Alright ! see you next time 😊🤖\n")
            print("-------------------------------------------------")
            print("*******************| | END | |*******************")
            print("-------------------------------------------------\n")
            break

    # End of game
    if balance <= 0:
        print("you exhausted your balance. Come back another time.\n")
        print("-------------------------------------------------")
        print("*******************| | END | |*******************")
        print("-------------------------------------------------\n")

# Luanch the game
Lucky_Wheel()