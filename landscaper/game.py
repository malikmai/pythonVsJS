# Lab 3: Landscaper

def main():
    money = 0
    tools = ['teeth']
    earnings = {'teeth': 1}

    print("Welcome to Landscaper!")
    print("You are starting a landscaping business, but all you have are your teeth.")

    while True:
        print(f"\nYou currently have ${money}.")
        print("What would you like to do?")
        print("1. Cut the lawn with your teeth and earn $1.")
        print("2. Quit the game.")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            money += earnings['teeth']
            print(f"\nYou cut the lawn with your teeth and earned $1. You now have ${money}.")
        elif choice == '2':
            print(f"\nThank you for playing! You ended with ${money}.")
            break
        else:
            print("\nInvalid choice. Please enter 1 or 2.")
    
if __name__ == "__main__":
    main()