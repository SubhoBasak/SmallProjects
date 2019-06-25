import os
import sys
import time
import getch
import random
from termcolor import cprint

cmd = '' # It will store the command, which will be used to change the wallpaper

# This is the main function of this project. It carry the main menu and call the other helper functions as needed.
def home_scr():
    global cmd # To access the global cmd variable

    os.system('clear')
    cprint('1. Change Wallpaper', 'green', attrs = ['bold'])
    cprint('2. Auto-change Wallpaper', 'green', attrs = ['bold'])
    cprint('3. Settings', 'green', attrs = ['bold'])
    cprint('4. Exit', 'green', attrs = ['bold'])
# The above lines of code show the main menu options and below the input function take the input from the user and do as the user inputed.
# The below's if else statements decide whice function has to called or what to do comparing the input value with the options value.
# If the user entered and integer value whiche is greater or less than the option range then it show that an invalid option has been chosen,
# and again reopen that page. But if user entered any non numarical value then it can't be converted into integer value using int() function.
# So, to not to suddenly close the programme for the error the entire code is written in the try except block.
    try:
        inp = int(input())
        if inp == 1:    # If user entered 1 as input then this function called it's helper function op1_scr(), which takes no parameter and don't return any value
            op1_scr()   # Here op1_scr is stands for option 1 screen

        elif inp == 2:  # If user entered 2 as input then this fucntion called it's helper function op2_scr(), which takes no parameter and don't return any value
            op2_scr()   # Here op2_scr is stands for option 2

        elif inp == 3:  # If user entered 3 as input then this function print some option, that which desktop env's wallpaper the user want to change
            cprint('1. GENOME', 'green', attrs = ['bold'])
            cprint('2. LXDE', 'green', attrs = ['bold'])
            cprint('3. Xfce', 'green', attrs = ['bold'])
            cprint('4. MATE', 'green', attrs = ['bold'])
            inp = int(input()) # This input statement is already in a try except block, so there is not seperate try except block for that one, and if it occurred
                               # any error then once again the programe show some error message and recall itself, but the entire programme will not stopped

            if inp == 1: # If the GENOME is chosen then it will assign the GENOME wallpaper changing command to the global variable cmd
                cmd = 'gsettings set org.gnome.desktop.background picture-uri \'file://{}\''
                cprint('Done! Settings changed for GNOME', 'yellow', attrs = ['bold'])

            elif inp == 2: # If the LXDE is chosen then it will assign the LXDE wallpaper changing command to the global variable cmd
                cmd = 'pcmanfm --set-wallpaper=\'{}\''
                cprint('Done! Settings changed for LXDE', 'yellow', attrs = ['bold'])

            elif inp == 3: # If the Xfce is chosen then it will assign the Xfce wallpaper changing command to the global variable cmd
                cmd = 'xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitor0/image-path --set {}'
                cprint('Done! Settings changed for Xfce', 'yellow', attrs = ['bold'])

            elif inp == 4: # If the MATE is chosen then it will assign the MATE wallpaper changing command to the global variable cmd
                cmd = 'dconf write /org/mate/desktop/background/picture-filename \'{}\''
                cprint('Done! Settings changed for MATE', 'yellow', attrs = ['bold'])
            else:
                cprint('Invalid option!', 'red', attrs = ['bold']) # If the input value is less or greater that the option range then it will show this message

            cprint('Press any key to continue...', 'blue', attrs = ['bold']) # After any of the above if else block run, it will asked user to press any key to continue
            getch.getch()

        elif inp == 4: # If the user entered 4 then if will asked the user if he really want to clese the programme or not
            cprint('Do you really want to close the programme(y/n)?', 'cyan', attrs = ['bold'])
            inp = input() # Because dont change the input values data type so, it dont need any try except block to handel any error

            if inp == 'y': # If the user entered small "y" then it will close the programme and which wallpaper it set at the last, will stay until the wallpaper is changed again
                cprint('Good bye...', 'magenta', attrs = ['bold'])
                time.sleep(1)
                return

            elif inp != 'n': # If the user entered small "n" then it will go to the home screen and continue working
                cprint('Invalid option !', 'red', attrs = ['bold'])

            cprint('Press any key to continue...', 'blue', attrs = ['bold']) # For any input after execute the above code, user will be asked for press any key to continue
            getch.getch()

        else:
            cprint('Invalid option!', 'red', attrs = ['bold']) # If in option chose stage user entered any integer value less or greater than the option range then this line will execute
            cprint('Press any key to continue...', 'blue', attrs = ['bold'])
            getch.getch()
    except: # If in above try block any error occured then the following lines will execute
        cprint('Invalid option!', 'red', attrs = ['bold'])
        cprint('Press any key to continue...', 'blue', attrs = ['bold'])
        getch.getch()
    home_scr() # After the above code run it will return the programme to the home screen if user dont exit in the above code


