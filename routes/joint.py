# ~/routes/joint.py

from flask import Response, request
from flask_restful import Resource
from handlers.joint import *
import json

class JointsApi(Resource):
    def get(self, robotid):
        res = getAllJoints(robotid)
        return Response({}, mimetype="application/json", status=200)

class JointApi(Resource):
    def get(self, robotid, jointid):
        res = getJoint(robotid, jointid)
        return Response({}, mimetype="application/json", status=200)

    def put(self, robotid, jointid):
        body = {}
        if request.data:
            body = request.get_json()
        res = updateJoint(robotid, jointid, body)
        return Response(json.dumps(res), mimetype="application/json", status=202)

def initializeJointRoutes(api):
    api.add_resource(JointsApi, '/api/robot/<robotid>/joint')
    api.add_resource(JointApi, '/api/robot/<robotid>/joint/<jointid>')