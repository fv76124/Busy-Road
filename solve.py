import random, copy

from board import Board

""" random solver algorithm"""
class RandomSolver:
    def __init__(self, board: Board):
        self.board = board

    """ method to do all moves """
    def do_move(self) -> Board:
        
        while True:
            # makes list of all moves based on if car position -1 +1 can do the move
            all_moves = []
            for car in self.board.cars.values():
                for cd in [-1, 1]:
                    if self.board.can_move(car, cd):
                        all_moves.append([car, cd])
                        
            if self.board.is_won():
                return self.board
                    
        # randomly pick a move from all possible moves
            move = random.choice(all_moves)

            self.board.move_car(move[0], move[1])

""" breadth first algorithm"""
class BreadthSolver:
    
    def __init__(self, board: Board):
        self.board = board
        self.move_queue = [copy.deepcopy(board)]
        self.visited = {}

    """ checks all possible moves """
    def possible_moves(self, board):
        all_moves = []
        for car in board.cars.values():
            for cd in [-1, 1]:
                mult = 1
                while board.can_move(car, cd * mult):
                    all_moves.append([car, cd * mult])
                    mult += 1
        return all_moves
    
    """ does all moves until the queue is emtpy or board is won"""    
    def do_move(self):
        last_depth = 0
        while len(self.move_queue) > 0:
            board = self.move_queue.pop(0)
            if board.is_won():
                return board
            if len(board.moves) != last_depth:
                last_depth = len(board.moves)
                print("Depth", last_depth)
            
            for move in self.possible_moves(board):
                child = copy.deepcopy(board)
                child.move_car(child.cars[move[0].name], move[1])
                
                # is the copy a visited state? continue, else append to visited and to queue
                if str(child) in self.visited:
                    continue
                else:
                    self.move_queue.append(child)
                    self.visited[str(child)] = True

""" depth first algorithm"""    
class DepthSolver: 
    def __init__(self, board: Board):
        self.board = board
        self.move_stack = [copy.deepcopy(board)]
        self.visited = {}
    
    def possible_moves(self, board):
        all_possible_moves = []
        for car in board.cars.values():
            for cd in [-1, 1]:
                multiple_steps = 1
                while board.can_move(car, cd * multiple_steps):
                    all_possible_moves.append([car, cd * multiple_steps])
                    multiple_steps += 1
        return all_possible_moves 
    
    def do_move(self):
         while not len(self.move_stack) == 0:
            board = self.move_stack.pop()
            if board.is_won():
                return board
            
            if len(board.moves) > 1500:
                continue

            for move in self.possible_moves(board):
                child = copy.deepcopy(board)
                child.move_car(child.cars[move[0].name], move[1])
                
                # is the copy a visited state? continue, else append to visited and to queue
                if str(child) not in self.visited:
                    self.move_stack.append(child)
                    self.visited[str(child)] = True
                else:
                    continue
           