#Import neccesary modules and libraries
from tkinter import Canvas, Label
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import random
from time import sleep


obj_collision = 0
user_name = ""

building_of_choice = ""
weapon_of_choice = ""
murderer = ""

murderer_guess = ""
weapon_guess = ""
location_guess = "" 
class App(tk.Tk):
    """Class representing the main application window.

    This class initializes the Tkinter Tk object and switches between frames.
    """
    def __init__(self):
        """
        Initialize the Tkinter Tk object and switch to the MapGUI frame initially.
        """
        tk.Tk.__init__(self)
        self._frame=None
        self.switch_frame(Startup)

    def switch_frame(self, frame_class):
        """
        Destroy the current frame and replace it with a new one.

        Args:
            frame_class (class): The frame class to switch to.
        """
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
class Startup(tk.Frame):
    """Class representing the startup frame.

    This class initializes the frame for the startup screen, which prompts the user to enter their name.
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.widgets_list=[]
        self.label_list=[]
        parent.geometry("600x800")
        
        self.label1 = tk.Label(self.parent, text="Welcome to the game!", font=("Comic Sans MS", 40, "bold"))
        self.label1.pack()
        self.widgets_list.append(self.label1)

        self.player_name()

        #insert name

        # player_name = "hello"
        # if player_name:
        #     self.label2 = tk.Label(self.parent, text="You are a young adventurer who has just arrived in the land of the Ghetto. \nThere has been a murder.\n  Your best friend, Jacob has been found dead in the {location_of_choice}\nYour job is to figure out who is the Murderer, where they murdered and with what weapon. \nGood luck on your adventures.")
        #     self.label2.pack()
        #     self.widgets_list.append(self.label2)


        # self.T = Text(startup, )

    def player_name(self):
        """Class representing the introduction frame.

        This class initializes the frame for the introduction screen, which displays the game's story and options.
        """
        Font = ("Comic Sans MS", 20)
        self.askname = tk.Label(self.parent, text="What is your name?", font=(Font), pady= 30, anchor='center')
        self.askname.pack()
        self.widgets_list.append(self.askname)


        entry = tk.Entry(self.parent, selectbackground="lightblue", selectforeground="black")
        entry.pack()
        self.widgets_list.append(entry)
        

        button=tk.Button(self.parent,text="Enter", command=lambda: self.check_len(entry))
        button.pack()
        self.widgets_list.append(button)

    def check_len(self, entry):
        """
        Check the length of the user's name.

        Args:
            entry (tk.Entry): The entry widget containing the user's name.
        """
        global user_name
        user_name = entry.get()
        for i in self.label_list:
            i.destroy()
        self.label_list.clear()
        if len(user_name) > 15:
            label = tk.Label(self.parent, text="Name too long - Please use fewer characters", font=("Impact", 15))
            label.config(bg="red", fg="black", borderwidth="1")
            label.pack()
            self.label_list.append(label)
        elif len(user_name) == 0:
            label2 = tk.Label(self.parent, text="Please enter a name...", font=("Impact", 15))
            label2.config(bg="red", fg="black", borderwidth="1")
            label2.pack()
            self.label_list.append(label2)
        else:
            self.start_game()
            
        
    def start_game(self):
        """
        Start the game.
        """
        global user_name
        # user_name = entry.get()
        print(user_name)

        # Create a progressbar widget
        progress = ttk.Progressbar(self.parent, orient="horizontal", length=300, mode="determinate")
        progress.pack(pady=20)
        self.widgets_list.append(progress)

        

        progress.start()

        # Simulate a task that takes time to complete
        for i in range(101):
        # Simulate some work
            sleep(0.05)  
            progress['value'] = i
            # Update the GUI
            self.update_idletasks()  
        progress.stop()
        self.switch_frame()


    # Switch to the MapGUI frame

    def switch_frame(self):
        """
        Switch to the specified frame.

        Args:
            dest (class): The frame class to switch to.
        """
        for w in self.widgets_list:
            w.destroy()
        self.parent.switch_frame(Introduction)

class Introduction(tk.Frame):
    """Class representing the introduction frame.

    This class initializes the frame for the introduction screen, which displays the game's story and options.
    """
    def __init__(self, parent):
        """
        Initialize the Introduction class.

        Args:
            parent (tk.Tk): The parent widget.
        """
        tk.Frame.__init__(self, parent)
        self.parent = parent
        parent.geometry("600x800")
        self.widgets_list=[]

        self.intro_text = tk.Text(self.parent, width=80, height=9.2, wrap=tk.WORD, font=("Comic Sans MS", 25))
        self.intro_text.pack()

        self.widgets_list.append(self.intro_text)

        global building_of_choice

        self.text = f"Welcome {user_name}, \nYou are a young adventurer who has just arrived in the land of the Ghetto. \nThere has been a murder. \nYour best friend, Jacob has been found dead from {weapon_of_choice.name} by {weapon_of_choice.description}\nYour job is to figure out who is the Murderer, where they murdered and with what weapon. \nGood luck on your adventures."

        self.i = 0

        # print(user_name)

        self.appear()


        button1=tk.Button(self.parent,text="Enter Game", command=lambda: self.switch_frames(MapGUI),padx=5,pady=5 )
        button1.pack(pady=(20,0))
        self.widgets_list.append(button1)

        button2=tk.Button(self.parent,text="View Rules", command=lambda: self.switch_frames(Rules),padx=5,pady=5 )
        button2.pack(pady=(20,0))
        self.widgets_list.append(button2)

    def appear(self):
        """
        Display the introduction text.
        """
        if self.i < len(self.text):
            self.intro_text.insert(tk.END, self.text[self.i])
            self.i += 1
            self.parent.after(50, self.appear)
            self.widgets_list.append(self.intro_text)


    def switch_frames(self, dest):
        """
        Switch to the specified frame.

        Args:
            dest (class): The frame class to switch to.
        """
        for w in self.widgets_list:
            w.destroy()
        self.parent.switch_frame(dest)



class Rules(tk.Frame):
    """Class representing the rules frame.

    This class initializes the frame for the rules screen, which displays the game's rules.
    """
    def __init__(self, parent):
        """
        Initialize the Rules class.

        Args:
            parent (tk.Tk): The parent widget.
        """

        tk.Frame.__init__(self, parent)
        self.parent = parent
        parent.geometry("600x800")
        self.widgets_list=[]

        self.intro_text = tk.Text(self.parent, width=80, height=16, wrap=tk.WORD, font=("Comic Sans MS", 25))
        self.intro_text.pack()
        self.widgets_list.append(self.intro_text)


        self.text = "The Rules:\nYour character is signified by a red square, and to move your character,the arrow keys must be used.\nWhen entering a room, you will be given the option to view the weapon inside that room or the person inside the room.\nWhen you have assessed and figured out who the murder was, what weapon they used, and the location of the murder; you will be required to make your way back to the church to confess your sins aswell as give a suggestion of who you believe the murderer is.\nIf you are correct with your suggestion, the game will end and you will win\n\nGood luck on your adventures."

        self.i = 0

        # print(user_name)

        self.appear()


        button=tk.Button(self.parent,text="Back to Introduction", command=lambda: self.switch_frames(Introduction),padx=5,pady=5 )
        button.pack(pady=(20,0))
        self.widgets_list.append(button)

        button1=tk.Button(self.parent,text="Continue to Game", command=lambda: self.switch_frames(MapGUI),padx=5,pady=5 )
        button1.pack(pady=(20,0))
        self.widgets_list.append(button1)

    def appear(self):
        """
        Display the rules text.
        """
        if self.i < len(self.text):
            self.intro_text.insert(tk.END, self.text[self.i])
            self.i += 1
            self.parent.after(10, self.appear)
            
            


    def switch_frames(self, dest):
        """
        Switch to the specified frame.

        Args:
            dest (class): The frame class to switch to.
        """
        for w in self.widgets_list:
            w.destroy()
        self.parent.switch_frame(dest)

### GUI Class ###
class MapGUI(tk.Frame):
    """Class representing the main graphical user interface (GUI) for the application.

    This class initializes the frame for the map screen, which displays the game's map and allows the user to move their character.
    """

    def __init__(self, parent):
        """Initialize the MapGUI class.

        Args:
            parent (tk.Tk): The parent widget.
        """

        self.labels = []
        self.buttons = []
        self.widgets = []


        tk.Frame.__init__(self, parent)
        self.parent = parent
        parent.geometry("600x800")
        #self.title("Movable Icon")

        # Load the background image
        self.original_image = Image.open("map4.png")
        max_width = 600
        max_height = 600
        resized_image = self.resize_image(self.original_image, max_width, max_height)
        self.bg_img = ImageTk.PhotoImage(resized_image)
        # self.widgets.append(self.bg_img)

        # Create a canvas
        self.canvas = Canvas(self.parent, width=max_width, height=max_height)
        self.canvas.pack()
        self.widgets.append(self.canvas)

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

        self.current_building =  None
        

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

        

        # Add a movable icon (rectangle)
        self.icon = self.canvas.create_rectangle(50,50,75,75, fill="red")

        
        # Start location
        self.icon_x = 62.5
        self.icon_y = 62.5

        # # Testing for location of icon
        # self.icon2 = self.canvas.create_rectangle(self.icon_x, self.icon_y,self.icon_x,self.icon_y, fill="black")

        # Bind arrow key events to move the icon
        self.bind_all("<Left>", self.move_left)
        self.bind_all("<Right>", self.move_right)
        self.bind_all("<Up>", self.move_up)
        self.bind_all("<Down>", self.move_down)

        # Start the Tkinter event loop
        # self.root.mainloop()

    def move_left(self, event):
        """Move the icon to the left.

        Args:
            event (tk.Event): The key press event.
        """
        self.move_icon(-20, 0)

    def move_right(self, event):
        """Move the icon to the right.

        Args:
            event (tk.Event): The key press event.
        """
        self.move_icon(20, 0)

    def move_up(self, event):
        """Move the icon up.

        Args:
            event (tk.Event): The key press event.
        """
        self.move_icon(0, -20)

    def move_down(self, event):
        """Move the icon down.

        Args:
            event (tk.Event): The key press event.
        """
        self.move_icon(0, 20)

    def move_icon(self, delta_x, delta_y):
        """Move the icon by the specified amount.

        Args:
            delta_x (int): The amount to move the icon horizontally.
            delta_y (int): The amount to move the icon vertically.
        """
        
        new_x = self.icon_x + delta_x
        new_y = self.icon_y + delta_y

        print(f"New position: ({new_x}, {new_y})")

        # Check if the new position overlaps with any building boundary
        for building_name, boundary_coords in self.building_boundaries.items():
            if self.is_overlapping(new_x, new_y, boundary_coords):
                if building_name!= self.current_building:
                    self.current_building = building_name
                    self.enter_building(building_name) # Run the method once
                # print("helloworld")
                self.icon_x = new_x
                self.icon_y = new_y
                self.canvas.move(self.icon, delta_x, delta_y)
                # overlapping_building = building_name
                break
            else:
                if self.current_building is not None:
                    self.exit_building()

        # Check if the new position overlaps with any road boundary
        for road_name, boundary_coords in self.road_boundaries.items():
            if self.is_overlapping(new_x, new_y, boundary_coords):
                # print("helloworld2")
                self.icon_x = new_x
                self.icon_y = new_y
                self.canvas.move(self.icon, delta_x, delta_y)
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
        # if overlapping_road is not None and overlapping_building is not None and self.is_connected(overlapping_building, overlapping_road):
        #     # self.icon_x = new_x
        #     # self.icon_y = new_y
        #     # self.canvas.move(self.icon, delta_x, delta_y)
        #     self.hide_collision_text()
        # elif overlapping_road is not None:
        #     # Display collision text for road
        #     self.show_collision_text(overlapping_road)


            # print(f"Overlapping boundary: {overlapping_boundary}")


    def enter_building(self, building_name):
        """Enter the specified building.

        Args:
            building_name (str): The name of the building to enter.
        """
        if building_name == "church":
            self.vote=tk.Button(self.parent,text="Cast your final vote", command=lambda: self.cast_vote(),padx=5,pady=5 )
            self.vote.pack(side="right", anchor='e')
            self.buttons.append(self.vote)
        # This method will be run once when the icon enters a new building
        print(f"Entered {building_name}")

        text_y = self.canvas.winfo_height() + 20 # Below the canvas
        print(text_y)
        self.label = tk.Label(self.parent, text=f"Entered {building_name}", font=("Comic Sans MS",20))
        self.label.pack()
        self.labels.append(self.label)
        # self.canvas.tag_raise(self.label)



        # option for viewing person or item in building
        # two buttons, on with person, other with item

        # if person button is pressed, then show person
        self.person_button=tk.Button(self.parent,text="Person", command=lambda: self.show_person(),padx=5,pady=5 )
        self.person_button.pack(pady=(20,0))
        self.buttons.append(self.person_button)

        # if item button is pressed, then show item
        self.weapon_button=tk.Button(self.parent,text="Weapon", command=lambda: self.show_weapon(),padx=5,pady=5 )
        self.weapon_button.pack(pady=(20,0))
        self.buttons.append(self.weapon_button)

    def exit_building(self):
        """Exit the current building"""
        self.weapon_button.config(state="normal")
        self.person_button.config(state="normal")

        # This method will be run when the icon exits the current building
        print("Exited building")
        for label in self.labels:
            label.destroy()
        for button in self.buttons:
            button.destroy()
        self.labels = []
        self.buttons = []
        self.current_building = None



    # def building_name(self):
    #     building_list = []
    #     for i in self.building_boundaries:
    #         building_list.append(i)
    #     return building_list

    #do Thursday

    def show_person(self):
        """Show the person in the current building."""
    
        self.weapon_button.config(state="disabled")

        # Get the current building
        current_building = self.current_building

        global  npc_list

        # Find the NPC in the current building
        npc_in_building = None
        for npc in npc_list:
            if npc.location == current_building:
                npc_in_building = npc
                break

        # Display the NPC
        if npc_in_building is not None:
            label = Label(self.parent, text=f"Person: {npc.name}", font=('Mistral 18 bold'))
            label.pack()
            self.labels.append(label)
        else:
            label = Label(self.parent, text="No person in this building", font=('Mistral 18 bold'))
            label.pack()
            self.labels.append(label)
        self.person_button.config(state="disabled")

        
    def show_weapon(self):
        """Show the weapon in the current building."""

        self.person_button.config(state="disabled")
        # Get the current building
        current_building = self.current_building

        # Find the NPC in the current building
        npc = None
        for npc_obj in npc_list:
            if npc_obj.location == current_building:
                npc = npc_obj
                break

        # Get the weapon that the NPC is holding
        if npc is not None:
            weapon = npc.holder
            label = Label(self.parent, text=f"Weapon: {weapon.name}", font=('Mistral 18 bold'))
            label.pack()
            self.labels.append(label)
        else:
            label = Label(self.parent, text="No weapon in this building", font=('Mistral 18 bold'))
            label.pack()
            self.labels.append(label)
        self.weapon_button.config(state="disabled")

    def cast_vote(self):
        """Cast the user's vote for the murderer, weapon, and location."""

        for button in self.buttons:
                button.destroy()
        
        for label in self.labels:
            label.destroy()
        # label for entry
        person_label = tk.Label(self.parent, text="Vote for a Person")
        person_label.pack()
        self.labels.append(person_label)

        # entry for person
        person_entry = tk.Entry(self.parent, selectbackground="lightblue", selectforeground="black")
        person_entry.pack()
        self.widgets.append(person_entry)

        # label for entry
        weapon_label = tk.Label(self.parent, text="Vote for a Weapon")
        weapon_label.pack()
        self.labels.append(weapon_label)

        # entry for weapon
        weapon_entry = tk.Entry(self.parent, selectbackground="lightblue", selectforeground="black")
        weapon_entry.pack()
        self.widgets.append(weapon_entry)

        # label for entry
        location_label = tk.Label(self.parent, text="Vote for a Location")
        location_label.pack()
        self.labels.append(location_label)

        # entry for location
        location_entry = tk.Entry(self.parent, selectbackground="lightblue", selectforeground="black")
        location_entry.pack()
        self.widgets.append(location_entry)

        # button to confirm vote
        button=tk.Button(self.parent,text="Enter", command=lambda: self.vote_process(person_entry,weapon_entry,location_entry))
        button.pack()
        self.buttons.append(button)

    def vote_process(self,person_entry,weapon_entry,location_entry):
        """Process the user's vote for the murderer, weapon, and location."""

        # global murderer
        # global weapon_of_choice
        # global location_of_choice
        
        # print(person_entry)
        # print(weapon_entry)
        # print(location_entry)

        person_guess = person_entry.get().lower()
        weapon_guess = weapon_entry.get().lower()
        location_guess = location_entry.get().lower()

        # print(person_guess)
        # print(weapon_guess)
        # print(location_guess)

        # print(murderer.name.lower())
        # print(weapon_of_choice.name.lower())
        # print(building_of_choice.lower())

        if person_guess == murderer.name.lower() and weapon_guess == weapon_of_choice.name.lower() and location_guess == building_of_choice.lower():
            # print("helloooooooo")

            self.switch_frames(Winning_screen)

        else:
            self.switch_frames(Losing_screen)

            
    # Add this helper method to check if the new position overlaps with a boundary
    def is_overlapping(self, x, y, boundary_coords):
        """Check if the icon is overlapping with the specified boundary.

        Args:
            x (int): The x-coordinate of the icon.
            y (int): The y-coordinate of the icon.
            boundary_coords (tuple): A tuple of two tuples representing the boundary coordinates.

        Returns:
            bool: True if the icon is overlapping with the boundary, False otherwise.
        """
        boundary_x1, boundary_y1 = boundary_coords[0]
        boundary_x2, boundary_y2 = boundary_coords[1]
        # print(f"{boundary_x1} < x < {boundary_x2} and {boundary_y1} < y < {boundary_y2}")
        # return boundary_x1 < x < boundary_x2 and boundary_y1 < y < boundary_y2
        if boundary_x1 < x < boundary_x2 and boundary_y1 < y < boundary_y2:
            # print("hello")

            return True
        else:
            return False

    # Add this helper method to check if two boundaries are connected
    def is_connected(self, boundary1_name, boundary2_name):
        """Check if two boundaries are connected.

        Args:
            boundary1_name (str): The name of the first boundary.
            boundary2_name (str): The name of the second boundary.

        Returns:
            bool: True if the boundaries are connected, False otherwise.
        """

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
        """Check if the given coordinates are within the specified boundary.

        Args:
            x (int): The x-coordinate of the point.
            y (int): The y-coordinate of the point.
            boundary_coords (tuple): A tuple of two tuples representing the boundary coordinates.

        Returns:
            bool: True if the point is within the boundary, False otherwise.
        """

        boundary_x1, boundary_y1 = boundary_coords[0]
        boundary_x2, boundary_y2 = boundary_coords[1]
        if (boundary_x1 < x < boundary_x2 and boundary_y1 < y < boundary_y2):
            return True
        return False
        
    def show_collision_text(self, building_name):
        """Show collision text for the specified building.

        Args:
            building_name (str): The name of the building.
        """
        
        if not self.border_control.get_collision_status(building_name):
            print("showing collision text")
            # Collision text should be displayed only if collision status is False
            #self.collision_text.config(text = f"Collided with {building_name}")
            print()
            self.collision_text_1 = Label(self.parent, text = "Ypu have collided")
            self.collision_text_2 = Label(self.parent, text=f"You are at the {building_name}", font=('Mistral 18 bold'))
            text_x = 10  # Adjust left margin
            text_y = self.canvas.winfo_height() + 10  # Below the canvas
            self.collision_text_1.place(x=text_x, y=text_y)
            self.collision_text_2.place(x=text_x, y=text_y)
            # print(self.collision_text_1)  # Print the collision text object
            self.widget
            

    def hide_collision_text(self):
        """Hide collision text."""
        print("hiding collision text")
        self.collision_text.place_forget()  # Clear the text



    

    def check_collision(self, obj_id, boundary_coords):
        """Check for collision between the given object and the specified boundary.

        Args:
            obj_id (int): The ID of the object to check for collision.
            boundary_coords (tuple): A tuple of two tuples representing the boundary coordinates.

        Returns:
            bool: True if there is a collision, False otherwise.
        """
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
        """Return a list of building names."""
        building_list=[]
        for i in self.building_boundaries:
            #print(i)
            building_list.append(i)
            #print(self.building_boundaries[0])
        return building_list

    def switch_frames(self, dest):
        """Switch to the specified frame.

        Args:
            dest (class): The frame class to switch to.
        """
        self.bg_img = None
        self.original_image.close()
        for i in self.labels:
            i.destroy()
        for i in self.buttons:
            i.destroy()
        for i in self.widgets:
            i.destroy()
        self.parent.switch_frame(dest)


