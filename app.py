from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import sys


class MainApp(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.canvasX = 500
        self.canvasY = 500
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

        btn_FindEdges = tk.Button(toolbar, text = "Find Edges", command = self.onEdges)
        btn_SharpenBlur = tk.Button(toolbar, text = "Sharpen/Blur", command = self.onSharpBlur)
        btn_ColourEdit = tk.Button(toolbar, text = "Colour Manupulation" , command = self.onColManip)
        btn_BrigtContr = tk.Button(toolbar, text = "Brightness/Contrast", command = self.onBrigtCont)
        btn_VisualEffect = tk.Button(toolbar, text = "VFX", command = self.onVFX)

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
        

    def onEdges(self):

        popup = tk.Tk()
        popup.wm_title("")
        label = ttk.Label(popup, text = "Find Edges")
        label.pack(side="top", fill="x", pady = 10)
        previewButton = ttk.Button(popup, text = "Preview", command = popup.destroy)
        acceptButton = ttk.Button(popup, text = "Accept", command = popup.destroy)
        cancelButton = ttk.Button(popup, text = "Cancel", command = popup.destroy)
        previewButton.pack(pady = 15)
        acceptButton.pack(side=tk.LEFT, padx=2, pady=2)
        cancelButton.pack(side=tk.LEFT, padx=2, pady=2)
        popup.mainloop()

    def onSharpBlur(self):
        popup = tk.Tk()
        popup.wm_title("")
        label = ttk.Label(popup, text = "Sharpen/Blur")
        label.pack(side="top", fill="x", pady = 10)
        previewButton = ttk.Button(popup, text = "Preview", command = popup.destroy)
        acceptButton = ttk.Button(popup, text = "Accept", command = popup.destroy)
        cancelButton = ttk.Button(popup, text = "Cancel", command = popup.destroy)
        previewButton.pack(pady = 15)
        acceptButton.pack(side=tk.LEFT, padx=2, pady=2)
        cancelButton.pack(side=tk.LEFT, padx=2, pady=2)
        popup.mainloop()

    def onColManip(self):
        popup = tk.Tk()
        popup.wm_title("")
        label = ttk.Label(popup, text = "Colour Manipulation")
        label.pack(side="top", fill="x", pady = 10)
        previewButton = ttk.Button(popup, text = "Preview", command = popup.destroy)
        acceptButton = ttk.Button(popup, text = "Accept", command = popup.destroy)
        cancelButton = ttk.Button(popup, text = "Cancel", command = popup.destroy)
        previewButton.pack(pady = 15)
        acceptButton.pack(side=tk.LEFT, padx=2, pady=2)
        cancelButton.pack(side=tk.LEFT, padx=2, pady=2)
        popup.mainloop()

    def onBrigtCont(self):
        popup = tk.Tk()
        popup.wm_title("")
        label = ttk.Label(popup, text = "Brightness/Contrast")
        label.pack(side="top", fill="x", pady = 10)
        previewButton = ttk.Button(popup, text = "Preview", command = popup.destroy)
        acceptButton = ttk.Button(popup, text = "Accept", command = popup.destroy)
        cancelButton = ttk.Button(popup, text = "Cancel", command = popup.destroy)
        previewButton.pack(pady = 15)
        acceptButton.pack(side=tk.LEFT, padx=2, pady=2)
        cancelButton.pack(side=tk.LEFT, padx=2, pady=2)
        popup.mainloop()

    def onVFX(self):
        popup = tk.Tk()
        popup.wm_title("")
        label = ttk.Label(popup, text = "Special Effect")
        label.pack(side="top", fill="x", pady = 10)
        previewButton = ttk.Button(popup, text = "Preview", command = popup.destroy)
        acceptButton = ttk.Button(popup, text = "Accept", command = popup.destroy)
        cancelButton = ttk.Button(popup, text = "Cancel", command = popup.destroy)
        previewButton.pack(pady = 15)
        acceptButton.pack(side=tk.LEFT, padx=2, pady=2)
        cancelButton.pack(side=tk.LEFT, padx=2, pady=2)
        popup.mainloop()


    def onExit(self):
        self.quit()

class Tool:
    def __init__(self, icon):
        self.icon = icon
    def action(self):
        return

class Find_Edges(Tool):
    def action(self, currentImage):
        self.currentImage = currentImage.filter(ImageFilter.FIND_EDGES)
        return

class Sharpness_Blur(Tool):
    def action(self, currentImage):
        blurRad = Scale(master, from_=0, to=5, orient=HORIZONTAL)
        blurRad.pack()
        self.currentImage = currentImage.filter(ImageFilter.GaussianBlur(radius = blurRad.get()))

        sharpFactor = Scale(master, from_=0, to=5, orient=HORIZONTAL)
        sharpFactor.pack()
        sharpener = ImageEnhance.Sharpness(self.currentImage)
        self.currentImage = sharpener.enhance(sharpFactor.get())
        return

class Colour_Manipulation(Tool):
    def action(self, currentImage):
        return

class Contrast_Brightness(Tool):
    def action(self, currentImage):
        return

class Neon_Effect(Tool):
    def action(self, currentImage):
        return

    
root = tk.Tk()
root.geometry()
app = MainApp()
root.mainloop()