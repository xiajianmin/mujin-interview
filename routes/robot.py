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
        body = {}
        if request.data:
            body = request.get_json()
        res = createRobot(body)
        return Response(json.dumps(res), mimetype="application/json", status=201)

class RobotApi(Resource):
    def get(self, robotid):
        res = getRobot(robotid)
        return Response(json.dumps(res), mimetype="application/json", status=200)

    def put(self, robotid):
        body = {}
        if request.data:
            body = request.get_json()
        res = updateRobot(robotid, body)
        return Response(json.dumps(res), mimetype="application/json", status=202)
    
    def delete(self, robotid):
        res = deleteRobot(robotid)
        return Response(json.dumps(res), mimetype="application/json", status=204)

def initializeRobotRoutes(api):
    api.add_resource(RobotsApi, '/api/robot')
    api.add_resource(RobotApi, '/api/robot/<robotid>')