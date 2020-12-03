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
        self.fileMenu.add_command(label="Exit", command=self.onExit)
        menuBar.add_cascade(label="File", menu=self.fileMenu)

        toolbar = tk.Frame(self.master, bd = 1, relief = tk.RAISED)


    def create_Canvas(self):
        self.canvas = tk.Canvas(root, height=700, width=700, bg="#deadbf")
        self.canvas.pack()

    def onExit(self):
        self.quit()

    
root = tk.Tk()
root.geometry("1600x900+300+300")
app = MainApp()
root.mainloop()