# Option1 screen
def op1_scr():

# First it will clear all the old stuff in the terminal
    os.system('clear')

# Then it will ask for the path of the image which the user want to set as wallpaper
    cprint('Enter the path of the picture:', 'cyan', attrs = ['bold'])
    path = input() # Because after take the input it dont change the data type so, it dont required any try-except block to handel errors

    if os.path.isfile(path): # It will check if the path entered by the user is really exists or not
        cprint('Do you really want to change the wallpaper(y/n)?', 'yellow', attrs = ['bold'])
        inp = input() # Because here it does not change the input value's data type, so it dont required to handel errors

        if inp == 'y': # If user entered small 'y' then it will change the wallpaper of the desktop set in the setting option

            if len(cmd) == 0: # If the user didn't set the desktop environment in the setting then the lenght of the value of the cmd remain 0 and if if's happend then it will show this go back to the home menu
                cprint('Pleast select the desktop environment first !', 'red', attrs = ['bold'])
                cprint('Press any key to continue !', 'blue', attrs = ['bold'])
                getch.getch()
                return
            os.system(cmd.format(path)) # If the user already set the desktop env then the above if block will be skip and it will change the wallpaper then go back to home menu
            cprint('Operation successfull!', 'blue', attrs = ['bold'])
            getch.getch()
            return
        elif inp == 'n': # At the confirmetion time of change the wallpaper if the user entered small 'n' then the wallpaper will not change and go back to the home menu
            cprint('Operation cancelled!\nPress any keu to continue...', 'blue', attrs = ['bold'])
            getch.getch()
            return
    elif os.path.isdir(path): # At the path input time if the user entered only the directory name, ont specified the file then this will be shown
        cprint('Error! Please enter the path of the image file not the directory', 'red', attrs = ['bold'])
    else: # And if the user entered something else then this message will be shown
        cprint('Error! Please enter a valid path of the image file', 'red', attrs = ['bold'])

# These 3 lines are common for all the above actions and code
    cprint('Press any key to continue...', 'blue', attrs = ['bold'])
    getch.getch()
    return

# Oprion 2 screen
def op2_scr():
    os.system('clear') # First clear the terminal

