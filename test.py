
import tkinter as tk
import random

class Game:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Number")

        self.secret_number = random.randint(1, 100)
        self.guesses_left = 10

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Guess", command=self.check_guess)
        self.button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
            return

        self.guesses_left -= 1

        if guess < self.secret_number:
            self.result_label.config(text="Too low! Guesses left: " + str(self.guesses_left))
        elif guess > self.secret_number:
            self.result_label.config(text="Too high! Guesses left: " + str(self.guesses_left))
        else:
            self.result_label.config(text="Congratulations! You guessed it!")
            self.button.config(state=tk.DISABLED)

        if self.guesses_left == 0:
            self.result_label.config(text="You ran out of guesses. The number was " + str(self.secret_number))
            self.button.config(state=tk.DISABLED)

root = tk.Tk()
game = Game(root)
root.mainloop()
