""" Class for the cars """
class Car():
    
    def __init__(self):
        self.position = []
        self.load_file(f"gameboards/Rushhour6x6_1.csv")
    
    """ loads file """
    def load_file(self, filename):
        """ reads the file """
        with open(filename) as file:
            header = file.readline()
            for line in file:
                car_info = line.split(',')
                car = car_info[0]
                orientation = car_info[1]
                column = car_info[2]
                row = car_info[3]
                length = car_info[4].strip("\n")
                self.position.append([car, orientation, column, row, length])
            return self.position
    
    """String representation""" 
    def __repr__(self) -> str:
        
        return f'{self.position}'