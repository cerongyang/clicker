

import time

clicks = 0
current_clickpower = 1
win = 0

print("Welcome to Enter Presser!")
input("Press Enter to begin!")
print()
print("Press S to see the current amount of money.")
print("Press U to buy an upgrade.")
print("Press P to prestige.")
print("Press W to check if you are a winner.")
print("Press Enter to increase your amount of money by 1 to start with.")
print("Autopress increases your current money by the power of your autopress automatically.")

def upgrade_store():
    print("1: +1 click upgrade")
    print("2: +1 autoclick")
    print("", end = "")

def prestige():
    pass

def save():
    pass

def win():
    pass

def main():
    while win != 1:
        a = input()
        a = a.lower()
        if a == "s":
            print(f"Current amount of money = £{clicks}")
        if a == "u":
            upgrade_store()
        if a == "p":
            prestige()
        main()
        return clicks + current_clickpower


if __name__ == "__main__":
    main()
