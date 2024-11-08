#calculating the costs of fences
#auther: panda
#date: 2024-11-1
#version: 3.0 //fixed spelling errors and added a title to the console
#py version: v2024.16.1
#os: windows 11'
#note: this is a simple program that calculates the cost of a fence based on the area and perimeter of the fence. it is a simple program that i made for my python class. i hope you enjoy it. i will be updating it in the future to make it better and more user friendly. thank you for using my program. i hope you enjoy it.

import msvcrt
import time
from os import system, name
import ctypes
def clear(): # i found this at one point and use it in all my code to clear the screen
    
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def get_input(prompt, input_type): # this function is used to get the input from the user and check if it is a valid number to calculate the area and perimeter
    while True:
        try:
            value = input_type(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while True: # this is the main loop that runs the program
    clear() #clears the screen and sets the title of the console
    ctypes.windll.kernel32.SetConsoleTitleW("Fence cost calculator:    Made with love by Panda <3")


    print("Welcome to the fence cost calculator!")
    print("Please enter the following information to calculate the cost of your fence.")
    print("")


    length = get_input("Enter the length of the fence in m: ", float) #this chunk fines the numbers it needs to calculate the cost of the fence
    width = get_input("Enter the width of the fence in m: ", float)
    cost_per_meter = get_input("Enter the cost per meter of the fence in $: ", float)
    perimeter = 2 * (length + width)# does the math
    total_cost = perimeter * cost_per_meter


    print(f"The total cost of your fence is ${total_cost} and the perimeter of your fence is {perimeter}")#prints the cost of the fence
    print("")


    print("Press any key to calculate another fence or press 'Enter' to quit.")#this is the end of the program
    if msvcrt.getch() == b'\r':  # Check if Enter key is pressed
        break

