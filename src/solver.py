from copy import deepcopy

initial_board = [
    [7,6,5],
    [8,4,9],
    [3,2,1]
]

solved_board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def isSolved(board):
    return areBoardsEqual(board, solved_board)

def areBoardsEqual(board1, board2):
    return board1 == board2

# Operations
def shiftQuadrant1(originalBoard):
    board = deepcopy(originalBoard)
    board[0][0], board[0][1], board[1][1], board[1][0] = board[1][0], board[0][0], board[0][1], board[1][1]
    return board

def shiftQuadrant2(originalBoard):
    board = deepcopy(originalBoard)
    board[0][1], board[0][2], board[1][2], board[1][1] = board[1][1], board[0][1], board[0][2], board[1][2]
    return board

def shiftQuadrant3(originalBoard):
    board = deepcopy(originalBoard)
    board[1][0], board[1][1], board[2][1], board[2][0] = board[2][0], board[1][0], board[1][1], board[2][1]
    return board

def shiftQuadrant4(originalBoard):
    board = deepcopy(originalBoard)
    board[1][1], board[1][2], board[2][2], board[2][1] = board[2][1], board[1][1], board[1][2], board[2][2]
    return board

def isBoardInPastBoardStates(board, pastBoardStates):
    for state in pastBoardStates:
        if(areBoardsEqual(board, state)):
            return True
    return False

attempt = 0
def solve(board, stack, pastBoardStates, maxMoves):
    global attempt
    attempt = attempt + 1

    if(len(stack) >= maxMoves):
        return

    if(isSolved(board)):
        print("Attempt: ", attempt, "Solution: ", stack)

    if isBoardInPastBoardStates(board, pastBoardStates):
        return

    solve(shiftQuadrant1(board), stack + ['Q1'], pastBoardStates + [board], maxMoves)
    solve(shiftQuadrant2(board), stack + ['Q2'], pastBoardStates + [board], maxMoves)
    solve(shiftQuadrant3(board), stack + ['Q3'], pastBoardStates + [board], maxMoves)
    solve(shiftQuadrant4(board), stack + ['Q4'], pastBoardStates + [board], maxMoves)

maxMoves = 11
solve(initial_board, [], [], maxMoves)