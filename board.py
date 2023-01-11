from car import Car

""" creates class for the grid """
class Board():
    def __init__(self):
        self.grid = []
        
    def create_board(self):
        for column in range (6):
            self.grid.append([])
            for row in range (6):
                self.grid[column].append('0')             
                
    def insert_car(self):
        for line in range(len(Car().position)):
            if Car().position[line][1] == 'H':
                name = str(Car().position[line][0])
                length = str(Car().position[line][4])
                x = int((Car().position[line][2]))
                y = int((Car().position[line][3]))
                if length == '2':
                    cor1 = (x, y)
                    cor2 = (x + 1, y)
                    print(cor1, cor2)
                elif length == '3':
                    cor1 = (x, y)
                    cor2 = (x + 1, y)
                    cor3 = (x + 2, y)
                    car = (cor1, cor2, cor3)
            elif Car().position[line][1] == 'V':
                name = str(Car().position[line][0])
                x = int((Car().position[line][2]))
                y = int((Car().position[line][3]))
                if length == '2':
                    cor1 = (x, y)
                    cor2 = (x, y + 1)
                    print(cor1, cor2)
                elif length == '3':
                    cor1 = (x, y)
                    cor2 = (x, y + 1)
                    cor3 = (x, y + 2)
                    print(cor1, cor2, cor3)
        
    def empty_grid(self):
        for column in range(len(self.grid)):
            for row in range(len(self.grid[0])):
                self.grid[column][row] = 0

    def __str__(self) -> str:
        # inserts enter after every line to create an actual grid
        line = ""

        for row in self.grid:
            for char in row:
                line += char + " "
            line += "\n"

        return line.strip()
    
    def __repr__(self) -> str:
        """String representation""" 
        
        return f'{Board()}'
    
