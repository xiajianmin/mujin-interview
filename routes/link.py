# ~/routes/link.py

from flask import Response, request
from flask_restful import Resource
from handlers import link

class LinksApi(Resource):
    def get(self, robotid):
        print("get links")
        return Response({}, mimetype="application/json", status=200)
    
    def post(self, robotid):
        body = request.get_json()
        # create link
        # if body.parentLinkId is not None:
        # create a joint with param of parentLinkId and ChildLinkId is the new link
        return {'id': 10}, 201

class LinkApi(Resource):
    def get(self, robotid, linkid):
        print("get a link")
        return Response({}, mimetype="application/json", status=200)

    def put(self, robotid, linkid):
        print("update link")
        return Response({}, mimetype="application/json", status=202)
    
    def delete(self, robotid, linkid):
        print("delete link")
        return Response({}, mimetype="application/json", status=204)

def initializeLinkRoutes(api):
    api.add_resource(LinksApi, '/api/robot/<robotid>/link')
    api.add_resource(LinkApi, '/api/robot/<robotid>/link/<linkid>')