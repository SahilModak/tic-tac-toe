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
    count = 0
    for i in board:
        for j in i:
            if (j == EMPTY):
                count += 1
    if(count%2 == 1):
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionSet = {}
    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                actionSet.add((i, j))
    return actionSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardCpy = copy.deepcopy(board)
    n = player(boardCpy)
    i = action[0]
    j = action[1]
    if(boardCpy[i][j] != EMPTY):
        raise NameError('Invalid action selected, cannot place marker there.')
    if(n == X):
        boardCpy[i][j] = X
    else:
        boardCpy[i][j] = O
    return boardCpy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    flag = board[1][1] is not EMPTY
    if(flag and board[0][0] == board[1][1] and board[0][0] == board[2][2]):
        return board[1][1]
    if(flag and board[0][2] == board[1][1] and board[0][2] == board[2][0]):
        return board[1][1]
    
    for i in range(3):
        if(EMPTY != board[i][1] and board[i][0] == board[i][1] and board[i][0] == board[i][2]):
            return board[i][1]
        if(EMPTY != board[1][i] and board[0][i] == board[1][i] and board[0][i] == board[2][i]):
            return board[1][i]
    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board) != EMPTY):
        return True
    for i in board:
        if EMPTY in i:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    n = winner(board)
    if(n == EMPTY):
        return 0
    elif(n == X):
        return 1
    return -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board) == True):
        return None
    computerPlayer = player(board)
