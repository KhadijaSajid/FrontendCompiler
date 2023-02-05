from createAndDelete import createDeleteScope

class helpingFunctions:

    def __init__(self):
        self.mainTableClassLst = []
        self.mainTableFuncLst = []
        self.funcTableLst = []
        self.classDataTable = []
        self.allClasses = []
        self.createDelScope = createDeleteScope()


    def insertMTClass(self, name, type, TM, parent, ref):
        for i in range(len(self.mainTableClassLst)):
            if self.mainTableClassLst[i][0] == name:
                return False
        Mtlst = [name, type, TM,  parent, ref]
        self.mainTableClassLst.append(Mtlst)
        return True

    def insertMTFunc(self, name, type, ref):

        for i in range(len(self.mainTableFuncLst)):
            if self.mainTableFuncLst[i][0] == name:
                if self.mainTableFuncLst[i][1] == type:
                    return False
        Mtlst = [name, type, ref]
        self.mainTableFuncLst.append(Mtlst)
        return True

    def insertFT(self, name, type, scope, entireSt):

        for i in range(len(self.funcTableLst)):
            if self.funcTableLst[i][0] == name:
                if self.funcTableLst[i][2] in entireSt:
                    return False
        Mtlst = [name, type, scope]
        self.funcTableLst.append(Mtlst)
        return True

    def insertDT(self, name, type, static, final, abstract):

        for i in range(len(self.classDataTable)):
            if self.classDataTable[i][0] == name:
                if self.classDataTable[i][1] == type:
                    return False
        Mtlst = [name, type, static, final, abstract]
        self.classDataTable.append(Mtlst)
        return True

    def insertInClass(self):
        self.allClasses.append(self.classDataTable)
        self.classDataTable = []
        return True


    def lookupMTClass(self, name):
        if len(self.mainTableClassLst) != 0:
            for i in range(len(self.mainTableClassLst)):
                if self.mainTableClassLst[i][0] == name:
                    return self.mainTableClassLst[i]
        return False


    def lookupMTFunc(self, name):
        if len(self.mainTableFuncLst) != 0:
            for i in range(len(self.mainTableFuncLst)):
                if self.mainTableFuncLst[i][0] == name:
                    return self.mainTableFuncLst[i]
        return False



    def lookupFT(self, var, scopeStack):
        if len(self.funcTableLst) != 0:
            for i in range(len(self.funcTableLst)):
                if self.funcTableLst[i][0] == var:
                    if self.funcTableLst[i][2] in scopeStack:
                        return self.funcTableLst[i]
        return False

    def compatibilty(self, type1, type2, operator):
        if ((type1 == 'int' and type2 == 'int') or
                (type1 == 'float' and type2 == 'float') or
                (type1 == 'text' and type2 == 'text')) and (operator == '+'):
            return type1 or type2
        elif ((type1 == 'int' and type2 == 'int') or
                (type1 == 'float' and type2 == 'float')) and (operator == '-' or operator == '*'):
            return type1 or type2
        elif type1 == 'char' and type2 == 'char' and  operator == '+':
            return 'text'
        elif (type1 == 'int' and type2 == 'float' or type1 == 'float' and type2 == 'int')  and  (operator == '+' or operator == '-' or operator == '*' or operator == '/'):
            return 'float'
        elif (type1 == 'text' and type2 == 'char' or type1 == 'char' and type2 == 'text') and  operator == '+':
            return 'str'
        elif ((type1 == 'int' and type2 == 'int') or
                (type1 == 'float' and type2 == 'float')) and operator == '/':
            return 'float'
        return 'NC'


    def lookupDT(self, refOfCT):
        pass

    def lookupDT(self, parameterList, refOfCT):
        pass