from tkinter import Tk, Button, Label, Entry, END, StringVar, DISABLED, NORMAL
import time
import random

root = Tk()
root.geometry("250x100")
root.title("Sock, Paper, Scissors!")
root.resizable(0, 0)
game_text = StringVar()
game_text.set("Welcome to Rock, Paper, Scissors!")
buttons = {}
revert_colour = root.cget("bg")
computer_choices = ["rock", "paper", "scissors"]

def rock():
    buttons["rock"].configure(bg="green")
    buttons["rock"].after(10, lambda: find_winner("rock"))

def paper():
    buttons["paper"].configure(bg="green")
    buttons["paper"].after(10, lambda: find_winner("paper"))

def scissors():
    buttons["scissors"].configure(bg="green")
    buttons["scissors"].after(10, lambda: find_winner("scissors"))

def find_winner(user_choice):
    for value in buttons.values():
        value.configure(state=DISABLED)

    winner_text = "You Won!"
    computer_choice = computer_choices[random.randint(0, 2)]

    if(
        (computer_choice == "paper" and user_choice == "rock") or
        (computer_choice == "scissors" and user_choice == "paper") or
        (computer_choice == "rock" and user_choice == "scissors")):
        winner_text  ="Computer Won!"

    if(computer_choice == user_choice):
        winner_text = "It was a tie!"
    

    game_text.set("Rock...")
    display_box.after(1000, lambda: game_text.set("Paper..."))
    display_box.after(2000, lambda: game_text.set("Scissors!"))
    display_box.after(3000, lambda: display_winner(winner_text))

def display_winner(winner_text):
    game_text.set(winner_text)

    for value in buttons.values():
        value.configure(bg=revert_colour)
        value.configure(state=NORMAL)

display_box = Label(root, textvariable=game_text, borderwidth=2, relief="groove", width=29, justify='left', anchor='nw')
display_box.grid(row=0, column=0, columnspan=3, padx=(5, 0), pady=(10, 10))

buttons["rock"] = Button(root, text="Rock", command=rock)
buttons["rock"].grid(row=1,column=0)

buttons["paper"] = Button(root, text="Paper", command=paper)
buttons["paper"].grid(row=1,column=1)

buttons["scissors"] = Button(root, text="Scissors", command=scissors)
buttons["scissors"].grid(row=1,column=2)

root.mainloop()