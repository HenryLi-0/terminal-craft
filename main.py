from subsystems.camera import *
from subsystems.debug import *
from subsystems.display import *
from subsystems.inputs import *
from subsystems.mathutil import *
from subsystems.render import *
from subsystems.world import *
import time

debug = Debug()
camera = Camera(debug, -100,-50,50)
world = WorldState(25)
renderer = Renderer(debug, camera, world)
display = Display(debug)

while True:
    time.sleep(0.03)
    temp = renderer.render()
    display.render(temp)

    # position controls
    if keyPressed("w"): camera.applyMovement( 0,-1, 0)
    if keyPressed("a"): camera.applyMovement(-1, 0, 0)
    if keyPressed("s"): camera.applyMovement( 0, 1, 0)
    if keyPressed("d"): camera.applyMovement( 1, 0, 0)
    if keyPressed("q"): camera.applyMovement( 0, 0,-1)
    if keyPressed("e"): camera.applyMovement( 0, 0, 1)

    # rotation controls
    if keyPressed("i"): camera.applyRotation(   0, 0.1)
    if keyPressed("m"): camera.applyRotation(   0,-0.1)
    if keyPressed("j"): camera.applyRotation(-0.1,   0)
    if keyPressed("k"): camera.applyRotation( 0.1,   0)

    debug.detail()