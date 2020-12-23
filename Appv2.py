from PIL import Image, ImageTk, ImageEnhance
from PIL import ImageFilter
import numpy as np
import colorsys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import sys

from inspect import currentframe

#from https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MainApp(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Photo Editing Software, by Eric Lacey & Juliana Clarke")
        tb = Toolbar()
        cv = Canvas(500,500)
        

class Toolbar(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        #create file menu
        menuBar = tk.Menu(self.master)
        self.fileMenu = tk.Menu(self.master, tearoff=0)
        self.fileMenu.add_command(label="Save")
        self.fileMenu.add_command(label="Load", command = self.onLoad)
        self.fileMenu.add_command(label="Exit", command = self.onExit)
        menuBar.add_cascade(label="File", menu=self.fileMenu)

        #create toolbar as tk.Frane
        toolbar = tk.Frame(self.master, bd = 1, relief = tk.RAISED)
        #create toolbar buttons as part of toolbar
        btn_FindEdges = tk.Button(toolbar, text = "Find Edges", command = Find_Edges)
        btn_SharpenBlur = tk.Button(toolbar, text = "Sharpen/Blur", command = Sharpen_Blur)
        btn_ColourEdit = tk.Button(toolbar, text = "Colour Manupulation", command = Colour_Manipulation)
        btn_BrigtContr = tk.Button(toolbar, text = "Brightness/Contrast", command = Brightness_Contrast)
        btn_VisualEffect = tk.Button(toolbar, text = "VFX", command = VFX)

        #pack buttons into toolbar
        btn_FindEdges.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES, padx=2, pady=2)
        btn_SharpenBlur.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES, padx=2, pady=2)
        btn_ColourEdit.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES, padx=2, pady=2)
        btn_BrigtContr.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES, padx=2, pady=2)
        btn_VisualEffect.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES, padx=2, pady=2)

        #pack toolbar into master
        toolbar.pack(side=tk.TOP, fill=tk.X)

        #config self and pack self
        self.master.config(menu=menuBar)
        self.pack()

    def onLoad(self):
        cv = Canvas(0,0)
        #create
        file_path = filedialog.askopenfilename()
        try:
            loadedImg = Image.open(file_path)

            self.currImg = loadedImg
            cv.workingImg = self.currImg
            cv.currImg = self.currImg

        except IOError:
            print("Unable to load image")
            sys.exit(1)

        #resize canvas to loaded image size
        cv.x, cv.y = cv.currImg.size 
        cv.canvas.config(width=cv.x, height=cv.y)

        #convert image into ImageTK.PhotoImage which can be loaded into canvas
        self.currImg = ImageTk.PhotoImage(self.currImg)
        imageSprite = cv.canvas.create_image(cv.x/2,cv.y/2,image = self.currImg)

    def onExit(self):
        self.quit()

class Tool:
    

    def __init__(self):
        self.popup = tk.Toplevel(root)
        self.popup.wm_title("")

        self.popup.protocol("WM_DELETE_WINDOW", self.onClosing)

        
    def preview(self):
        pass
    def apply(self):
        cv = Canvas(0,0)
        self.preview()
        cv.currImg = cv.workingImg
        self.onClosing()

    def commonButtons(self):
        #create and pack buttons, which call commmands when completed
        previewButton = ttk.Button(self.popup, text = "Preview", command = self.preview)
        acceptButton = ttk.Button(self.popup, text = "Accept", command = self.apply)
        cancelButton = ttk.Button(self.popup, text = "Cancel", command = self.onClosing)
        previewButton.pack(pady = 15)
        acceptButton.pack(side=tk.LEFT, padx=2, pady=2)
        cancelButton.pack(side=tk.LEFT, padx=2, pady=2)

        self.popup.mainloop()

    def onClosing(self):
        cv = Canvas(0,0)
        cv.canvas.delete("all")
        try:
            self.previewImg = cv.currImg    
            self.previewImg = ImageTk.PhotoImage(self.previewImg)
            imageSprite = cv.canvas.create_image(cv.x/2,cv.y/2,image = self.previewImg)
            self.popup.destroy()        
        except:
            self.popup.destroy()

        
    

class Find_Edges(Tool):
    def __init__(self):
        super().__init__()
        label = ttk.Label(self.popup, text = "Find Edges")
        label.pack(side="top", pady = 10)
        self.commonButtons()
    def preview(self):
        cv = Canvas(0,0)
        self.previewImg = cv.currImg
        self.previewImg = self.previewImg.convert(mode = "L")
        self.previewImg = self.previewImg.filter(ImageFilter.FIND_EDGES)
        cv.workingImg = self.previewImg
        self.previewImg = ImageTk.PhotoImage(self.previewImg)
        imageSprite = cv.canvas.create_image(cv.x/2,cv.y/2,image = self.previewImg)

