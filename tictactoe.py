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
            if (j == None):
                count += 1
    if(count%2 == 0):
        return O
    return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    lst = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] == None):
                lst.append((i, j))
    return lst


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardcpy = copy.deepcopy(board)
    i = action[0]
    j = action[1] 
    if(boardcpy[i][j] == None):
        boardcpy[i][j] = player(boardcpy)
        return boardcpy
    raise NotImplementedError

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    flag = True
    for i in range(3):
        if (board[i][0] != None and 
        board[i][0] == board[i][2] and 
        board[i][0] == board[i][1]):
            return board[i][0]
        elif(board[0][i] != None and
        board[0][i] == board[2][i] and 
        board[0][i] == board[1][i]):
            return board[0][i]
        elif(flag):
            flag = False
            if(board[1][1] != None and
            board[0][0] == board[2][2] and
            board[0][0] == board[1][1]):
                return board[0][0]
            if(board[1][1] != None and
            board[2][0] == board[1][1] and
            board[2][0] == board[0][2]):
                return board[2][0]
    return None
            


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) != None):
        return True
    for i in board:
        for j in i:
            if j == None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    temp = winner(board)
    if(temp == "X"):
        return 1
    elif(temp == "O"):
        return -1
    return 0

def maxim(board):
    if(terminal(board)):
        return utility(board), None
    v = -10
    lst = []
    allact = actions(board)
    for act in allact:
        x, y = minim(result(board, act))
        if(x >= v):
            v = x
            lst.append([v, act])
            if(x == 1):
                return v, lst
    return v, lst


def minim(board):
    if(terminal(board)):
        return utility(board), None
    v = 10
    lst = []
    allact = actions(board)
    for act in allact:
        x, y = maxim(result(board,act))
        if(x <= v):
            v = x
            lst.append([v, act])
            if (x == -1):
                return v, lst
    return v, lst

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return None

    if(player(board) == "X"):
        a, lst = maxim(board)
        maxi = -10
        for i in lst:
            if (i[0] > maxi):
                maxi = i[0]
                act = i[1]
    else:
        a, lst = minim(board)
        mini = 10
        for i in lst:
            if i[0] < mini:
                mini = i[0]
                act = i[1]
    return act