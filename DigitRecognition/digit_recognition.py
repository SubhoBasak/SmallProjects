import time
import joblib
import random
import threading
import numpy as np
import tkinter as tk
import pyttsx3
import conf_paths as cf
from PIL import Image, ImageTk, ImageDraw
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from tkinter import messagebox

class MainWindow:
    def __init__(self, root):
        self.top = None
        self.old_x = None
        self.old_y = None
        self.draw = False

        self.sound_var = tk.IntVar()
        self.sound_var.set(1)

        self.root = root
        self.root.title('Digit Recognition')
        self.root.geometry('250x400+200+200')
        self.root.resizable(False, False)

        self.main_menu = tk.Menu(self.root, tearoff = False)
        self.root.config(menu = self.main_menu)

        self.sound_menu = tk.Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label = 'Sound', menu = self.sound_menu)
        self.sound_menu.add_radiobutton(label = 'On', variable = self.sound_var, value = True)
        self.sound_menu.add_radiobutton(label = 'Off', variable = self.sound_var, value = False)

        self.output_label = tk.Label(self.root)
        self.output_label.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        self.output_label.config(bg = '#adcaf7')

        self.input_canvas = tk.Canvas(self.root, width = 100, height = 100)
        self.input_canvas.pack(side = tk.BOTTOM, fill = tk.BOTH, expand = True)
        self.input_canvas.config(bg = '#bfd4f5')
        self.input_canvas.bind('<B1-Motion>', self.paint)
        self.input_canvas.bind('<ButtonRelease-1>', self.reset)

        self.root.update()
        self.classifier = joblib.load(cf.__CLASSIFIER__)
        self.engine = pyttsx3.init()

        self.tmp_img = Image.new('L', (self.input_canvas.winfo_width(), self.input_canvas.winfo_height()), 'black')
        self.tmp_draw = ImageDraw.Draw(self.tmp_img)

    def paint(self, event):
        if self.top:
            self.top.destroy()
        if self.old_x != None:
            self.input_canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                          width = 15, smooth = True, capstyle = 'round')
            self.tmp_draw.line([self.old_x, self.old_y, event.x, event.y], 'white', 15)
            self.draw = True
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

        if self.draw == False:
            return None

        self.tmp_img = self.tmp_img.resize((28, 28))
        self.tmp_img = np.array(self.tmp_img)
        self.predict_digit()

        self.top = tk.Toplevel()
        self.top.geometry('200x200+100+100')

        fig = plt.figure()
        axs = fig.add_subplot(1, 1, 1)

        axs.imshow(self.tmp_img.ravel().reshape(28, 28))

        fig_cnv = FigureCanvasTkAgg(fig, self.top)
        widget = fig_cnv.get_tk_widget()
        widget.pack()

        self.tmp_img = Image.new('L', (self.input_canvas.winfo_width(), self.input_canvas.winfo_height()), 'black')
        self.tmp_draw = ImageDraw.Draw(self.tmp_img)
        self.input_canvas.delete('all')


    def predict_digit(self):
        x = self.classifier.predict_proba([self.tmp_img.ravel()])[0]
        indx = x.argmax()

        if x[indx] < 0.6:
            self.output_label.config(text = '')
            if self.sound_var.get() == 1:
                task = threading.Thread(target = self.not_found)
                task.start()
            messagebox.showerror('Not recognized',
                                 'I can\'t recognized what you write, Plese make the image more clear.')
            return None
        if indx == 0:
            self.output_label.config(text = '0', font = ('Arial', 30))
        elif indx == 1:
            self.output_label.config(text = '1', font = ('Arial', 30))
        elif indx == 2:
            self.output_label.config(text = '2', font = ('Arial', 30))
        elif indx == 3:
            self.output_label.config(text = '3', font = ('Arial', 30))
        elif indx == 4:
            self.output_label.config(text = '4', font = ('Arial', 30))
        elif indx == 5:
            self.output_label.config(text = '5', font = ('Arial', 30))
        elif indx == 6:
            self.output_label.config(text = '6', font = ('Arial', 30))
        elif indx == 7:
            self.output_label.config(text = '7', font = ('Arial', 30))
        elif indx == 8:
            self.output_label.config(text = '8', font = ('Arial', 30))
        elif indx == 9:
            self.output_label.config(text = '9', font = ('Arial', 30))

        if self.sound_var.get() == 1:
            task = threading.Thread(target = self.speak, args = [indx, x[indx]])
            task.start()

    def not_found(self):
        try:
            self.engine.say('Sorry, but I can\'t recognized what you write, Plese make the image more clear.')
            self.engine.runAndWait()
        except RuntimeError:
            time.sleep(1000)
            self.not_found()

    def speak(self, val, prob):
        if prob > 0.9:
            speech = random.sample(['Ohh, It is ', 'I am sure it is '], 1)
            speech += str(val)
            self.engine.say(speech)
        elif prob > 0.8:
            speech = random.sample(['I think it is ', 'eighty percent sure it is '], 1)
            speech += str(val)
            self.engine.say(speech)
        elif prob > 0.7:
            speech = random.sample(['It is very close to ', 'There is little bit of confusion, but may be it is '], 1)
            speech += str(val)
            self.engine.say(speech)
        elif prob > 0.6:
            speech = random.sample(['Not sure, but looking like ', 'May be I am wrong, but it is look like '], 1)
            speech += str(val)
            self.engine.say(speech)
        try:
            self.engine.runAndWait()
        except RuntimeError:
            time.sleep(2000)
            self.speak(val, prob)


if __name__ == '__main__':
    root = tk.Tk()
    root.iconphoto(False, tk.PhotoImage(file = cf.__ICON__))
    app = MainWindow(root)
    root.mainloop()