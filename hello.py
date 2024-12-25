import random
import time
import sys
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def falling_stripes():
    # Get terminal dimensions
    width = 80  # Assuming standard console width
    height = 20  # Adjust as needed

    # Set the phrase to display
    text = "Open University of Sri Lanka"
    center_x = width // 2 - len(text) // 2
    center_y = height // 2

    # Create a list of columns for the falling effect
    columns = list(range(width))

    # Main loop for falling stripes effect
    try:
        while True:
            # Randomly select a column for a stripe
            stripe_column = random.choice(columns)
            stripe_height = random.randint(1, height - 1)

            # Print the falling stripe
            sys.stdout.write(f"\033[{stripe_height};{stripe_column}H{Fore.GREEN}|")
            sys.stdout.flush()

            # Print the main text in the center
            sys.stdout.write(f"\033[{center_y};{center_x}H{Fore.YELLOW}{text}")
            sys.stdout.flush()

            # Pause for a short time to make the effect visible
            time.sleep(0.1)

            # Clear the screen after each iteration (to simulate falling effect)
            sys.stdout.write("\033[2J")
            sys.stdout.flush()

    except KeyboardInterrupt:
        print("Exiting...")

# Start the falling stripes effect
falling_stripes()
