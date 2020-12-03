from PIL import Image
import tkinter as tk
import os


class MainApp(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_Toolbar()
        self.create_Canvas()

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


    def create_Canvas(self):
        self.canvas = tk.Canvas(root, height=700, width=700, bg="#deadbf")
        self.canvas.pack()

    def onSave(self):
        self.quit()

    def onLoad(self):
        self.quit()

    def onExit(self):
        self.quit()

    
root = tk.Tk()
root.geometry("1600x900+300+300")
app = MainApp()
root.mainloop()