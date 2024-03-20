#Import neccesary modules and libraries
from tkinter import *
from PIL import ImageTk, Image, ImageFilter
import os
import random

##temporary map used for player movement testing
loc_list = [
    {"location": "A", "dest": ["B", "C", "D", "E", "F", "G"]},
    {"location": "B", "dest": ["C", "D", "E", "F", "G"]},
    {"location": "C", "dest": ["D", "E", "F", "G"]},
    {"location": "D", "dest": ["E", "F", "G"]},
    {"location": "E", "dest": ["F", "G"]},
    {"location": "F", "dest": ["G"]},
    {"location": "G", "dest": []}
]

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


    #def move to change the location of player based on players input
    def move(self):
        dest = str(input('Where do you want to move? ')).upper()
        for loc in loc_list:
            if loc["location"] == self._location:
                if dest in loc["dest"]:
                    self._location = dest
                    return dest
        move_error = "Sorry But You Cannot Move There"
        return move_error


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
        root = Tk()
        root.title("Tkinter Image test")
        original_image = Image.open("map2.png")
        max_width = 800
        max_height = 600
        resized_image = mapgui.resize_image(original_image, max_width, max_height)
        img = ImageTk.PhotoImage(resized_image)
        ##defining the panel sizes
        panel = Label(root, image = img)
        panel.pack(side = "left", expand = "False")
        # root.geometry('600x400')
        #Adjusting the geometry of the window according to the size of the image
        root.geometry(f"{resized_image.width}x{resized_image.height}")
        root.mainloop()

    def __str__(self):
        pass

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


