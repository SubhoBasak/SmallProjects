import os
import wikipedia as wiki
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter.font import Font
from tkfontchooser import askfont

BG_COLOR = 'gray'
TEXT_BG_COLOR = 'white'
TEXT_FG_COLOR = 'black'

home = None

def init_programme():
    global BG_COLOR
    global TEXT_BG_COLOR
    global TEXT_FG_COLOR

    global home
    home = os.environ.get('HOMEPATH')
    home = 'C://'+home
    if not os.path.isdir(os.path.join(home, '.wikipedia')):
        os.mkdir(os.path.join(home, '.wikipedia'))
    if not os.path.isfile(os.path.join(home, '.wikipedia/history.txt')):
        history_file = open(os.path.join(home, '.wikipedia/history.txt'), 'w')
        history_file.close()
    if not os.path.isfile(os.path.join(home, '.wikipedia/color.txt')):
        color_file = open(os.path.join(home, '.wikipedia/color.txt'), 'w')
        color_file.write('grey:white:black')
        color_file.close()
    with open(os.path.join(home, '.wikipedia/color.txt'), 'r') as color_file:
        colors = color_file.read().split(':')
        if len(colors) == 3:
            BG_COLOR = colors[0]
            TEXT_BG_COLOR = colors[1]
            TEXT_FG_COLOR = colors[2]

def search():
    inp = entry.get()
    if inp == None or len(inp) == 0:
        return
    text_box.delete(1.0, END)
    text_box.insert(INSERT, 'Searched for : '+inp+'\n'+'='*50+'\n')
    try:
        result = wiki.summary(inp)
        with open(os.path.join(home, '.wikipedia/history.txt'), 'a+') as history_file:
            history_file.write(inp+'<;>')
        text_box.config(fg = TEXT_FG_COLOR)
        text_box.insert(INSERT, result)
    except:
        text_box.config(fg = 'red')
        text_box.insert(INSERT, 'Something went wrong !\nPlease check your entered keyword\'s spelling or the internet connection')

def search_(event):
    search()

def search_h_(inp):
    entry.delete(0, END)
    entry.insert(0, inp)
    search()

def open_history():
    history = []
    with open(os.path.join(home, '.wikipedia/history.txt'), 'r') as history_file:
        history = history_file.read().split('<;>')
    if len(history) < 2:
        messagebox.showinfo('History', 'No history found !')
    else:
        history_window = Toplevel(root)
        history_window.resizable(False, False)
        #history_window.iconbitmap('wiki_icon.ico')

        list_box = Listbox(history_window, width = 30, height = 10, bg = BG_COLOR, fg = TEXT_FG_COLOR, selectmode = SINGLE)
        list_box.bind('<Double-Button>', lambda wrapper: search_h_(list_box.get(list_box.curselection())))
        list_box.pack()
        for i in range(len(history)):
            list_box.insert(i, history[i])

def clear_history():
    reply = messagebox.askquestion(title = 'Clear history',
                           message = 'Do you really want to clear the history ?')
    if reply == 'yes':
        with open(os.path.join(home, '.wikipedia/history.txt'), 'w') as history_file:
            history_file.write('')

def close_programme():
    reply = messagebox.askquestion(title = 'Exit',
                           message = 'Do you really want to close the programme ?')
    if reply == 'yes':
        root.quit()

def chang_bg_color():
    global BG_COLOR
    color = colorchooser.askcolor()
    if color[1] != None:
        BG_COLOR = color[1]
        with open(os.path.join(home, '.wikipedia/color.txt'), 'w') as colors:
            colors.write(':'.join([color[1], TEXT_BG_COLOR, TEXT_FG_COLOR]))
        root.config(bg = color[1])
        frame1.config(bg = color[1])
        frame2.config(bg = color[1])

def change_text_bg_color():
    global TEXT_BG_COLOR
    color = colorchooser.askcolor()
    if color[1] != None:
        TEXT_BG_COLOR = color[1]
        with open(os.path.join(home, '.wikipedia/color.txt'), 'w') as colors:
            colors.write(':'.join([BG_COLOR, color[1], TEXT_FG_COLOR]))
        text_box.config(bg=color[1])

def change_text_fg_color():
    global TEXT_FG_COLOR
    color = colorchooser.askcolor()
    if color[1] != None:
        TEXT_FG_COLOR = color[1]
        with open(os.path.join(home, '.wikipedia/color.txt'), 'w') as colors:
            colors.write(':'.join([BG_COLOR, TEXT_BG_COLOR, color[1]]))
        text_box.config(fg = color[1])

def change_font_style():
    font_ = askfont(root)
    if type(font_) == dict:
        font_ = list(font_.values())
        font_ = Font(family = font_[0], size = font_[1], weight = font_[2], slant = font_[3], underline = font_[4], overstrike = font_[5])
        text_box.config(font = font_)

root = Tk()
root.title('Wikipedia')
#root.iconbitmap('wiki_icon.ico')
root.resizable(False, False)

main_menu = Menu(root)
root.config(menu = main_menu)

file_menu = Menu(main_menu)
view_menu = Menu(main_menu)

text_color = Menu(view_menu)

main_menu.add_cascade(label = 'File', menu = file_menu)
main_menu.add_cascade(label = 'View', menu = view_menu)

file_menu.add_command(label = 'Change font', command = change_font_style)
file_menu.add_command(label = 'History', command = open_history)
file_menu.add_command(label = 'Clear history', command = clear_history)
file_menu.add_separator()
file_menu.add_command(label = 'Quit', command = close_programme)

view_menu.add_command(label = 'Background color', command = chang_bg_color)
view_menu.add_cascade(label = 'Text color', menu = text_color)

text_color.add_command(label = 'Text background', command = change_text_bg_color)
text_color.add_command(label = 'Text foreground', command = change_text_fg_color)

frame1 = Frame(root, padx = 5, pady = 5)
frame2 = Frame(root, padx = 2, pady = 2)

entry = Entry(frame1)
button = Button(frame1, text = 'Search', command = search)

root.bind('<Return>', search_)

scroll_bar = Scrollbar(frame2)
text_box = Text(frame2, width = 50, height = 20, yscrollcommand = scroll_bar.set, wrap = WORD)

scroll_bar.config(command = text_box.yview)

frame1.pack(side = TOP)
frame2.pack(side = BOTTOM)

entry.pack(side = LEFT)
button.pack(side = RIGHT)

text_box.pack(side = LEFT)
scroll_bar.pack(side = RIGHT, fill = Y)

if __name__ == '__main__':
    init_programme()
    root.config(bg = BG_COLOR)
    frame1.config(bg = BG_COLOR)
    frame2.config(bg = BG_COLOR)
    text_box.config(bg = TEXT_BG_COLOR, fg = TEXT_FG_COLOR)
    root.mainloop()
