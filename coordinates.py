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
        # # Add a movable icon (rectangle)
        # self.icon = self.canvas.create_rectangle(50,50,75,75, fill="red")

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

        self.road_boundaries = {
            # Add road boundaries here
            # Example:
            "church-lib": [(95, 46), (185, 108)],
            "lib-bank": [(293, 29), (365, 90)],
            "lib-tav,twnhall": [(210, 142), (210, 245), (172,245), (172, 294), (306, 294), (306, 251), (263,251), (263,142), (210, 142)],
            "tav-farm": [(57, 323), (120, 401)],
            "bank-twnsq": [(370,95),(414,138)],
            "twnsq-twnhall": [(329,202),(377,245)],

        }


        # Draw building boundaries
        for building_name, boundary_coords in self.building_boundaries.items():
            x1, y1 = boundary_coords[0]
            x2, y2 = boundary_coords[1]
            self.canvas.create_rectangle(x1, y1, x2, y2, outline="red")
        # Draw "T" shape boundaries
        for road_name, boundary_coords in self.road_boundaries.items():
            # Check for "T" shape and draw lines accordingly
            if road_name == "lib-tav,twnhall":
                x1, y1 = boundary_coords[0]
                x2, y2 = boundary_coords[1]
                x3, y3 = boundary_coords[2]
                x4, y4 = boundary_coords[3]
                x5, y5 = boundary_coords[4]
                x6, y6 = boundary_coords[5]
                x7, y7 = boundary_coords[6]
                x8, y8 = boundary_coords[7]
                x9, y9 = boundary_coords[8]

                
                # Draw horizontal line
                self.canvas.create_line(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, fill="yellow", width=2)
                
                # Draw vertical line
                self.canvas.create_line(x2, y2, x3, y3, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, fill="yellow", width=2)
            else:
                x1, y1 = boundary_coords[0]
                x2, y2 = boundary_coords[1]
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="blue")
        # Connecting Mapgui to border control
        # self.border_control = Border_Control(self.canvas)
        self.border_control = BorderControl(self.canvas, self.building_boundaries)
        self.border_control = BorderControl(self.canvas, self.road_boundaries)

        # Assign boundaries to events
        # self.canvas.tag_bind("church_coord", lambda event: self.border_control.church_func("church_coord"))
        # self.canvas.tag_bind("library_coord", lambda event: self.on_road_click("library_coord"))


        # Add a movable icon (rectangle)
        self.icon = self.canvas.create_rectangle(50,50,75,75, fill="red")

        # Create a text object for displaying collision messages
        self.collision_text = Label(self.root, text="jksdhfl", font=('Mistral 18 bold'))
        self.collision_text.pack()
        # Start location
        self.icon_x = 62.5
        self.icon_y = 62.5

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
        # new_x = self.icon_x + delta_x
        # new_y = self.icon_y + delta_y

        # # Check if the new position stays within any building boundaries
        # within_building_boundary = False
        # for boundary_coords in self.building_boundaries.values():
        #     if self.is_within_boundary(new_x, new_y, boundary_coords):
        #         within_building_boundary = True
        #         break

        # if within_building_boundary:
        #     # Move the icon only if the new position stays within any building boundary
        #     self.icon_x = new_x
        #     self.icon_y = new_y
        #     self.canvas.move(self.icon, delta_x, delta_y)

        #     # Check for collision with building boundaries
        #     collided_building = None
        #     for boundary_name, boundary_coords in self.building_boundaries.items():
        #         if self.check_collision(self.icon, boundary_coords):
        #             collided_building = boundary_name
        #             break

        #     # Update collision status and clear text accordingly
        #     if collided_building:
        #         # Collision detected with a building
        #         self.border_control.update_collision_status(collided_building, True)
        #         self.show_collision_text(collided_building)
        #     else:
        #         # No collision detected with any building
        #         self.border_control.clear_all_collision_status()
        #         self.hide_collision_text()

        new_x = self.icon_x + delta_x
        new_y = self.icon_y + delta_y

        print(f"New position: ({new_x}, {new_y})")

        overlapping_boundary = None
        for boundary_name, boundary_coords in self.building_boundaries.items():
            if self.is_overlapping(new_x, new_y, boundary_coords):
                overlapping_boundary = boundary_name
                break

        print(f"Overlapping boundary: {overlapping_boundary}")

        for boundary_name, boundary_coords in self.road_boundaries.items():
            if self.is_overlapping(new_x, new_y, boundary_coords):
                if self.is_connected(overlapping_boundary, boundary_name):
                    self.icon_x = new_x
                    self.icon_y = new_y
                    self.canvas.move(self.icon, delta_x, delta_y)
                    return
                else:
                    return
        
        for boundary_coords in self.building_boundaries.values():
            if self.is_within_boundary(new_x, new_y, boundary_coords):
                self.icon_x = new_x
                self.icon_y = new_y
                self.canvas.move(self.icon, delta_x, delta_y)
                return


        # # Check if the new position overlaps with any building boundary
        # overlapping_boundary = None
        # for boundary_name, boundary_coords in self.building_boundaries.items():
        #     if self.is_overlapping(new_x, new_y, boundary_coords):
        #         overlapping_boundary = boundary_name
        #         break

        # # Check if the new position overlaps with any road boundary
        # for boundary_name, boundary_coords in self.road_boundaries.items():
        #     if self.is_overlapping(new_x, new_y, boundary_coords):
        #         # Check if the overlapping boundary is connected to the current one
        #         if self.is_connected(overlapping_boundary, boundary_name):
        #             # Move the icon if the boundaries are connected
        #             self.icon_x = new_x
        #             self.icon_y = new_y
        #             self.canvas.move(self.icon, delta_x, delta_y)
        #             return
        #         else:
        #             # Boundaries are not connected, don't allow movement
        #             return

        # # If there's no overlapping boundary, check if the new position stays within any building boundary
        # for boundary_coords in self.building_boundaries.values():
        #     if self.is_within_boundary(new_x, new_y, boundary_coords):
        #         # Move the icon only if the new position stays within any building boundary
        #         self.icon_x = new_x
        #         self.icon_y = new_y
        #         self.canvas.move(self.icon, delta_x, delta_y)
        #         return

    # Add this helper method to check if the new position overlaps with a boundary
    def is_overlapping(self, x, y, boundary_coords):
        """Check if the given coordinates overlap with the specified boundary."""
        boundary_x1, boundary_y1 = boundary_coords[0]
        boundary_x2, boundary_y2 = boundary_coords[1]
        return boundary_x1 < x < boundary_x2 and boundary_y1 < y < boundary_y2

    # Add this helper method to check if two boundaries are connected
    def is_connected(self, boundary1_name, boundary2_name):
        """Check if two boundaries are connected."""
        # Define your connection logic here, based on your boundary names
        # For example, you can have a dictionary storing connections between boundaries
        connections = {
            "church": ["church-lib"],
            "library": ["lib-bank", "lib-tav,twnhall"],
            "bank": ["lib-bank", "bank-twnsq"],
            "town_square": ["bank-twnsq", "twnsq-twnhall"],
            # Add more connections as needed
        }
        return boundary2_name in connections.get(boundary1_name, [])

    def is_within_boundary(self, x, y, boundary_coords):
        """Check if the given coordinates are within the specified boundary."""
        boundary_x1, boundary_y1 = boundary_coords[0]
        boundary_x2, boundary_y2 = boundary_coords[1]
        if (boundary_x1 < x < boundary_x2 and boundary_y1 < y < boundary_y2):
            return True
        return False
        
    def show_collision_text(self, building_name):
        """Show collision text for the specified building."""
        if not self.border_control.get_collision_status(building_name):
            # Collision text should be displayed only if collision status is False
            self.collision_text.config(text=f"Collided with {building_name}")
            text_x = 10  # Adjust left margin
            text_y = self.canvas.winfo_height() + 10  # Below the canvas
            self.canvas.coords(self.collision_text, text_x, text_y)
            self.collision_text.place(x=text_x, y=text_y)

    def hide_collision_text(self):
        """Hide collision text."""
        self.collision_text.config(text="")  # Clear the text



    

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

        # Dictionary to keep track of collision status for each building
        self.collision_status = {building: False for building in building_boundaries}

    def update_collision_status(self, building_name, status):
        """Update collision status for the specified building."""
        self.collision_status[building_name] = status

    def clear_all_collision_status(self):
        """Clear collision status for all buildings."""
        for building in self.collision_status:
            self.collision_status[building] = False

    def get_collision_status(self, building_name):
        """Get collision status for the specified building."""
        return self.collision_status.get(building_name, False)

    # Define a method for each building
    def church_func(self):
        print("Collided with church")

    def library_func(self):
        global obj_collision
        if not self.collision_status["library"]:
            self.collision_status["library"] = True
            Label(self.canvas, text="Hello world!", font=('Mistral 18 bold')).place(x=20, y=600)
        else:
            print("Already collided with library")

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

    def churchtolib(self):
        print("collided with boundary")
MapGUI()