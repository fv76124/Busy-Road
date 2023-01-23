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

    """ checks all possible moves """
    def possible_moves(self, board):
        all_moves = []
        for car in board.cars.values():
            for cd in [-1, 1]:
                while board.can_move(car, cd):
                    all_moves.append([car, cd])
        return all_moves
    
    """ does all moves until the queue is emtpy or board is won"""    
    def do_move(self):
        while not self.empty():
            board = self.move_queue.pop(0)
            if board.is_won():
                return board

            for move in self.possible_moves(board):
                child = copy.deepcopy(board)
                child.move_car(child.cars[move[0].name], move[1])

    """ checks if queue is emtpy """        
    def empty(self):
        if len(self.move_queue) > 0:
            return False
        else:
            return True