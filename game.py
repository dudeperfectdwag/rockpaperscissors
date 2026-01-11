import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def dramatic_countdown():
    print("\n\033[93mRock...\033[0m", end="", flush=True)
    time.sleep(1)
    print("\n\033[96mPaper...\033[0m", end="", flush=True)
    time.sleep(1)
    print("\n\033[95mScissors...\033[0m", end="", flush=True)
    time.sleep(1)
    print("\n\033[91mSHOOT!\033[0m\n", flush=True)
    time.sleep(0.8)

def print_rules():
    print("\n" + "="*60)
    print("         ROCK PAPER SCISSORS LIZARD SPOCK - ROAST EDITION 🔥")
    print("="*60)
    print("\nHow to play:")
    print("  • Classic:")
    print("    ✂ Scissors cuts 📄 Paper")
    print("    📄 Paper covers 🪨 Rock")
    print("    🪨 Rock crushes ✂ Scissors")
    print("\n  • Lizard & Spock:")
    print("    🪨 Rock crushes 🦎 Lizard")
    print("    🦎 Lizard poisons 🖖 Spock")
    print("    🖖 Spock smashes ✂ Scissors")
    print("    🖖 Spock vaporizes 🪨 Rock")
    print("    🦎 Lizard eats 📄 Paper")
    print("    📄 Paper disproves 🖖 Spock")
    print("    ✂ Scissors decapitates 🦎 Lizard")
    print("\nEach choice beats 2 others and loses to 2 others.")
    print("Type 'q' to quit anytime.\n" + "="*60 + "\n")

def main():
    clear_screen()
    print_rules()

    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    emojis = {
        'rock': '🪨', 'paper': '📄', 'scissors': '✂️',
        'lizard': '🦎', 'spock': '🖖'
    }

    roasts = [
        "Brutal execution 💀",
        "You got Vulcan nerve pinched",
        "Lizard ate your lunch",
        "Folded like cheap origami",
        "Rock crushed your dreams",
        "Spock mind-melded your brain",
        "Scissors snipped your hopes",
        "Ultimate skill issue detected",
        "Computer lives rent-free in your head",
        "Even the multiverse is laughing"
    ]

    win_phrases = [
        "GOD MODE ACTIVATED 🔥",
        "You're unstoppable fr",
        "Computer is uninstalling itself",
        "Peak strat execution",
        "Lizard/Spock MVP",
        "History made today",
        "You're the chosen one",
        "Absolute domination 😈"
    ]

    player_score = 0
    computer_score = 0

    while True:
        print(f"\n\033[1mScore → You: {player_score}  |  Computer: {computer_score}\033[0m")
        player_input = input("\nYour move (rock/paper/scissors/lizard/spock) or 'q' to quit: ").strip().lower()

        if player_input == 'q':
            print("\nYou ragequit? Understandable.")
            print(f"Final score: You {player_score} - Computer {computer_score}")
            if player_score > computer_score:
                print("You somehow survived... suspicious 🤨")
            elif player_score < computer_score:
                print("Computer owned you. As expected.")
            else:
                print("Tie? Both equally trash.")
            print("Come back when you're ready to get roasted again 😈\n")
            break

        if player_input not in choices:
            print("That's not a valid move bro... try again 😂")
            time.sleep(1.5)
            continue

        print(f"\nYou chose: {emojis[player_input]} {player_input.capitalize()}")
        dramatic_countdown()

        computer_choice = random.choice(choices)
        print(f"Computer chose: {emojis[computer_choice]} {computer_choice.capitalize()}\n")

        if player_input == computer_choice:
            print("Tie! Both mid 🤝💩")
        elif (
            (player_input == 'rock' and computer_choice in ['scissors', 'lizard']) or
            (player_input == 'paper' and computer_choice in ['rock', 'spock']) or
            (player_input == 'scissors' and computer_choice in ['paper', 'lizard']) or
            (player_input == 'lizard' and computer_choice in ['paper', 'spock']) or
            (player_input == 'spock' and computer_choice in ['rock', 'scissors'])
        ):
            player_score += 1
            print(random.choice(win_phrases))
        else:
            computer_score += 1
            print(random.choice(roasts))

        time.sleep(2)  # Short pause before next round
        clear_screen()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nLater loser... 👋")\



