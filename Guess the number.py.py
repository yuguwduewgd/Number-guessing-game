import random
import os
import time

def guess_the_number():
    """
    A simple 'Guess the Number' game with a simulated dark theme.
    """
    # ANSI escape codes for dark theme (might not work in all terminals)
    # Background Black, Foreground Green for contrast
    BG_BLACK = "\033[40m"
    FG_GREEN = "\033[32m"
    FG_CYAN = "\033[36m"
    FG_YELLOW = "\033[33m"
    RESET = "\033[0m" # Resets all formatting

    # Clear terminal (OS-dependent)
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{BG_BLACK}{FG_CYAN}=========================================={RESET}")
    print(f"{BG_BLACK}{FG_CYAN}  Welcome to Guess the Number! (Dark Mode){RESET}")
    print(f"{BG_BLACK}{FG_CYAN}=========================================={RESET}")
    print(f"{BG_BLACK}{FG_GREEN}I'm thinking of a number between 1 and 100.{RESET}")
    print(f"{BG_BLACK}{FG_GREEN}Can you guess it?{RESET}")
    print(f"{BG_BLACK}{FG_CYAN}------------------------------------------{RESET}")


    secret_number = random.randint(1, 100)
    guesses_taken = 0

    while True:
        try:
            guess_input = input(f"{BG_BLACK}{FG_YELLOW}Take a guess: {RESET}")
            guess = int(guess_input)
            guesses_taken += 1

            if guess < secret_number:
                print(f"{BG_BLACK}{FG_GREEN}Your guess is too low.{RESET}")
            elif guess > secret_number:
                print(f"{BG_BLACK}{FG_GREEN}Your guess is too high.{RESET}")
            else:
                print(f"{BG_BLACK}{FG_GREEN}Good job! You guessed my number in {guesses_taken} guesses!{RESET}")
                print(f"{BG_BLACK}{FG_YELLOW}------------------------------------------{RESET}")
                break
        except ValueError:
            print(f"{BG_BLACK}{FG_GREEN}That's not a valid number. Please enter an integer.{RESET}")

        # Add a small delay for better readability in dark mode
        time.sleep(0.5)

    # Reset colors before the final message if the terminal doesn't handle it automatically
    print(f"{RESET}")

if __name__ == "__main__":
    guess_the_number()

    # This is where the "hyper-realistic" visual comes in (as an image)
    print("Here's your hyper-realistic credit graphic:")
    # The image generation model will create the requested image here.
    # The description for the image will be inferred from the surrounding text.