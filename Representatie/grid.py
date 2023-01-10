""" creates class for the grid """
class Grid():
    def __init__(self):
        self.grid = []
        element = "-"
        for column in range (1, 7):
            for row in range (1, 7):
                self.grid.append(element)
    
    def __repr__(self):
        return f'{self.grid}'