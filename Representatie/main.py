from grid import Grid

def load_file(filename):
    """ reads the file """
    with open(filename) as file:
        header = file.readline
        for line in file:
            set = line.split(',')
            car = set[0]
            orientation = set[1]
            column = set[2]
            row = set[3]
            length = set[4]

if __name__ == "__main__":
    board = Grid()
    board.create_board()
    print(board)
