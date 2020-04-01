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

def createRobot(data):
    # generate a random number
    id = 1
    return {}

def getRobot(id):
    res = {
        "id": "robotid"
    }
    return res

def updateRobot(id, body):
    robot = getRobot(id)
    name = body.get("name", None)
    links = body.get("links", None)
    joints = body.get("joints", None)
    if name is not None:
        print("update name")
    if links is not None:
        print("update links")
    if joints is not None:
        print("update joints")
    return True

def deleteRobot(id):
    # delete the joint
    # delete the link
    return True