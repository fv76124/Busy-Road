from car import Car

""" creates class for the grid """
class Board():
    def __init__(self):
        self.grid = []
        self.cor_car = []

    def create_board(self):
        for column in range(6):
            # print("hoi")
            self.grid.append([])
            for row in range (6):
                self.grid[column].append('0')

    def cordinates_of_car(self):
        cor_car = []
        for line in range(len(Car().position)):
            if Car().position[line][1] == 'H':
                name = str(Car().position[line][0])
                length = str(Car().position[line][4])
                x = int((Car().position[line][2]))
                y = int((Car().position[line][3]))
                if length == '2':
                    cor1 = [x, y]
                    cor2 = [x + 1, y]
                    cor_car.append([name, cor1, cor2])
                elif length == '3':
                    cor1 = [x, y]
                    cor2 = [x + 1, y]
                    cor3 = [x + 2, y]
                    cor_car.append([name, cor1, cor2, cor3])
            elif Car().position[line][1] == 'V':
                name = str(Car().position[line][0])
                x = int((Car().position[line][2]))
                y = int((Car().position[line][3]))
                if length == '2':
                    cor1 = [x, y]
                    cor2 = [x, y + 1]
                    cor_car.append([name, cor1, cor2])
                elif length == '3':
                    cor1 = [x, y]
                    cor2 = [x, y + 1]
                    cor3 = [x, y + 2]
                    cor_car.append([name, cor1, cor2, cor3])
        self.cor_car = cor_car

    def insert_car(self):
        for column in range(len(self.grid) + 1):
            for row in range(len(self.grid[0]) + 1):
                for line in range(len(self.cor_car)):
                    print(len(self.cor_car))
                    if [column, row] == self.cor_car[line][1]:
                        self.grid[row -1][column -1] = self.cor_car[line][0]
                    if [column, row] == self.cor_car[line][2]:
                        self.grid[row -1][column -1] = self.cor_car[line][0]
                        print(len(self.cor_car[line]))
                        # if len(self.cor_car[line]) == 3:
                        #     if [column, row] == self.cor_car[line][3]:
                        #         self.grid[row - 1][column - 1] = self.cor_car[line][0]

    def empty_grid(self):
        for column in range(len(self.grid)):
            for row in range(len(self.grid[0])):
                self.grid[column][row] = 0

    def __str__(self) -> str:
        # inserts enter after every line to create an actual grid
        line = ""

        for row in self.grid:
            for char in row:
                line += str(char) + " "
            line += "\n"

        return line.strip()

    def __repr__(self) -> str:
        """String representation"""

        return f'{self.grid}'
