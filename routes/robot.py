#~/routes/robot.py

from flask import Response, request
from flask_restful import Resource

class RobotsApi(Resource):
    def get(self):
        print("get robots")
        return Response({}, mimetype="application/json", status=200)
    
    def post(self):
        print("create robot")
        return {'id': 10}, 201

class RobotApi(Resource):
    def get(self, robotid):
        print("get a robot")
        return Response(robot, mimetype="application/json", status=200)

    def put(self, robotid):
        print("update a robot")
        return '', 202
    
    def delete(self, robotid):
        print("delete a robot")
        return '', 204

def initializeRobotRoutes(api):
    api.add_resource(RobotsApi, '/api/robot')
    api.add_resource(RobotApi, '/api/robot/<robotid>')