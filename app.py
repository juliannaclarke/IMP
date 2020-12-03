from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import os
import sys


class MainApp(tk.Frame):

    canvasX = 500
    canvasY = 500


    def __init__(self, master=None):
        super().__init__(master)
        self.create_Toolbar()
        self.create_Canvas(self.canvasX,self.canvasY)

    def create_Toolbar(self):
        self.master.title("Toolbar")

        menuBar = tk.Menu(self.master)
        self.fileMenu = tk.Menu(self.master, tearoff=0)
        self.fileMenu.add_command(label="Save", command=self.onSave)
        self.fileMenu.add_command(label="Load", command=self.onLoad)
        self.fileMenu.add_command(label="Exit", command=self.onExit)
        menuBar.add_cascade(label="File", menu=self.fileMenu)

        toolbar = tk.Frame(self.master, bd = 1, relief = tk.RAISED)

        btn_FindEdges = tk.Button(toolbar, text = "Find Edges")
        btn_SharpenBlur = tk.Button(toolbar, text = "Sharpen/Blur")
        btn_ColourEdit = tk.Button(toolbar, text = "Colour Manupulation")
        btn_BrigtContr = tk.Button(toolbar, text = "Brightness/Contrast")
        btn_VisualEffect = tk.Button(toolbar, text = "VFX")

        btn_FindEdges.pack(side=tk.LEFT, padx=2, pady=2)
        btn_SharpenBlur.pack(side=tk.LEFT, padx=2, pady=2)
        btn_ColourEdit.pack(side=tk.LEFT, padx=2, pady=2)
        btn_BrigtContr.pack(side=tk.LEFT, padx=2, pady=2)
        btn_VisualEffect.pack(side=tk.LEFT, padx=2, pady=2)

        toolbar.pack(side=tk.TOP, fill=tk.X)
        self.master.config(menu=menuBar)
        self.pack()


    def create_Canvas(self, x, y):
        self.canvas = tk.Canvas(root, height=x, width=y, bg="#deadbf")
        self.canvas.pack()

    def onSave(self):
        self.quit()

    def onLoad(self):
        file_path = filedialog.askopenfilename()
        try:
            self.pilImg = Image.open(file_path)

        except IOError:
            print("Unable to load image")
            sys.exit(1)

        self.canvasX, self.canvasY = self.pilImg.size 
        self.canvas.config(width=self.canvasX, height=self.canvasY)

        self.tkImage = ImageTk.PhotoImage(self.pilImg)
        self.imagesprite = self.canvas.create_image(self.canvasX/2,self.canvasY/2,image = self.tkImage)



    def onExit(self):
        self.quit()

    
root = tk.Tk()
root.geometry()
app = MainApp()
root.mainloop()