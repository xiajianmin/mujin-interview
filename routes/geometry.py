# ~/routes/geometry.py

from flask import Response, request
from flask_restful import Resource
from handlers import geometry

class GeometriesApi(Resource):
    def get(self, robotid, linkid):
        
        return Response({}, mimetype="application/json", status=200)
    
    def post(self, robotid, linkid):
        print("create geometry")
        return Response({}, mimetype="application/json", status=201)

class GeometryApi(Resource):
    def get(self, robotid, linkid, geometryid):
        print("get a geometry")
        return Response({}, mimetype="application/json", status=200)

    def put(self, robotid, linkid, geometryid):
        print("update a geometry")
        return Response({}, mimetype="application/json", status=202)
    
    def delete(self, robotid, linkid, geometryid):
        print("delete a geometry")
        return Response({}, mimetype="application/json", status=204)

def initializeGeometryRoutes(api):
    api.add_resource(GeometriesApi, '/api/robot/<robotid>/link/<linkid>/geometry')
    api.add_resource(GeometryApi, '/api/robot/<robotid>/link/<linkid>/geometry/<geometryid>')