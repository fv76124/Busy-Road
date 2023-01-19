import copy

from board import *

""" Class for the cars """
class Car():

    def __init__(self, name: str, orientation: str, column: int, row: int, length: int):
        self.name = name
        
        # creates list with all coordinates based on the length and orientation
        self.coordinates = []
        
        self.orientation = orientation

        if orientation == 'H':
            for i in range(length):
                self.coordinates.append([column + i, row])
        if orientation == 'V':
            for i in range(length):
                self.coordinates.append([column, row + i])
                
    """ moves the car """
    def move(self, cd: int) -> int:
        if self.orientation == 'H':
            coordinate_to_move = 0 
        else:
            coordinate_to_move = 1
            
        for cor in self.coordinates:
            cor[coordinate_to_move] += cd

    """ gets the coordinates of the part that moves the car (front or back coordinates)"""  
    def get_front_coordinate(self, cd: int) -> int:
        if cd < 0:
            return self.coordinates[0].copy()
        else:
            return self.coordinates[len(self.coordinates) - 1].copy()

    """String representation"""
    def __repr__(self) -> str:
        return self.name