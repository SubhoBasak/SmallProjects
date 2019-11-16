import os
import tkinter as tk
from tkinter.font import Font
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
import tkfontchooser

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.font_dict = {'family': 'Arial', 'size': 10, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}
        self.font = Font(family = self.font_dict.get('family'),
                         size = self.font_dict.get('size'),
                         weight = self.font_dict.get('weight'),
                         slant = self.font_dict.get('slant'),
                         underline = self.font_dict.get('underline'),
                         overstrike = self.font_dict.get('overstrike'))
        self.master.title('SB Text Editor')
        self.file_name = None
        self.bg = 'white'
        self.fg = 'black'
        self.insert = 'red'
        self.insert_width = 2

        # text box
        self.text = tk.Text(relief = tk.FLAT, undo = True, font = self.font)
        self.text.config(insertbackground = self.insert)
        self.text.config(insertwidth = self.insert_width)
        self.text.pack(fill=tk.BOTH, expand=True)
        self.text.focus()

        # main menu
        self.main_menu = tk.Menu()
        self.master.config(menu = self.main_menu)

        # file menu
        self.file_menu = tk.Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label = 'File', menu = self.file_menu)
        self.file_menu.add_command(label = 'New', accelerator = 'Ctrl+N', command = self.new_file)
        self.file_menu.add_command(label = 'Open', accelerator = 'Ctrl+O', command = self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = 'Save', accelerator = 'Ctrl+S', command = self.save_file)
        self.file_menu.add_command(label = 'Save as', accelerator = 'Ctrl+Shift+S', command = self.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = 'Quit', command = self.close_programe)

        # edit menu
        self.edit_menu = tk.Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label = 'Edit', menu = self.edit_menu)
        self.edit_menu.add_command(label = 'Undo', accelerator = 'Ctrl+Z', command = self.text.edit_undo)
        self.edit_menu.add_command(label = 'Redo', accelerator = 'Ctrl+Y',command = self.text.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label = 'Copy', accelerator = 'Ctrl+C', command = self.copy)
        self.edit_menu.add_command(label = 'Cut', accelerator = 'Ctrl+X', command = self.cut)
        self.edit_menu.add_command(label = 'Paste', accelerator = 'Ctrl+V', command = self.paste)
        self.edit_menu.add_command(label = 'Delete', command = self.delete)

        # view menu
        self.view_menu = tk.Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label = 'View', menu = self.view_menu)
        self.view_menu.add_command(label = 'Zoon in', command = self.zoom_in)
        self.view_menu.add_command(label = 'Zoom out', command = self.zoom_out)
        self.view_menu.add_separator()
        self.view_menu.add_command(label = 'Change font', command = self.change_font)

        # color menu
        self.color_menu = tk.Menu(self.view_menu, tearoff = False)
        self.view_menu.add_cascade(label = 'Change Colors', menu = self.color_menu)
        self.color_menu.add_command(label = 'Change background color', command = self.change_bg)
        self.color_menu.add_command(label = 'Change foreground color', command = self.change_fg)

        # cursor menu
        self.cursor_menu = tk.Menu(self.view_menu, tearoff = False)
        self.view_menu.add_cascade(label = 'Change cursor', menu = self.cursor_menu)
        self.cursor_menu.add_command(label = 'Change color', command = self.change_cursor_color)
        self.cursor_menu.add_command(label = 'Change width', command = self.change_cursor_width)

        # shortcuts
        self.master.bind('<Control-n>', self.new_file)
        self.master.bind('<Control-N>', self.new_file)
        self.master.bind('<Control-o>', self.open_file)
        self.master.bind('<Control-O>', self.open_file)
        self.master.bind('<Control-s>', self.save_file)
        self.master.bind('<Control-S>', self.save_file)
        self.master.bind('<Shift-Control-s>', self.save_as)
        self.master.bind('<Shift-Control-S>', self.save_as)
        self.master.bind('<Control-plus>', self.zoom_in)
        self.master.bind('<Control-minus>', self.zoom_out)
        self.master.protocol('WM_DELETE_WINDOW', self.close_programe)

    def load(self):
        self.home = os.getenv('HOMEPATH')
        self.home = 'C://'+self.home
        if not os.path.isdir(os.path.join(self.home, '.SB_Text_Editor')):
            os.mkdir(os.path.join(self.home, '.SB_Text_Editor'))
        if os.path.isfile(os.path.join(self.home, '.SB_Text_Editor/settings.txt')):
            with open(os.path.join(self.home, '.SB_Text_Editor/settings.txt'), 'r') as settings:
                tmp = settings.readline().strip().split(';')
                if len(tmp) == 6:
                    self.font_dict['family'] = tmp[0]
                    self.font_dict['size'] = int(tmp[1])
                    self.font_dict['weight'] = tmp[2]
                    self.font_dict['slant'] = tmp[3]
                    self.font_dict['underline'] = int(tmp[4])
                    self.font_dict['overstrike'] = int(tmp[5])
                    self.font = Font(family = self.font_dict['family'],
                                     size = self.font_dict['size'],
                                     weight = self.font_dict['weight'],
                                     slant = self.font_dict['slant'],
                                     underline = self.font_dict['underline'],
                                     overstrike = self.font_dict['overstrike'])
                    self.text.config(font = self.font)
                tmp = settings.readline().strip().split(';')
                if len(tmp) == 2:
                    self.bg = tmp[0]
                    self.fg = tmp[1]
                    self.text.config(bg = self.bg, fg = self.fg)
                tmp = settings.readline().strip().split(';')
                if len(tmp) == 2:
                    self.insert = tmp[0]
                    self.insert_width = tmp[1]
                    self.text.config(insertbackground = self.insert, insertwidth = self.insert_width)

    def new_file(self, event = None):
        if len(self.text.get(1.0, tk.END)) > 1:
            inp = messagebox.askyesnocancel('SB Text Editor', 'Do you want to save this file?')
            if inp == True:
                self.save_file()
            elif inp == None:
                return None
            self.file_name = None
            self.text.delete(1.0, tk.END)
            self.text.edit_reset()

    def open_file(self, event = None):
        file = filedialog.askopenfile(filetype = [('Text file', '.txt'), ('All file', '*.*')])
        if file != None:
            self.text.delete(1.0, tk.END)
            for line in file:
                self.text.insert(tk.INSERT, line)
            self.file_name = file.name

    def save_file(self, event = None):
        if self.file_name == None:
            self.save_as()
        else:
            with open(self.file_name, 'w') as file:
                file.write(self.text.get(1.0, tk.END))

    def save_as(self, event = None):
        file = filedialog.asksaveasfile(mode='w',
                                        filetypes=[('Text file', '.txt'), ('All file', '*.*')],
                                        defaultextension='.txt')
        if file != None:
            file.write(self.text.get(1.0, tk.END))
            self.file_name = file.name
            file.close()

    def close_programe(self, event = None):
        if len(self.text.get(1.0, tk.END)) > 1:
            inp = messagebox.askyesnocancel('SB Text Editor', 'Do you want to save this file?')
            if inp == True:
                self.save_file()
            elif inp == None:
                return None
        self.master.quit()

    def copy(self, event = None):
        self.text.event_generate('<<Copy>>')

    def cut(self, event = None):
        self.text.event_generate('<<Cut>>')

    def paste(self, event = None):
        self.text.event_generate('<<Paste>>')

    def delete(self, event = None):
        try:
            i1 = self.text.index('sel.first')
            i2 = self.text.index('sel.last')
            self.text.delete(i1, i2)
        except:
            return None

    def zoom_in(self, event = None):
        size = self.font.cget('size')
        size += 1
        if size > 30:
            size = 30
        self.font_dict['size'] = size
        self.font.config(size = size)
        self.text.config(font = self.font)

    def zoom_out(self, event = None):
        size = self.font.cget('size')
        size -= 1
        if size < 3:
            size = 3
        self.font_dict['size'] = size
        self.font.config(size = size)
        self.text.config(font = self.font)

    def change_font(self, event = None):
        font_dict = tkfontchooser.askfont(**self.font_dict)
        if font_dict != '':
            self.font_dict = font_dict
            font_dict = list(font_dict.values())
            font = Font(family = font_dict[0],
                        size = font_dict[1],
                        weight = font_dict[2],
                        slant = font_dict[3],
                        underline = font_dict[4],
                        overstrike = font_dict[5])
            self.font = font
            self.text.config(font = self.font)
            with open(os.path.join(self.home, '.SB_Text_Editor/settings.txt'), 'w') as settings:
                tmp = ';'.join(map(lambda item: str(item), list(self.font_dict.values())))
                tmp += '\n'+self.bg+';'+self.fg
                tmp += '\n' + self.insert + ';' + str(self.insert_width)
                settings.write(tmp)

    def change_bg(self, event = None):
        color = colorchooser.askcolor()
        if color[1] != None:
            self.bg = color[1]
            self.text.config(bg = self.bg)
            with open(os.path.join(self.home, '.SB_Text_Editor/settings.txt'), 'w') as settings:
                tmp = ';'.join(map(lambda item: str(item), list(self.font_dict.values())))
                tmp += '\n' + self.bg + ';' + self.fg
                tmp += '\n' + self.insert + ';' + str(self.insert_width)
                settings.write(tmp)

    def change_fg(self, event = None):
        color = colorchooser.askcolor()
        if color[1] != None:
            self.fg = color[1]
            self.text.config(fg = self.fg)
            with open(os.path.join(self.home, '.SB_Text_Editor/settings.txt'), 'w') as settings:
                tmp = ';'.join(map(lambda item: str(item), list(self.font_dict.values())))
                tmp += '\n'+self.bg+';'+ self.fg
                tmp += '\n' + self.insert + ';' + str(self.insert_width)
                settings.write(tmp)

    def change_cursor_color(self):
        color = colorchooser.askcolor()
        if color[1] != None:
            self.insert = color[1]
            self.text.config(insertbackground = self.insert)
            with open(os.path.join(self.home, '.SB_Text_Editor/settings.txt'), 'w') as settings:
                tmp = ';'.join(map(lambda item: str(item), list(self.font_dict.values())))
                tmp += '\n' + self.bg + ';' + self.fg
                tmp += '\n' + self.insert + ';' + str(self.insert_width)
                settings.write(tmp)

    def make_small(self):
        self.insert_width = 1
        self.text.config(insertwidth = self.insert_width)

        with open(os.path.join(self.home, '.SB_Text_Editor/settings.txt'), 'w') as settings:
            tmp = ';'.join(map(lambda item: str(item), list(self.font_dict.values())))
            tmp += '\n' + self.bg + ';' + self.fg
            tmp += '\n' + self.insert + ';' + str(self.insert_width)
            settings.write(tmp)

        self.tmp_window.destroy()

    def make_medium(self):
        self.insert_width = 3
        self.text.config(insertwidth = self.insert_width)

        with open(os.path.join(self.home, '.SB_Text_Editor/settings.txt'), 'w') as settings:
            tmp = ';'.join(map(lambda item: str(item), list(self.font_dict.values())))
            tmp += '\n' + self.bg + ';' + self.fg
            tmp += '\n' + self.insert + ';' + str(self.insert_width)
            settings.write(tmp)

        self.tmp_window.destroy()

    def make_large(self):
        self.insert_width = 5
        self.text.config(insertwidth = self.insert_width)

        with open(os.path.join(self.home, '.SB_Text_Editor/settings.txt'), 'w') as settings:
            tmp = ';'.join(map(lambda item: str(item), list(self.font_dict.values())))
            tmp += '\n' + self.bg + ';' + self.fg
            tmp += '\n' + self.insert + ';' + str(self.insert_width)
            settings.write(tmp)

        self.tmp_window.destroy()

    def change_cursor_width(self):
        self.tmp_window = tk.Toplevel()
        self.tmp_window.title('Select size')
        self.tmp_window.resizable(False, False)

        button_1 = tk.Button(self.tmp_window, text = 'Small', command = self.make_small)
        button_1.pack(side = tk.LEFT)

        button_2 = tk.Button(self.tmp_window, text='Medium', command=self.make_medium)
        button_2.pack(side = tk.LEFT)

        button_3 = tk.Button(self.tmp_window, text='Large', command=self.make_large)
        button_3.pack(side = tk.LEFT)

if __name__ == '__main__':
    root = tk.Tk()
    text_editor = TextEditor(root)
    text_editor.load()
    root.mainloop()
