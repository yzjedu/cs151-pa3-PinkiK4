# Programmed by Krishon Pinkins
# Loyola CS151, Professor Zee
# Due Date: November 7, 2024
# Programming Assignment: 03

# The purpose of this code was to design a display for user-input line art, random art, and circle art

# Import random module into the code
import random

# Purpose:  [run the main code]
# Parameters: [NONE]
# Return: [NONE]
def main():
# Collects user's input, converts it to lowercase, and strips it of whitespace
    user_option = input("Please enter your choice of design (circle, random, or line):")
    user_option = user_option.lower().strip()
# If user inputs an incorrect value, code will continue to ask for proper input
    while user_option != 'circle' and user_option != 'random' and user_option != 'line':
        print('Invalid input, please try again.')
        user_option = input("Please enter your choice of design (circle, random, or line):")
# Invokes functions circle_drawing, line_drawing, and random_drawing
    circle_drawing(user_option)
    line_drawing(user_option)
    random_drawing(user_option)

# Purpose:  [Output the circle art]
# Parameters: [the user's option]
# Return: [NONE]
def circle_drawing(user_option):
    if user_option == "circle":
        print(f'{"x"*2:^19}\n{"x":>5}{"x":>9}\n'
              f'{"x":>3}{"x":>13}\n{"x":>3}{"x":>13}\n{"x":>5}{"x":>9}\n{"x"*2:^19}')
        return

# Purpose:  [Collect user's input about the design to generate and output the line art]
# Parameters: [the user's option]
# Return: [NONE]
def line_drawing(user_option):
    if user_option == "line":
# Collects user's input, converts it to lowercase, and strips it of whitespace
        line_character = input("Please enter a character to draw line: ")
        line_character = line_character.lower().strip()
# Collects user's input and strips it of whitespace
        character_occ = input("How many characters do you want per line?: ")
        character_occ = character_occ.strip()
# If user input is not a digit, code will continue to ask for proper input
        while not character_occ.isdigit():
            print('Invalid input, please try again.')
            character_occ = input("How many characters do you want per line?: ")
        character_occ = int(character_occ)
# Collects user's input and strips it of whitespace
        line_num = input("How many lines do you want?: ")
        line_num = line_num.strip()
# If user input is not a digit, code will continue to ask for proper input
        while not line_num != line_num.isdigit():
            print('Invalid input, please try again.')
            line_num = input("How many lines do you want?: ")
            line_num = int(line_num)
# Continues to output new lines of characters chosen by the user at the amount the user chose
        line_num = int(line_num)
        for i in range(1, line_num+1):
            print(f'{line_character * character_occ}', end='\n')

# Purpose:  [Output random art]
# Parameters: [the user's option]
# Return: [NONE]
def random_drawing(user_option):
    if user_option == "random":
# Assign a variable to random module to output random number
        random_draw = random.randint(1, 3)
# Assigns each number in range to different art pieces
        if random_draw == 1:
            print(f'{",":>2}{",":>6}')
            print(" )\___/(")
            print("{(@)v(@)}")
            print(" {|~~~|}")
            print(' {/^^^\}')
            print(f'{"`m-m`":>7}')
        elif random_draw == 2:
            print(f' {"*"*20}')
            asterisk_list = '***********'
            for char in asterisk_list:
                print(f'{char}{char:>21}')
            print(f' {"*"*20}\n {"*"*20}\n {"*"*20}')
        else:
            print(f' {"*"*20:>40}\n {"*"*26:>46}\n {"*"*26:>46}\n {"*"*20:>40}\n {"*"*46:}\n {"*"*46:}\n '
                  f'{"*"*46:}\n {"*"*46:}')
            asterisk_list = '****'
            for char in asterisk_list:
                print(f'{char:>23}{char:>13}')
                print(f'{"*"*5:>30}')
        return


# Invoke the main function
main()