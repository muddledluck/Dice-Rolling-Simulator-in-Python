import random

print("This is Dice Rolling Simulator, roll the dice until you get your choice!!! \nTo Quit press \" q \" and to continue to play Press any key !!!!!!!!! \nEnjoy :) \n")
while True:
    dice = random.randrange(1, 7)
    print(f"And the Outcome is: {dice} \n")
    print("Continue or Quit: ", end = "")
    user_input = input()            # Get user input
    if user_input == "q" or user_input == "Q":
        print("Thanks for rolling a dice :)")           # Printing a thankyou massage
        break
    else:
        print("\n \n")          #To make two line change
        continue