class Winning_screen(tk.Frame):
    """Class representing the winning screen.

    This class initializes the frame for the winning screen, which displays a message indicating that the user has won.
    """

    def __init__(self, parent):
        """
        Initialize the Winning_screen class.

        Args:
            parent (tk.Tk): The parent widget.
        """

        tk.Frame.__init__(self, parent)
        self.parent = parent
        parent.geometry("600x800")
        self.widgets_list=[]

        self.intro_text = tk.Text(self.parent, width=80, height=6, wrap=tk.WORD, font=("Comic Sans MS", 25))
        self.intro_text.pack()
        self.widgets_list.append(self.intro_text)


        self.text = "Congratulation,\nYou made it through alive... suprisingly\nDespite the trauma which has been caused from Jacob's death, you continue making your life the best life that you possibly can."

        self.i = 0

        # print(user_name)

        self.appear()


        button=tk.Button(self.parent,text="Play Again", command=lambda: self.switch_frames(Startup),padx=5,pady=5 )
        button.pack(pady=(20,0))
        self.widgets_list.append(button)

        button1=tk.Button(self.parent,text="Quit", command=lambda: self.quit(),padx=5,pady=5 )
        button1.pack(pady=(20,0))
        self.widgets_list.append(button1)

    def appear(self):
        """
        Display the winning message.
        """

        if self.i < len(self.text):
            self.intro_text.insert(tk.END, self.text[self.i])
            self.i += 1
            self.parent.after(50, self.appear)
            
            
    def quit(self):
        """
        Quit the game.
        """
        self.parent.destroy()

    def switch_frames(self, dest):
        """
        Switch to the specified frame.

        Args:
            dest (class): The frame class to switch to.
        """
        for w in self.widgets_list:
            w.destroy()
        self.parent.switch_frame(dest)

