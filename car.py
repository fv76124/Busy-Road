from grid import Grid

""" Class for the cars """
class Car():
    
    def __init__(self):
        self.load_file(f"gameboards/Rushhour6x6_1.csv")
    
    def load_file(self, filename):
        """ reads the file """
        with open(filename) as file:
            header = file.readline
            for line in file:
                car_info = line.split(',')
                column = str(car_info[2])
                row = str(car_info[3])
                car_tile = Grid()
                car_tile[column][row]
                
                # car = car_info[0]
                # orientation = car_info[1]
                # length = car_info[4]
                return car_tile[column][row]
    
    def __repr__(self) -> str:
        """String representation""" 
        
        return f'{self.load_file("gameboards/Rushhour6x6_1.csv")}'