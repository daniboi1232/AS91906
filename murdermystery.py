#Import neccesary modules and libraries
from tkinter import *
from PIL import ImageTk, Image
import os

##temporary map used for player testing
loc_list = [
    {"location": "A", "dest": ["B", "C", "D", "E", "F", "G"]},
    {"location": "B", "dest": ["C", "D", "E", "F", "G"]},
    {"location": "C", "dest": ["D", "E", "F", "G"]},
    {"location": "D", "dest": ["E", "F", "G"]},
    {"location": "E", "dest": ["F", "G"]},
    {"location": "F", "dest": ["G"]},
    {"location": "G", "dest": []}
]

#Player class
class Player:
    def __init__(self,name,location):
        self._name = name
        self._location = location

    def __str__(self):
        return  f'The player, {self._name}, is currently in {self._location}'
    
    #def name
    @property
    def name(self): 
        return self._name

    @name.setter
    def name(self,newname):
        self.name = newname

    #def location
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self,newloc):
        self.location = newloc

    def move(self):
        dest = str(input('Where do you want to move? ')).upper()
        for loc in loc_list:
            if loc["location"] == self._location:
                if dest in loc["dest"]:
                    self._location = dest
                    return dest
        return False


#test player
bob = Player("Bob","A")
print(str(bob))
print(bob.move())




#location class
class Loc:
    def __init__():
        pass

    def __str__():
        pass


##testing printing of image for future map
# root = Tk()
# root.title("Tkinter Image test")
# root.geometry('600x400')
# img = ImageTk.PhotoImage(Image.open("wavestest.jpeg"))

# ##defining the panel sizes
# panel = Label(root, image = img)
# panel.pack(side = "left", expand = "False")

# ##runs root loop
# root.mainloop()


