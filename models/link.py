

class Link:
    def __init__(self, parentLinkId, name, transform, geometries):
        self.id = ""
        self.parentLinkId = "" # read - only
        self.name = ""
        self.transform = [] #7
        self.geometries = []

    # always called when a new Link is created with parentLinkId != ""
    def createJoint():
        return