""" creates class for the grid """
class Grid():
    def __init__(self):
        self.grid = []
        
    def create_grid(self):
        """ Generates a board based on a 6x6 grid """
        for column in range(1, 6):
            for row in range (1, 6):
                self.grid[column][row].append("-")

    def __repr__(self):
        return f'{self.grid}'