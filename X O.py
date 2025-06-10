computer = 'X'
player = 'O'

board = {1: '-', 2: '-', 3: '-',
         4: '-', 5: '-', 6: '-',
         7: '-', 8: '-', 9: '-'}
#######################################
def printBoard(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("\n")
#######################################
def spaceIsFree(position):
    return board[position] == '-'
#######################################
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if checkGameResult(letter):
            exit()
        return
    else:
        print("Invalid position")
        position = int(input("Please enter a new position: "))
        insertLetter(letter, position)
        return
#######################################
def checkGameResult(letter):
    if checkDraw():
        print("Draw!")
        return True
    elif checkWin(letter):
        if letter == 'X':
            print("Bot wins!")
        else:
            print("Player wins!")
        return True
    return False
#######################################
def checkDraw():
    for key in board.keys():
        if board[key] == '-':
            return False
    return True
#######################################
def checkWin(mark):
    # all win cases
    win_cases = [(1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
                            (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
                            (1, 5, 9), (7, 5, 3) ]            # Diagonals
    
    for case in win_cases:
        if board[case[0]] == board[case[1]] == board[case[2]] == mark:
            return True

    return False
#######################################
def playerMove():
    position = int(input("Enter a position for 'O': "))
    insertLetter(player, position)
    return
#######################################
def compMove():
    bestScore = -800
    bestMove = 1
    for key in board.keys():
        if board[key] == '-':
            board[key] = computer
            score = minimax(board, False)
            board[key] = '-'
            if score > bestScore:
                bestScore = score
                bestMove = key
    insertLetter(computer, bestMove)
    return
#######################################
def minimax(board, isMaximizing):   
    if checkWin(computer):
        return 1
    elif checkWin(player):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -800
        for key in board.keys():
            if board[key] == '-':
                board[key] = computer
                score = minimax(board, False)
                board[key] = '-'
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 800
        for key in board.keys():
            if board[key] == '-':
                board[key] = player
                score = minimax(board, True)
                board[key] = '-'
                bestScore = min(score, bestScore)
        return bestScore
#######################################
while not checkWin(computer) and not checkWin(player):
    playerMove()    
    compMove()