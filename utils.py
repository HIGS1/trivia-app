from os import system, name
from sys import exit


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def input_int(prompt: str = 'Enter Number: ', min: int | None = None, max: int | None = None) -> int:
    valid_input = False
    number = int()
    while not valid_input:
        try:
            user_input = input(prompt)
            number = int(user_input)

            if min != None:
                if number < min:
                    print(f'The minimum value is {min}')
                    continue
            if max != None:
                if number > max:
                    print(f'The maximum value is {max}')
                    continue
            valid_input = True
        except ValueError:
            print('You did not enter a valid number.')
        except KeyboardInterrupt:
            print('\nClosing Program...')
            exit(0)

    return number
