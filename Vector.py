import math

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def negate(self):
        self.x = -self.x
        self.y = -self.y
        
    def add(self, vector):
        self.x = self.x + vector.x
        self.y = self.y + vector.y

    def set(self, vector):
        self.x = vector.x
        self.y = vector.y

    def dist(self, point):
        dist = math.sqrt(((self.x - point.x) ** 2) + ((self.y - point.y) ** 2))
        return dist

    def dot(self, vector):
        dot = (self.x * vector.x) + (self.y * vector.y)
        return dot