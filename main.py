from subsystems.camera import *
from subsystems.display import *
from subsystems.inputs import *
from subsystems.mathutil import *
from subsystems.render import *
from subsystems.world import *

camera = Camera()
world = WorldState(25)
renderer = Renderer(camera, world)
display = Display()

while True:
    time.sleep(0.03)
    temp = renderer.render()
    display.render(temp)