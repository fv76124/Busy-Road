from car import Car
import random

""" creates class for the grid """
class Board():
    def __init__(self):
        self.grid = []
        self.cor_car = []
        
    """ method that creates a board with only zero's """
    def create_board(self):
        for column in range(6):
            self.grid.append([])
            for row in range (6):
                self.grid[column].append('0')
                
    """ takes the file from the car class and reads the information from the car and puts it into a list """
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

    """ inserts the cars into the empty grid """
    # def insert_car(self):
    #     colors = [0,2,3,4,5,6]

    #     for column in range(len(self.grid) + 1):
    #         for row in range(len(self.grid[0]) + 1):
    #             for line in range(len(self.cor_car)):
    #                 if [column, row] == self.cor_car[line][1]:
    #                     self.grid[row - 1][column - 1] = f'\033[1;3{colors[line % 6]};40m{self.cor_car[line][0]}'
    #                 if [column, row] == self.cor_car[line][2]:
    #                     self.grid[row -1][column -1] = f'\033[1;3{colors[line % 6]};40m{self.cor_car[line][0]}'
    #                 if len(self.cor_car[line]) > 3:
    #                     if [column, row] == self.cor_car[line][3]:
    #                         self.grid[row - 1][column - 1] = f'\033[1;3{colors[line % 6]};40m{self.cor_car[line][0]}'
    #                 if self.grid[column - 1][row - 1] == '0':
    #                     self.grid[column - 1][row - 1] = f'\033[1;37;40m{self.grid[column - 1][row - 1]}'
    #                 if self.cor_car[line][0] == 'X':
    #                     self.cor_car[line][0] = f'\033[1;31;40m{self.cor_car[line][0]}'
    
    def insert_car(self):

        for column in range(len(self.grid) + 1):
            for row in range(len(self.grid[0]) + 1):
                for line in range(len(self.cor_car)):
                    if [column, row] == self.cor_car[line][1]:
                        self.grid[row - 1][column - 1] = self.cor_car[line][0]
                    if [column, row] == self.cor_car[line][2]:
                        self.grid[row -1][column -1] = self.cor_car[line][0]
                    if len(self.cor_car[line]) > 3:
                        if [column, row] == self.cor_car[line][3]:
                            self.grid[row - 1][column - 1] = self.cor_car[line][0]
                    if self.grid[column - 1][row - 1] == '0':
                        self.grid[column - 1][row - 1] = self.grid[column - 1][row - 1]
                    if self.cor_car[line][0] == 'X':
                        self.cor_car[line][0] = self.cor_car[line][0]

    def move_car(self):
        
        # eind doel: rode auto [row 3][colom 5 en 6], dus doe de conditie tot dit zo is

        # while self.cor_car[12][2] != self.grid[5][3]:
        rand_car = random.choice(self.cor_car)


        print(rand_car[0])
        print(rand_car[1])
        print(rand_car[2])
            # verticaal
        column1 = rand_car[1][0]
        # print(column1)
        column2 = rand_car[2][0]
        # print(column2)
        row1 = rand_car[1][1]
        # print(row1)
        row2 = rand_car[2][1]
        # print(row2)
        
        # if self.grid[row1 - 2][column1 -1] != None or self.grid[row2][column2 -1] != None or self.grid[row1 - 1][column1 - 2] != None or self.grid[row2 + 1][column2 + 2] != None:
        # verticaal
        if column1 == column2:
            # kijken of hij omhoog kan
            if self.grid[row1 -2][column1 -1] == "0":
                self.grid[row1 -2][column1 - 1] = rand_car[0]
                print(self.grid[row1 -2][column1 -1])
                self.grid[row2 - 1][column2 - 1] = "0"
                print(self.grid[row2 - 1][column1 -1]) 
            # kijken of hij omlaag kan
            elif self.grid[row2][column2 - 1] == "0":
                self.grid[row2][column2 -1] = rand_car[0]
                print(self.grid[row2][column2 + 1])
                self.grid[row2 -2][column2 -1] = "0"
                print(self.grid[row2 -2][column2 -1]) 
            else:
                return 0
    
        #horizontaal
        elif row1 == row2:
            # kijken of hij naar links kan
            if self.grid[row1 - 1][column1 - 2] == "0":
                self.grid[row1 - 1][column1 - 2] = rand_car[0]
                print(self.grid[row1 - 1][column1 - 2])
                self.grid[row2 - 1][column2 - 1] = "0"
                print(self.grid[row2 - 1][column1 - 1])
                # kijken of hij naar rechts kan 
            elif self.grid[row2 + 1][column2 + 2] == "0":
                self.grid[row2 + 1][column2 + 2] = rand_car[0]
                print(self.grid[row2 + 1][column2 + 2])
                self.grid[row2 + 1][column2 + 1] = "0"
                print(self.grid[row2 + 1][column2 + 1]) 
            else:
                return 0
        else:
            return 0


        
        # auto kan alleen, afhankelijk van zijn orientatie, verplaatsen naar 0 boven of opzij ervan
        # auto kan alleen naar 0 in dezelfde lijn
        # auto kan niet buiten de grid
        # Zodra auto verplaatst is, moeten de oude coordinaten een 0 worden
        # Als er twee 0 boven en onder staan moet je random de 0 kiezen
    """ creates empty grid if new file needs to be loaded """
    def empty_grid(self):
        for column in range(len(self.grid)):
            for row in range(len(self.grid[0])):
                self.grid[column][row] = 0

    """ inserts enter after every line to create an actual grid """
    def __str__(self) -> str:
        line = ""
        
        for row in self.grid:
            for char in row:
                line += str(char) + " "
            line += "\n"

        return line.strip()

    """ string rerpesentation """
    def __repr__(self) -> str:
        return f'{self.grid}'