class Losing_screen(tk.Frame):
    def __init__(self, parent):
        """
        Initialize the Losing_screen class.

        Args:
            parent (tk.Tk): The parent widget.
        """
        tk.Frame.__init__(self, parent)
        self.parent = parent
        parent.geometry("600x800")
        self.widgets_list=[]

        self.intro_text = tk.Text(self.parent, width=80, height=6.5, wrap=tk.WORD, font=("Comic Sans MS", 25))
        self.intro_text.pack()
        self.widgets_list.append(self.intro_text)


        self.text = f"Well {user_name}, you chose... poorly\n\nthere are some lessons to be learn from that but now is the decision of whether you quit or play again\n***i suggest you play again***"

        self.i = 0

        # print(user_name)

        self.appear()


        button=tk.Button(self.parent,text="Play Again", command=lambda: self.switch_frames(Startup),padx=5,pady=5 )
        button.pack(pady=(20,0))
        self.widgets_list.append(button)

        button1=tk.Button(self.parent,text="Quit", command=lambda: self.quit(),padx=5,pady=5 )
        button1.pack(pady=(20,0))
        self.widgets_list.append(button1)

    def appear(self):
        """
        Display the losing message.
        """

        if self.i < len(self.text):
            self.intro_text.insert(tk.END, self.text[self.i])
            self.i += 1
            self.parent.after(50, self.appear)
            
            
    def quit(self):
        """
        Quit the game.
        """

        self.parent.destroy()

    def switch_frames(self, dest):
        """
        Switch to the specified frame.

        Args:
            dest (class): The frame class to switch to.
        """
        for w in self.widgets_list:
            w.destroy()
        self.parent.switch_frame(dest)

