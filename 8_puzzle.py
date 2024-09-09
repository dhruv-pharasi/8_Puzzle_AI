'''
The moves in this 8 puzzle are not according to the empty cell, but
according to the values surrounding the empty cell. 

For example, if the move is up, the empty cell would not move up,
but the number below the empty cell will move up. 

To move up, there must be atleast one row below the empty cell, so the condition: 
empty cell row < total rows - 1 (to account for 0-indexing)

To move down, there must be atleast one row above the empty cell, so the condition:
0 < empty cell row 

Similar conditions for moving left and right apply

'''

from copy import deepcopy
import heapq
from sys import argv, exit

class Board:
    def __init__(self, board_state: list[list[int]]):
        self.board_state = board_state

    def __lt__(self, other):
        '''Compare board objects based on their heuristic value'''
        return self.heuristic_value() < other.heuristic_value()

    def legal_moves(self) -> str:
        '''Gives all legal moves for the current board state.'''
        board = self.board_state
        rows, cols = len(self.board_state), len(self.board_state[0])

        # Find the position of the empty cell (-1)
        empty_row, empty_col = [(r, c) for r in range(rows) for c in range(cols) if board[r][c] == -1][0]
        
        # Initialize an empty list to store valid moves
        moves = []
        
        # Check the available moves based on the position of the empty cell
        if empty_row < rows - 1:  # Can move up
            moves.append('u')
        if 0 < empty_row:  # Can move down
            moves.append('d')
        if empty_col < cols - 1:  # Can move left
            moves.append('l')
        if 0 < empty_col:  # Can move right
            moves.append('r')
        
        # return the available legal moves
        return moves

    def make_move(self, move: str):
        moves = self.legal_moves()
        board = self.board_state
        row, col = [(i, j) for i in range(len(self.board_state)) for j in range(len(self.board_state[i])) if self.board_state[i][j] == -1][0]

        if move.strip().lower() == 'd' and 'd' in moves:
            # column unchanged; row = row - 1
            board[row][col], board[row - 1][col] = board[row - 1][col], board[row][col]

        elif move.strip().lower() == 'u' and 'u' in moves:
            # column unchanged; row = row + 1
            board[row][col], board[row + 1][col] = board[row + 1][col], board[row][col]

        elif move.strip().lower() == 'l' and 'l' in moves:
            # row unchanged; column = column + 1
            board[row][col], board[row][col + 1] = board[row][col + 1], board[row][col]

        elif move.strip().lower() == 'r' and 'r' in moves:
            # row unchanged; column = column - 1
            board[row][col], board[row][col - 1] = board[row][col - 1], board[row][col]

        else:
            print("Invalid move!")
            return -1
        
        return 1
        
    def draw(self):
        for row in self.board_state:
            print(" | ".join(str(cell) if cell != -1 else ' ' for cell in row))
            print("-" * 9)

    def heuristic_value(self) -> int:
        '''Number of misplaced values is the heuristic value.
        So lesser the heuristic, the better the partial solution'''
        goal_state = [[1,2,3],[4,5,6],[7,8,-1]]
        val = 0

        for i in range(len(goal_state)):
            for j in range(len(goal_state[0])):
                if self.board_state[i][j] != goal_state[i][j]:
                    val += 1

        return val

def bfs(queue: list[Board]):
    visited = set()  # Track visited board states
    
    while queue:
        board = queue.pop(0)

        if board.board_state == [[1,2,3],[4,5,6],[7,8,-1]]:
            return board
        
        visited.add(tuple(tuple(row) for row in board.board_state))  # Mark current state as visited
        
        moves = board.legal_moves()
        
        # Extract children of parent node
        for move in moves:
            new_board = deepcopy(board)
            new_board.make_move(move)
            
            # Only add to queue if the state hasn't been visited
            if tuple(tuple(row) for row in new_board.board_state) not in visited:
                queue.append(new_board)
        
        print('\n')
        board.draw()

    return None

def dfs(stack: list[Board]):
    visited = set()

    while stack:
        board = stack.pop(0)

        if board.board_state == [[1,2,3],[4,5,6],[7,8,-1]]:
            return board
        
        visited.add(tuple(tuple(row) for row in board.board_state))  # Mark current state as visited
        
        moves = board.legal_moves()
        
        # Extract children of parent node
        for move in moves:
            new_board = deepcopy(board)
            new_board.make_move(move)
            
            # Only add to stack if the state hasn't been visited
            if tuple(tuple(row) for row in new_board.board_state) not in visited:
                stack = [new_board] + stack
        
        print('\n')
        board.draw()

    return None

def best_first_search(queue: list[tuple[Board, int]]):
    '''Uses heuristic value to speed up the search.'''
    visited = set() # Track visited board states
    heapq.heapify(queue)    # Treat python list as a heap

    while queue:
        board_tuple = heapq.heappop(queue)  # Pop the board with the least heuristic value
        board = board_tuple[0]

        if board.board_state == [[1,2,3],[4,5,6],[7,8,-1]]:
            return board
        
        visited.add(tuple(tuple(row) for row in board.board_state))  # Mark current state as visited
        
        moves = board.legal_moves()
        
        # Extract children of parent node
        for move in moves:
            new_board = deepcopy(board)
            new_board.make_move(move)

            if tuple(tuple(row) for row in new_board.board_state) not in visited:
                heapq.heappush(queue, (new_board, new_board.heuristic_value()))  # Add child to priority queue

        print('\n')
        board.draw()
        
    return None



board = Board([
            [8, 6, 7],
            [5, 2, 1],
            [3, 4, -1]
        ])


# 0 for breadth first search
# 1 for depth first search
# 2 for best first search

if len(argv) != 2:
    print(f"\nUsage: python3 8_puzzle.py <mode>\n\n0 for breadth first search\n1 for depth first search \n2 for best first search")
    exit(1)

if argv[1] == '0':
    result = bfs([board])
if argv[1] == '1':
    result = dfs([board])
if argv[1] == '2':
    result = best_first_search([(board, board.heuristic_value())])

if not result:
    print("Puzzle is unsolvable!")
    exit(0)

result.draw()
print("\nPuzzle solved!\n")

