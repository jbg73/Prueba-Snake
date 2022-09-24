import copy

PossibleDirs = ['L', 'R', 'D', 'U']
FoundPaths = 0


## Movement is applied to the head, the rest of elements move one step ahead 

# Moves Snake left (fil, col-1)
def moveLeft(snake):
    for i in range(len(snake)-1, 0, -1):
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
    snake[0][1] -= 1
    return snake

# Moves Snake right (fil, col+1)
def moveRight(snake):
    for i in range(len(snake)-1, 0, -1):
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
    snake[0][1] += 1
    return snake

# Moves Snake down (fil+1, col)
def moveDown(snake):
    for i in range(len(snake)-1, 0, -1):
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
    snake[0][0] += 1
    return snake

# Moves Snake up (fil-1, col)
def moveUp(snake):
    for i in range(len(snake)-1, 0, -1):
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
    snake[0][0] -= 1
    return snake

# Checks if a movement in 'move' direction is allowed (No crossing borders nor colliding with itself)
def MovementAllowed(move, snake, board):
    if move == 'L':
        if snake[0][1] - 1 >= 0 and [snake[0][0], snake[0][1] - 1] not in snake[:len(snake)-1]:
            return True
        else: 
            return False

    elif move == 'R':
        if snake[0][1] + 1 < board[1] and [snake[0][0], snake[0][1] + 1] not in snake[:len(snake)-1]:
            return True
        else:
            return False

    elif move == 'D':
        if snake [0][0] + 1 < board[0] and [snake[0][0] + 1, snake[0][1]] not in snake[:len(snake)-1]:
            return True
        else:
            return False

    elif move == 'U':
        if snake[0][0] -1 >= 0 and [snake[0][0] - 1, snake[0][1]] not in snake[:len(snake)-1]:
            return True
        else:
            return False
    return True

# Applies the movement in direction 'dir'
def ApplyMovement(dir, snake):
    snake2Move = copy.deepcopy(snake)
    if dir == 'L':
        return moveLeft(snake2Move)
    elif dir == 'R':
        return moveRight(snake2Move)
    elif dir == 'D':
        return moveDown(snake2Move)
    elif dir == 'U':
        return moveUp(snake2Move)
           
# Backtracking function. At each position, tries to go to every direction until the path reaches size depth, then returns
def PossiblePaths(board, snake, depth, currentSize):
    if currentSize == depth:
        global FoundPaths
        FoundPaths += 1
        return 
    
    for dir in PossibleDirs:
        if MovementAllowed(dir, snake, board): 
            PossiblePaths(board, ApplyMovement(dir,snake), depth, currentSize + 1)

    return FoundPaths

# Shows the current state of the board with the snake on it. Helps visualizing the movements. 
def showBoard(board, snake):
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    for i in range(board[0]):
        for j in range(board[1]):
            if [i,j] in snake:
                print(snake.index([i,j]), end = " ")
            else:
                print("_", end = " ")
        print("\n")

def main():
    print("---Snake Problem---")
    snake_org = [[2,1], [1,1], [0,1], [0,0]]
    board = [3,3]
    depth = 2
    showBoard(board, snake_org)
    TEST1 = PossiblePaths(board, snake_org, depth, 0)
    print("TEST 1 ANSWER: ", TEST1)
if __name__ == '__main__':
    main()