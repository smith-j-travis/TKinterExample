from tkinter import Tk, Button, Label, Entry, Frame, END, StringVar, DISABLED, NORMAL
import time
import random

class Game:
    def __init__(self, root, outof):
        self.game_frame = Frame(root)
        self.replay_frame = Frame(root)

        self.game_text = StringVar()
        self.win_target = outof
        self.player_wins = 0
        self.computer_wins = 0
        self.computer_choices = ["rock", "paper", "scissors"]
        self.buttons = {}
        self.revert_colour = root.cget("bg")
        self.display_box = Label(self.game_frame, textvariable=self.game_text, borderwidth=2, relief="groove", width=29, justify='left', anchor='nw')
        self.display_box.grid(row=0, column=0, columnspan=4, padx=(5, 0), pady=(10, 0))

        self.player_score = Label(self.game_frame, justify='left', anchor='nw')
        self.player_score.grid(row=1, column=0)
        self.computer_score = Label(self.game_frame, justify='left', anchor='nw')
        self.computer_score.grid(row=1, column=1, columnspan=2)

        self.buttons["rock"] = Button(self.game_frame, text="Rock", command=self.rock, width=6)
        self.buttons["rock"].grid(row=2, column=0, padx=(5, 0))

        self.buttons["paper"] = Button(self.game_frame, text="Paper", command=self.paper, width=6)
        self.buttons["paper"].grid(row=2, column=1)

        self.buttons["scissors"] = Button(self.game_frame, text="Scissors", command=self.scissors, width=6)
        self.buttons["scissors"].grid(row=2, column=2)

    def close(self):
        self.game_frame.destroy()

    def show(self):
        self.update_scores()
        self.game_text.set("Welcome to Rock, Paper, Scissors!")

        self.game_frame.pack()
        return self.game_frame

    def rock(self):
        self.buttons["rock"].configure(bg="green")
        self.buttons["rock"].after(10, lambda: self.find_winner("rock"))

    def paper(self):
        self.buttons["paper"].configure(bg="green")
        self.buttons["paper"].after(10, lambda: self.find_winner("paper"))

    def scissors(self):
        self.buttons["scissors"].configure(bg="green")
        self.buttons["scissors"].after(10, lambda: self.find_winner("scissors"))

    def update_scores(self):
        self.player_score["text"] = "Player: " + str(self.player_wins)
        self.computer_score["text"] = "Computer: " + str(self.computer_wins)

    def find_winner(self, user_choice):
        for value in self.buttons.values():
            value.configure(state=DISABLED)

        winner_text = "You Won!"
        computer_choice = self.computer_choices[random.randint(0, 2)]

        if(computer_choice == user_choice):
            winner_text = "It was a tie!"
        else:
            if(
                (computer_choice == "paper" and user_choice == "rock") or
                (computer_choice == "scissors" and user_choice == "paper") or
                (computer_choice == "rock" and user_choice == "scissors")):
                winner_text = "Computer Won!"
                self.computer_wins += 1
            else:
                self.player_wins += 1

        if self.computer_wins == self.win_target:
            winner_text = "Computer has won the game!"
        elif self.player_wins == self.win_target:
            winner_text = "You have won the game!"

        self.game_text.set("Rock...")
        self.display_box.after(1000, lambda: self.game_text.set("Paper..."))
        self.display_box.after(2000, lambda: self.game_text.set("Scissors!"))
        self.display_box.after(3000, lambda: self.display_winner(winner_text))

    def display_winner(self, winner_text):
        self.update_scores()
        self.game_text.set(winner_text)

        if self.computer_wins == self.win_target or self.player_wins == self.win_target:
            self.display_box.after(1000, self.close)

        for value in self.buttons.values():
            value.configure(bg=self.revert_colour)
            value.configure(state=NORMAL)

class Menu:
    def __init__(self, root):
        self.root = root
        self.menu_frame = Frame(root)

        Button(self.menu_frame, text="Best of 3", command=lambda: self.start_game(2)).grid(row=0, column=0)
        Button(self.menu_frame, text="Best of 5", command=lambda: self.start_game(3)).grid(row=1, column=0)
        Button(self.menu_frame, text="Best of 7", command=lambda: self.start_game(5)).grid(row=2, column=0)

        self.menu_frame.pack()

    def start_game(self, outof):
        self.menu_frame.pack_forget()
        game = Game(self.root, outof)

        self.root.wait_window(game.show())
        self.menu_frame.pack()

if __name__ == "__main__":
    root = Tk()
    root.geometry("250x100")
    root.title("Sock, Paper, Scissors!")
    root.resizable(0, 0)

    menu = Menu(root)

    root.mainloop()