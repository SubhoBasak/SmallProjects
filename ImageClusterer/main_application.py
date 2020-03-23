import tkinter as tk
import tkinter.ttk as ttk
import path_manager as pm
import numpy as np
from PIL import Image, ImageDraw
from tkinter import messagebox
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MainApplication:
    def __init__(self):
        self.inp_data = []
        self.draw_started_or_not = False
        self.count = 0

        self.old_x = None
        self.old_y = None
        self.paint_or_erase = 1

        self.root = tk.Tk()

        self.style = ttk.Style()
        self.style.map('TButton', foreground = [('active', 'green'), ('!focus', '#f229e8'), ('focus', 'blue')],
                       background = [('active', 'green'), ('!focus', '#f229e8'), ('focus', 'blue')])
        self.style.map('TMenubutton', foreground = [('active', 'green'), ('!focus', '#3923b8')])

        self.active_model = tk.StringVar()
        self.n_clusters = tk.StringVar()

        self.root._width_ = 640
        self.root._height_ = 480
        self.root.title('Cluster it')
        self.root.geometry('%dx%d+%d+%d'%(self.root._width_,
                                          self.root._height_,
                                          self.root.winfo_screenwidth()/2-self.root._width_/2,
                                          self.root.winfo_screenheight()/2-self.root._height_/2))
        self.root.minsize(250, 200)
        self.root.iconphoto(False, tk.PhotoImage(file = pm.app_icon))
        self.root.protocol('WM_DELETE_WINDOW', self.quit)

        self.option_fram = tk.Frame(self.root, bg = '#af79e8')
        self.option_fram.pack(side = 'top', fill = 'x')

        self.model = ttk.OptionMenu(self.option_fram, self.active_model, 'KMeans', 'KMeans', 'DBSCAN')
        self.model.config()
        self.model.pack(side = 'left', padx = 20)

        self.clusters = ttk.OptionMenu(self.option_fram, self.n_clusters, 'Auto', 'Auto', 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.clusters.pack(side = 'left', padx = 20)

        self.make_cluster = ttk.Button(self.option_fram, text = 'Cluster it', command = self.cluster_imgs)
        self.make_cluster.pack(side = 'right', padx = 10)

        self.next = ttk.Button(self.option_fram, text = 'Next', command = self.load_next)
        self.next.pack(side = 'right', padx = 10)

        self.lower_frame = tk.Frame(self.root)
        self.lower_frame.pack(side = 'top', fill = 'both', expand = True)

        self.tools_frame = tk.Frame(self.lower_frame, bg = '#79afe8')
        self.tools_frame.pack(side = 'left', fill = 'y')

        self.pen = ttk.Button(self.tools_frame, image = tk.PhotoImage(file = pm.pencil_icon), text = 'Pencil', command = self.use_pencil)
        self.pen.grid(row = 1, column = 1, padx = 2, pady = 3)

        self.eraser = ttk.Button(self.tools_frame, image = tk.PhotoImage(file = pm.eraser_icon), text = 'Eraser', command = self.use_eraser)
        self.eraser.grid(row = 2, column = 1, padx = 2, pady = 3)

        self.clear = ttk.Button(self.tools_frame, image = tk.PhotoImage(file = pm.clear_icon), text = 'Clear all', command = self.clear_all)
        self.clear.grid(row = 3, column = 1, padx = 2, pady = 3)

        self.exit = ttk.Button(self.tools_frame, text = 'Quit', command = self.quit)
        self.exit.grid(row = 4, column = 1, padx = 2, pady = 3)

        self.count_label = tk.Label(self.tools_frame, text = 'Images : 0', font = ('Arial',10), bg = '#79afe8')
        self.count_label.grid(row = 5, column = 1, padx = 2, pady = 3)

        self.canvas = tk.Canvas(self.lower_frame, bg = '#f2aee0')
        self.canvas.pack(side = 'left', fill = 'both', expand = True)
        self.canvas.update()

        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

        self.pil_img = None
        self.draw = None

    def quit(self):
        if messagebox.askquestion('Quit', 'Do you really want to quit?', default = 'no') == 'yes':
            self.root.quit()
            exit()

    def paint(self, event):
        if self.pil_img == None:
            self.pil_img = Image.new('L', (self.canvas.winfo_width(), self.canvas.winfo_height()), 'white')
            self.draw = ImageDraw.Draw(self.pil_img)

        color = ['#fff71c' if self.paint_or_erase else '#f2aee0']
        if self.old_x:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width = 10, smooth = True, capstyle = 'round', fill = color)
            self.draw.line([self.old_x, self.old_y, event.x, event.y], 'black', 10)
            self.draw_started_or_not = True
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def clear_all(self):
        self.canvas.delete('all')
        self.pil_img = Image.new('L', (self.canvas.winfo_width(), self.canvas.winfo_height()), 'white')
        self.draw = ImageDraw.Draw(self.pil_img)
        self.draw_started_or_not = False

    def use_pencil(self):
        self.paint_or_erase = 1

    def use_eraser(self):
        self.paint_or_erase = 0
        messagebox.showwarning('Mis-clustering!', 'Use eraser only for correct the drawing. If you \
erase all the image using eraser and then click on next button the it will take the empty image \
as a data set and it can cause mis-clustering. So if you want to skip this drawed image and want \
to draw it again then click the clear all button.')

    def load_next(self):
        if not self.draw_started_or_not:
            return None
        tmp = np.array(self.pil_img)
        w, h = len(tmp[0]), len(tmp)
        x1, x2, y1, y2 = 0, w, 0, h
        for i in range(w):
            flag = 0
            for j in tmp[:, i]:
                if j == 0:
                    x1 = i
                    flag = 1
                    break
            if flag == 1:
                break
        for i in range(w-1, -1, -1):
            flag = 0
            for j in tmp[:, i].ravel():
                if j == 0:
                    x2 = i
                    flag = 1
                    break
            if flag == 1:
                break
        for i in range(h):
            flag = 0
            for j in tmp[i]:
                if j == 0:
                    y1 = i
                    flag = 1
                    break
            if flag == 1:
                break
        for i in range(h-1, -1, -1):
            flag = 0
            for j in tmp[i]:
                if j == 0:
                    y2 = i
                    flag = 1
                    break
            if flag == 1:
                break
        if abs(x2-x1) > 100 or abs(y2-y1) > 100:
            self.inp_data.append(np.array(self.pil_img.resize((100, 100))).ravel())
        else:
            if abs(x1-x2) < 100:
                dis = (100-abs(x1-x2))//2
                if x1-dis < 0:
                    x1 = 0
                    x2 = 100
                elif x2+dis > w:
                    x2 = w
                    x1 = w-100
                else:
                    x1 -= dis
                    x2 += dis
                    if abs(x1-x2) == 99:
                        if x1 >= 1:
                            x1 -= 1
                        else:
                            x2 += 1
            if abs(y1 - y2) < 100:
                dis = (100 - abs(y1 - y2)) // 2
                if y1 - dis < 0:
                    y1 = 0
                    y2 = 100
                elif y2 + dis > h:
                    y2 = h
                    y1 = h - 100
                else:
                    y1 -= dis
                    y2 += dis
                    if abs(y1 - y2) == 99:
                        if y1 >= 1:
                            y1 -= 1
                        else:
                            y2 += 1
            self.inp_data.append(tmp[y1:y2, x1:x2].ravel())
        self.canvas.delete('all')
        self.pil_img = None
        self.draw = None
        self.draw_started_or_not = False
        self.count += 1
        self.count_label.config(text = 'Images : '+str(self.count))

    def cluster_imgs(self):
        if self.draw_started_or_not:
            self.load_next()
        if len(self.inp_data) < 3:
            messagebox.showerror('Few data', 'There is too few data to cluster. Please add more images.')
            return None
        self.inp_data = np.array(self.inp_data)
        if self.n_clusters.get() == 'Auto':
            range_cluster = range(2, len(self.inp_data))
            silhouette_score_ = []
            for k in range_cluster:
                kmeans = KMeans(n_clusters = k)
                kmeans.fit(self.inp_data)

                silhouette_score_.append(silhouette_score(self.inp_data, kmeans.labels_))
            k = range_cluster[np.argmax(silhouette_score_)]
        else:
            k = int(self.n_clusters.get())
        if self.active_model.get() == 'KMeans':
            kmeans = KMeans(n_clusters = k)
            kmeans.fit(self.inp_data)

        top = tk.Toplevel()
        top.resizable(False, False)

        notebook = ttk.Notebook(top)
        for i in np.unique(kmeans.labels_):
            fm = tk.Frame(notebook, height = 300, width = 500)
            indx = kmeans.labels_ == i
            ln = len(self.inp_data[indx])
            rows = ln//5+1
            fig = plt.figure(figsize = (6, 3))
            for j, k in enumerate(self.inp_data[indx]):
                axs = fig.add_subplot(rows, 5, j+1)
                axs.imshow(k.reshape(100, 100), cmap = 'binary_r')
                axs.axis(False)
            cnv = FigureCanvasTkAgg(fig, fm)
            widget = cnv.get_tk_widget()
            widget.pack(side = 'left')
            notebook.add(fm, text = 'Cluster '+str(i+1))
        notebook.pack()

        self.inp_data = []
        self.canvas.delete('all')
        self.pil_img = Image.new('L', (self.canvas.winfo_width(), self.canvas.winfo_height()), 'white')
        self.draw = ImageDraw.Draw(self.pil_img)
        self.count = 0
        self.count_label.config(text='Images : ' + str(self.count))

        top.protocol('WM_DELETE_WINDOW', top.destroy)
        top.mainloop()

if __name__ == '__main__':
    App = MainApplication()
    App.root.mainloop()