import tkinter as tk
from tkinter import simpledialog, messagebox
import random

def play_game(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    result = ""
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=result)

def exit_game():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()

root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(bg='#b3ffb3')

player_name = simpledialog.askstring("Player Name", "Please enter your name:")
player_name_label = tk.Label(root, text=f"Player: {player_name}", font=("Times New Roman", 12), bg='#b3ffb3')
player_name_label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play_game('Rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play_game('Paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play_game('Scissors'))
scissors_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Times New Roman", 14), bg='#b3ffb3')
result_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Times New Roman", 14), bg='#b3ffb3')
result_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Times New Roman", 14), bg='#b3ffb3')
result_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Times New Roman", 14), bg='#b3ffb3')
result_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Times New Roman", 14), bg='#b3ffb3')
result_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Times New Roman", 14), bg='#b3ffb3')
result_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Times New Roman", 14), bg='#b3ffb3')
result_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Times New Roman", 14), bg='#b3ffb3')
result_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Times New Roman", 14), bg='#b3ffb3')
result_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Times New Roman", 14), bg='#b3ffb3')
result_label.pack(pady=10)

exit_button = tk.Button(root, text="Exit", width=10, command=exit_game)
exit_button.pack(pady=5)

root.mainloop()
