def get_player_name():
    # Ask the player for their name and return it
    name = input("Enter your name: ")
    return name

def get_player_choice():
    # Ask the player for their choice (e.g., "left" or "right") and return it
    choice = input("Choose a path (left or right): ")
    return choice

def print_message(name, choice):
    # Print a message that includes the player's name and chosen path
    print(f"{name}, you have chosen the {choice} path.")

    # Print different outcomes based on the player's choice
    if choice.lower() == "left":
        print("You encounter a dragon!")
    elif choice.lower() == "right":
        print("You find a treasure chest!")
    else:
        print("Invalid choice. Please choose 'left' or 'right'.")

def main():
    # Use the above functions to get the player's name and choice, and print the message
    name = get_player_name()

    # Annotate this code chunk
    while True:
      choice = get_player_choice()
      print_message(name, choice)
      
      play_again = input("Do you want to play again? (yes/no): ")
      if play_again.lower() != "yes":
          break

    print("Thanks for playing!")

# Call the main function to start the game
if __name__ == "__main__":
    main()