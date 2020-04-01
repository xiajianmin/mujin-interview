# ~/routes/robot.py

from flask import Response, request
from flask_restful import Resource
from handlers import robot

class RobotsApi(Resource):
    def get(self):
        robots = robot.getAllRobots()
        return Response(robots, mimetype="application/json", status=200)
    
    def post(self):
        body = request.get_json()
        name = body.name
        res, status = robot.saveRobot(name)
        return Response(robots, mimetype="application/json", status=201)

class RobotApi(Resource):
    def get(self, robotid):
        robot = robot.getRobot(robotid)
        return Response(robot, mimetype="application/json", status=200)

    def put(self, robotid):
        body = request.get_json()
        robot.updateRobot(robotid, **body)
        return Response({}, mimetype="application/json", status=202)
    
    def delete(self, robotid):
        print("delete a robot")
        return Response({}, mimetype="application/json", status=204)

def initializeRobotRoutes(api):
    api.add_resource(RobotsApi, '/api/robot')
    api.add_resource(RobotApi, '/api/robot/<robotid>')