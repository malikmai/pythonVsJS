# Lab 3: Landscaper

def main():
    money = 0
    tools = ['teeth']
    earnings = {'teeth': 1, 'rusty scissors': 5, 'old-timey push lawnmower': 50, 'fancy battery-powered lawnmower': 100}
    has_scissors = False
    has_lawnmower = False
    has_fancy_lawnmower = False
    
    print("Welcome to the Landscaper game!")
    print("You are starting a landscaping business, but all you have are your teeth.")
    
    while True:
        print(f"\nYou currently have ${money}.")
        print("What would you like to do?")
        
        # Display options based on the tools the player has
        print("1. Cut the lawn with your teeth and earn $1.")
        if has_scissors:
            print("2. Cut the lawn with your rusty scissors and earn $5.")
        if has_lawnmower:
            print("3. Cut the lawn with your old-timey push lawnmower and earn $50.")
        if has_fancy_lawnmower:
            print("4. Cut the lawn with your fancy battery-powered lawnmower and earn $100.")
        
        # Conditional buying options
        if not has_scissors:
            print("5. Buy a pair of rusty scissors for $5.")
        elif not has_lawnmower:
            print("5. Buy an old-timey push lawnmower for $25.")
        elif not has_fancy_lawnmower:
            print("5. Buy a fancy battery-powered lawnmower for $250.")
        
        print("6. Quit the game.")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            money += earnings['teeth']
            print(f"\nYou cut the lawn with your teeth and earned $1. You now have ${money}.")
        elif choice == '2' and has_scissors:
            money += earnings['rusty scissors']
            print(f"\nYou cut the lawn with your rusty scissors and earned $5. You now have ${money}.")
        elif choice == '3' and has_lawnmower:
            money += earnings['old-timey push lawnmower']
            print(f"\nYou cut the lawn with your old-timey push lawnmower and earned $50. You now have ${money}.")
        elif choice == '4' and has_fancy_lawnmower:
            money += earnings['fancy battery-powered lawnmower']
            print(f"\nYou cut the lawn with your fancy battery-powered lawnmower and earned $100. You now have ${money}.")
        elif choice == '5' and not has_scissors:
            if money >= 5:
                money -= 5
                tools.append('rusty scissors')
                has_scissors = True
                print("\nYou bought a pair of rusty scissors for $5.")
            else:
                print("\nYou don't have enough money to buy the rusty scissors.")
        elif choice == '5' and has_scissors and not has_lawnmower:
            if money >= 25:
                money -= 25
                tools.append('old-timey push lawnmower')
                has_lawnmower = True
                print("\nYou bought an old-timey push lawnmower for $25.")
            else:
                print("\nYou don't have enough money to buy the old-timey push lawnmower.")
        elif choice == '5' and has_lawnmower and not has_fancy_lawnmower:
            if money >= 250:
                money -= 250
                tools.append('fancy battery-powered lawnmower')
                has_fancy_lawnmower = True
                print("\nYou bought a fancy battery-powered lawnmower for $250.")
            else:
                print("\nYou don't have enough money to buy the fancy battery-powered lawnmower.")
        elif choice == '6':
            print(f"\nThank you for playing! You ended with ${money}.")
            break
        else:
            print("\nInvalid choice. Please enter a valid number.")
        
if __name__ == "__main__":
    main()