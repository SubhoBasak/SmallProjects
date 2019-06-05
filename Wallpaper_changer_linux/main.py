import os
import sys
import time
import getch
import random
from termcolor import cprint

cmd = ''

def home_scr():
    os.system('clear')
    cprint('1. Change Wallpaper', 'green', attrs = ['bold'])
    cprint('2. Auto-change Wallpaper', 'green', attrs = ['bold'])
    cprint('3. Help', 'green', attrs = ['bold'])
    cprint('4. Settings', 'green', attrs = ['bold'])
    cprint('5. Exit', 'green', attrs = ['bold'])
    inp = int(input())
    if inp == 1:
        op1_scr()
    elif inp == 2:
        op2_scr()
    elif inp == 3:
        help_scr()
    elif inp == 4:
        cprint('1. GENOME', 'green', attrs = ['bold'])
        cprint('2. LXDE', 'green', attrs = ['bold'])
        cprint('3. Xfce', 'green', attrs = ['bold'])
        cprint('4. MATE', 'green', attrs = ['bold'])
        inp = int(input())
        if inp == 1:
            cmd = 'gsettings set org.gnome.desktop.background picture-uri \'file://{}\''
            cprint('Done! Settings changed for GNOME', 'yellow', attrs = ['bold'])
            cprint('\nPress any key to continue...', 'blue', attrs = ['bold'])
            getch.getch()
        elif inp == 2:
            cmd = 'pcmanfm --set-wallpaper=\'{}\''
            cprint('Done! Settings changed for LXDE', 'yellow', attrs = ['bold'])
            cprint('\nPress any key to continue...', 'blue', attrs = ['bold'])
            getch.getch()
        elif inp == 3:
            cmd = 'xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitor0/image-path --set {}'
            cprint('Done! Settings changed for Xfce', 'yellow', attrs = ['bold'])
            cprint('\nPress any key to continue...', 'blue', attrs = ['bold'])
            getch.getch()
        elif inp == 4:
            cmd = 'dconf write /org/mate/desktop/background/picture-filename \'{}\''
            cprint('Done! Settings changed for MATE', 'yellow', attrs = ['bold'])
            cprint('\nPress any key to continue...', 'blue', attrs = ['bold'])
            getch.getch()
        else:
            cprint('Invalid option!', 'red', attrs = ['bold'])
            cprint('Press any key to continue...', 'blue', attrs = ['bold'])
            getch.getch()
    elif inp == 5:
        cprint('Do you really want to close the programme(y/n)?', 'cyan', attrs = ['bold'])
        inp = input()
        if inp == 'y':
            cprint('Good bye...', 'magenta', attrs = ['bold'])
            time.sleep(1)
            exit()
        elif inp != 'n':
            cprint('Invalid option !', 'red', attrs = ['bold'])
            cprint('Press any key to continue...', 'blue', attrs = ['bold'])
            getch.getch()
        else:
            cprint('Invalid option!', 'red', attrs = ['bold'])
            cprint('Press any key to continue...', 'blue', attrs = ['bold'])
            getch.getch()
    else:
        cprint('Invalid option!', 'red', attrs = ['bold'])
        cprint('Press any key to continue...', 'blue', attrs = ['bold'])
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
                    timer(paths)
                    return
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
        paths = []
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
        os.chdir(path)
        lst = os.listdir()
        for i in lst:
            if os.path.isfile(i) and (i.endswith('.png') or i.endswith('.jpg') or i.endswith('.jpeg') or i.endswith('.svg')):
                paths.append(os.path.join(path, i))
        if len(paths) == 0:
            cprint('There is no image file in the directory!', 'red', attrs = ['bold'])
            cprint('Press any key to continue...\nPress \'c\' to cancel...', 'blue', attrs = ['bold'])
            if getch.getch() == 'c':
                return
            op2_scr()
        else:
            timer(paths)
    else:
        cprint('Invalid option!', 'red', attrs = ['bold'])
        cprint('\nPress any key to continue...', 'blue', attrs = ['bold'])
        getch.getch()
        return

def timer(lst):
    cprint('\tSET TIMER', 'yellow', attrs = ['bold'])
    cprint('Hour : ', 'blue', attrs = ['bold'])
    hh = int(input())
    cprint('Minute : ', 'blue', attrs = ['bold'])
    mm = int(input())
    cprint('Second : ', 'blue', attrs = ['bold'])
    ss = int(input())
    delay = (hh*3600)+(mm*60)+ss
    cprint('\tCHOSE WALLPAPER', 'yellow', attrs = ['bold'])
    cprint('1. Random')
    cprint('2. Ascending')
    cprint('3. Descending')
    inp = int(input())
    if inp == 1:
        while True:
            path = lst[random.randint(0, len(lst)-1)]
            cprint('Wallpaper has been changed', 'magenta', attrs = ['bold'])
            os.system('pcmanfm --set-wallpaper=\'{}\''.format(path))
            time.sleep(delay)
    elif inp == 2:
        count = 0
        while True:
            path = lst[count]
            count += 1
            if count >= len(lst):
                count = 0
            cprint('Wallpaper has been changed', 'magenta', attrs = ['bold'])
            os.system('pcmanfm --set-wallpaper=\'{}\''.format(path))
            time.sleep(delay)
    elif inp == 3:
        count = len(lst)-1
        while True:
            path = lst[count]
            count -= 1
            if count < 0:
                count = len(lst)-1
            cprint('Wallpaper has been changed', 'magenta', attrs = ['bold'])
            os.system('pcmanfm --set-wallpaper=\'{}\''.format(path))
            time.sleep(delay+5)
    else:
        cprint('Invalid option !', 'red', attrs = ['bold'])
        cprint('Wallpaper has been changed', 'magenta', attrs = ['bold'])
        cprint('\nPress any key to continue...\nPress \'c\' to cancel...', 'blue', attrs = ['bold'])
        if getch.getch() == 'c':
            return
        else:
            timer(lst)

def help_scr():
    pass

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        home_scr()
