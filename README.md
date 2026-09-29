# Tic-Tac-Toe

A small two-player Tic-Tac-Toe game built with Python, Pygame, and NumPy.

## Requirements

- Python 3
- `pygame`
- `numpy`

## Installation

Install the dependencies with:

```bash
python -m pip install pygame numpy
```

## Run the game

From the project directory, run:

```bash
python tictactoe.py
```

The game opens in a 600 x 600 window.

## How to play

- Player 1 places circles (`O`).
- Player 2 places crosses (`X`).
- Click an empty square to place the current player's mark.
- The first player to complete a horizontal, vertical, or diagonal line wins.
- Press `R` to restart the game.
- Close the game window to exit.

## Project structure

```text
.
├── README.md
└── tictactoe.py
```

The main Python file contains the board state, drawing functions, move validation, win detection, and the Pygame event loop.
