import os
import getch
import termcolor

show_hidden_file = False
cursor_indx = -1
view_start = 0
view_end = None

def dir_view(path):
    os.system('clear')
    cur_dir = os.chdir(path)
    lst = os.listdir(cur_dir)
    if show_hidden_file == False:
        i = 0
        while i < len(lst):
            if lst[i].startswith('.'):
                lst.pop(i)
                i -= 1
            i += 1
    for i, j in enumerate(lst):
        if os.path.isdir(j):
            lst[i] = termcolor.colored(j, 'green', attrs = ['bold'])
        elif os.path.isfile(j):
            if os.access(j, os.X_OK):
                lst[i] = termcolor.colored(j, 'magenta', attrs = ['bold'])
            else:
                lst[i] = termcolor.colored(j, 'blue', attrs = ['bold'])
    lst.sort()
    return lst

def add_cursor(lst, cursor_indx):
    lst[cursor_indx] = termcolor.colored(lst[cursor_indx], on_color = 'on_cyan', attrs = ['bold'])

def remove_cursor(lst, cur_indx):
    lst[cur_indx] = lst[cur_indx][9:]

def move_cursor(lst, direction):
    global cursor_indx
    global view_start
    global view_end

    remove_cursor(lst, cursor_indx)
    if direction == 0:
        cursor_indx -= 1
        if cursor_indx < 0:
            cursor_indx = len(lst)-1
    else:
        cursor_indx += 1
        if cursor_indx > len(lst)-1:
            cursor_indx = 0
    add_cursor(lst, cursor_indx)

    if cursor_indx < view_start:
        view_start -= 1
        view_end -= 1
        if view_start < 0:
            view_start = len(lst)-abs(view_start-view_end)-1
            view_end = len(lst)-1

    elif cursor_indx > view_end:
        view_start += 1
        view_end += 1
        if view_end > len(lst)-1:
            view_end = abs(view_start-view_end)
            view_start = 0

    view_end = manage_view(lst, view_start)

def manage_view(lst, start):
    col, row = os.get_terminal_size()
    for i in lst[start:start+row-1]:
        print(i)
    return start+row

if __name__ == '__main__':
    lst = dir_view('/home/pi/')
    add_cursor(lst, cursor_indx)
    col, row = os.get_terminal_size()
    view_end = row
    move_cursor(lst, 1)
    while True:
        gtch = getch.getch()
        if gtch == '+':
            move_cursor(lst, 1)
        elif gtch == '-':
            move_cursor(lst, 0)
