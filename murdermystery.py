#Import neccesary modules and libraries
from tkinter import Tk, Canvas, Label, Text, Entry
import tkinter as tk
from PIL import ImageTk, Image
import os
import random
import time


obj_collision = 0
### Player Class ###
class Player:
    def __init__(self,name,location):
        self._name = name
        self._location = location
        #self._item = item

    def __str__(self):
        return  f'The player, {self._name}, is currently in {self._location}'
    
    ##Decorators##
    #getter - shown as @property - is used for returning a variable
    #setter - shown as @method.setter - is used for changing a variable
    #deleter - shown as @method.deleter - is used for removing a variables contents

    #def name for returning contents of variable
    @property
    def name(self): 
        return self._name

    #Change the name to newname
    @name.setter
    def name(self,newname):
        self.name = newname

    #def location for returning contents of variable
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self,newloc):
        self.location = newloc

    # @property
    # def item(self):
    #     return self._item

    # @item.setter
    # def item(self):
    #     pass


    ### def move to change the location of player based on players input moved to the map class due to different format ###


# #test player
# bob = Player("Bob","F")
# print(str(bob))
# print(bob.move())

class Startup(tk.Tk):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        


        self.label = tk.Label(self.parent, text="Welcome to the game!", font=("Comic Sans MS", 40, "bold"))
        self.label.pack()

        self.player_name()

        #insert name

        player_name = "hello"
        if player_name == True:
            self.label2 = tk.Label(self.parent, text="You are a young adventurer who has just arrived in the land of the Ghetto. \nThere has been a murder. \nYour job is to figure out who is the Murderer, where they murdered and with what weapon. \nGood luck on your adventures.")
            self.label2.pack()

        # self.T = Text(startup, )

    def player_name(self):
        Font = ("Comic Sans MS", 20)
        self.askname = tk.Label(self.parent, text="What is your name?", font=(Font), pady= 30)
        self.askname.pack()

        entry = tk.Entry(self.parent, selectbackground="lightblue", selectforeground="black")
        entry.pack()

        self.button=tk.Button(self.parent,text="Enter", command=self.PassCheck)
        self.button.pack()




