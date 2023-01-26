import copy
from typing import Optional, List
from colorama import *
from car import Car
import random

""" creates class for the grid """
class Board:
    def __init__(self, cars):
        # dictionary for cars, name is key and car is value
        self.cars = {}
        for car in cars:
            self.cars[car.name] = car

        # empty list for the grid 
        self.grid = []

        # empty dict for colours
        self.colour_dict = {}

        # empty list for the made moves
        self.moves = []

    """ method that creates a board with None and appends the car to the set coordinates """
    def create_board(self):
        for column in range(9):
            self.grid.append([])
            for row in range(9):
                self.grid[column].append(None)

        for car in self.cars.values():
            for position in car.coordinates:
                self.set_position(position, car)
                
    """ method to check if new positions of car is within the grid """
    def range(self, position: list) -> bool:
        if position[0] < len(self.grid[0]) and position[0] >= 0 and position[1] < len(self.grid) and position[1] >= 0:
            return True
        else:
            return False

    """ returns the name of a car based on the given coordinates"""
    def at(self, x: int, y: int) -> Optional[Car]:
        return self.grid[y][x]

    """ returns position (coordinates) of the car """
    def at_position(self, position: List) -> Optional[Car]:
        return self.at(position[0], position[1])
            
    """ saves name of the car at the new coordinates in car """
    def set_position(self, position: List, car: Optional[Car]) -> None:
        self.grid[position[1]][position[0]] = car
        
    """ checks if the given car can move """
    def can_move(self, car: Car, cd: int) -> bool:
        # saves last move as nothing
        last_move = None
        
        # returns last item of moves list (so the last move)
        if len(self.moves) > 0:
            last_move = self.moves[len(self.moves) - 1]

        # saves opposite direction of last moved car, makes sure car does not move back straight away
        if last_move is not None:
            if car.name == last_move[0]:
                if last_move[1] == 1:
                    opposite_direction = -1
                else:
                    opposite_direction = 1
                if cd == opposite_direction:
                    return False
                
        # gets front or back coordinate that can move
        car_front_coordinate = car.get_front_coordinate(cd)
        
        # if horizontal, get column and moves -1 or +1 otherwise get row
        if car.orientation == 'H':
            car_front_coordinate[0] += cd
        else:
            car_front_coordinate[1] += cd
            
        # return true if new coordinates stay within the range of grid and the cordinate is empty (None)
        if self.range(car_front_coordinate) and self.at_position(car_front_coordinate) is None:
            return True
        else:
            return

    """ method to move the given car based on old coordinates and new coordinates position """
    def move_car(self, car: Car, cd: int) -> None:
        # make deep copy of the coordinates
        old_coordinates = copy.deepcopy(car.coordinates)

        car.move(cd)
        
        # set old coordinate to None and car to new coordinates, and add the move to the moves list
        for cor in old_coordinates:
            self.set_position(cor, None)
        for cor in car.coordinates:
            self.set_position(cor, car)
        self.moves.append([car.name, cd])
    

        
    """ checks if the X car is in winning position /different solutios per grid """
    def is_won(self) -> bool:
        # for a 6x6 grid
        # car = self.at(5, 2)
        # if car is not None and car.name == 'X':
        #     return True
        # return False
    
        # for a 9x9 grid
        car = self.at(8, 4)
        if car is not None and car.name == 'X':
            return True
        return False

        # # for a 12x12 grid
        # car = self.at(11, 5)
        # if car is not None and car.name == 'X':
        #     return True
        # return False
    
    """ inserts enter after every line to create an actual grid """
    def __str__(self) -> str:
        line = ""
        red = "\033[1;31m"
        white = "\033[1;37;40m"
        colour_list = [0, 2, 3, 4, 5, 6]
        colour = 0
        for row in self.grid:
                for char in row:
                    c = '0' if char is None else str(char)
                    if c == 'X':
                        c = red+c
                    elif c == '0':
                        c = white+c
                    elif c not in self.colour_dict:
                        self.colour_dict[c] = f'\033[1;3{colour_list[colour % 6]};40m'+c
                        c = self.colour_dict[c]
                        colour += 1
                    else:
                        c = self.colour_dict[c]
                    line += c + " "
                line += "\n"

        return line.strip()

    """ string rerpesentation """
    def __repr__(self) -> str:
        return f'{self.grid}'
