from board import Board
from car import Car
import time
if __name__ == "__main__":
    # board = Board()
    # board.create_board()
    # print(board)
    counter = 0

    positie = Board()
    positie.create_board()
    positie.cordinates_of_car()
    positie.insert_car()
    while True:
        counter += 1
        positie.move_car()
        time.sleep(1)
        print(positie)
        print("----------")
        if positie.is_won():
            print(f"You have won in {counter} sets!!")
            break

    