### GUI Class ###
class MapGUI(tk.Frame):
    """Class representing the main graphical user interface (GUI) for the application."""

    def __init__(self):
        """Initialize the MapGUI class."""

        self.title("Movable Icon")

        # Load the background image
        original_image = Image.open("map4.png")
        max_width = 600
        max_height = 800
        resized_image = self.resize_image(original_image, max_width, max_height)
        self.bg_img = ImageTk.PhotoImage(resized_image)

        # Create a canvas
        self.canvas = Canvas(self.parent, width=max_width, height=max_height)
        self.canvas.pack()

        # Add the background image to the canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_img)
        # # Add a movable icon (rectangle)
        # self.icon = self.canvas.create_rectangle(50,50,75,75, fill="red")

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
            "lib-rd": [(210,142),(263,245)],
            "rd-twnhll,tav": [(172,245),(306,294)],
            "tav-farm": [(57, 323), (120, 401)],
            "bank-twnsq": [(370,95),(414,138)],
            "bank-rd2": [(448,29),(552,77)],
            "rd2-market": [(500,77),(552,162)],
            "twnsq-twnhall": [(329,202),(377,245)],
            # "market-blksmth": [(490,390),(545,310)], """not working for some reason""" - removed due to map layout change
            "farm-rvrsde": [(136,465),(215,515)],
            "rvrsde-blksmth": [(323,465),(414,522)],
            "twnhall-market": [(388,255),(485,300)]
        }


        # Draw building boundaries
        for building_name, boundary_coords in self.building_boundaries.items():
            x1, y1 = boundary_coords[0]
            x2, y2 = boundary_coords[1]
            self.canvas.create_rectangle(x1, y1, x2, y2, outline="")
            # self.canvas.create_rectangle(x1, y1, x2, y2, outline="red")
        # Draw "T" shape boundaries
        for road_name, boundary_coords in self.road_boundaries.items():
            # Check for "T" shape and draw lines accordingly
                x1, y1 = boundary_coords[0]
                x2, y2 = boundary_coords[1]
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="")
                # self.canvas.create_rectangle(x1, y1, x2, y2, outline="blue")
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
        # self.collision_text = Label(self.root, text="You are at the Church", font=('Mistral 18 bold'))
        # self.collision_text.pack()
        # Start location
        self.icon_x = 62.5
        self.icon_y = 62.5

        # # Testing for location of icon
        # self.icon2 = self.canvas.create_rectangle(self.icon_x, self.icon_y,self.icon_x,self.icon_y, fill="black")

        # Bind arrow key events to move the icon
        self.root.bind_all("<Left>", self.move_left)
        self.root.bind_all("<Right>", self.move_right)
        self.root.bind_all("<Up>", self.move_up)
        self.root.bind_all("<Down>", self.move_down)

        # Start the Tkinter event loop
        # self.root.mainloop()

    def move_left(self, event):
        self.move_icon(-20, 0)

    def move_right(self, event):
        self.move_icon(20, 0)

    def move_up(self, event):
        self.move_icon(0, -20)

    def move_down(self, event):
        self.move_icon(0, 20)

    def move_icon(self, delta_x, delta_y):
        
        new_x = self.icon_x + delta_x
        new_y = self.icon_y + delta_y

        print(f"New position: ({new_x}, {new_y})")

        # Check if the new position overlaps with any building boundary
        overlapping_building = None
        for building_name, boundary_coords in self.building_boundaries.items():
            if self.is_overlapping(new_x, new_y, boundary_coords) == True:
                print("helloworld")
                self.icon_x = new_x
                self.icon_y = new_y
                self.canvas.move(self.icon, delta_x, delta_y)
                self.show_collision_text(building_name)
                overlapping_building = building_name
                break

        # Check if the new position overlaps with any road boundary
        overlapping_road = None
        for road_name, boundary_coords in self.road_boundaries.items():
            if self.is_overlapping(new_x, new_y, boundary_coords):
                print("helloworld2")
                self.icon_x = new_x
                self.icon_y = new_y
                self.canvas.move(self.icon, delta_x, delta_y)
                overlapping_road = road_name
                break

        
        # Move the icon if the new position doesn't overlap with any building boundary
        # if overlapping_building is None:
        #     self.icon_x = new_x
        #     self.icon_y = new_y
        #     self.canvas.move(self.icon, delta_x, delta_y)
        #     self.hide_collision_text()
        # else:
        #     # Display collision text for building
        #     self.show_collision_text(overlapping_building)
        #     # Update collision status for buildings
        #     self.border_control.update_collision_status(overlapping_building, True)

        # If the new position overlaps with a road boundary and the boundaries are connected
        if overlapping_road is not None and overlapping_building is not None and self.is_connected(overlapping_building, overlapping_road):
            # self.icon_x = new_x
            # self.icon_y = new_y
            # self.canvas.move(self.icon, delta_x, delta_y)
            self.hide_collision_text()
        elif overlapping_road is not None:
            # Display collision text for road
            self.show_collision_text(overlapping_road)


            # print(f"Overlapping boundary: {overlapping_boundary}")

        
    # Add this helper method to check if the new position overlaps with a boundary
    def is_overlapping(self, x, y, boundary_coords):
        """Check if the given coordinates overlap with the specified boundary."""
        boundary_x1, boundary_y1 = boundary_coords[0]
        boundary_x2, boundary_y2 = boundary_coords[1]
        # print(f"{boundary_x1} < x < {boundary_x2} and {boundary_y1} < y < {boundary_y2}")
        # return boundary_x1 < x < boundary_x2 and boundary_y1 < y < boundary_y2
        if boundary_x1 < x < boundary_x2 and boundary_y1 < y < boundary_y2:
            print("hello")

            return True
        else:
            return False

    # Add this helper method to check if two boundaries are connected
    def is_connected(self, boundary1_name, boundary2_name):
        """Check if two boundaries are connected."""
        # Define your connection logic here, based on your boundary namess
        connections = {
            "church": ["church-lib"],
            "library": ["lib-bank", "lib-tav,twnhall"],
            "bank": ["lib-bank", "bank-twnsq"],
            "town_square": ["bank-twnsq", "twnsq-twnhall"],
            # Add more connections as needed
        }
        print(boundary2_name, "  ", boundary1_name)
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
            print("showing collision text")
            # Collision text should be displayed only if collision status is False
            #self.collision_text.config(text = f"Collided with {building_name}")
            print()
            self.collision_text_1 = Label(self.root, text = "Ypu have collided")
            self.collision_text_2 = Label(self.root, text=f"You are at the {building_name}", font=('Mistral 18 bold'))
            text_x = 10  # Adjust left margin
            text_y = self.canvas.winfo_height() + 10  # Below the canvas
            self.collision_text_1.place(x=text_x, y=text_y)
            self.collision_text_2.place(x=text_x, y=text_y)
            # print(self.collision_text_1)  # Print the collision text object
            

    def hide_collision_text(self):
        """Hide collision text."""
        print("hiding collision text")
        self.collision_text.place_forget()  # Clear the text



    

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
    
    #@staticmethod
    def building_name(self):
        print("Hjtgdfgjhgtf")
        building_list=[]
        for i in self.building_boundaries:
            #print(i)
            building_list.append(i)
            #print(self.building_boundaries[0])
        return building_list

    

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

