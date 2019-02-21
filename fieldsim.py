import random, Vector, Particle, Field, math, pyglet

winWidth, winHeight = 700, 700

# pygame.init()
# win = pygame.display.set_mode((winWidth, winHeight))
win = pyglet.window.Window(winWidth, winHeight)
# pygame.display.set_caption("Simulator")

particles = []
f = Field.Field(0, 0, 700, 700)
for i in range(f.dim.x):
     for j in range(f.dim.y):
          x = i-350
          y = j-350
          scale = 5000
          dy = (x+4*y-4)*math.sin(x*y) /scale
          dx = (y - x ** 2) /scale
          f.setVectors(i, j, Vector.Vector(dx, dy))

for i in range(100):
     p = Particle.Particle(random.randint(300, 400), random.randint(300, 400), 0, 0, 5, (255, 0, 0), 'win')
     particles.append(p)

# running = True
# while running:
     # pygame.time.delay(10)
     # win.fill(0)

     # for event in pygame.event.get():
     #    if event.type == pygame.QUIT:
     #        running = False

def update(self):
     win.clear()
     for p in particles:
          if p.pos.x > 600:
               p.pos.x = 100
          if p.pos.x < 100:
               p.pos.x = 600
          if p.pos.y > 600:
               p.pos.y = 100
          if p.pos.y < 100:
               p.pos.y = 600
          p.pos.add(f.getVector(p.pos.x, p.pos.y))
          #p.pos.add(p.vel)
          p.draw()

#      pygame.display.update()

pyglet.clock.schedule_interval(update, 1/60)

# pygame.quit()

pyglet.app.run()