# Class to handle borders
class BorderControl:
    """Class responsible for controlling collisions and interactions with building boundaries.

    This class initializes the BorderControl object, which handles collisions between the character and building boundaries.
    """

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

    # # Define a method for each building
    # def church_func(self):
    #     print("Collided with church")

    # def library_func(self):
    #     global obj_collision
    #     if not self.collision_status["library"]:
    #         self.collision_status["library"] = True
    #         Label(self.canvas, text="Hello world!", font=('Mistral 18 bold')).place(x=20, y=600)
    #     else:
    #         print("Already collided with library")

    # def bank_func(self):
    #     print("Collided with bank")

    # def town_square_func(self):
    #     print("Collided with town square")

    # def market_func(self):
    #     print("Collided with market")

    # def town_hall_func(self):
    #     print("Collided with town hall")

    # def tavern_func(self):
    #     print("Collided with tavern")

    # def farm_stead_func(self):
    #     print("Collided with farm stead")

    # def riverside_func(self):
    #     print("Collided with riverside")

    # def blacksmith_func(self):
    #     print("Collided with blacksmith")

    # def churchtolib(self):
    #     print("collided with boundary")



### Weapons Class ###
class Weapon:
    """Class representing a weapon.

    This class initializes a weapon object, which can be held by an NPC.
    """
    def __init__(self,name,description):
        """
        Initialize the Weapon class.

        Args:
            name (str): The name of the weapon.
            description (str): The description of the weapon.
        """
        self.name = name
        self.description = description
        self.holder = None

    def __str__(self):
        """
        Return a string representation of the weapon.

        Returns:
            str: A string representation of the weapon.
        """
        return f"Weapon(name={self.name}, description={self.description}, holder={self.holder})"



    def assign_holder(self, npc):
        """
        Assign an NPC as the holder of the weapon.

        Args:
            npc (NPC): The NPC who will hold the weapon.
        """
        self.holder = npc
        
