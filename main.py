from tkinter import Tk, Button, Label, Entry, END
import queue 

class Demo:

    def __init__(self, master):
        self.buffer = queue.Queue(maxsize=25)
        self.master = master

        self.display_box = Label(master, borderwidth=2, relief="groove", width=59, height=25, justify='left', anchor='nw')
        self.display_box.grid(row=0, column=0, columnspan=10, padx=(10, 10))

        Label(master, text="Command: ").grid(row=1, column=0)
        self.command = Entry(master, width=41)
        self.command.grid(row=1, column=2, columnspan=6)
        self.command.focus_set()

        # bind the enter keys so you can press them to send a command
        self.command.bind("<Return>", self.enter_hit)
        self.command.bind("<KP_Enter>", self.enter_hit)
        Button(master, text="SEND", command=self.show_name).grid(row=1, column=9, padx=(10, 10))

    def enter_hit(self, event):
        self.show_name()

    def show_name(self):

        # get the command, set it to lowercase and then clear the entry box
        command_sent = self.command.get().lower()
        self.command.delete(0, END)

        # if nothing was entered, do nothing
        if not command_sent:
            return

        if self.buffer.full():
            self.buffer.get()

        # add the item to the queue
        self.buffer.put("{0}\n".format(command_sent))

        # clear the display so we can re-write everything
        self.display_box['text'] = ""

        # run the command
        self.handle_command(command_sent)

        # output everything to the console again
        for item in list(self.buffer.queue):
            self.display_box['text'] += item

    def handle_command(self, command):
        if command == "clear":
            self.buffer.queue.clear()
        elif command == "exit":
            self.master.quit()


root = Tk()
root.geometry("500x500")
root.title("Hello there!")
root.resizable(0, 0)

app = Demo(root)

root.mainloop()