import os
import time
import getch
import sqlite3
from termcolor import colored, cprint

col, row = os.get_terminal_size()

cursor_indx = 0
list_cursor_indx = 0
start = 0
end = row

class database:
    def __init__(self):
        home_dir = os.environ.get('HOME')
        trg_dir = os.path.join(home_dir, '.students_db')
        if not os.path.isdir(trg_dir):
            cprint('Target directory not present !', 'red', attrs = ['bold'])
            time.sleep(0.2)
            os.chdir(home_dir)
            os.mkdir('.students_db')
            cprint('Created target directory', 'cyan', attrs = ['bold'])
            time.sleep(0.2)
        os.chdir(trg_dir)
        self.connect = sqlite3.connect('students.db')
        cprint('Database connected', 'cyan', attrs = ['bold'])
        time.sleep(0.2)
        self.cursor = self.connect.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    First_name VARCHAR(10),
    Last_name VARCHAR(10),
    Class INTEGER,
    Section VARCHAR(1),
    Date_of_birth TEXT,
    Address TEXT,
    Phone INTEGER
    )''')

    def insert_new(self, data):     # data tuple type
        self.cursor.execute('''INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', data)
        self.connect.commit()

    def all_list(self):
        self.cursor.execute('''SELECT * FROM students''')
        return self.cursor.fetchall()

    def search(self, data):
        a, b, c, d, e, g= data
        data = {'id': a, 'first': b, 'last': c, 'clas': d, 'sec': e, 'phn': f}
        self.cursor.execute(''' SELECT * FORM students WHERE ID LIKE :id, First_name LIKE :first, Last_name LIKE :last,
    Class LIKE :clas, Section LIKE :sec, Phone LIKE :phn''', data)
        return self.cursor.fetchall()

    def update_old(self, data):
        #transfer the parameter data from tuple to dictionary
        a, b, c, d, e, f, g, h = data
        data = {'id': a, 'first': b, 'last': c, 'clas': d, 'sec': e, 'dob': f, 'adrs': g, 'phn': h} 
        self.cursor.execute('''UPDATE students SET First_name = :first, Last_name = :last,
    Class = :clas, Section = :sec, Date_of_birth = :dob, Address = :adrs, Phone = :phn WHERE ID = :id''', data)
        self.connect.commit()

def welcome_scr():
    os.system('clear')
    col, row = os.get_terminal_size()
    for i in range(row-2):
        if i == 0 or i == row-3:
            cprint('='*col, 'yellow', attrs = ['bold'])
        else:
            cprint('||'+' '*(col-4)+'||', 'yellow', attrs = ['bold'])
    cprint('Loading...', 'green', attrs = ['bold'])
    for i in range(col):
        cprint('\r'+'#'*i,'magenta', end = '', attrs = ['bold'])
        time.sleep(0.02)
    os.system('clear')
    cprint('\rPress any key to continue...', 'green', attrs = ['bold'])

def main_menu():
    os.system('clear')
    op1 = colored('1. Add', 'green', attrs = ['bold'])
    op2 = colored('2. View', 'green', attrs = ['bold'])
    op3 = colored('3. Edit', 'green', attrs = ['bold'])
    op4 = colored('4. Search', 'green', attrs = ['bold'])
    op5 = colored('5. Exit', 'green', attrs = ['bold'])
    return [op1, op2, op3, op4, op5]

def add_cursor(lst, indx):
    if len(lst) != 0:
        lst[indx] = colored(lst[indx], on_color = 'on_cyan')

def remove_cursor(lst, indx):
    if len(lst) != 0:
        lst[indx] = lst[indx][5:-4]

def move_cursor(lst, direction):
    global cursor_indx
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
    os.system('clear')
    for i in lst:
        print(i)

