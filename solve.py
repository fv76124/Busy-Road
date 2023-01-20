import random

from board import Board

""" random solver algorithm"""
class RandomSolver:
    def __init__(self, board: Board):
        self.board = board

    """ method to do all moves """
    def do_move(self) -> Board:
        # makes list of all moves based on if car position -1 +1 can do the move
        all_moves = []
        for car in self.board.cars.values():
            for cd in [-1, 1]:
                if self.board.can_move(car, cd):
                    all_moves.append([car, cd])
                    
        # randomly pick a move from all possible moves
        move = random.choice(all_moves)

        self.board.move_car(move[0], move[1])

        return self.board

class BreathSolve:
    def __init__(self, moves, board: Board):
        self.board = board
        self.dict = {}
        self.queue = []
        self.visited = moves

    def breath(self):
        #coordinates car nodig
        #coordinates grid nodig
        #kijken of hij naar rechts of links kan en dan toevoegen in lijst
        pass