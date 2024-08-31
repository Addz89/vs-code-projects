import tkinter as tk
from tkinter import messagebox
import random

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("650x400")
        self.root.title("Zombie Game")
        self.label = tk.Label(root, text="You wake up and get ready for work.", wraplength=400)
        self.label.pack(pady=120)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.button1 = tk.Button(self.button_frame, text="Continue", command=self.intro_step2)
        self.button1.pack(pady= 1)

    def intro_step2(self):
        self.label.config(text="You walk around the house but see no one around.")
        self.button1.config(text="Where to?", command=self.where_to)

    def where_to(self):
        self.button1.pack_forget()
        
        self.button2 = tk.Button(self.button_frame, text="Go to the car", command=self.car)
        self.button3 = tk.Button(self.button_frame, text="Stay at home", command=self.stay_home)

        self.button2.pack(side="left", padx=20)
        self.button3.pack(side="right", padx=20)

    def street(self):
        self.clear_buttons()
        self.label.config(text="You walk further down the street and see someone running towards you, "
        "you yell STOP. But the person runs faster towards you, they then jump and try to bite you, then you "
        "realise its a zombie. and try fight them off, that gun would have been good right now. The zombie then bites you "
        "on the neck.  YOU HAVE DIED")
        
        self.button2 = tk.Button(self.button_frame, text="Play Again", command=self.play_again)
        self.button3 = tk.Button(self.button_frame, text="Exit", command=self.end)

        self.button2.pack(side="left", padx=20)
        self.button3.pack(side="right", padx=20)

    def run_away(self):
        self.clear_buttons()
        self.label.config(text="You run away from the zombie. ")


    def shoot_zombie(self):
        self.clear_buttons()
        self.label.config(text="You slowly grab the gun and aim at the zombie. You start to slowly pull the trigger. "
        "but then there is a loud BANG!. The zombie then runs towards the bang and you grab some drinks and food and "
        "then qickly walk out.")



    def gas_station(self):
        self.clear_buttons()
        zombie = random.choice(['Zombie with Red eyes', 'Zombie with a limp', 'Zombie with one arm'])
        self.label.config(text="You walk towards the gas station and noone is around. You walk in and "
        f"see a {zombie}, Now what do you do?")

        self.button2 = tk.Button(self.button_frame, text="Shoot Zombie", command=self.shoot_zombie)
        self.button3 = tk.Button(self.button_frame, text="Run away", command=self.run_away)

        self.button2.pack(side="left", padx=20)
        self.button3.pack(side="right", padx=20)


    def running(self):
        self.clear_buttons()





    def walk_past(self):
        self.clear_buttons()
        self.label.config(text="You keep walking down and turn around and see at lest 50 zombies running towards you."
        "You start running and fall over. The zombies get you but you take out your gun and shot one in the head, "
        "and run as fast as you can."
        "You get away..")

        self.button1 = tk.tk.Button(self.button_frame, text="Keep running", command=self.running)
        
        self.button1.pack(side="left", padx=20)

    def pick_up(self):
        self.clear_buttons()
        self.label.config(text="You Reach for the Gun and pick it up. You turn around and someone is running at you."
        "You hold the gun tight and yell stop. They keep running towards you. You notice blood on there face, "
        "you lift the gun up and "
        "shoot, it was a zombie. You then walk down the street, you then come across a gas station. \n "
        "Do you walk in or keep walking..")

        self.button2 = tk.Button(self.button_frame, text="Gas Station", command=self.gas_station)
        self.button3 = tk.Button(self.button_frame, text="Keep walking", command=self.walk_past)

        self.button2.pack(side="left", padx=20)
        self.button3.pack(side="right", padx=20)


    def get_out(self):
        self.clear_buttons()
        self.label.config(text="You get out the car and walk to the police car."
        "You dont see anyone in there, you open the door and see a gun. Do you take the gun")
        self.button2 = tk.Button(self.button_frame, text="Pick up", command=self.pick_up)
        self.button3 = tk.Button(self.button_frame, text="Walk away", command=self.street)

        self.button2.pack(side="left", padx=20)
        self.button3.pack(side="right", padx=20)

    def car_ride(self):
        self.clear_buttons()
        self.label.config(text="You jump in the car. You try to start it again, "
        "it turns over and you drive down the street. You then see a police car on the side of the road. "
        "Do you pull over or keep driving.")
        self.button2 = tk.Button(self.button_frame, text="Get out", command=self.get_out)
        self.button3 = tk.Button(self.button_frame, text="Back to house", command=self.stay_home)

        self.button2.pack(side="left", padx=20)
        self.button3.pack(side="right", padx=20)


    def car(self):
        self.clear_buttons()
        self.label.config(text="You have walked to the car. But it won't start! What will you do now?")
        self.button2 = tk.Button(self.button_frame, text="Try again", command=self.car_ride)
        self.button3 = tk.Button(self.button_frame, text="Back to house", command=self.stay_home)

        self.button2.pack(side="left", padx=20)
        self.button3.pack(side="right", padx=20)
        

    def stay_home(self):
        self.clear_buttons()
        self.label.config(text="You decide to stay home. Suddenly, "
        "you hear a strange noise coming from the kitchen... Do you walk towards the sound or go back outside to the car?")

        self.button2 = tk.Button(self.button_frame, text="Go to the car", command=self.car)
        self.button3 = tk.Button(self.button_frame, text="Towards sound", command=self.toward_sound)

        self.button2.pack(side="left", padx=20)
        self.button3.pack(side="right", padx=20)

    def toward_sound(self):
        self.label.config(text="You walk towards the noise. it is very quite, not one sound. Only your foot steps.")

    def end_game(self):
        self.button1 = tk.Button(self.button_frame, text="Play Again", command=self.play_again)
        self.button1.pack()

    def play_again(self):
        response = messagebox.askquestion("Play Again?", "Would you like to play again?")
        if response == 'yes':
            self.reset_game()
        else:
            self.root.quit()

    def reset_game(self):
        self.clear_buttons()
        self.label.config(text="You wake up and get ready for work.")
        self.button1 = tk.Button(self.button_frame, text="Continue", command=self.intro_step2)
        self.button1.pack(pady=10)

    def clear_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def end(self):
        self.clear_buttons()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()