# It's show it own menus or submenus
    cprint('1. Select Individual images', 'green', attrs = ['bold'])
    cprint('2. Select directory of images', 'green', attrs = ['bold'])

    try:
        inp = int(input()) # Beacuse there the data type of the inputed value is changed to integer so, to avoid any error the following line are in try block

        if inp == 1: # If the user entered 1 then the following code for this if block will run
            paths = [] # It will store all the individual image's path

            while True: # This loop will run until it's inner code stop this

                cprint('{}\nEnter the path of the image:\n'.format(len(paths)), 'cyan', attrs = ['bold']) # This line will ask the user to enter the one image's path
                path = input() # Take the input from the user of the image's path as a string valur so, it doesn't required any try-except block to handel the error
                if os.path.isfile(path): # If the path given by the user is of any file then
                    paths.append(path)   # it will add the file to the local list variable paths

                    cprint('Do you want to add more images(y/n)?', 'yellow', attrs = ['bold']) # After it take one image's path it asked the user if he/she want to add more images
                    inp = input()
                    if inp == 'y': # If the user entered small 'y' then the loop will run continue and once again take ones more image's path until the user entered any thing else at this stage in any cycle of this loop
                        continue

                    elif inp == 'n': # If the usr entered small 'n' then the loop it will call it's helper function timer and after the time function executed this finction will be terminated
                        timer(paths) # Timer function take all the images path entered by the user and saved in the local list variable paths
                        return # After the timer function executed this return function stopped the while loop and terminate this function

                    else: # If the user entered something else then the input will be ignored and the while loop will run continue with all the saved paths
                        cprint('Invalid option!', 'red', attrs = ['bold'])
                        cprint('\nPress any key to continue...', 'blue', attrs = ['bold'])
                        getch.getch()
                        continue

                else: # In this loop at the image's path entered stage if the user entered any path which is not a files path then the following code will be executed
                    cprint('Error! Invalid path', 'red', attrs = ['bold'])
                    cprint('\nPress any key to continue...\nPress \'c\' for cancel...', 'blue', attrs = ['bold'])
                    if getch.getch() == 'c': # At this stage if the user c then the loop and also the function will be terminated, but for any other input the loop will run continue with all the saved paths
                        return

        elif inp == 2: # In the option 2 function at the submenu selection time if the user entered 2 then the code contained by this elif block will be run
            paths = [] # As the previous block this local list variable will store all the files path

            while True: # And again this while loop will run for infinitive time until the innner code stopped it
                cprint('Enter the path of the directory:\n', 'yellow', attrs = ['bold']) # At this stage user will be asked for enter the directory's path which contain the files which the user want set as wallpaper one by one
                path = input()
                if os.path.isdir(path): # If the path enterd by the user is really any directory's path then it will break this while loop to run the next code after the while loop block
                    break
                else: # For any other input the following block will run
                    cprint('Invalid path! Please enter a valid path of the directory...', 'red', attrs = ['bold'])
                    cprint('\nPress any key to continue...\nPress \'c\' for cancel...', 'blue', attrs = ['bold'])
                    if getch.getch() == 'c': # At this stage if the user press 'c' then the while loop will be break and the function will be terminate and go back to the main menu
                        return

            os.chdir(path) # It will go to the entered directory path
            lst = os.listdir() # It will list all the subfolders and files contain in that directory
            for i in lst: # In this for loop all items stored in the 'lst' list variable, will be examined one by one, if it's a subfolder or file and if it's a file then if it's a image file or not
                if os.path.isfile(i) and (i.endswith('.png') or i.endswith('.jpg') or i.endswith('.jpeg') or i.endswith('.svg')): # If the item's extentainon ends with .png or .jpg or .jped or .svg then it will be accepted for the next stage
                    paths.append(os.path.join(path, i)) # If the item passed in the above stage then it will stored that item in the empty 'paths' list variable

            if len(paths) == 0: # After the for loop run if the 'paths' list remain empty or if there is not any image file then the following block will run and then it go bace to the main menu
                cprint('There is no image file in the directory!', 'red', attrs = ['bold'])
                cprint('Press any key to continue...\nPress \'c\' to cancel...', 'blue', attrs = ['bold'])
                if getch.getch() == 'c': # At this stage if the user pressed 'c' then this function will be terminated and go to the main menu
                    return
                op2_scr() # and for any other input this function will call itself
            else:
                timer(paths) # If the paths list not empty then it will call it's helper function timer

        else: # At the option selection stage in this function of it's own menu if the user entered any invalid value then the following code will run and then go back to the main menu
            cprint('Invalid option!', 'red', attrs = ['bold'])
            cprint('\nPress any key to continue...', 'blue', attrs = ['bold'])
            getch.getch()
            return
    except: # In that try block if user entered any string value at the option chosing stage then the value error will be occured. And if that happened then this block of code will run and the function will be terminated
        cprint('Invalid input !', 'red', attrs = ['bold'])
        cprint('\nPress any key to continue...', 'blue', attrs = ['bold'])
        getch.getch()

