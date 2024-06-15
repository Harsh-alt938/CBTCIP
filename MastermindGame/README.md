
# Mastermind Game🎮

This is a Python implementation of the classic Mastermind game, where players take turns setting a secret two-digit number and guessing their opponent's number based on hints. The game is built using the Tkinter library for creating a graphical user interface (GUI).

## How to Play

1. Player 1 sets a secret two-digit number (between 10 and 99).
2. Player 2 tries to guess the number.
3. After each guess, Player 2 receives hints indicating:
  - The number of correct digits in the correct positions.
  - The number of correct digits in the wrong positions.
4. Player 2 continues guessing until the secret number is correctly guessed.
5. After Player 2 correctly guesses the number, the roles switch, and Player 1 becomes the guesser, while Player 2 sets a new secret number.
6. The game continues until both players have had a chance to guess the secret number.
7. The player who correctly guesses the number in fewer attempts wins the game and is crowned the "Mastermind."

## Features

- Graphical User Interface (GUI) built with Tkinter.
- Two-player mode with alternating roles of setting the secret number and guessing.
- Input validation to ensure that players enter valid two-digit numbers.
- Real-time hints provided after each guess, indicating the number of correct digits in the correct positions and the number of correct digits in the wrong positions.
- Game history display showing all previous attempts and guesses.
- Result window displaying the winner and a summary of all attempts made during the game.
- Ability to reset the game and start a new round.

## Requirements

- Python 3.x
- Tkinter library (typically included in Python's standard library)

## How to Run

1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the following command:
python mastermind_game.py
The game window will open, and you can start playing.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
