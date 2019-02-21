import Vector, pyglet

class Particle():
    def __init__(self, x, y, xvel, yvel, radius, color, surface):
        self.pos = Vector.Vector(x, y)
        self.vel = Vector.Vector(xvel, yvel)
        self.acc = Vector.Vector(0, 0)
        self.radius = radius
        self.color = color
        self.surface = surface

    def draw(self):
        pyglet.graphics.draw(3, pyglet.gl.GL_POLYGON, 
            ('v2i', (int(self.pos.x), int(self.pos.y - 5), int(self.pos.x - 3), int(self.pos.y), int(self.pos.x + 3), int(self.pos.y)))
        )
        # pygame.draw.circle(self.surface, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)

    def update(self):
          self.vel.add(self.acc)
