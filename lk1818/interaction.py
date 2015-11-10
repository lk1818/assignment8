import sys
import numpy as np

''' Asks the user to input a valid list of positions. '''
def get_positions():
    try:
        pos_input = raw_input('Please provide a list of positions, select from 1, 10, 100, 1000.')
        pos_input = pos_input.replace(' ', '') 

    except (KeyboardInterrupt,EOFError): 
        sys.exit()
    
    if (pos_input == 'quit' or pos_input == 'Quit' or pos_input == 'q' or pos_input == 'QUIT'): 
        sys.exit()

    try:
        return get_list(pos_input)

    except (InvalidListException, InvalidIntegerException):
        print("Invalid input - please input positive integers and format your input into a list. ")
        return get_positions()

    except InvalidPositionException:
        print("Positions can only be chosen from 1, 10, 100, or 1000")
        return get_positions()


''' Asks the user to input the number of trials. '''
def get_num_trials():
    try:
        num_trials_input=raw_input('Please input the number of trials of simulations. ')
        num_trials_input=num_trials_input.replace(' ', '') 

    except (KeyboardInterrupt,EOFError): 
        sys.exit()
        
        if (pos_input == 'quit' or pos_input == 'Quit' or pos_input == 'q' or pos_input == 'QUIT'): 
            sys.exit()
    
    try:
        return get_int(num_trials_input)
    
    except InvalidIntegerException:
        print("The input must be a positive integer")
        return get_num_trials()


''' Check if a position in user's input list of is valid. '''
def get_position(pos):
    if pos.isdigit():
        if (int(pos) == 1 or int(pos) == 10 or int(pos) == 100 or int(pos) == 1000):
            return int(pos)

        else:
            raise InvalidPositionException()

    else:
        raise InvalidIntegerException()


''' Get an integer from the input. '''
def get_int(input_str):
    if input_str.isdigit(): 
        return int(input_str)
    else:
        raise InvalidIntegerException()


''' Out of the input string, Create a list of positive integers separated by commas. '''
def get_list(input_str):
    input_list = []
    if input_str[0] == '[' and input_str[-1] == ']': 
        input_str = input_str.replace(' ', '')        
        input_str = input_str[1:-1]
        input_str_split = input_str.split(',')
        for int_str in input_str_split:
            buff = get_position(int_str)
            input_list.append(buff)
        return input_list
    else:
        raise InvalidListException()


class InvalidPositionException(Exception):
    def __str__(self):
        return 'The positions in the list must be 1, 10, 100, or 1000.'
    # Gives a warning when the input is not a executable position.

class InvalidListException(Exception):
    def __str__(self):
        return 'Please format your input into a list.'
    # Gives a warning when the input is not formatted as a list

class InvalidIntegerException(Exception):
    def __str__(self):
        return 'This input list should contain positive integers only.'
    # Gives a warning when the input contains other datatypes.

	





