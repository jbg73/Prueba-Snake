import copy
PossibleDirs = ['L', 'R', 'D', 'U']
FoundPaths = 0

def moveLeft(snake):
    for i in range(len(snake)-1, 0, -1):
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
    snake[0][1] -= 1
    return snake

def moveRight(snake):
    for i in range(len(snake)-1, 0, -1):
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
    snake[0][1] += 1
    return snake

def moveDown(snake):
    for i in range(len(snake)-1, 0, -1):
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
    snake[0][0] += 1
    return snake

def moveUp(snake):
    for i in range(len(snake)-1, 0, -1):
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
    snake[0][0] -= 1
    return snake

def applyMovement(move, snake, board):
    if move == 'L':
        if snake[0][1] - 1 >= 0 and [snake[0][0], snake[0][1] - 1] not in snake[:len(snake)-1]:
            # moveLeft(snake)
            return True
        else: 
            return False

    elif move == 'R':
        if snake[0][1] + 1 < board[1] and [snake[0][0], snake[0][1] + 1] not in snake[:len(snake)-1]:
            # moveRight(snake)
            return True
        else:
            return False

    elif move == 'D':
        if snake [0][0] + 1 < board[0] and [snake[0][0] + 1, snake[0][1]] not in snake[:len(snake)-1]:
            # moveDown(snake)
            return True
        else:
            return False

    elif move == 'U':
        if snake[0][0] -1 >= 0 and [snake[0][0] - 1, snake[0][1]] not in snake[:len(snake)-1]:
            # moveUp(snake)
            return True
        else:
            return False

    showBoard(board, snake)
    return True

def snakeMoved(dir, snake):
    snake2Move = copy.deepcopy(snake)
    if dir == 'L':
        return moveLeft(snake2Move)
    elif dir == 'R':
        return moveRight(snake2Move)
    elif dir == 'D':
        return moveDown(snake2Move)
    elif dir == 'U':
        return moveUp(snake2Move)
           

def PossiblePaths(board, snake, depth, currentSize):
    showBoard(board, snake)
    if currentSize == depth:
        global FoundPaths
        FoundPaths += 1
        return 
    
    for dir in PossibleDirs:
        if applyMovement(dir, snake, board): 
            PossiblePaths(board, snakeMoved(dir,snake), depth, currentSize + 1)

    return FoundPaths

def showBoard(board, snake):
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx")
    for i in range(board[0]):
        for j in range(board[1]):
            if [i,j] in snake:
                print(snake.index([i,j]), end = " ")
            else:
                print("_", end = " ")
        print("\n")

def main():
    print("---Snake Problem---")
    snake_org = [[5,5], [5,4], [4,4], [4,5]]
    board = [10, 10]
    depth = 4
    showBoard(board, snake_org)
    TEST1 = PossiblePaths(board, snake_org, depth, 0)
    print("TEST 1 ANSWER: ", TEST1)
if __name__ == '__main__':
    main()