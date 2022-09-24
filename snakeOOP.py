import copy

class SnakeTask():
    def __init__(self):
        self.__current_size = 0
        self.found_paths = 0
        self.__possible_dirs = ['L', 'R', 'D', 'U']

    def moveLeft(self, snake):
        for i in range(len(snake)-1, 0, -1):
            snake[i][0] = snake[i-1][0]
            snake[i][1] = snake[i-1][1]
        snake[0][1] -= 1
        return snake

    def moveRight(self, snake):
        for i in range(len(snake)-1, 0, -1):
            snake[i][0] = snake[i-1][0]
            snake[i][1] = snake[i-1][1]
        snake[0][1] += 1
        return snake

    def moveDown(self, snake):
        for i in range(len(snake)-1, 0, -1):
            snake[i][0] = snake[i-1][0]
            snake[i][1] = snake[i-1][1]
        snake[0][0] += 1
        return snake

    def moveUp(self, snake):
        for i in range(len(snake)-1, 0, -1):
            snake[i][0] = snake[i-1][0]
            snake[i][1] = snake[i-1][1]
        snake[0][0] -= 1
        return snake

    def MovementAllowed(self, move, snake, board):
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

    def ApplyMovement(self, dir, snake):
        snake2Move = copy.deepcopy(snake)
        if dir == 'L':
            return self.moveLeft(snake2Move)
        elif dir == 'R':
            return self.moveRight(snake2Move)
        elif dir == 'D':
            return self.moveDown(snake2Move)
        elif dir == 'U':
            return self.moveUp(snake2Move)

    def showBoard(self, board, snake):
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        for i in range(board[0]):
            for j in range(board[1]):
                if [i,j] in snake:
                    print(snake.index([i,j]), end = " ")
                else:
                    print("_", end = " ")
            print("\n")

    def PossiblePaths(self, board, snake, depth):
        if self.__current_size == depth:
            self.__current_size -= 1
            self.found_paths += 1
            return 
        
        for dir in self.__possible_dirs:
            if self.MovementAllowed(dir, snake, board):
                self.__current_size += 1 
                self.PossiblePaths(board, self.ApplyMovement(dir,snake), depth)

        self.__current_size -= 1
        return self.found_paths

def main():
    print("---Snake Problem---")

    board_1 = [4, 3]
    snake_org_1 = [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
    depth_1 = 3
    #-----------
    board_2 = [2, 3]
    snake_org_2 = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
    depth_2 = 10
    #-----------
    board_3 = [10, 10]
    snake_org_3 = [[5,5], [5,4], [4,4], [4,5]]
    depth_3 = 4
    #-----------

    print("TEST 1")
    snakeObject1 = SnakeTask()
    snakeObject1.showBoard(board_1, snake_org_1)
    snakeObject1.PossiblePaths(board_1, snake_org_1, depth_1)
    print("TEST 1 RESULT: ", snakeObject1.found_paths)

    print("\n\nTEST 2")
    snakeObject2 = SnakeTask()
    snakeObject2.showBoard(board_2, snake_org_2)
    snakeObject2.PossiblePaths(board_2, snake_org_2, depth_2)
    print("TEST 2 RESULT: ", snakeObject2.found_paths)

    print("\n\nTEST 3")
    snakeObject3 = SnakeTask()
    snakeObject3.showBoard(board_3, snake_org_3)
    snakeObject3.PossiblePaths(board_3, snake_org_3, depth_3)
    print("TEST 3 RESULT: ", snakeObject3.found_paths)

if __name__ == '__main__':
    main()