# def open_popup():
#     """open_popup creates a new window on-top of the main window"""
#     top= Toplevel(win)
#     top.geometry("550x250")
#     top.title("Child Window")
#     Label(top, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)


### Weapons Class ###
class Weapon:
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.holder = None

    def __str__(self):
        pass

    def assign_holder(self, npc):
        self.holder = npc
        
### NPC Class ###
class NPC:
    def __init__(self, name):
        self.name = name
        
    def set_location(self, building):
        self.location = building


class menu:
    def __init__(self):
        pass




    # def __str__(self):
    #     return "this is an npc"
    
    # def interact(self):
    #     pass

    


def main():
    npc_list = [NPC("John"), 
    NPC("Mary"), 
    NPC("Tom"), 
    NPC("Caleb"), 
    NPC("Marcus")]

    weapon_list = [Weapon("Revolver","Shot through the head"),
    Weapon("Dagger","Stabbed through the aorta artery"),
    Weapon("Poison","Cyanide pill hid inside the dinner"),
    Weapon("Crowbar","Head smashed in by a steel crowbar"),
    Weapon("Bible","Head flattened by the word")]
    ### Setting values to different thingz ###
    #weapons = ["Revolver","Dagger","Poison","Rope","Crowbar","Bible"]

    # location_list = MapGUI.building

    ### Shuffling the items randomly ###
    random.shuffle(npc_list)
    random.shuffle(weapon_list)


    ### Assign weapons to NPCs ###
    for npc, weapon in zip(npc_list, weapon_list):
        Weapon.assign_holder(weapon,npc)
        #print(f"{Weapon.name} is held by {NPC.name}")
        print(weapon.name," is held by ",npc.name)
        #print(self.holder)
    # If the number of NPCs and weapons are different, handle the remaining NPCs or weapons as needed
    for npc in npc_list[len(weapon_list):]:
        print(f"No weapon assigned to {npc.name}")
    for weapon in weapon_list[len(npc_list):]:
        print(f"{weapon.name} is not held by any NPC")


    # map_gui_instance = MapGUI()# Create an instance of the MapGUI class

    # building_names = map_gui_instance.building_name()  # Call the building_name method on the instance

    # MapGUI()
    # print(building_names)
    # for npc, building_names in zip(npc_list, building_names):
    #     npc.set_location(building_names)
    #     print(npc.name, " is in ", npc.location)


    # map_gui_instance.root.mainloop()

    root = tk.Tk()
    startup_instance = Startup(root)
    startup_instance.mainloop()





