import random
import matplotlib.pyplot as plt
from board import Board
from car import Car

from solve import RandomSolver, BreadthSolver, DepthSolver

# load file 
def load_file(filename: str) -> Board:
    cars = []
    with open(filename) as file:
        header = file.readline()
        for line in file:
            car_info = line.split(',')
            car = car_info[0]
            orientation = car_info[1]
            column = int(car_info[2]) - 1
            row = int(car_info[3]) - 1
            length = int(car_info[4].strip("\n"))
            cars.append(Car(car, orientation, column, row, length))

    return Board(cars)

if __name__ == "__main__":
    random.seed()
    board = load_file("gameboards/Rushhour6x6_3.csv")
    board.create_board()
    # solver = RandomSolver(board)
    solver = BreadthSolver(board)
    # solver = DepthSolver(board)
    board = solver.do_move()
    
    # print sets and board if won
    if board.is_won():
        print(f"You have won in {len(board.moves)} sets!!")
        print(board)
        # print(board.moves)

        # # print all boards once winning board is found
        # start_board = load_file("gameboards/Rushhour9x9_5.csv")
        # start_board.create_board()
        # print(start_board)
        # print("------")
        # for move in board.moves:
        #     start_board.move_car(start_board.cars[move[0]], move[1])
        #     print(start_board)
        #     print("-------")

    # # for histogram
    # count_list = [33, 1433, 21000]
    # lijst = [1, 2, 3]
    # oplossingen = []
    # for i in range(100):
    # solver.possible_moves(board)
    # tick_label = ["Breadth First", "Depth First", "Random"]
    # # for histogram
    # plt.bar(lijst, count_list, tick_label = tick_label, width = 0.8, color = ['blue'])

    # plt.title("Grafiek game 3")
    # plt.xlabel("Algoritmes")
    # plt.ylabel("Aantal zetten")
    # plt.savefig("Histogram/Grafiek Game 3.png")

