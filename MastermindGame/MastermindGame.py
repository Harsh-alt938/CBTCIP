import tkinter as tk
from tkinter import messagebox

class MastermindGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mastermind Game")
        self.root.configure(bg="#add8e6")  

        self.title_label = tk.Label(root, text="Mastermind Game", font=("Times New Roman", 24), bg="#add8e6")
        self.title_label.pack(pady=(10, 20))

        self.title_label = tk.Label(root, text="by Harsh Bhardwaj", font=("Times New Roman", 10), bg="#add8e6")
        self.title_label.pack(pady=(10, 20))

        self.frame = tk.Frame(root, bg="#add8e6")
        self.frame.pack(padx=20, pady=20)

        self.info_label = tk.Label(self.frame, text="Player 1, set a two-digit number (10-99):", bg="#add8e6", font=("Helvetica", 14))
        self.info_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        self.entry = tk.Entry(self.frame, show="*", font=("Helvetica", 14))
        self.entry.grid(row=1, column=0, columnspan=2, pady=(0, 10))

        self.submit_button = tk.Button(self.frame, text="Submit", command=self.set_number, font=("Helvetica", 14), bg="#4caf50", fg="white")
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=(0, 10))

        self.hint_label = tk.Label(self.frame, text="", fg="blue", bg="#add8e6", font=("Helvetica", 12))
        self.hint_label.grid(row=3, column=0, columnspan=2, pady=(10, 0))

        self.secret_number = ""
        self.attempts = 0
        self.current_player = 1
        self.guess_history = []

    def set_number(self):
        if self.current_player == 1:
            self.secret_number = self.entry.get()
            if self.secret_number.isdigit() and 10 <= int(self.secret_number) <= 99:
                self.entry.delete(0, tk.END)
                self.info_label.config(text="Player 2, guess the number:")
                self.submit_button.config(text="Guess", command=self.guess_number)
            else:
                messagebox.showerror("Invalid input", "Please enter a valid two-digit number (10-99).")
        else:
            self.secret_number = self.entry.get()
            if self.secret_number.isdigit() and 10 <= int(self.secret_number) <= 99:
                self.entry.delete(0, tk.END)
                self.info_label.config(text="Player 1, guess the number:")
                self.submit_button.config(text="Guess", command=self.guess_number)
                self.attempts = 0
            else:
                messagebox.showerror("Invalid input", "Please enter a valid two-digit number (10-99).")

    def guess_number(self):
        guess = self.entry.get()
        self.attempts += 1
        self.guess_history.append((self.attempts, guess))
        if guess == self.secret_number:
            messagebox.showinfo("Correct!", f"Player {3 - self.current_player} guessed the number in {self.attempts} attempts!")
            if self.current_player == 1:
                self.previous_attempts = self.attempts
                self.current_player = 2
                self.info_label.config(text="Player 2, set a two-digit number (10-99):")
                self.submit_button.config(text="Submit", command=self.set_number)
            else:
                if self.attempts < self.previous_attempts:
                    winner = "Player 1 wins and is crowned Mastermind!"
                else:
                    winner = "Player 2 wins and is crowned Mastermind!"
                messagebox.showinfo("Result", winner)
                self.show_results(winner)
                self.reset_game()
        else:
            correct_positions, correct_digits = self.give_hint(self.secret_number, guess)
            self.hint_label.config(text=f"Hint: {correct_positions} correct positions, {correct_digits} correct digits.")

    def give_hint(self, secret, guess):
        correct_positions = 0
        correct_digits = 0
        secret_counts = {}
        guess_counts = {}

        for s, g in zip(secret, guess):
            if s == g:
                correct_positions += 1
            else:
                secret_counts[s] = secret_counts.get(s, 0) + 1
                guess_counts[g] = guess_counts.get(g, 0) + 1

        for digit in guess_counts:
            if digit in secret_counts:
                correct_digits += min(secret_counts[digit], guess_counts[digit])

        return correct_positions, correct_digits

    def show_results(self, winner):
        result_window = tk.Toplevel(self.root)
        result_window.title("Game Results")
        result_window.configure(bg="#add8e6")  

        result_label = tk.Label(result_window, text=f"Game Results - {winner}", font=("Helvetica", 16), bg="#add8e6")
        result_label.pack(pady=10)

        history_frame = tk.Frame(result_window, bg="#add8e6")
        history_frame.pack(pady=10)

        tk.Label(history_frame, text="Attempt", font=("Helvetica", 12), bg="#add8e6").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(history_frame, text="Guess", font=("Helvetica", 12), bg="#add8e6").grid(row=0, column=1, padx=5, pady=5)

        for attempt, guess in self.guess_history:
            tk.Label(history_frame, text=str(attempt), bg="#add8e6").grid(row=attempt, column=0, padx=5, pady=5)
            tk.Label(history_frame, text=guess, bg="#add8e6").grid(row=attempt, column=1, padx=5, pady=5)

        close_button = tk.Button(result_window, text="Close", command=result_window.destroy, font=("Helvetica", 12), bg="#4caf50", fg="white")
        close_button.pack(pady=10)

    def reset_game(self):
        self.entry.delete(0, tk.END)
        self.info_label.config(text="Player 1, set a two-digit number (10-99):")
        self.submit_button.config(text="Submit", command=self.set_number)
        self.hint_label.config(text="")
        self.secret_number = ""
        self.attempts = 0
        self.current_player = 1
        self.guess_history = []
        self.previous_attempts = None

def main():
    root = tk.Tk()
    app = MastermindGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
