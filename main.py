import random
import matplotlib.pyplot as plt
from board import Board
from car import Car
import time

from solve import RandomSolver

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
    counter = 0
    # count_list = []
    # lijst = list(range(1,101))
    # oplossingen = []
    # for i in range(100):
    board = load_file("gameboards/Rushhour9x9_5.csv")
    board.create_board()
    solver = RandomSolver(board)
    print(board)
    while True:
        counter += 1
        board = solver.do_move()

            # time.sleep(0.5)
            # print("----------")
        if board.is_won():
            print(f"You have won in {counter} sets!!")
            print(board)
            break
    #     count_list.append(counter)
    #     counter = 0
    
    # plt.bar(lijst, count_list, color = ['blue', 'red'])
    # plt.title("Histogram Random")
    # plt.xlabel("Oplossingen")
    # plt.ylabel("Aantal zetten")
    # plt.xlim(1,100)
    # plt.ylim(0, 50000)
    # plt.savefig("Histogram/Histogram3.png")

