import copy

PossibleDirs = ['L', 'R', 'D', 'U']
FoundPaths = 0
CurrentSize = 0

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
def PossiblePaths(board, snake, depth):
    global CurrentSize
    if CurrentSize == depth:
        CurrentSize -= 1
        global FoundPaths
        FoundPaths += 1
        return 
    
    for dir in PossibleDirs:
        if MovementAllowed(dir, snake, board):
            CurrentSize += 1 
            PossiblePaths(board, ApplyMovement(dir,snake), depth)

    CurrentSize -= 1
    return FoundPaths

# Shows the current state of the board with the snake on it. Helps visualizing the movements. 
# Not needed when eve
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
    global FoundPaths
    global CurrentSize
    #---------------
    board_1 =  [4, 3]
    snake_org_1 = [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
    depth_1 = 3
    #---------------
    board_2 =  [2, 3]
    snake_org_2 = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
    depth_2 = 10
    #---------------
    board_3 =  [10, 10]
    snake_org_3 =  [[5,5], [5,4], [4,4], [4,5]]
    depth_3 =  4
    #---------------

    TEST1 = PossiblePaths(board_1, snake_org_1, depth_1)
    FoundPaths = 0
    CurrentSize = 0
    TEST2 = PossiblePaths(board_2, snake_org_2, depth_2)
    FoundPaths = 0
    CurrentSize = 0
    TEST3 = PossiblePaths(board_3, snake_org_3, depth_3)
    FoundPaths = 0
    CurrentSize = 0

    print("TEST 1:")
    showBoard(board_1, snake_org_1)
    print("TEST 1 ANSWER: ", TEST1)

    print("\n\nTEST 2: ")
    showBoard(board_2, snake_org_2)
    print("TEST 2 ANSWER: ", TEST2)

    print("\n\nTEST 3: ")
    showBoard(board_3, snake_org_3)
    print("TEST 3 ANSWER: ", TEST3)

if __name__ == '__main__':
    main()