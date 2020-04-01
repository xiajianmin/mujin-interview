from models import Robot

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

def updateRobot(id, name=None, links=None, joints=None):
    robot = getRobot(id)
    if name is not None:
        robot.update('name', name)
    if links is not None:
        robot.update('links', links)
    if joints is not None:
        links.update('joints', joints)
    return res

def deleteRobot(id):
    # delete the joint
    # delete the link
    return