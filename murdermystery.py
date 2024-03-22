#Import neccesary modules and libraries
from tkinter import Tk, Canvas
from PIL import ImageTk, Image
import os
import random

### temporary map used for player movement testing ###
### Turns out i dont need it ###
# loc_list = [
#     {"location": "A", "dest": ["B", "C", "D", "E", "F", "G"]},
#     {"location": "B", "dest": ["C", "D", "E", "F", "G"]},
#     {"location": "C", "dest": ["D", "E", "F", "G"]},
#     {"location": "D", "dest": ["E", "F", "G"]},
#     {"location": "E", "dest": ["F", "G"]},
#     {"location": "F", "dest": ["G"]},
#     {"location": "G", "dest": []}
# ]

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


### NPC Class ###
class NPC:
    def __init__(self, name):
        self.name = name
        
    
    # def __str__(self):
    #     return "this is an npc"
    
    # def interact(self):
    #     pass

    


### Location Class ###
class Loc:
    def __init__(self, ):
        pass

    def __str__():
        return ""


### GUI Class ###
class mapgui:
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
        

npc_list = [NPC("John"), NPC("Mary"), NPC("Tom")]

weapon_list = [Weapon("Revolver","Shot through the head"),
Weapon("Dagger","Stabbed through the aorta artery"),
Weapon("Poison","Cyanide pill hid inside the dinner"),
Weapon("Crowbar","Head smashed in by a steel crowbar"),
Weapon("Bible","Head flattened by the word")]
### Setting values to different thingz ###
#weapons = ["Revolver","Dagger","Poison","Rope","Crowbar","Bible"]


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


mapinit = mapgui()










# ##testing printing of image for future map
# root = Tk()
# root.title("Tkinter Image test")
# root.geometry('600x400')
# img = ImageTk.PhotoImage(Image.open("wavestest.jpeg"))

# ##defining the panel sizes
# panel = Label(root, image = img)
# panel.pack(side = "left", expand = "False")

# ##runs root loop
# root.mainloop()


