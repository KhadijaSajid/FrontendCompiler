class stack:
    def __init__(self):
        self.stackLst = []
        self.scope = 1

    def push(self):
        self.stackLst.append(self.scope)
        self.scope += 1
        return

    def pop(self):
        if len(self.stackLst) == 0:
            return
        self.stackLst.pop(-1)
        return

    def scopeVal(self):
        return self.stackLst

    def topofStack(self):
        if len(self.stackLst) == 0:
            return
        return self.stackLst[-1]