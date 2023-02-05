from stackDS import stack

class createDeleteScope:

    def __init__(self):
        self.stackDS = stack()

    def createScope(self):
        return self.stackDS.push()

    def deleteScope(self):
        return self.stackDS.pop()

    def scopeValue(self):
        return self.stackDS.scopeVal()

    def ST(self):
        return self.stackDS.topofStack()

    def entireStack(self):
        return self.stackDS.stackLst