# Timer function, it's task is if the user chose the auto change option then it will change the given wallpapers time to time
def timer(lst):

    try:
    # First it take the delay time to change the wallpaper, in hour, minut and second unit
        cprint('\tSET TIMER', 'yellow', attrs = ['bold'])
        cprint('Hour : ', 'blue', attrs = ['bold'])
        hh = int(input())
        cprint('Minute : ', 'blue', attrs = ['bold'])
        mm = int(input())
        cprint('Second : ', 'blue', attrs = ['bold'])
        ss = int(input())

    # Then it convert the hour minut and second to only second
        delay = (hh*3600)+(mm*60)+ss

    # Then it aske the user that in which way the wallpapers have to change (random selection or ascending order or descending order)
        cprint('\tCHOSE WALLPAPER', 'yellow', attrs = ['bold'])
        cprint('1. Random')
        cprint('2. Ascending')
        cprint('3. Descending')
        inp = int(input())

# Random option's code block. It will chose image file randomly from the 'path' list for infintive time until the user pressed ctrl+c to terminate the programme
        if inp == 1:
            while True:
                path = lst[random.randint(0, len(lst)-1)] # The main code that chose the random file from the 'lst' list
                cprint('Wallpaper has been changed', 'magenta', attrs = ['bold'])
                os.system(cmd.format(path)) # The main code that use the command saved in the global variable 'cmd' and change the wallpaper
                time.sleep(delay) # Make delay between changing wallpapers as the time mentioned by the user

# Ascending option's code block. It will chose image file from index 0 to the last index from the 'lst' list for infinitive time until the user pressd ctrl+c to terminate the programme
        elif inp == 2:
            count = 0 # This variable keep track which image have to now set as wallpaper by saving the files index in the 'lst' list
            while True: # This infinitive loop will change the wallpaper continiously until the user press ctrl+c to terminate the programme.
                path = lst[count] # This will extrace the image file from the 'lst' list which have to be set as wallpaper now.
                count += 1 # After the current wallpaper extracted from the 'lst' list this will increse the count's value by 1 for the next one
                if count >= len(lst): # If the value of count become greater than the length of the 'lst' list the it will set the count to it's initial state 0
                    count = 0
                cprint('Wallpaper has been changed', 'magenta', attrs = ['bold'])
                os.system(cmd.format(path)) # This will use the command saved in the cmd variable and will change the wallpaper
                time.sleep(delay) # This will hold the function for the user defined time

# Descending option's code block. It will chose image file from the last index to first index
        elif inp == 3:
            count = len(lst)-1
            while True:
                path = lst[count]
                count -= 1
                if count < 0:
                    count = len(lst)-1
                cprint('Wallpaper has been changed', 'magenta', attrs = ['bold'])
                os.system(cmd.format(path))
                time.sleep(delay)

# If the user entered any invalid option in the option chosing stage in this function then this block will be run and then the function will call itself
        else:
            cprint('Invalid option !', 'red', attrs = ['bold'])
            cprint('Wallpaper has been changed', 'magenta', attrs = ['bold'])
            cprint('\nPress any key to continue...\nPress \'c\' to cancel...', 'blue', attrs = ['bold'])
            if getch.getch() == 'c': # In this stage if the user press c then the function will be terminated and it will go back to the main menu, and for any other key press the function will call itself
                return
            else:
                timer(lst)

# In the above try block if the user entered any value that can not be converted into integer then the valur error will be occured and then the following block will be run and then the function will be terminated
    except:
        cprint('Entered invalid input !', 'red', attrs = ['bold'])
        cprint('Press any key to continue...', 'blue', attrs = ['bold'])
        getch.getch()

# The following lines of code will start the programme
if __name__ == '__main__':
    if len(sys.argv) <= 1:
        home_scr()
