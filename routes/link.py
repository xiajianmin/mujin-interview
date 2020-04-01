# ~/routes/link.py

from flask import Response, request
from flask_restful import Resource
from handlers.link import *
import json

class LinksApi(Resource):
    def get(self, robotid):
        res = getAllLinks(robotid)
        return Response(json.dumps(res), mimetype="application/json", status=200)
    
    def post(self, robotid):
        body = {}
        if request.data:
            body = request.get_json()
        res = createLink(robotid, body)
        # create link
        # if body.parentLinkId is not None:
        # create a joint with param of parentLinkId and ChildLinkId is the new link
        return Response(json.dumps(res), mimetype="application/json", status=201)

class LinkApi(Resource):
    def get(self, robotid, linkid):
        res = getLink(robotid, linkid)
        return Response(json.dumps(res), mimetype="application/json", status=200)

    def put(self, robotid, linkid):
        body = {}
        if request.data:
            body = request.get_json()
        res = updateLink(robotid, linkid, body)
        return Response(json.dumps(res), mimetype="application/json", status=202)
    
    def delete(self, robotid, linkid):
        res = deleteLink(robotid, linkid)
        return Response(json.dumps(res), mimetype="application/json", status=204)

def initializeLinkRoutes(api):
    api.add_resource(LinksApi, '/api/robot/<robotid>/link')
    api.add_resource(LinkApi, '/api/robot/<robotid>/link/<linkid>')