class Sharpen_Blur(Tool):
    def __init__(self):
        super().__init__()
        #create and pack text & slider for sharpness/blur
        label = ttk.Label(self.popup, text = "Sharpen/Blur")
        label.pack(side="top", pady = 10)
        self.slider = tk.Scale(self.popup, from_=-100, to = 100, orient=tk.HORIZONTAL)
        self.slider.pack(pady=20)
        self.commonButtons()
    def preview(self):
        cv = Canvas(0,0)

        if (self.slider.get() < 0):
            self.previewImg = cv.currImg
            self.previewImg = self.previewImg.filter(ImageFilter.GaussianBlur(self.slider.get() / 10))
            cv.workingImg = self.previewImg
            self.previewImg = ImageTk.PhotoImage(self.previewImg)
            imageSprite = cv.canvas.create_image(cv.x/2,cv.y/2,image = self.previewImg)
        elif (self.slider.get() > 0):
            self.previewImg = cv.currImg
            self.previewImg = self.previewImg.filter(ImageFilter.UnsharpMask(2, self.slider.get()* 2, 3))
            cv.workingImg = self.previewImg
            self.previewImg = ImageTk.PhotoImage(self.previewImg)
            imageSprite = cv.canvas.create_image(cv.x/2,cv.y/2,image = self.previewImg)
        else:
            self.previewImg = cv.currImg
            cv.workingImg = self.previewImg
            self.previewImg = ImageTk.PhotoImage(self.previewImg)
            imageSprite = cv.canvas.create_image(cv.x/2,cv.y/2,image = self.previewImg)


class Colour_Manipulation(Tool):
    def __init__(self):
        super().__init__()
        #create and pack text
        label = ttk.Label(self.popup, text = "Hue")
        label.pack(side="top", pady = 10)
        self.slider = tk.Scale(self.popup, from_=-180, to = 180, orient=tk.HORIZONTAL)
        self.slider.pack(pady=20)
        self.commonButtons()
        

    #https://stackoverflow.com/questions/7274221/changing-image-hue-with-python-pil
    def preview(self):
        cv = Canvas(0,0)
        rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
        hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

        def shift_hue(arr, hout):
            r, g, b, a = np.rollaxis(arr, axis=-1)
            h, s, v = rgb_to_hsv(r, g, b)
            h = hout
            r, g, b = hsv_to_rgb(h, s, v)
            arr = np.dstack((r, g, b, a))
            return arr

        def colorize(image, hue):
            """
            Colorize PIL image `original` with the given
            `hue` (hue within 0-360); returns another PIL image.
            """
            img = image.convert('RGBA')
            arr = np.array(np.asarray(img).astype('float'))
            new_img = Image.fromarray(shift_hue(arr, hue/360.).astype('uint8'), 'RGBA')

            return new_img

        self.previewImg = cv.currImg
        self.previewImg = colorize(self.previewImg, self.slider.get())
        self.previewImg = ImageTk.PhotoImage(self.previewImg)
        imageSprite = cv.canvas.create_image(cv.x/2,cv.y/2,image = self.previewImg)



        


class Brightness_Contrast(Tool):
    def __init__(self):
        super().__init__()
        #create and pack text & slider for brightness
        brightLabel = ttk.Label(self.popup, text = "Brightness")
        brightSlider = tk.Scale(self.popup, from_=-100, to=100, orient=tk.HORIZONTAL)
        brightLabel.pack(pady = 10)
        brightSlider.pack(pady = 20)
        contrLabel = ttk.Label(self.popup, text="Contrast")
        contSlider = tk.Scale(self.popup, from_=-100, to=100, orient=tk.HORIZONTAL)
        contrLabel.pack(pady=10)
        contSlider.pack(pady=20)
        self.commonButtons()

class VFX(Tool):
    def __init__(self):
        super().__init__()
        #create and pack text
        label = ttk.Label(self.popup, text = "Special Effect")
        label.pack(side="top", pady = 10)
        self.commonButtons()

class Canvas(metaclass = Singleton):
    def __init__(self, x, y):
        #create a canvas and pack it
        self.currImg = Image
        self.workingImg = Image

        self.x = x
        self.y = y
        self.canvas = tk.Canvas(root, height=x, width=y, bg="#deadbf")
        self.canvas.pack()



root = tk.Tk()
root.geometry()
app = MainApp()
root.mainloop()