### NPC Class ###
class NPC:
    """Class representing a non-player character (NPC).

    This class initializes an NPC object, which can hold a weapon and be assigned a location.
    """
    def __init__(self, name):
        """
        Initialize the Weapon class.

        Args:
            name (str): The name of the weapon.
            description (str): The description of the weapon.
        """
        self.name = name
        self.location = None
        self.holder = None

    # def __str__(self):
    #     return "this is an npc"
        
    def set_location(self, building):
        """
        Set the location of the weapon.

        Args:
            building (str): The name of the building where the weapon is located.
        """
        self.location = building
    
    def set_weapon(self, weapon):
        """
        Set the NPC as the holder of the weapon.

        Args:
            npc (NPC): The NPC who will hold the weapon.
        """
        self.holder = weapon

    
npc_list = [NPC("John"), 
    NPC("Mary"), 
    NPC("Tom"), 
    NPC("Caleb"), 
    NPC("Marcus")]

weapon_list = [Weapon("Revolver","shot wound through the forehead"),
    Weapon("Dagger","stabbing through the aorta artery"),
    Weapon("Poison","cyanide pill hid inside his dinner"),
    Weapon("Crowbar","whack by a strong bar"),
    Weapon("Bible","flattenning by the word")]

building_names = ['church',
                'library',
                'bank', 
                'town_square', 
                'market', 
                'town_hall', 
                'tavern', 
                'farm_stead', 
                'riverside', 
                'blacksmith']

