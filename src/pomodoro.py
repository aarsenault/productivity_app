
import os
import time
import datetime

VERSION = 0.1

acceptable_commands = ['work', 'break', 'long', 'help', 'quit']

def prod_app():

    print("")
    print("Pomodoro timer and productivity tracker V.{}:".format(VERSION))

    command_loop()

def command_loop():

    command = ''

    while command not in acceptable_commands:
            command = input("type 'work' or 'break' to start ('help' for more options): ")

    parse_commands(command)



def parse_commands(command):

    if command == 'work':
        work_block()
        return command_loop()

    elif command == 'break':
        ## todo break_block()
        return command_loop()

    elif command == 'help':
        # todo help_page()
        return command_loop()

    elif command == 'quit':
        # todo quit_pom():
        return 0

    else:
        return 1





def work_block():



    print("")
    print ('starting work block XX')
    # sleep(1500) # - sleep for 25 mins

    for i in range(3):
        os.system('afplay /System/Library/Sounds/Ping.aiff')
        time.sleep(0.125)

    time.sleep(1)
    print("")

    EasyDialogs.Message
    print('sleep done')
    # os.system('say "your work block has finished"')
    os.system('afplay /System/Library/Sounds/Glass.aiff')





# runs the app if called
if __name__ == "__main__":
    prod_app()