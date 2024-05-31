# Lab 3: Landscaper

def main():
    money = 0
    tools = ['teeth']
    earnings = {'teeth': 1, 'rusty scissors': 5}
    has_scissors = False
    
    print("Welcome to the Landscaper game!")
    print("You are starting a landscaping business, but all you have are your teeth.")
    
    while True:
        print(f"\nYou currently have ${money}.")
        print("What would you like to do?")
        print("1. Cut the lawn with your teeth and earn $1.")
        if not has_scissors:
            print("2. Buy a pair of rusty scissors for $5.")
        else:
            print("2. Cut the lawn with your rusty scissors and earn $5.")
        print("3. Quit the game.")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            money += earnings['teeth']
            print(f"\nYou cut the lawn with your teeth and earned $1. You now have ${money}.")
        elif choice == '2':
            if not has_scissors:
                if money >= 5:
                    money -= 5
                    tools.append('rusty scissors')
                    has_scissors = True
                    print("\nYou bought a pair of rusty scissors for $5.")
                else:
                    print("\nYou don't have enough money to buy the rusty scissors.")
            else:
                money += earnings['rusty scissors']
                print(f"\nYou cut the lawn with your rusty scissors and earned $5. You now have ${money}.")
        elif choice == '3':
            print(f"\nThank you for playing! You ended with ${money}.")
            break
        else:
            print("\nInvalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main()