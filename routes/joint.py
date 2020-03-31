# ~/routes/joint.py

from flask import Response, request
from flask_restful import Resource

class JointsApi(Resource):
    def get(self, robotid):
        print("get joints")
        return Response({}, mimetype="application/json", status=200)

class JointApi(Resource):
    def get(self, robotid, jointid):
        print("get a joint")
        return Response({}, mimetype="application/json", status=200)

    def put(self, robotid, jointid):
        print("update a joint")
        return '', 202

def initializeJointRoutes(api):
    api.add_resource(JointsApi, '/api/robot/<robotid>/joint')
    api.add_resource(JointApi, '/api/robot/<robotid>/joint/<jointid>')