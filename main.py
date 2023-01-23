import random
import matplotlib.pyplot as plt
from board import Board
from car import Car

from solve import RandomSolver, BreadthSolver

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
    # count_list = []
    # lijst = list(range(1,101))
    # oplossingen = []
    # for i in range(100):
    board = load_file("gameboards/Rushhour6x6_3.csv")
    board.create_board()
    # solver = RandomSolver(board)
    solver = BreadthSolver(board)
    print(board)
    board = solver.do_move()

    if board.is_won():
        print(f"You have won in {len(board.moves)} sets!!")
        print(board)
        print(board.moves)

    # plt.bar(lijst, count_list, color = ['blue', 'red'])
    # plt.title("Histogram Random")
    # plt.xlabel("Oplossingen")
    # plt.ylabel("Aantal zetten")
    # plt.xlim(1,100)
    # plt.ylim(0, 50000)
    # plt.savefig("Histogram/Histogram3.png")

