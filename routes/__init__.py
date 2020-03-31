from .geometry import *
from .joint import *
from .link import *
from .robot import *

def initalizeRoutes(api):
    initializeRobotRoutes(api)
    initializeLinkRoutes(api)
    initializeJointRoutes(api)
    initializeGeometryRoutes(api)