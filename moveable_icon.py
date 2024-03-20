from tkinter import *
from PIL import *
from PIL import ImageTk, Image
from tkinter import ttk

class MapGUI:
    def __init__(self):
        # Initialize Tkinter window
        self.root = Tk()
        self.root.title("Tkinter Image test - Movable Icon")

        # Create a canvas
        self.canvas1 = Canvas(self.root, width=800, height=600)
        self.canvas1.pack()

        # Image perameters #
        max_width = 800
        max_height = 600

        # Image for bg #
        original_image = Image.open("map2.png")
        resized_image = MapGUI.resize_image(original_image, max_width, max_height)
        img = ImageTk.PhotoImage(resized_image)
        # root = Tk()
        # root.title("Tkinter Image test")
        # original_image = Image.open("map2.png")
        # max_width = 800
        # max_height = 600
        # resized_image = MapGUI.resize_image(original_image, max_width, max_height)
        # img = ImageTk.PhotoImage(resized_image)
        ##defining the panel sizes
        self.canvas2 = Canvas(self.root ,width = max_width,height = max_height)
        self.canvas2.place(x=0,y=0,relheight=1,relwidth=1)
        self.canvas2.create_image(0,0, image = img, anchor = "nw")
        # root.geometry('600x400')
        #Adjusting the geometry of the window according to the size of the image
        self.root.geometry(f"{resized_image.width}x{resized_image.height}")

        # Add a movable icon
        self.icon = self.canvas1.create_rectangle(50, 50, 100, 100, fill="red")
        self.canvas1.tag_bind(self.icon, "<Button-1>", self.bring_to_front)
        # self.icon.pack()
        # print(type(self.icon))
        #start location
        self.icon_x = 50
        self.icon_y = 50

        # Bind arrow key events to move the icon
        self.root.bind_all("<Left>", self.move_left)
        self.root.bind_all("<Right>", self.move_right)
        self.root.bind_all("<Up>", self.move_up)
        self.root.bind_all("<Down>", self.move_down)

        # Start the Tkinter event loop
        self.root.mainloop()

    def resize_image(image, max_width, max_height):
        width, height = image.size
        if width > max_width or height > max_height:
            aspect_ratio = min(max_width / width, max_height / height)
            new_width = int(width * aspect_ratio)
            new_height = int(height * aspect_ratio)
            return image.resize((new_width, new_height))
        return image

    def bring_to_front(self):
        self.canvas.tag_raise(self.icon)

    def move_left(self, event):
        self.move_icon(-20, 0)

    def move_right(self, event):
        self.move_icon(20, 0)

    def move_up(self, event):
        self.move_icon(0, -20)

    def move_down(self, event):
        self.move_icon(0, 20)

    def move_icon(self, delta_x, delta_y):
        self.icon_x += delta_x 
        self.icon_y += delta_y 
        self.canvas1.move(self.icon, delta_x, delta_y)

    # def on_icon_click(self, event):
    #     self.start_x = event.x
    #     self.start_y = event.y

    # def on_icon_drag(self, event):
    #     delta_x = event.x - self.start_x
    #     delta_y = event.y - self.start_y
    #     self.canvas.move(self.icon, delta_x, delta_y)
    #     self.start_x = event.x
    #     self.start_y = event.y

# Create an instance of MapGUI
MapGUI()
