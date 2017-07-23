
import os
import time
import datetime
import tkinter
from tkinter import messagebox
import my_timer


# hide main window
root = tkinter.Tk()
root.withdraw()

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
        print("")

    parse_commands(command)



def parse_commands(command):

    if command == 'work':
        work_block()
        return command_loop()

    elif command == 'break':
        ## todo break_block()
        print('entered break')
        return command_loop()

    elif command == 'help':
        # todo help_page()
        print('entered help')
        return command_loop()

    elif command == 'quit':
        print('entered quit')
        # todo quit_pom():
        return 0

    else:
        return 1





def work_block():

    print("")
    print ('starting work block XX')
    # sleep(1500) # - sleep for 25 mins

    start_sequence()

    my_timer.countdown(1)
    print("")

    # messagebox.showinfo("Title", "a Tk MessageBox")


    print('sleep done')
    # os.system('say "your work block has finished"')
    os.system('afplay /System/Library/Sounds/Glass.aiff')


# Counts down and chimes before a sequence starts
def start_sequence():
    print( " starting in: ")
    for i in range(3):
        print(3 - i)
        os.system('afplay /System/Library/Sounds/Ping.aiff')

        time.sleep(0.125)



# runs the app if called
if __name__ == "__main__":
    prod_app()
