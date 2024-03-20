from tkinter import Tk, Canvas
from PIL import Image, ImageTk

class MapGUI:
    def __init__(self):
        # Initialize Tkinter window
        self.root = Tk()
        self.root.title("Movable Icon")

        # Load the background image
        original_image = Image.open("map2.png")
        max_width = 800
        max_height = 600
        resized_image = self.resize_image(original_image, max_width, max_height)
        self.bg_img = ImageTk.PhotoImage(resized_image)

        # Create a canvas
        self.canvas = Canvas(self.root, width=max_width, height=max_height)
        self.canvas.pack()

        # Add the background image to the canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_img)

        # Add a movable icon (rectangle)
        self.icon = self.canvas.create_rectangle(25, 25, 50, 50, fill="red")

        # Start location
        self.icon_x = 50
        self.icon_y = 50

        # Bind arrow key events to move the icon
        self.root.bind_all("<Left>", self.move_left)
        self.root.bind_all("<Right>", self.move_right)
        self.root.bind_all("<Up>", self.move_up)
        self.root.bind_all("<Down>", self.move_down)

        # Start the Tkinter event loop
        self.root.mainloop()

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
        self.canvas.move(self.icon, delta_x, delta_y)

    @staticmethod
    def resize_image(image, max_width, max_height):
        width, height = image.size
        if width > max_width or height > max_height:
            aspect_ratio = min(max_width / width, max_height / height)
            new_width = int(width * aspect_ratio)
            new_height = int(height * aspect_ratio)
            return image.resize((new_width, new_height))
        return image

# Create an instance of MapGUI
MapGUI()