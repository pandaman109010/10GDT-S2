import msvcrt
import time
from os import system, name


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def get_input(prompt, input_type):
    while True:
        try:
            value = input_type(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def shape():
    choices = {
        '1': "Square",
        '2': "Rectangle",
        '3': "Circle"
    }
    print("Choose a shape by typing the corresponding number:\n1. Square\n2. Rectangle\n3. Circle")
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice in choices:
            return choice
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

while True:
    # Call the shape function and store the returned choice
    clear()
    selected_shape = shape()

    # Initialize variables
    first_num = None
    second_num = None
    radius = None

    # Get the necessary inputs based on the selected shape
    if selected_shape == '1':
        first_num = get_input("Enter the length of one side of your square in cm: ", float)
    elif selected_shape == '2':
        first_num = get_input("Enter the length of the first side of your rectangle in cm: ", float)
        second_num = get_input("Enter the length of the second side of your rectangle in cm: ", float)
    elif selected_shape == '3':
        radius = get_input("Enter the radius of your circle in cm: ", float)

    # Use the selected_shape variable later in your code
    if selected_shape == '1':
        print("You selected Square.")
        print("Calculating...")
        time.sleep(0.5)
        area = first_num ** 2
        perimeter = 4 * first_num
        print(f"The area of your square is {area:.2f} cm²")
        print(f"The perimeter of your square is {perimeter:.2f} cm")
    elif selected_shape == '2':
        print("You selected Rectangle.")
        print("Calculating...")
        time.sleep(0.5)
        area = first_num * second_num
        perimeter = 2 * (first_num + second_num)
        print(f"The area of your rectangle is {area:.2f} cm²")
        print(f"The perimeter of your rectangle is {perimeter:.2f} cm")
    elif selected_shape == '3':
        print("You selected Circle.")
        print("Calculating...")
        time.sleep(0.5)
        area = 3.14159 * radius ** 2
        perimeter = 2 * 3.14159 * radius
        print(f"The area of your circle is {area:.2f} cm²")
        print(f"The perimeter of your circle is {perimeter:.2f} cm")
        print(f"Radius: {radius:.2f} cm")

    print("Press any key to enter another shape or Enter to exit.")
    if msvcrt.getch() == b'\r':  # Check if Enter key is pressed
        break