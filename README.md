# AI algorithms for TicTacToe and Minesweeper written in Python

This repository contains AI implementations for two classic games: Tic-Tac-Toe and Minesweeper. These AI algorithms are designed to play these games effectively, providing both challenge and entertainment.

## Tic-Tac-Toe

The Tic-Tac-Toe AI implementation in this repository allows you to play against an AI opponent that employs various strategies to make optimal moves. The AI uses the minimax algorithm with alpha-beta pruning to search through the game tree and determine the best possible move. It ensures that the AI makes moves that either lead to a win or prevent the opponent from winning.

Features:
- Minimax algorithm with alpha-beta pruning for optimal move selection.
- Ability to play against the AI or another human player.
- Simple command-line interface for easy interaction.

## Minesweeper AI

The Minesweeper AI in this repository is designed to play the classic Minesweeper game intelligently. It utilizes logical reasoning, constraint propagation, and randomized exploration to effectively reveal safe cells and avoid mines. The AI maintains a knowledge base of logical statements about the game state and dynamically updates its strategy based on the revealed information.

Features:
- Logical reasoning and constraint propagation for intelligent move selection.
- Randomized exploration strategy to handle uncertainty.
- Ability to play Minesweeper automatically or manually.

## Run the games

Change directory to either TicTacToe or Minesweeper.
`cd TicTacToe`
`cd Minesweeper`

Install dependencies:
`pip install -r requirements.txt`

Run the program:
`python runner.py`
