# Lab 3: Landscaper

def main():
    # Function to reset the game state
    def reset_game():
        return {
            'money': 0,
            'tools': {'teeth': 1},
            'earnings': {'teeth': 1, 'rusty scissors': 5, 'old-timey push lawnmower': 50, 'fancy battery-powered lawnmower': 100, 'team of starving students': 250},
            'prices': {'rusty scissors': 5, 'old-timey push lawnmower': 25, 'fancy battery-powered lawnmower': 250, 'team of starving students': 500},
            'has_team': False
        }

    # Initialize the game state
    game_state = reset_game()

    print("Welcome to the Landscaper game!")
    print("You are starting a landscaping business, but all you have are your teeth.")

    # Main game loop
    while True:
        print(f"\nYou currently have ${game_state['money']}.")
        print("What would you like to do?")
        
        # Display main menu options
        print("1. Cut the lawn and earn money.")
        print("2. Buy tools.")
        print("3. Sell tools.")
        print("4. Reset game.")
        print("5. Quit the game.")
        
        # Get user's choice
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            # Calculate daily earnings based on owned tools
            daily_earnings = sum(game_state['earnings'][tool] * count for tool, count in game_state['tools'].items())
            game_state['money'] += daily_earnings
            print(f"\nYou cut the lawn and earned ${daily_earnings}. You now have ${game_state['money']}.")
        elif choice == '2':
            # Display tools available for purchase
            print("\nTools available for purchase:")
            for tool, price in game_state['prices'].items():
                if tool not in game_state['tools']:
                    print(f"{tool}: ${price}")
            tool_choice = input("Enter the tool you want to buy: ").lower()
            # Buy the chosen tool if affordable
            if tool_choice in game_state['prices'] and game_state['money'] >= game_state['prices'][tool_choice]:
                game_state['money'] -= game_state['prices'][tool_choice]
                if tool_choice in game_state['tools']:
                    game_state['tools'][tool_choice] += 1
                else:
                    game_state['tools'][tool_choice] = 1
                print(f"\nYou bought {tool_choice} for ${game_state['prices'][tool_choice]}.")
                if tool_choice == 'team of starving students':
                    game_state['has_team'] = True
            else:
                print("\nYou don't have enough money to buy that tool or it is not available.")
        elif choice == '3':
            # Display tools available for sale
            print("\nTools available for sale:")
            for tool, count in game_state['tools'].items():
                if tool != 'teeth' and count > 0:
                    print(f"{tool}: ${game_state['prices'][tool] // 2} (You have {count})")
            tool_choice = input("Enter the tool you want to sell: ").lower()
            # Sell the chosen tool if owned
            if tool_choice in game_state['tools'] and game_state['tools'][tool_choice] > 0:
                game_state['tools'][tool_choice] -= 1
                game_state['money'] += game_state['prices'][tool_choice] // 2
                if game_state['tools'][tool_choice] == 0:
                    del game_state['tools'][tool_choice]
                print(f"\nYou sold {tool_choice} for ${game_state['prices'][tool_choice] // 2}.")
            else:
                print("\nYou don't have that tool to sell.")
        elif choice == '4':
            # Reset the game state
            game_state = reset_game()
            print("\nThe game has been reset.")
        elif choice == '5':
            # Quit the game
            print(f"\nThank you for playing! You ended with ${game_state['money']}.")
            break
        else:
            print("\nInvalid choice. Please enter a valid number.")

        # Check for win condition
        if game_state['has_team'] and game_state['money'] >= 1000:
            print(f"\nCongratulations! You've won the game with a team of starving students and ${game_state['money']}!")
            break

if __name__ == "__main__":
    main()