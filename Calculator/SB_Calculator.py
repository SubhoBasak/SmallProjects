import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.master.title('SB Calculator')
        self.master.iconbitmap('icon.ico')
        self.master.config(bg = '#636664')
        self.master.minsize(300, 400)

        self.font = ('Arial', 18)
        self.data = tk.StringVar()
        self.val = None
        self.operator = None
        self.clrscr = False

        self.top_level = tk.Frame(self.master, bg = '#636664')
        self.top_level.pack(fill = tk.BOTH, expand = True, padx = 5, pady = 5)

        self.entry = tk.Entry(self.top_level, font = ('Arial', 30), width = 10, textvariable = self.data, bg = '#7d827e')
        self.entry.pack(fill = tk.BOTH, expand = True, pady = 5)

        self.frame_0 = tk.Frame(self.top_level, bg = '#636664')
        self.frame_0.pack(fill = tk.BOTH, expand = True)

        self.frame_1 = tk.Frame(self.top_level, bg = '#636664')
        self.frame_1.pack(fill = tk.BOTH, expand = True)

        self.frame_2 = tk.Frame(self.top_level, bg = '#636664')
        self.frame_2.pack(fill = tk.BOTH, expand = True)

        self.frame_3 = tk.Frame(self.top_level, bg = '#636664')
        self.frame_3.pack(fill = tk.BOTH, expand = True)

        self.frame_4 = tk.Frame(self.top_level, bg = '#636664')
        self.frame_4.pack(fill = tk.BOTH, expand = True)

        self.button_DEL = tk.Button(self.frame_0, text = 'Delete', font = ('Arial', 12), command = self.delete, height = 1)
        self.button_DEL.config(relief = tk.FLAT, bg = 'gray')
        self.button_DEL.pack(side = tk.RIGHT, padx = 2, pady = 2)

        self.button_CLR = tk.Button(self.frame_0, text = 'Clear', font = ('Arial', 12), command = self.clear, height = 1)
        self.button_CLR.config(relief = tk.FLAT, bg = 'gray')
        self.button_CLR.pack(side = tk.RIGHT, padx = 2, pady = 2)

        self.button_1 = tk.Button(self.frame_1, text = '1', font = self.font, command = self.one, height = 2, width = 4)
        self.button_1.config(relief = tk.FLAT, bg = 'gray')
        self.button_1.pack(side = tk.LEFT, fill = tk.BOTH, expand = True, padx = 2, pady = 2)

        self.button_2 = tk.Button(self.frame_1, text = '2', font = self.font, command = self.two, height = 2, width = 4)
        self.button_2.config(relief=tk.FLAT, bg='gray')
        self.button_2.pack(side = tk.LEFT, fill = tk.BOTH, expand = True, padx = 2, pady = 2)

        self.button_3 = tk.Button(self.frame_1, text = '3', font = self.font, command = self.three, height = 2, width = 4)
        self.button_3.config(relief=tk.FLAT, bg='gray')
        self.button_3.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        self.button_4 = tk.Button(self.frame_2, text = '4', font = self.font, command = self.four, height = 2, width = 4)
        self.button_4.config(relief=tk.FLAT, bg='gray')
        self.button_4.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        self.button_5 = tk.Button(self.frame_2, text = '5', font = self.font, command = self.five, height = 2, width = 4)
        self.button_5.config(relief=tk.FLAT, bg='gray')
        self.button_5.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        self.button_6 = tk.Button(self.frame_2, text = '6', font = self.font, command = self.six, height = 2, width = 4)
        self.button_6.config(relief=tk.FLAT, bg='gray')
        self.button_6.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        self.button_7 = tk.Button(self.frame_3, text = '7', font = self.font, command = self.seven, height = 2, width = 4)
        self.button_7.config(relief=tk.FLAT, bg='gray')
        self.button_7.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        self.button_8 = tk.Button(self.frame_3, text = '8', font = self.font, command = self.eight, height = 2, width = 4)
        self.button_8.config(relief=tk.FLAT, bg='gray')
        self.button_8.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        self.button_9 = tk.Button(self.frame_3, text = '9', font = self.font, command = self.nine, height = 2, width = 4)
        self.button_9.config(relief=tk.FLAT, bg='gray')
        self.button_9.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        self.button_0 = tk.Button(self.frame_4, text = '0', font = self.font, command = self.zero, height = 2, width = 4)
        self.button_0.config(relief=tk.FLAT, bg='gray')
        self.button_0.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        self.button_DOT = tk.Button(self.frame_4, text = '.', font = self.font, command = self.dot, height = 2, width = 4)
        self.button_DOT.config(relief=tk.FLAT, bg='gray')
        self.button_DOT.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        self.button_EQL = tk.Button(self.frame_4, text = '=', font = self.font, command = self.enter, height = 2, width = 4)
        self.button_EQL.config(relief=tk.FLAT, bg='gray')
        self.button_EQL.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        self.button_ADD = tk.Button(self.frame_4, text = '+', font = self.font, command = self.add_function, height = 2, width = 4)
        self.button_ADD.config(relief=tk.FLAT, bg='gray')
        self.button_ADD.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        self.button_SUB = tk.Button(self.frame_3, text = '-', font = self.font, command = self.sub_function, height = 2, width = 4)
        self.button_SUB.config(relief=tk.FLAT, bg='gray')
        self.button_SUB.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        self.button_MUL = tk.Button(self.frame_2, text = '*', font = self.font, command = self.mul_fuction, height = 2, width = 4)
        self.button_MUL.config(relief=tk.FLAT, bg='gray')
        self.button_MUL.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

        self.button_DIV = tk.Button(self.frame_1, text = '/', font = self.font, command = self.div_function, height = 2, width = 4)
        self.button_DIV.config(relief=tk.FLAT, bg='gray')
        self.button_DIV.pack(side = tk.LEFT, fill=tk.BOTH, expand=True, padx = 2, pady = 2)

    def delete(self):
        tmp = self.data.get()
        if len(tmp) > 0:
            tmp = tmp[:-1]
            self.data.set(tmp)

    def clear(self):
        self.data.set('')
        self.val = None
        self.operator = None
        self.clrscr = False

    def one(self):
        if self.clrscr:
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '1')

    def two(self):
        if self.clrscr:
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '2')

    def three(self):
        if self.clrscr:
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '3')

    def four(self):
        if self.clrscr:
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '4')

    def five(self):
        if self.clrscr:
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '5')

    def six(self):
        if self.clrscr:
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '6')

    def seven(self):
        if self.clrscr:
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '7')

    def eight(self):
        if self.clrscr:
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '8')

    def nine(self):
        if self.clrscr:
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '9')

    def zero(self):
        if self.clrscr:
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            self.entry.insert(tk.END, '0')

    def dot(self):
        if self.clrscr:
            self.clrscr = False
            self.data.set('')
        if len(self.data.get()) < 12:
            if not '.' in self.data.get():
                if len(self.data.get()) > 0:
                    self.entry.insert(tk.END, '.')
                else:
                    self.entry.insert(tk.END, '0.')

    def enter(self):
        if self.val != None:
            tmp = self.data.get()
            if len(tmp) < 0:
                return None
            self.data.set(eval(self.val + self.operator + tmp))
            self.val = None
            self.operator = None
            self.clrscr = True

    def add_function(self):
        if self.val == None:
            tmp = self.data.get()
            if len(tmp) > 0:
                self.val = tmp
            self.operator = '+'
            self.data.set('')
        else:
            tmp = self.data.get()
            if len(tmp) > 0:
                result = str(eval(self.val+self.operator+tmp))
                self.data.set(result)
                self.val = result
                self.operator = '+'
                self.clrscr = True
            else:
                self.operator = '+'

    def sub_function(self):
        if self.val == None:
            tmp = self.data.get()
            if len(tmp) > 0:
                self.val = tmp
            self.operator = '-'
            self.data.set('')
        else:
            tmp = self.data.get()
            if len(tmp) > 0:
                result = str(eval(self.val + self.operator + tmp))
                self.data.set(result)
                self.val = result
                self.operator = '-'
                self.clrscr = True
            else:
                self.operator = '-'

    def mul_fuction(self):
        if self.val == None:
            tmp = self.data.get()
            if len(tmp) > 0:
                self.val = tmp
            self.operator = '*'
            self.data.set('')
        else:
            tmp = self.data.get()
            if len(tmp) > 0:
                result = str(eval(self.val + self.operator + tmp))
                self.data.set(result)
                self.val = result
                self.operator = '*'
                self.clrscr = True
            else:
                self.operator = '*'

    def div_function(self):
        if self.val == None:
            tmp = self.data.get()
            if len(tmp) > 0:
                self.val = tmp
            self.operator = '/'
            self.data.set('')
        else:
            tmp = self.data.get()
            if len(tmp) > 0:
                result = str(eval(self.val + self.operator + tmp))
                self.data.set(result)
                self.val = result
                self.operator = '/'
                self.clrscr = True
            else:
                self.operator = '/'

root = tk.Tk()
app = App(root)
root.mainloop()
