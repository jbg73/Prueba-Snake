
def moveLeft(snake):
    for i in range(len(snake)-1, 0, -1):
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
    snake[0][1] -= 1

def moveRight(snake):
    for i in range(len(snake)-1, 0, -1):
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
    snake[0][1] += 1

def moveDown(snake):
    for i in range(len(snake)-1, 0, -1):
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
    snake[0][0] += 1

def moveUp(snake):
    for i in range(len(snake)-1, 0, -1):
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
    snake[0][0] -= 1

def applyMovement(move, snake, board):
    if move == 'L':
        if snake[0][1] - 1 <= board[1] and [snake[0][0], snake[0][1] - 1] not in snake:
            moveLeft(snake)
        else: 
            print("Cant move left")

    elif move == 'R':
        if snake[0][1] + 1 >= board[1] and [snake[0][0], snake[0][1] + 1] not in snake:
            moveRight(snake)
        else:
            print("Cant move right")

    elif move == 'D':
        if snake [0][0] + 1 <= board[0] and [snake[0][0] + 1, snake[0][1]] not in snake:
            print([snake[0][0]+1, snake[0][1]] not in snake)
            moveDown(snake)
        else:
            print("Cant move down")

    elif move == 'U':
        if snake[0][0] -1 >= board[0] and [snake[0][0] - 1, snake[0][1]] not in snake:
            moveUp(snake)
        else:
            print("Cant move up")


def PossiblePaths(board, snake, depth):
    pass

def showBoard(board, snake):
    for i in range(board[0]):
        for j in range(board[1]):
            if [i,j] in snake:
                print("S", end = " ")
            else:
                print("_", end = " ")
        print("\n")

def main():
    print("---Snake Problem---")
    snake = [[0,1],[0,2], [0,3], [1,3], [1,2], [1,1]]
    board = [6, 5]
    showBoard(board, snake)
    applyMovement('L', snake, board)
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx")
    showBoard(board, snake)
    print("snake after moveLeft: ", snake)
if __name__ == '__main__':
    main()