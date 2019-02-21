import Vector

class Field():
     def __init__(self, originx, originy, dimx, dimy):
          self.origin = Vector.Vector(originx, originy)
          self.dim = Vector.Vector(dimx, dimy)
          self.field = [[Vector.Vector(0, 0) for j in range(self.dim.y)] for i in range(self.dim.x)]

     def getVector(self, i, j):
          return self.field[int(i)][int(j)]

     def setVectors(self, i, j, vector):
          self.field[i][j] = vector

