from subsystems.camera import *
from subsystems.world import *
from subsystems.display import *

class Renderer:
    def __init__(self, camera:Camera, world:WorldState):
        self.camera = camera
        self.world = world
        self.displayData = DisplayData() 
    def render(self):
        # clear
        self.camera.update()
        self.displayData.reset()
        # calculations
        rotationMatrix = self.camera.latestRotation
        projectionMatrix = self.camera.latestProjection
        for x in range(self.world.offset*2):
            for y in range(self.world.offset*2):
                for z in range(self.world.offset*2):
                    if self.world.getBlock(x,y,z) == Block.AIR:
                        continue
                    translation = [x-self.camera.x, y-self.camera.y, z-self.camera.z]
                    projection = self.camera.project(translation)

                    distance = numpy.linalg.norm(translation)

                    self.displayData.setPixel(projection[0], projection[1], [255,255,255], distance)
        return self.displayData