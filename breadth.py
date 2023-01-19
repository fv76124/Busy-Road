from board import *
from car import *
class Breadth:
    def __init__(self, cor_car):
        self.dict = {}
        self.queue = []
        self.visited = []
        self.cor_car = cor_car

    def breedte(self):
        #coordinates car nodig
        #coordinates grid nodig
        #kijken of hij naar rechts of links kan en dan toevoegen in lijst
        print(Board().grid)
        print("hoi")