def new_scr():
    os.system('clear')
    cprint('First name : ', 'yellow', end = '', attrs = ['bold'])
    fname = input()
    cprint('Last name : ', 'yellow', end = '', attrs = ['bold'])
    lname = input()
    cprint('Date of birth : ', 'yellow', end = '', attrs = ['bold'])
    dob = input()
    cprint('Class : ', 'yellow', end = '', attrs = ['bold'])
    try:
        clas = int(input())
    except:
        cprint('Entered invalid input !', 'red', attrs = ['bold'])
        cprint('Press any key to continue...\nPress c to cancel...', 'blue', attrs = ['bold'])
        if getch.getch() == 'c':
            return None
        return new_scr()
    cprint('Section : ', 'yellow', end = '', attrs = ['bold'])
    sec = input()
    cprint('Address : ', 'yellow', end = '', attrs = ['bold'])
    adrs = input()
    cprint('Phone : ', 'yellow', end = '', attrs = ['bold'])
    try:
        phn = int(input())
    except:
        cprint('Entered invalid input !', 'red', attrs = ['bold'])
        cprint('Press any key to continue...\nPress c to cancel...', 'blue', attrs = ['bold'])
        if getch.getch() == 'c':
            return None
        return new_scr()
    os.system('clear')
    cprint('Name : ', 'yellow', end = '', attrs = ['bold'])
    cprint(fname+' '+lname, 'cyan', attrs = ['bold'])
    cprint('Class : ', 'yellow', end = '', attrs = ['bold'])
    cprint(str(clas)+', '+sec, 'cyan', attrs = ['bold'])
    cprint('Date of birth : ', 'yellow', end = '', attrs = ['bold'])
    cprint(dob, 'cyan', attrs = ['bold'])
    cprint('Address : ', 'yellow', end = '', attrs = ['bold'])
    cprint(adrs, 'cyan', attrs = ['bold'])
    cprint('Phone : ', 'yellow', end = '', attrs = ['bold'])
    cprint(phn, 'cyan', attrs = ['bold'])
    cprint('\n\nDo you rally want to save this record? (y/n)', 'magenta', attrs = ['bold'])
    inp = input()
    if inp == 'y':
        return (None, fname, lname, clas, sec, dob, adrs, phn)
    return None

def add_list_cursor(lst, indx):
    lst[indx] = list(lst[indx])
    for i, j in enumerate(lst[indx]):
        lst[indx][i] = colored(j, on_color = 'on_cyan')
    lst[indx] = tuple(lst[indx])

def remove_list_cursor(lst, indx):
    lst[indx] = list(lst[indx])
    for i, j in enumerate(lst[indx]):
        lst[indx][i] = lst[indx][i][5:-4]
    lst[indx] = tuple(lst[indx])

def manage_list_view(lst, direction):
    global list_cursor_indx
    global start
    global end
    col, row = os.get_terminal_size()
    row -= 2
    remove_list_cursor(lst, list_cursor_indx)
    if direction == 0:
        list_cursor_indx -= 1
        if list_cursor_indx < start:
            start -= 1
            end = start+row
            if start < 0:
                start = len(lst)-row-1
                end = start+row
        if list_cursor_indx < 0:
            list_cursor_indx = len(lst)-1
            start = len(lst)-row-1
            end = start+row
    else:
        list_cursor_indx += 1
        if list_cursor_indx > end:
            end += 1
            start += 1
            if end >= len(lst):
                start = 0
                end = row
        if list_cursor_indx >= len(lst):
            list_cursor_indx = 0
            start = 0
            end = row
    add_list_cursor(lst, list_cursor_indx)
    cprint('ID', 'red', end = '', attrs = ['bold'])
    cprint('   Name   ', 'green', end = '', attrs = ['bold'])
    cprint('Class', 'magenta', end = '', attrs = ['bold'])
    cprint('Section', 'blue', end = '', attrs = ['bold'])
    cprint('Date of birth', 'yellow', end = '', attrs = ['bold'])
    cprint('  Address  ', 'white', end = '', attrs = ['bold'])
    cprint('   Phone   ', 'cyan', attrs = ['bold'])
    os.system('clear')
    for i in lst:
        a, b, c, d, e, f, g, h = i
        print(a, b, c, d, e, f, g, h)

