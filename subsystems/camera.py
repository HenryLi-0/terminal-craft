import numpy
from  subsystems.display import DisplaySettings

class Camera:
    def __init__(self, x = 0, y = 0, z = 0, pitch = 0, yaw = 0):
        self.x = x
        self.y = y
        self.z = z
        self.pitch = pitch
        self.yaw = yaw

        # not in inital for now
        self.fov = numpy.pi / 4
        self.nearPlane = 0.1
        self.farPlane = 100
    
    def applyMovement(self, controllerX, controllerY):
        self.x += numpy.cos(self.yaw) * controllerX
        self.y += numpy.sin(self.yaw) * controllerY

    def applyRotation(self, controllerX, controllerY):
        self.yaw += controllerX
        self.yaw = (self.yaw + numpy.pi) % (2 * numpy.pi) - numpy.pi
        self.pitch += controllerY
        self.pitch = numpy.clip(self.pitch, -numpy.pi/2, numpy.pi/2)

    def getPosition(self):
        return [self.x,self.y,self.z]

    def getRotation(self):
        cosPitch =  numpy.cos(self.pitch)
        sinPitch =  numpy.sin(self.pitch)
        cosYaw =  numpy.cos(self.yaw)
        sinYaw =  numpy.sin(self.yaw)

        return numpy.array([
            [ cosYaw, -sinYaw*cosPitch,  sinYaw*sinPitch],
            [ sinYaw,  cosYaw*cosPitch, -cosYaw*sinPitch],
            [      0,         sinPitch,         cosPitch]
        ])


    def getProjection(self):
        f = 1/numpy.tan(self.fov/2)
        return numpy.array([
            [f/DisplaySettings.ASPECT_RATIO,  0,                                                                  0,  0],
            [                             0,  f,                                                                  0,  0],
            [                             0,  0,      (self.nearPlane+self.farPlane)/(self.nearPlane-self.farPlane), -1],
            [                             0,  0,    (2*self.farPlane*self.nearPlane)/(self.nearPlane-self.farPlane),  0]
        ])
    
    def update(self):
        self.latestRotation = self.getRotation()
        self.latestProjection = self.getProjection()

    def project(self, point):
        source = numpy.append(point, 1)
        screenSpacePoint = numpy.dot(self.latestProjection, numpy.dot(self.latestRotation, source))
        if screenSpacePoint[3] != 0:
            screenSpacePoint /= screenSpacePoint[3]
        return screenSpacePoint[:2]