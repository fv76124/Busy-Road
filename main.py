from grid import Grid
from car import Car
            
if __name__ == "__main__":
    board = Grid()
    board.create_board()
    print(board)
    
    
    list = Car()
    list.load_file(f"gameboards/Rushhour6x6_1.csv")
    print(list)