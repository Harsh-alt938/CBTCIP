import tkinter as tk
from tkinter import simpledialog, messagebox
import random

player_score = 0
computer_score = 0
history = []

def play_game(player_choice):
    global player_score, computer_score
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
        player_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    history.append(f"Player: {player_choice}, Computer: {computer_choice} - {result}")

    result_label.config(text=result)
    score_label.config(text=f"Score - Player: {player_score}, Computer: {computer_score}")
    update_history()

def update_history():
    history_text.config(state=tk.NORMAL)
    history_text.delete('1.0', tk.END)
    for item in history[-5:]:
        history_text.insert(tk.END, item + "\n")
    history_text.config(state=tk.DISABLED)

def exit_game():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()

root = tk.Tk()
root.title("ROCK-PAPER-SCISSORS GAME")
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

score_label = tk.Label(root, text="Score - Player: 0, Computer: 0", font=("Times New Roman", 12), bg='#b3ffb3')
score_label.pack(pady=10)

history_label = tk.Label(root, text="Game History:", font=("Times New Roman", 12), bg='#b3ffb3')
history_label.pack(pady=5)

history_text = tk.Text(root, height=5, width=50, font=("Courier New", 10), bg='white', wrap=tk.WORD)
history_text.pack(pady=5)
history_text.config(state=tk.DISABLED)

exit_button = tk.Button(root, text="Exit", width=10, command=exit_game)
exit_button.pack(pady=5)

made_by_label = tk.Label(root, text="Made by: Harsh Bhardwaj", font=("Arial", 10, "italic"), bg='#b3ffb3')
made_by_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
