# this is a bit calculater
# tbh idk what that does or how it works, just following what the powerpoint says
#calculating the costs of fences
#auther: panda
#date: 2024-11-1
#version: 8.0 //added more comments
#py version: v2024.16.1
#os: windows 11'

import os   #for history
import shutil
import msvcrt
import time
import ctypes  # sets the title of the console

# Set the title of the console
ctypes.windll.kernel32.SetConsoleTitleW("bit calculator:   Made with love by Panda <3")

# Check if history.log exists, if not, create it
if not os.path.exists('history.log'):
    with open('history.log', 'w') as file:
        file.write('\n---History---\n')

# definitions
def clear(): #clears the screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered(text): #prints text in the senter ralative to the border of the window
    columns = shutil.get_terminal_size().columns
    print(text.center(columns))

def get_centered_input(prompt): #uses the funtion above for inputs
    """Prints a centered prompt and gets input from the user."""
    print_centered(prompt)
    return input().strip()

def get_input(prompt, input_type): #better error checker
    """Gets input from the user and checks if it is a valid number."""
    while True:
        try:
            value = input_type(get_centered_input(prompt))
            if value > 0:
                return value
            else:
                print_centered("Please enter a number greater than 0.")
        except ValueError:
            print_centered("Invalid input. Please enter a valid number.")

def shape_type(): #the menu and check for the shape type
    """Gets the shape that the user wants to calculate the area and perimeter of."""
    choices = {
        '1': "Integer",
        '2': "Text",
        '3': "Image"
    }
    print_centered("Choose a type by typing the corresponding number:\n1. Integer\n2. Text\n3. Image")
    while True:
        choice = get_centered_input("").strip()
        if choice in choices:
            return choice
        else:
            print_centered("Invalid input. Please enter 1, 2, or 3.")

def add_to_history(*args): #adds your past questions to the .log file
    with open('history.log', 'a') as file:
        if len(args) == 2:
            file.write(f'input = {args[0]},  bits needed = {args[1]}\n')
        elif len(args) == 3:
            file.write(f'input = {args[0]}x{args[1]},  bits needed = {args[2]}\n')

def calculate_bits(first_num, second_num): #calculates the bits
    bits_needed = first_num * second_num * 24
    print_centered(f'Bits needed: {bits_needed}')
    return bits_needed



clear()
instructions = input("Do you want to see the instructions? (y/n): ")
if instructions == 'y':
    time.sleep(0.4)
    print_centered("---Instructions---")
    print_centered("Welcome to my bit calculater!")
    print_centered("You can calculate the bits needed for a square, text, or image.")
    print("")
    print_centered("To calculate the bits needed for a square, enter the length of one side of the square.")
    print_centered("To calculate the bits needed for text, enter the text you want to calculate the bits of.")
    print_centered("it can be more then one word")
    print_centered("To calculate the bits needed for an image, enter the width and height of the image.")
    time.sleep(0.2)
    print("")
    os.system('pause')
    clear()
elif instructions == 'n':
    print("")
    print_centered("Welcome to my bit calculater!")
    print_centered("please enter the information to calculate the bits needed for your shape/int/text.")
    print("")

while True:  # Main loop
    show_history = input("Do you want to see the history? (y/n): ")
    if show_history.lower() == 'y':
        with open('history.log', 'r') as file:
            for line in file:
                print_centered(line.strip())
        print_centered("Press any key to calculate another bit or press Enter to exit.")
        if msvcrt.getch() == b'\r':  # Check if Enter key is pressed
            break
    
    elif show_history.lower() == 'n':
        pass

    clear()
    print_centered('Welcome to my bit calculator!')
    print_centered('Please enter the following information to calculate the bits needed.\n')

    picked_type = shape_type()

    # Initialize variables
    num = None
    text = None
    first_num = None
    second_num = None

    # Get the necessary inputs based on the selected type
    if picked_type == '1':  # this is the int input
        clear()
        print_centered('You picked Integer')
        num = get_input('Enter your number: ', int)
#        add_to_history(num)  # Add to history for integer input
    elif picked_type == '2':  # this is the text input
        clear()
        print_centered('You picked Text')
        text = get_centered_input("Enter the text you want to calculate the bits of: ")
#        add_to_history(text)  # Add to history for text input
    elif picked_type == '3':  # this is the image input
        clear()
        print_centered('You picked Image')
        first_num = get_input('Enter the width of the image: ', int)
        second_num = get_input('Enter the height of the image: ', int)
#        add_to_history(first_num, second_num)  # Add to history for image input

    # Calculate and display the results
    if picked_type == '1':  # this is the int calculation
        binary_num = bin(num)
        print_centered(f'Calculating the bits for the number {num}...')
        print_centered(f'Bits needed: {len(binary_num) - 2}')
        add_to_history(num, len(binary_num) - 2)
    elif picked_type == '2':  # this is the text calculation
        print_centered(f'Calculating the bits for the text "{text}"...')
        bits_needed = len(text) * 8
        print_centered(f'Bits needed: {bits_needed}')
        add_to_history(text, bits_needed)
    elif picked_type == '3':  # this is the image calculation
        print_centered(f'Calculating the bits needed for a {first_num}x{second_num} image...')
        bits_needed = calculate_bits(first_num, second_num)
        add_to_history(first_num, second_num, bits_needed)
    print_centered("Press any key to calculate another bit or press Enter to exit.")
    if msvcrt.getch() == b'\r':  # Check if Enter key is pressed
        break