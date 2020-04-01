from models import robot

def getAllRobots():

    res = [
        {
            "id": "robot1"
        },
        {
            "id": "robot2"
        }
    ]
    return res

def createRobot(name, links, joints):
    # generate a random number
    id = 1
    return id

def getRobot(id):
    res = {
        "id": "robotid"
    }
    return res

def updateRobot(id, name, links, joints):
    robot = robot.Robot()
    res = {}
    return res

def deleteRobot(id):
    # delete the joint
    # delete the link
    return