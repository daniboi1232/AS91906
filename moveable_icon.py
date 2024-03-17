from tkinter import Tk, Canvas

class MapGUI:
    def __init__(self):
        # Initialize Tkinter window
        self.root = Tk()
        self.root.title("Movable Icon")

        # Create a canvas
        self.canvas = Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        # Add a movable icon
        self.icon = self.canvas.create_rectangle(50, 50, 100, 100, fill="red")  # Example rectangle
        
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
