
import os
import time
import datetime

VERSION = 0.1

acceptable_commands = ['work', 'break', 'long', 'help', 'quit']

def prod_app():

    print("")
    print("Pomodoro timer and productivity tracker V.{}:".format(VERSION))

    command = input("Hit 'Enter' to start 25 min work block")

    if command == '':
        work_block()

    else:
        while command not in acceptable_commands:
            command = input("type 'work' or 'break' or 'help' for more options")



def parse_commands(command):

    if command == 'work':
        work_block()
        return 0

    elif command == 'break':
        ## todo break_block()
        return 0

    elif command == 'help':
        # todo help_page()
        return 0

    elif command == 'quit':
        # todo quit_pom():
        return 0

    else:
        return 1





def work_block():

    print("")
    print ('starting work block XX')
    # sleep(1500) # - sleep for 25 mins
    time.sleep(10)
    print("")
    print('sleep done')













# runs the app if called
if __name__ == "__main__":
    prod_app()