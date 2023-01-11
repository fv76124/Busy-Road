""" creates class for the grid """
class Grid():
    def __init__(self):
        self.grid = []
    
    def create_board(self):
        for column in range (6):
            self.grid.append([])
            for row in range (6):
                self.grid[column].append('-')
                
                
    def __repr__(self):
        return f'{self.grid}'
    
    
    def __str__(self) -> str:
        # inserts enter after every line to create an actual grid
        line = ""

        for row in self.grid:
            line += str(row) + "\n"

        return line.strip()
