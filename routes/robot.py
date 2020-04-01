# ~/routes/robot.py

from flask import Response, request
from flask_restful import Resource
from handlers.robot import *
import json

class RobotsApi(Resource):
    def get(self):
        robots = getAllRobots()
        return Response(json.dumps(robots), mimetype="application/json", status=200)
    
    def post(self):
        body = request.get_json()
        # name = body.name
        res = createRobot('', '', '')
        return Response(res, mimetype="application/json", status=201)

class RobotApi(Resource):
    def get(self, robotid):
        robot = getRobot(robotid)
        return Response(robot, mimetype="application/json", status=200)

    def put(self, robotid):
        body = request.get_json()
        print(body)
        return Response({}, mimetype="application/json", status=202)
    
    def delete(self, robotid):
        print("delete a robot")
        return Response({}, mimetype="application/json", status=204)

def initializeRobotRoutes(api):
    api.add_resource(RobotsApi, '/api/robot')
    api.add_resource(RobotApi, '/api/robot/<robotid>')