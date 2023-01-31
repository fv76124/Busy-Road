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
<<<<<<< HEAD:main.py
    board = load_file("gameboards/Rushhour9x9_5.csv")
=======
    board = load_file("gameboards/Rushhour6x6_1.csv")
>>>>>>> 51b89e9eb76d0a925a9cd9539fec6b068b4ca8f2:code/main.py
    board.create_board()
    # solver = RandomSolver(board)
    # solver = BreadthSolver(board)
    solver = DepthSolver(board)
    board = solver.do_move()
    
    # print sets and board if won
    if board.is_won():
        print(f"You have won in {len(board.moves)} sets!!")
        # print(board)
        print(board.moves)
        
        # print all boards once winning board is found
        start_board = load_file("gameboards/Rushhour9x9_5.csv")
        start_board.create_board()
        print(start_board)
        print("------")
        for move in board.moves:
            start_board.move_car(start_board.cars[move[0]], move[1])
            print(start_board)
            print("-------")
    
    
    

    # # for histogram
    # count_list = []
    # lijst = list(range(1,101))
    # oplossingen = []
    # for i in range(100):
    # solver.possible_moves(board)
        
    # # for histogram
    # plt.bar(lijst, count_list, color = ['blue', 'red'])
    # plt.title("Histogram Random")
    # plt.xlabel("Oplossingen")
    # plt.ylabel("Aantal zetten")
    # plt.xlim(1,100)
    # plt.ylim(0, 50000)
    # plt.savefig("Histogram/Histogram3.png")

