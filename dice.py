import random

print("This is Dice Rolling Simulator, roll the dice until you get your choice!!! \nTo Quit press \" q \" and to continue to play Press any key !!!!!!!!! \nEnjoy :) \n")
while True:
    dice = random.randrange(1, 7)
    print(f"And the Outcome is: {dice} \n")
    print("Continue or Quit: ", end = "")
    user_input = input()
    if user_input == "q" or user_input == "Q":
        print("Thanks for rolling a dice :)")
        break
    else:
        print("\n \n")
        continue