if __name__ == '__main__':
    welcome_scr()
    getch.getch()
    data_base = database()
    lst = main_menu()
    add_cursor(lst, cursor_indx)
    for i in lst:
        print(i)
    while True:
        inp = getch.getch()
        if inp == '\n':
            if cursor_indx == 0:
                data = new_scr()
                if data !=  None:
                    data_base.insert_new(data)
                    cprint('Added new record successfully !', 'cyan', attrs = ['bold'])
                    cprint('Press any key to continue...', 'blue', attrs = ['bold'])
                    getch.getch()
                else:
                    os.system('clear')
                    cprint('New record adding failed !', 'red', attrs = ['bold'])
                    cprint('Press any key to continue...', 'blue', attrs = ['bold'])
                    getch.getch()
                cursor_indx = 0
                lst = main_menu()
                add_cursor(lst, cursor_indx)
                for i in lst:
                    print(i)
            elif cursor_indx == 1:
                tmp_lst = data_base.all_list()
                for i, j in enumerate(tmp_lst):
                    a, b, c, d, e, f, g, h = j
                    a = colored(a, 'red', attrs = ['bold'])
                    b = colored(b, 'green', attrs = ['bold'])
                    c = colored(c, 'green', attrs = ['bold'])
                    d = colored(d, 'magenta', attrs = ['bold'])
                    e = colored(e, 'blue', attrs = ['bold'])
                    f = colored(f, 'yellow', attrs = ['bold'])
                    g = colored(g, 'white', attrs = ['bold'])
                    h = colored(h, 'cyan', attrs = ['bold'])
                    tmp_lst[i] = (a, b, c, d, e, f, g, h)
                os.system('clear')
                add_list_cursor(tmp_lst, list_cursor_indx)
                for i in tmp_lst:
                    for j in i:
                        print(j, end = ' ')
                    print()
                while True:
                    inp = getch.getch()
                    if inp == '+':
                        manage_list_view(tmp_lst, 1)
                    elif inp == '-':
                        manage_list_view(tmp_lst, 0)
                    elif inp == '\n':
                        ID, fname, lname, clas, sec, dob, adrs, phn = tmp_lst[list_cursor_indx]
                        os.system('clear')
                        cprint('ID : ', 'yellow', end = '', attrs = ['bold'])
                        cprint(ID, 'cyan', attrs = ['bold'])
                        cprint('Name : ', 'yellow', end = '', attrs = ['bold'])
                        cprint(fname+' '+lname, 'cyan', attrs = ['bold'])
                        cprint('Class : ', 'yellow', end = '', attrs = ['bold'])
                        cprint(str(clas)+', '+sec, 'cyan', attrs = ['bold'])
                        cprint('Date of birth : ', 'yellow', end = '', attrs = ['bold'])
                        cprint(dob, 'cyan', attrs = ['bold'])
                        cprint('Address : ', 'yellow', end = '', attrs = ['bold'])
                        cprint(adrs, 'cyan', attrs = ['bold'])
                        cprint('Phone : ', 'yellow', end = '', attrs = ['bold'])
                        cprint(phn, 'cyan', attrs = ['bold'])
                        cprint('Press any key to continue...', 'blue', attrs = ['bold'])
                        getch.getch()
                        break
                os.system('clear')
                for i in lst:
                    print(i)
            elif cursor_indx == 4:
                os.system('clear')
                cprint('Do you rally want to exit? (y/n)', 'red', attrs = ['bold'])
                inp = input()
                if inp == 'y':
                    data_base.cursor.close()
                    cprint('Database cursor closed successfully !', 'blue', attrs = ['bold'])
                    time.sleep(0.2)
                    data_base.connect.close()
                    cprint('Databse connection closed successfully !', 'blue', attrs = ['bold'])
                    time.sleep(0.2)
                    cprint('Good bye...', 'cyan', attrs = ['bold'])
                    time.sleep(0.5)
                    exit()
                cursor_indx = 0
                lst = main_menu()
                add_cursor(lst, cursor_indx)
                for i in lst:
                    print(i)
        elif inp == '+':
            move_cursor(lst, 1)
        elif inp == '-':
            move_cursor(lst, 0)
