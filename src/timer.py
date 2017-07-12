import os
import time


def clear():
    os.system('clear')  # on linux / os x

HEIGHT = 5

NUMBERS = {

'1':'''\
  ██  
████  
  ██  
  ██  
██████
''',
'2':'''\
 ████ 
█   ██
   ██ 
 ██   
██████
''',
'3':'''\
 ████ 
█    █
   ██ 
█    █
 ████ 
''',
'4':'''\
  ███ 
 █ ██ 
█  ██ 
██████
   ██ 
''',
'5':'''\
██████
█     
██████
     █
██████
''',
'6':'''\
██████
█     
██████
█    █
██████
''',
'7':'''\
██████
█   ██
   ██ 
  ██  
 ██   
''',
'8':'''\
 ████ 
█    █
██████
█    █
 ████ 
''',
'9':'''\
██████
█    █
██████
    ██
    ██
''',
'0':'''\
 ████ 
█    █
█    █
█    █
 ████ 
''',
":":'''\
      
  ██  
      
  ██  
      
'''}

def test():

    for number in NUMBERS:
        print(NUMBERS[number])
        time.sleep(1)
        clear()

        #TODO: supress cursor
# test()

# input in the form of hours and minutes
def vertical_display(time):
    for char in time:
        print(NUMBERS[char])


def display_time(time):

    # break down each letter into individual lines
    letter_lines = []
    for char in time:

        big_letter = NUMBERS[char]
        letter_lines.append(big_letter.split('\n'))
    #
    # # create scan line
    # composed_lines = [[]]*HEIGHT
    #
    # # print(letter_lines)
    # print(composed_lines)

    # Loops over the lines
    for n in range(HEIGHT):
        # Loops over the letters
        for letter in letter_lines:
            # takes the nth line of the letter
            print(letter[n], end=' ')
        print(' ')

    # for line in composed_lines:
    #     print(''.join(line))


def countdown(time):

    # for now assume time is minutes


    # convert it to a sting
    time = str(time)

    if len(time)

    if len(time) == 2:
        time = time + ':00'

    # counter
    digits = time.split(':')

    ld = len(digits)

    if ld > 0:
        sec