def main():
    
    ### Setting values to different thingz ###
    #weapons = ["Revolver","Dagger","Poison","Rope","Crowbar","Bible"]

    # location_list = MapGUI.building

    ### Shuffling the items randomly ###
    random.shuffle(npc_list)
    random.shuffle(weapon_list)
    random.shuffle(building_names)

    global murderer
    global weapon_of_choice
    global building_of_choice
    
    

        ### Assign weapons to NPCs ###
    for npc, weapon in zip(npc_list, weapon_list):
        Weapon.assign_holder(weapon,npc)
        NPC.set_weapon(npc,weapon)
        #print(f"{Weapon.name} is held by {NPC.name}")
        print(weapon.name," is held by ",npc.name)
        #print(self.holder)
    # If the number of NPCs and weapons are different, handle the remaining NPCs or weapons as needed
    for npc in npc_list[len(weapon_list):]:
        print(f"No weapon assigned to {npc.name}")
    for weapon in weapon_list[len(npc_list):]:
        print(f"{weapon.name} is not held by any NPC")
    
    for npc_object, building_name in zip(npc_list, building_names):
        print(f"{npc_object.name} is in the {building_name}")
        NPC.set_location(npc_object,building_name)


    # Choose a random NPC as the murderer
    murderer = npc_list[1]
    weapon_of_choice = murderer.holder
    building_of_choice = murderer.location

    print(f"The murderer is {murderer.name} with the weapon {weapon_of_choice.name} in the {building_of_choice}.")

    # print(f"{murderer.name} is the murderer")

    # print(weapon_of_choice)
    # print(f"{weapon_of_choice} is the weapon of choice")

    # building_of_choice = murderer.location
    # print(f"{building_of_choice} is the weapon of choice")

    # while weapon_of_choice == None or building_of_choice == None:
    #     # Choose a random NPC as the murderer
    #     murderer = random.choice(npc_list)
    #     print(f"{murderer.name} is the murderer")

    #     weapon_of_choice = murderer.holder
    #     print(f"{weapon_of_choice} is the weapon of choice")

    #     building_of_choice = murderer.location
    #     print(f"{building_of_choice} is the weapon of choice")



    app = App()
    app.mainloop()

main()



