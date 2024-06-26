from tkinter import *
from tkinter import Tk, Canvas, ttk, Label
from PIL import Image, ImageTk

obj_collision = 0



class MapGUI:
    """Class representing the main graphical user interface (GUI) for the application."""

    def __init__(self):
        """Initialize the MapGUI class."""

        # Initialize Tkinter window
        self.root = Tk()
        self.root.title("Movable Icon")

        # Load the background image
        original_image = Image.open("map3.png")
        max_width = 600
        max_height = 800
        resized_image = self.resize_image(original_image, max_width, max_height)
        self.bg_img = ImageTk.PhotoImage(resized_image)

        # Create a canvas
        self.canvas = Canvas(self.root, width=max_width, height=max_height)
        self.canvas.pack()

        # Add the background image to the canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_img)

        # Road Boundaries
        church_to_library = [()]

        # Building Boundaries
        # church = [(13,25),(95,165)]
        # library = [(185,18),(293,142)]
        # bank = [(365,12),(448,95)]
        # town_square = [(317,138),(425,202)]
        # market = [(485,162),(573,310)]
        # town_hall = [(306,245),(388,328)]
        # tavern = [(54,221),(172,323)]
        # farm_stead = [(12,401),(136,534)]
        # riverside = [(215,450),(323,545)]
        # blacksmith = [(414,390),(550,545)]

        self.building_boundaries = {
            "church": [(13,25),(95,165)],
            "library": [(185,18),(293,142)],
            "bank": [(365,12),(448,95)],
            "town_square": [(317,138),(425,202)],
            "market": [(485,162),(573,310)],
            "town_hall": [(306,245),(388,328)],
            "tavern": [(54,221),(172,323)],
            "farm_stead": [(12,401),(136,534)],
            "riverside": [(215,450),(323,545)],
            "blacksmith": [(414,390),(550,545)]
        }


        # Draw road boundaries
        # self.canvas.create_rectangle(*church, fill="", outline="red", tags="church_coord")
        # self.canvas.create_rectangle(*library, fill="", outline="blue", tags="library_coord")
        # self.canvas.create_rectangle(*bank, fill="", outline="blue", tags="bank_coord")
        # self.canvas.create_rectangle(*town_square, fill="", outline="blue", tags="town_square_coord")
        # self.canvas.create_rectangle(*market, fill="", outline="blue", tags="market_coord")
        # self.canvas.create_rectangle(*town_hall, fill="", outline="blue", tags="town_hall_coord")
        # self.canvas.create_rectangle(*tavern, fill="", outline="blue", tags="tavern_coord")
        # self.canvas.create_rectangle(*farm_stead, fill="", outline="blue", tags="farm_stead_coord")
        # self.canvas.create_rectangle(*riverside, fill="", outline="blue", tags="riverside_coord")
        # self.canvas.create_rectangle(*blacksmith, fill="", outline="blue", tags="blacksmith_coord")

        # Connecting Mapgui to border control
        # self.border_control = Border_Control(self.canvas)

        self.border_control = BorderControl(self.canvas, self.building_boundaries)

        # Assign boundaries to events
        # self.canvas.tag_bind("church_coord", lambda event: self.border_control.church_func("church_coord"))
        # self.canvas.tag_bind("library_coord", lambda event: self.on_road_click("library_coord"))


        # Add a movable icon (rectangle)
        self.icon = self.canvas.create_rectangle(25,25,50,50, fill="red")

        # Create a text object for displaying collision messages
        self.collision_text = Label(self.root, text="", font=('Mistral 18 bold'))
        self.collision_text.pack()
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

        if self.check_collision:
            self.collision_text.config(text="Collision detected")
            # Calculate the coordinates to place the text below the canvas
            text_x = 0  # Adjust horizontally as needed
            text_y = self.canvas.winfo_height() + 10  # Place below the canvas with some margin
            self.collision_text.place(x=text_x, y=text_y)
        else:
            self.collision_text.config(text="")  # Clear the text if no collision


        # Check for collision with building boundaries
        for boundary_name, boundary_coords in self.building_boundaries.items():
            if self.check_collision(self.icon, boundary_coords):
                # Call the corresponding building method in BorderControl
                getattr(self.border_control, f"{boundary_name}_func")()
                text_x = 10  # Adjust left margin
                text_y = self.canvas.winfo_height() + 10  # Below the canvas
                self.canvas.coords(self.collision_text, text_x, text_y)
                self.canvas.itemconfig(self.collision_text, text=f"Collided with {boundary_name}")

    

    def check_collision(self, obj_id, boundary_coords):
        # Get the coordinates of the object
        obj_x1, obj_y1, obj_x2, obj_y2 = self.canvas.coords(obj_id)

        # Get the coordinates of the building boundary
        boundary_x1, boundary_y1 = boundary_coords[0]
        boundary_x2, boundary_y2 = boundary_coords[1]

        # Check for collision
        if (obj_x1 < boundary_x2 and obj_x2 > boundary_x1 and
            obj_y1 < boundary_y2 and obj_y2 > boundary_y1):
            return True
        return False

    @staticmethod
    def resize_image(image, max_width, max_height):
        """Resize the given image to fit within the specified dimensions.

        Args:
            image (PIL.Image.Image): The image to resize.
            max_width (int): The maximum width for the resized image.
            max_height (int): The maximum height for the resized image.

        Returns:
            PIL.Image.Image: The resized image.
        """
        width, height = image.size
        if width > max_width or height > max_height:
            aspect_ratio = min(max_width / width, max_height / height)
            new_width = int(width * aspect_ratio)
            new_height = int(height * aspect_ratio)
            return image.resize((new_width, new_height))
        return image

    

# Class to handle borders
class BorderControl:
    """Class responsible for controlling collisions and interactions with building boundaries."""

    def __init__(self, canvas, building_boundaries):
        """Initialize the BorderControl class.

        Args:
            canvas (tk.Canvas): The Tkinter canvas on which the objects are drawn.
            building_boundaries (dict): A dictionary containing building boundaries.
        """        
        self.canvas = canvas
        self.building_boundaries = building_boundaries

    # Define a method for each building
    def church_func(self):
        print("Collided with church")

    def library_func(self):
        global obj_collision
        if obj_collision == 0:
            obj_collision = 1
            label = Label(self.canvas,text= "Hello World!", font=('Mistral 18 bold')).place(x=20,y=600)
            # label.place(x=150,y=80)
            # Tk.update(label)
            # label.config(fg = "white")
            # Insert instructions and info here
            
            # win.mainloop()
        else: 
            print("Collided with library")

    def bank_func(self):
        print("Collided with bank")

    def town_square_func(self):
        print("Collided with town square")

    def market_func(self):
        print("Collided with market")

    def town_hall_func(self):
        print("Collided with town hall")

    def tavern_func(self):
        print("Collided with tavern")

    def farm_stead_func(self):
        print("Collided with farm stead")

    def riverside_func(self):
        print("Collided with riverside")

    def blacksmith_func(self):
        print("Collided with blacksmith")

# def open_popup():
#     """open_popup creates a new window on-top of the main window"""
#     top= Toplevel(win)
#     top.geometry("550x250")
#     top.title("Child Window")
#     Label(top, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)

# Create an instance of MapGUI
MapGUI()