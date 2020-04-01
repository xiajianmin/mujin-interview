# ~/routes/geometry.py

from flask import Response, request
from flask_restful import Resource
from handlers.geometry import *
import json

class GeometriesApi(Resource):
    def get(self, robotid, linkid):
        res = getAllGeometry(robotid, linkid)
        return Response(json.dumps(res), mimetype="application/json", status=200)
    
    def post(self, robotid, linkid):
        body = {}
        if request.data:
            body = request.get_json()
        res = createGeometry(robotid, linkid, body)
        return Response(res, mimetype="application/json", status=201)

class GeometryApi(Resource):
    def get(self, robotid, linkid, geometryid):
        res = getGeometry(robotid, linkid, geometryid)
        return Response(json.dumps(res), mimetype="application/json", status=200)

    def put(self, robotid, linkid, geometryid):
        body = {}
        if request.data:
            body = request.get_json()
        res = updateGeometry(robotid, linkid, geometryid, body)
        return Response(json.dumps(res), mimetype="application/json", status=202)
    
    def delete(self, robotid, linkid, geometryid):
        res = deleteGeometry(robotid, linkid, geometryid)
        return Response(json.dumps(res), mimetype="application/json", status=204)

def initializeGeometryRoutes(api):
    api.add_resource(GeometriesApi, '/api/robot/<robotid>/link/<linkid>/geometry')
    api.add_resource(GeometryApi, '/api/robot/<robotid>/link/<linkid>/geometry/<geometryid>')