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
