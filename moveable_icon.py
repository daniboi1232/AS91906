from tkinter import Tk, Canvas
from PIL import Image, ImageTk

class MapGUI:
    def __init__(self):
        # Initialize Tkinter window
        self.root = Tk()
        self.root.title("Movable Icon")

        # Load the background image
        original_image = Image.open("map3.png")
        max_width = 600
        max_height = 600
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
        church = [(13,25),(95,165)]
        library = [(185,18),(293,142)]
        bank = [(365,12),(448,95)]
        town_square = [(317,138),(425,202)]
        market = [(485,162),(573,310)]
        town_hall = [(306,245),(388,328)]
        tavern = [(54,221),(172,323)]
        farm_stead = [(12,401),(136,534)]
        riverside = [(215,450),(323,545)]
        blacksmith = [(414,390),(550,545)]

        # Draw road boundaries
        self.canvas.create_rectangle(*church, fill="", outline="red", tags="church_coord")
        self.canvas.create_rectangle(*library, fill="", outline="blue", tags="library_coord")
        self.canvas.create_rectangle(*bank, fill="", outline="blue", tags="bank_coord")
        self.canvas.create_rectangle(*town_square, fill="", outline="blue", tags="town_square_coord")
        self.canvas.create_rectangle(*market, fill="", outline="blue", tags="market_coord")
        self.canvas.create_rectangle(*town_hall, fill="", outline="blue", tags="town_hall_coord")
        self.canvas.create_rectangle(*tavern, fill="", outline="blue", tags="tavern_coord")
        self.canvas.create_rectangle(*farm_stead, fill="", outline="blue", tags="farm_stead_coord")
        self.canvas.create_rectangle(*riverside, fill="", outline="blue", tags="riverside_coord")
        self.canvas.create_rectangle(*blacksmith, fill="", outline="blue", tags="blacksmith_coord")

        # Connecting Mapgui to border control
        self.border_control = Border_Control(self.canvas)

        # Assign boundaries to events
        # self.canvas.tag_bind("church_coord", lambda event: self.border_control.church_func("church_coord"))
        # self.canvas.tag_bind("library_coord", lambda event: self.on_road_click("library_coord"))


        # Add a movable icon (rectangle)
        self.icon = self.canvas.create_rectangle(25,25,50,50, fill="red")

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

    

# Class to handle borders
class Border_Control:
    def __init__(self,canvas):
        self.canvas = canvas

    # Function for building boundaries
    def church_func(self):
        pass

    def library_func(self):
        pass

    def library_func(self):
        pass

    def library_func(self):
        pass

    def library_func(self):
        pass

    def library_func(self):
        pass

    def library_func(self):
        pass

    def library_func(self):
        pass

    def library_func(self):
        pass

    def library_func(self):
        pass

    
# Create an instance of MapGUI
MapGUI()