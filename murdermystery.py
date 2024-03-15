#Import neccesary modules and libraries
from tkinter import *
from PIL import ImageTk, Image
import os

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


#test player
bob = Player("Bob","F")
print(str(bob))
print(bob.move())


### NPC Class ###
class NPC:
    def __init__(self, name, location, item):
        self.name = name
        self._location = location
        self._item = item
    
    def __str__(self):
        return "this is an npc"
    


### Location Class ###
class Loc:
    def __init__(self, ):
        pass

    def __str__():
        return ""


class mapgui:
    def __init__(self):
        pass


##testing printing of image for future map
root = Tk()
root.title("Tkinter Image test")
root.geometry('600x400')
img = ImageTk.PhotoImage(Image.open("wavestest.jpeg"))

##defining the panel sizes
panel = Label(root, image = img)
panel.pack(side = "left", expand = "False")

##runs root loop
root.mainloop()


