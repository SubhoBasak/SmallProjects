import os
import time
import getch
import termcolor

# As the name it store the data that if the hidded files will be show or not
show_hidden_file = False

# Store the current position of the cursor. -1 is the initial value
cursor_indx = -1

# This two variables sotre the index of the starting and ending index of the list for display
view_start = 0
view_end = None

# It read the file system and create the list of all subfolders and files in it's current directory
def dir_view(path):
    os.system('clear')
    os.chdir(path) # Change to the given path
    cur_dir = os.getcwd() # Store the current directory's path
    lst = os.listdir(cur_dir) # List all the subfolder and files in the current directory

# If 'show_hidden_files' is false or if the user don't want to see the hidden files then it will short the list and removed all the hidden files ( starts with '.' )
    if show_hidden_file == False:
        i = 0
# Here the while loop is used because after any element poped up index of it's next elements will be changed. So it will cause error.
        while i < len(lst):
            if lst[i].startswith('.'):
                lst.pop(i)
                i -= 1
            i += 1
# This for loop block will colored all the element as the type of the items (folder - green, files - blue, executable - magents)
    for i, j in enumerate(lst):
        if os.path.isdir(j):
            lst[i] = termcolor.colored(j, 'green', attrs = ['bold'])
        elif os.path.isfile(j):
            if os.access(j, os.X_OK):
                lst[i] = termcolor.colored(j, 'magenta', attrs = ['bold'])
            else:
                lst[i] = termcolor.colored(j, 'blue', attrs = ['bold'])
# Then the list will be sorted according to the color.
    lst.sort()
# After all the above operations done it will return the list.
    return lst

# This function add the cursor to the given index (cursor_indx) of the list 'lst'
def add_cursor(lst, cursor_indx):
# If the list is empty the function will not do anything and will be terminate. Otherwise it will set a highlght color to the item (which will indicate the cursor)
# in the list at the cursor_indx index
    if len(lst) != 0:
        lst[cursor_indx] = termcolor.colored(lst[cursor_indx], on_color = 'on_cyan', attrs = ['bold'])

# This will remove the cursor form item in the given list 'lst' at given index cur_indx
def remove_cursor(lst, cur_indx):
# If the list is empty then the function do nothing and terminated. Otherwise it will remove the highlight color set by the add_cursor function from the item in the
# given list 'lst' at index cur_indx
    if len(lst) != 0:
        lst[cur_indx] = lst[cur_indx][9:-4] # it will remove the color code from

# It move the cursor and manage items to be shown in the screen with current screen row numbers
def move_cursor(lst, direction): # It take the list of the elemenst and the direction that tells that if the cursor have to go up or down

# Take the global variables
    global cursor_indx
    global view_start
    global view_end

# Get the current screen size
    col, row = os.get_terminal_size()

# Calculate where to stop shown the list items for current screen size
    view_end = view_start+row-1

# It first remove the cursor from the position
    remove_cursor(lst, cursor_indx)

# If the given direction is 0 (up) then it will run the following block of code
    if direction == 0:
        cursor_indx -= 1 # First it will decrese the cursor index by 1
        if cursor_indx < view_start: # It the cursor index become smaller than the starting point then it will decrese the starting and ending point by one and
            view_start -= 1          # the view will be go up by one
            view_end -= 1

            if view_start < 0: # If the view start index become smaller than 0 then
                view_start = len(lst)-row+1 # the starting point will be set to the (length of the list - current number of rows in the screen)
                view_end = len(lst) # and the end point will be set to the total length of the list.

        # And if the cursor index become smaller than 0 then the cursor index will be set to at the last item or length of the list - 1
        if cursor_indx < 0: 
            cursor_indx = len(lst)-1

# And if the given direction is 1 (down) then it will run the following block of code
    else:
        cursor_indx += 1 # First it will increse the cursor index by 1
        if cursor_indx > view_end-1: # And if the cursor index become greater than the end point then
            view_start += 1          # the start point will be increse by 1
            view_end += 1            # and the end point will also be increse by 1

            if view_end > len(lst): # If the end point become greater than the length of the list then
                view_start = 0      # the start point will be set to the 0
                view_end = row-1    # and the end point will be set to the current screen rows - 1

        # And if the cursor index become greater than the length of the list then the cursor will be set to the first item or at index 0
        if cursor_indx > len(lst)-1:
            cursor_indx = 0

# And after all the above operation performed and the new cursor index is decided this will be set the cursor at the new cursor index
    add_cursor(lst, cursor_indx)

# Then it will clear the screen
    os.system('clear')
# And it will print the items from the index stored in the view_started to the index stored in the view_end-1
    for i in lst[view_start:view_end]:
        print(i)

# This will start the programme
if __name__ == '__main__':

# The following 3 line is for initialize the programme and all the values
    lst = dir_view(os.getcwd()) # First it will get all the items list is in the current directory and the dir_view function will clear the screen
    
    add_cursor(lst, cursor_indx) # Then it will be add the cursor to the initial cursor index or at index -1 or at the last item

    move_cursor(lst, 1) # Then it will remove the cursor to the downword. Because the cursor is in the last item so after remove the cursor to the downword by one step
                        # it will come to the first item and then the move_cursor will print all the items from the starting point to the end point for first time 

# This will run the programme until the user stopped the programme by pressing ctrl+c
    while True:
        gtch = getch.getch() # At every cycle of the loop it will detect for any keyboard input and will store the input value in the gtch variable

# If the user press the + button then it will call the move_cursor with the direction parameter 1. Thats mean it will down the cursor and the move_cursor will manage the screen view
        if gtch == '+':
            move_cursor(lst, 1)
# If the user press the - button then it will call teh move_cursor with the direction parameter 0. Thats mean it will up the cursor and the move_cursor will manage the screen view
        elif gtch == '-':
            move_cursor(lst, 0)
# If the usre press the enter button then it will run the following block of code and at that time it the cursor is on any folder item then ite will change the directory to the folder
        elif gtch == '\n':
            if len(lst) != 0: # First it will check if the current folder is empty or not by checking the 'lst' list length.
                path = lst[cursor_indx][18:-8] # It remove all the color code from the current item where the cursor is present
                if os.path.isdir(path) and path != '': # Then it check if the item is of any directory or not
                    remove_cursor(lst, cursor_indx) # If the item is a directory then it remove the cursor from the item
                    os.chdir(path) # Then it will change the current directory to the directory at the cursor item
                    lst = dir_view(os.getcwd()) # Then once again it will list all the subfolder, files and executable in the new directory
                    cursor_indx = -1 # Then the cursor poosition is set to it's initial state
                    add_cursor(lst, cursor_indx) # Then again set the cursor at the initial index
                    move_cursor(lst, 1) # Then it move the cursor to the first item and manage the output and show the list

        elif gtch == '\x7f': # If the user press the backspace key then the following block of code will run. '\x7f' is the code of backspace.
            path = os.path.abspath('..') # It will return to the current directory's parent directory
            remove_cursor(lst, cursor_indx) # Then it remove the cursor from the current item
            os.chdir(path) # Then it will change the current directory to the parent directory
            lst = dir_view(os.getcwd()) # Then once again it will list all the subfolder, files and executable in the new directory
            cursor_indx = -1 # Then the cursor poosition is set to it's initial state
            add_cursor(lst, cursor_indx) # Then again set the cursor at the initial index
            move_cursor(lst, 1) # Then it move the cursor to the first item and manage the output and show the list
