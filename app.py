from PIL import Image, ImageTk
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

        btn_FindEdges.pack(side=tk.LEFT, expand=tk.YES, padx=2, pady=2)
        btn_SharpenBlur.pack(side=tk.LEFT, expand=tk.YES, padx=2, pady=2)
        btn_ColourEdit.pack(side=tk.LEFT, expand=tk.YES, padx=2, pady=2)
        btn_BrigtContr.pack(side=tk.LEFT, expand=tk.YES, padx=2, pady=2)
        btn_VisualEffect.pack(side=tk.LEFT, expand=tk.YES, padx=2, pady=2)

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
        popup = tk.Toplevel(root)
        popup.wm_title("")
        label = ttk.Label(popup, text = "Find Edges")
        label.pack(side="top", pady = 10)
        previewButton = ttk.Button(popup, text = "Preview", command = popup.destroy)
        acceptButton = ttk.Button(popup, text = "Accept", command = popup.destroy)
        cancelButton = ttk.Button(popup, text = "Cancel", command = popup.destroy)
        previewButton.pack(pady = 15)
        acceptButton.pack(side=tk.LEFT, padx=2, pady=2)
        cancelButton.pack(side=tk.LEFT, padx=2, pady=2)
        popup.mainloop()

    def onSharpBlur(self):
        popup = tk.Toplevel(root)
        popup.wm_title("")

        label = ttk.Label(popup, text = "Sharpen/Blur")
        label.pack(side="top", pady = 10)
        slider = tk.Scale(popup, from_=-10, to = 10, orient=tk.HORIZONTAL)
        slider.pack(pady=20)

        previewButton = ttk.Button(popup, text = "Preview", command = popup.destroy)
        acceptButton = ttk.Button(popup, text = "Accept", command = popup.destroy)
        cancelButton = ttk.Button(popup, text = "Cancel", command = popup.destroy)
        previewButton.pack(pady = 15)
        acceptButton.pack(side=tk.LEFT, padx=2, pady=2)
        cancelButton.pack(side=tk.LEFT, padx=2, pady=2)
        popup.mainloop()

    def onColManip(self):
        popup = tk.Toplevel(root)
        popup.wm_title("")

        label = ttk.Label(popup, text = "Hue")
        label.pack(side="top", pady = 10)
        slider = tk.Scale(popup, from_=-100, to = 100, orient=tk.HORIZONTAL)
        slider.pack(pady=20)

        previewButton = ttk.Button(popup, text = "Preview", command = popup.destroy)
        acceptButton = ttk.Button(popup, text = "Accept", command = popup.destroy)
        cancelButton = ttk.Button(popup, text = "Cancel", command = popup.destroy)
        previewButton.pack(pady = 15)
        acceptButton.pack(side=tk.LEFT, padx=2, pady=2)
        cancelButton.pack(side=tk.LEFT, padx=2, pady=2)
        popup.mainloop()

    def onBrigtCont(self):
        popup = tk.Toplevel(root)
        popup.wm_title("")

        brightLabel = ttk.Label(popup, text = "Brightness")
        brightSlider = tk.Scale(popup, from_=0, to=100, orient=tk.HORIZONTAL)
        brightLabel.pack(pady = 10)
        brightSlider.pack(pady = 20)

        contrLabel = ttk.Label(popup, text="Contrast")
        contSlider = tk.Scale(popup, from_=0, to=100, orient=tk.HORIZONTAL)
        contrLabel.pack(pady=10)
        contSlider.pack(pady=20)

        previewButton = ttk.Button(popup, text = "Preview", command = popup.destroy)
        acceptButton = ttk.Button(popup, text = "Accept", command = popup.destroy)
        cancelButton = ttk.Button(popup, text = "Cancel", command = popup.destroy)
        previewButton.pack(pady = 15)
        acceptButton.pack(side=tk.LEFT, padx=2, pady=2)
        cancelButton.pack(side=tk.LEFT, padx=2, pady=2)
        popup.mainloop()

    def onVFX(self):
        popup = tk.Toplevel(root)
        popup.wm_title("")
        label = ttk.Label(popup, text = "Special Effect")
        label.pack(side="top", pady = 10)
        previewButton = ttk.Button(popup, text = "Preview", command = popup.destroy)
        acceptButton = ttk.Button(popup, text = "Accept", command = popup.destroy)
        cancelButton = ttk.Button(popup, text = "Cancel", command = popup.destroy)
        previewButton.pack(pady = 15)
        acceptButton.pack(side=tk.LEFT, padx=2, pady=2)
        cancelButton.pack(side=tk.LEFT, padx=2, pady=2)
        popup.mainloop()


    def onExit(self):
        self.quit()

    
root = tk.Tk()
root.geometry()
app = MainApp()
root.mainloop()