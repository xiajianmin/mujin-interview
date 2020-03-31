#~/routes/link.py

from flask import Response, request
from flask_restful import Resource

class LinksApi(Resource):
    def get(self, robotid):
        print("get links")
        return Response({}, mimetype="application/json", status=200)
    
    def post(self, robotid):
        print("post links")
        return {'id': 10}, 201

class LinkApi(Resource):
    def get(self, robotid, linkid):
        print("get a link")
        return Response({}, mimetype="application/json", status=200)

    def put(self, robotid, linkid):
        print("update link")
        return '', 202
    
    def delete(self, robotid, linkid):
        print("delete link")
        return '', 204

def initializeRobotRoutes(api):
    api.add_resource(LinksApi, '/api/robot/<robotid>/link')
    api.add_resource(LinkApi, '/api/robot/<robotid>/link/<linkid>')