from subsystems.camera import *
from subsystems.world import *
from subsystems.display import *
from subsystems.debug import *

class Renderer:
    def __init__(self, debug: Debug, camera:Camera, world:WorldState):
        self.debug = debug
        self.camera = camera
        self.world = world
        self.displayData = DisplayData() 
        self.lastBlocksProccessed = 0
    def render(self):
        # clear
        self.camera.update()
        self.displayData.reset()
        # calculations
        rotationMatrix = self.camera.latestRotation
        projectionMatrix = self.camera.latestProjection
        i = 0
        for x in range(self.world.offset*2):
            for y in range(self.world.offset*2):
                for z in range(self.world.offset*2):
                    if self.world.getBlock(x,y,z) == Block.AIR:
                        continue
                    translation = [x-self.camera.x, y-self.camera.y, z-self.camera.z]
                    projection = self.camera.project(translation)

                    distance = numpy.linalg.norm(translation)

                    self.displayData.setPixel(projection[0]+DisplaySettings.WIDTH/2, projection[1]+DisplaySettings.HEIGHT/2, Block.COLOR_MAP[self.world.getBlock(x,y,z)], distance)
                    i += 1
        self.lastBlocksProccessed = i
        self.debug.post(" | Renderer: {} blocks processed".format(i))
        return self.displayData