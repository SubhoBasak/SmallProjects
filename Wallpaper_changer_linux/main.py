import os
import sys
import time
import getch
from termcolor import cprint, colored

def home_scr():
    os.system('clear')
    cprint('1. Change Wallpaper', 'green', attrs = ['bold'])
    cprint('2. Auto-change Wallpaper', 'green', attrs = ['bold'])
    cprint('3. Help', 'green', attrs = ['bold'])
    cprint('4. Exit', 'green', attrs = ['bold'])
    inp = int(input())
    if inp == 1:
        op1_scr()
    elif inp == 2:
        op2_scr()
    elif inp == 3:
        op3_scr()
    elif inp == 4:
        cprint('Do you really want to close the programme(y/n)?', 'cyan', attrs = ['bold'])
        inp = input()
        if inp == 'y':
            cprint('Good bye...')
            time.sleep(1)
            exit()
        elif inp != 'n':
            cprint('Invalid option !', 'red', attrs = ['bold'])
            cprint('Press any key to continue...', 'blue', attrs = ['bold'])
            getch.getch()
    else:
        cprint('Invalid option !', 'red', attrs = ['bold'])
        cprint('\nPress any key to continue...', 'blue', attrs = ['bold'])
        getch.getch()
    home_scr()

def op1_scr():
    os.system('clear')
    cprint('Enter the path of the picture:', 'cyan', attrs = ['bold'])
    path = input()
    if os.path.isfile(path):
        cprint('Do you really want to change the wallpaper(y/n)?', 'yellow', attrs = ['bold'])
        inp = input()
        if inp == 'y':
            os.system('pcmanfm --set-wallpaper=\'{}\''.format(path))
            cprint('Operation successfull!\nPress any key to continue...', 'blue', attrs = ['bold'])
            getch.getch()
            return
        elif inp == 'n':
            cprint('Operation cancelled!\nPress any keu to continue...', 'blue', attrs = ['bold'])
            getch.getch()
            return
    elif os.path.isdir(path):
        cprint('Error! Please enter the path of the image file not the directory', 'red', attrs = ['bold'])
        cprint('Press any key to continue...', 'blue', attrs = ['bold'])
        getch.getch()
        return
    else:
        cprint('Error! Please enter a valid path of the image file', 'red', attrs = ['bold'])
        cprint('Press any key to continue...', 'blue', attrs = ['bold'])
        getch.getch()
        return

def op2_scr():
    os.system('clear')
    cprint('1. Select Individual images', 'green', attrs = ['bold'])
    cprint('2. Select directory of images', 'green', attrs = ['bold'])
    inp = int(input())
    if inp == 1:
        paths = []
        nxt = True
        while nxt:
            cprint('{}\nEnter the path of the image:\n'.format(len(paths)), 'cyan', attrs = ['bold'])
            path = input()
            if os.path.isfile(path):
                paths.append(path)
                cprint('Do you want to add more images(y/n)?', 'yellow', attrs = ['bold'])
                inp = input()
                if inp == 'y':
                    continue
                elif inp == 'n':
                    pass
                else:
                    cprint('Invalid option!', 'red', attrs = ['bold'])
                    cprint('\nPress any key to continue...', 'blue', attrs = ['bold'])
                    getch.getch()
                    continue
            else:
                cprint('Error! Invalid path', 'red', attrs = ['bold'])
                cprint('\nPress any key to continue...\nPress \'c\' for cancel...', 'blue', attrs = ['bold'])
                if getch.getch() == 'c':
                    return
    elif inp == 2:
        while True:        
            cprint('Enter the path of the directory:\n', 'yellow', attrs = ['bold'])
            path = input()
            if os.path.isdir(path):
                break
            else:
                cprint('Invalid path! Please enter a valid path of the directory...', 'red', attrs = ['bold'])
                cprint('\nPress any key to continue...\nPress \'c\' for cancel...', 'blue', attrs = ['bold'])
                if getch.getch() == 'c':
                    return
        pass

home_scr()
