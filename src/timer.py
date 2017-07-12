import os
import time
import cursor_hide



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

    clear()

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


def digitmaker(time):

    # for now assume time is minutes


    # convert it to a sting
    time = str(time)

    if len(time) < 2:
        # TODO throw error
        pass

    if len(time) == 2:
        time = time + ':00'

    # counter
    digits = time.split(':')


    return digits






# for now focus on minutes and secconds
def countdown(mins):

    digits = digitmaker(mins)

    ld = len(digits)

    secconds = int(digits[ld - 1])  # last list
    minutes = int(digits[ld - 2])

    # TODO:  divide minutes into hours
    if ld >= 3:
        hours = digits[ld - 3]

    # turn cursor off before displaying time
    # TODO: cursor needs to be tweaked for cross platform
    cursor_hide.hide()

    # countdown
    while True:
        if secconds > 0:
            secconds -= 1

        elif minutes > 0:
            minutes -= 1
            secconds = 59

        else:
            print('Timer Done!')

            # turn cursor back on
            cursor_hide.show()
            return

        time_to_disp = int_to_time(minutes) + ':' + int_to_time(secconds)


        display_time(time_to_disp)
        time.sleep(1)





def int_to_time(int_time):

    if int_time < 10:
        str_time = '0' + str(int_time)

    else:
        str_time = str(int_time)

    return str_time



#TODO: make cursor blink go away
#TODO: time and make sure 25 mins ~= 25 mins (within a few secconds)

#TODO: Fix display screen


countdown(2)