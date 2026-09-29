# Tic Tac Toe

A tic tac toe game built with Python and Pygame. Play against a friend, or against a computer opponent that uses the **minimax algorithm** and never loses.

## Features

- Main menu with two modes: **Player vs Player** and **Player vs Computer**
- Unbeatable computer opponent (minimax with full game-tree search)
- Status bar showing whose turn it is, and the result: **O wins**, **X wins**, or **draw**
- Press **R** at any time to return to the main menu

## Requirements

- Python 3.11 or newer
- [NumPy](https://numpy.org/) 2.4.6
- [Pygame](https://www.pygame.org/) 2.6.1

## Installation

1. Download or clone this project and open a terminal (PowerShell or Command Prompt) in its folder.
2. (Optional but recommended) Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the game

```
python tictactoe.py
```

## How to play

| Action | Control |
| --- | --- |
| Choose a game mode | Click a button on the main menu |
| Place your mark | Click an empty square |
| Return to the main menu | Press `R` |

- **O** always goes first.
- In **Player vs Computer** mode, you play **O** and the computer plays **X**.

## How the computer works

The computer uses **minimax**, a recursive algorithm that looks at every possible way the game could continue and picks the move with the best guaranteed outcome.

- A computer win scores `+1`, a human win scores `-1`, and a draw scores `0`.
- On the computer's turn it picks the highest score. On the human's turn it assumes the human picks the lowest.
- The search has no depth limit, because tic tac toe is small enough to search to the end of the game. This makes the computer unbeatable: the best a human can do is draw.

## Project structure

```
.
├── tictactoe.py       # the whole game
├── requirements.txt   # Python dependencies
└── README.md
```

