# Welcome to Grid Iron Tactics

import os
import random

def clear_screen():
    """Clears the console screen."""
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Mac and Linux (os.name is 'posix')
    else:
        os.system('clear')


def set_field(position: int) -> list:
    """Set the field with the football at the position marked by 'X'."""
    field_width = 20
    total_segments = 101
    border_segment = "+----" * field_width + "+"
    # Top boundary
    field = [border_segment]

    # Field segments
    field_segment = ""
    for i in range(total_segments):
        char = "*"
        if i == position:
            char = "X"
        elif i % 5 == 0:
            char = "|"

        field_segment += char

    field.append(field_segment)
    field.append(border_segment)
    return field


def draw_field(field: list) -> None:
    """Draws the field by printing the elements of the list."""
    for segment in field:
        print(segment)
    return None


def coin_toss():
    """Simulate a coin toss to determine initial possession."""
    print("Coin Toss! Heads or Tails?")
    choice = input("Choose Heads or Tails: ").strip().lower()
    outcome = random.choice(["h", "t"])
    print(f"The coin shows: {outcome.capitalize()}!")

    if choice == outcome:
        print("You win the toss and will start on offense!")
        return True  # 'o' for offense
    else:
        print("You lose the toss. The opponent starts on offense.")
        return False  # 'd' for defense

def display_field(position):
    """Display the game field with the ball position marked as 'X'."""
    field = ['-' for _ in range(100)]
    field[position] = 'X'
    print("".join(field))

def main():
    """Main function to run the game."""
    print("Welcome to the Grid Iron Tactics!")

    # Initialize game variables
    turns = 50
    position = 25  # Ball starts at the 25-yard line
    possession = coin_toss() # Decide who starts with the ball
    current_down = 1
    yards_to_go = 10
    player_score = 0
    computer_score = 0


    # Main Game Loop

    while turns > 0:
        current_position = set_field(position)
        draw_field(current_position)
        gain = 0
        chance = random.randint(1,100)
        print(f"\nPlayer: {player_score}\tComputer: {computer_score}")
        print(f"Turns remaining: {turns}\n{current_down} and {yards_to_go}"
              f"\t{100 - position} yards to go\n")

        if possession:
            print("You are on offense.")
            # Placeholder for function call to run through an offensive snap
            # Prompt user for their offensive play call.
            offensive_play_call = input("Do you want to Run, Pass, or Kick: ")
            # Clear the console screen
            clear_screen()
            # Change game state based on offensive outcomes
            if offensive_play_call.strip().lower() == 'r':
                gain += int(random.randint(-2,12))
                yards_to_go -= gain
                current_down += 1
                position += gain
                if chance <= 5:
                    possession = not possession
                    yards_to_go = 10
                    current_down = 1
                    print("The ball is fumbled and recovered by the defense!")
                elif gain > 0:
                    print("The offense had a gain of {} yards!".format(gain))
                elif gain == 0:
                    print("The back was stopped at the line of scrimmage.")
                else:
                    print("The back was tackled for a loss of {} yards!".format(gain))
            elif offensive_play_call.strip().lower() == 'p':
                gain += int(random.randint(-5,25))
                yards_to_go -= gain
                current_down += 1
                position += gain
                if chance <= 5:
                    possession = not possession
                    yards_to_go = 10
                    current_down = 1
                    print("The ball is intercepted by the defense!")
                elif gain > 0:
                    print("The wide receiver caught it for {} yards!".format(gain))
                elif gain == 0:
                    print("The wide receiver made it back to line to gain.")
                else:
                    print("The wide receiver was tackled for a loss of {} yards.".format(gain))
            elif offensive_play_call.strip().lower() == 'k':
                if position >= 65:
                    possession = not possession
                    yards_to_go = 10
                    current_down = 1
                    if position + chance > 125:
                        print("The kick is good!")
                        player_score += 3
                    position = 100 - position
                    print("The kick is wide! Opponent takes the field on the {} yard line.".format(position))
                elif position < 65:
                    position = (position + (chance // 2)) // 4
                    print(f"The punt was returned to the {position} yard line.")
        else:
            print("You are on defense.")
            # Placeholder for defensive decision-making logic
            # Prompt user for their defensive play call.
            defensive_play_call = input("Do you want to load the box, drop "
                                        "back, or balanced: ")
            # Clear the console screen.
            clear_screen()
            # Change game state based on defensive outcomes.
            if defensive_play_call.strip().lower() == 'l':
                gain += int(random.randint(-4,7))
                yards_to_go -= gain
                current_down += 1
                position += gain
                if chance <= 5:
                    possession = not possession
                    yards_to_go = 10
                    current_down = 1
                    print("The ball is fumbled and recovered by the defense!")
                elif gain > 0:
                    print("The running back ran it for {} yards.".format(gain))
                elif gain == 0:
                    print("The offense was stopped at the line to gain.")
                else:
                    print("The running back was tackled for a loss of {} yards.".format(gain))
            elif defensive_play_call.strip().lower() == 'd':
                gain += int(random.randint(-5,9))
                yards_to_go -= gain
                current_down += 1
                position += gain
                if chance <= 5:
                    possession = not possession
                    yards_to_go = 10
                    current_down = 1
                    print("The ball is intercepted by the defense!")
                elif gain > 0:
                    print("The wide receiver caught it for {} yard gain.".format(gain))
                elif gain == 0:
                    print("The wide receiver caught it at the line to gain.")
                else:
                    print("The wide receiver was tackled for a loss of {} yards.".format(gain))
            elif defensive_play_call.strip().lower() == 'r':
                if position >= 65:
                    possession = not possession
                    yards_to_go = 10
                    current_down = 1
                    if position + chance > 125:
                        print("The kick is good!")
                        computer_score += 3
                    position = 100 - position
                    print("The kick is wide! Opponent takes the field on the {} yard line.".format(position))
                elif position < 65:
                    position = (position + (chance // 2)) // 4
                    print(f"The punt was returned to the {position} yard line.")

        # Check if either team has scored
        if possession and position >= 100:
            player_score += 7
            possession = not possession
            print("You scored a touchdown!")
        elif not possession and position >= 100:
            computer_score += 7
            possession = not possession
            print("The opponent scored a touchdown!")

        # Change the down and distance
        if yards_to_go <= 0:
            print("First down!")
            yards_to_go = 10
            current_down = 1
        elif current_down == 5 and yards_to_go > 0:  # Turnover on downs
            print("Turnover on downs! Opponent takes over.")
            position = 100 - position  # Reverse field position
            possession = not possession
            yards_to_go = 10
            current_down = 1

        # Decrement the turn counter
        turns -= 1

    print("\nGame Over!")
    # Placeholder for determining the winner

if __name__ == "__main__":
    main()



