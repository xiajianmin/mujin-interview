from sqlalchemy import Table, Column, Integer, Text
from sqlalchemy.orm import mapper
from db import metadata, db_session

class Robot:
    
    def __init__(self, id="", name="", links=[], joints=[]):
        self.id = id
        self.name = name
        self.links = links
        self.joints = joints

    def update(self, name="", links=[], joints=[]):
        return

    def addLink(self, linkid):
        self.links.append(linkid)
        return

    def addJoint(self, jointid):
        self.joints.append(jointid)
