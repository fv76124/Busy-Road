""" creates class for the grid """
class Grid():
    def __init__(self):
        self.grid = []
        element = "-"
        for column in range (6):
            self.grid.append([])
            for row in range (6):
                self.grid[column].append(row)
    
    def __repr__(self):
        return f'{self.grid}'