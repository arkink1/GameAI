"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    for i in board:
        for j in i:
            if j == X:
                x+=1
            elif j == O:
                o+=1
            else:
                pass
    if x == o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_spots = set()
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                empty_spots.add((i, j))
    return empty_spots


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = []
    person = player(board)
    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = person
    else:
        raise NameError('Invalid move')
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in [X, O]:
        for j in range(0, 3):
            if board[j][0] == board[j][1] == board[j][2] == i:
                return i
            if board[0][j] == board[1][j] == board[2][j] == i:
                return i
    for i in [X, O]:
        if board[0][0] == board[1][1] == board[2][2] == i:
            return i
        elif board[0][2] == board[1][1] == board[2][0] == i:
            return i
        else:
            pass
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == EMPTY:
                    return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            return max_value(board)[1]
        else:
            return min_value(board)[1]
        

def max_value(board):
    v = -1*math.inf
    b = None
    if terminal(board):
        return utility(board), 0
    else:
        for action in actions(board):
            min = min_value(result(board, action))
            if min[0] > v:
                v = min[0]
                b = action
                if v == 1:
                    return v, b
        return v, b

def min_value(board):
    v = math.inf
    b = None
    if terminal(board):
        return utility(board), 0
    else:
        for action in actions(board):
            max = max_value(result(board, action))
            if v > max[0]:
                v = max[0]
                b = action
                if v == -1:
                    return v, b
        return v, b
