# #     self.parent = self.helpFuncs.lookupMTClass(split[self.index][1])
# #     if self.extParent != self.parent[3]:
# #         print("undeclared error at line", self.lineno)
# # par = ''
#
# # from stackDS import stack
# # from createAndDelete import createDeleteScope
# #
# # scope = createDeleteScope()
# #
# # scope.createScope()
# # scope.createScope()
# # scope.createScope()
# #
# # print(scope.scopeValue())
# # scope.deleteScope()
# # scope.deleteScope()
# #
# # print(scope.scopeValue())
# #
# # # # #
# # # # # # a = True
# # # # # # b ="ss"
# # # # # # print(type(a))
# # # # # # print(type(b))
# # # # # # print(type(a/b))
# # # # # # print(a*b)
# # # # #
# # # # #
# # # # # class A:
# # # # #     def name(self):
# # # # #         return 1
# # # # #
# # # # #
# # # # # class B:
# # # # #     def name(self):
# # # # #         return 1
# # # # #
# # # # #     class C:
# # # # #         def name(self):
# # # # #             return 2
# # # # #
# # # # # #
# # # # # # a = A()
# # # # # # print(a.name())
# # # # # # b = B().C()
# # # # # # d = b
# # # # # # print(b.name())
# # # # # class helpingFunctions:
# # # # #
# # # # #     def __init__(self):
# # # # #         self.mainTableClassLst = []
# # # # #         self.mainTableFuncLst = []
# # # # #         self.funcTableLst = []
# # # # #         self.classDataTable = []
# # # # #         self.allClasses = []
# # # # #
# # # # #     def insertMTClass(self, name, type, parent, ref):
# # # # #         Mtlst = [name, type, parent, ref]
# # # # #         self.mainTableClassLst.append(Mtlst)
# # # # #
# # # # #     def insertMTFunc(self, name, type, ref):
# # # # #         MtFunclst = [name, type, parent, ref]
# # # # #         self.mainTableFuncLst.append(MtFunclst)
# # # # #
# # # # #
# # # # #     def insertFT(self, name, type, scope):
# # # # #         FT = [name, type, scope]
# # # # #         self.funcTableLst.append(FT)
# # # # #
# # # # #
# # # # #     def insertDT(self, name, type, static, final, abstract):
# # # # #         CDT = [name, type, static, final, abstract]
# # # # #         self.classDataTable.append(CDT)
# # # # #
# # # # #
# # # # #     def insertInClass(self):
# # # # #         self.allClasses.append(CDT)
# # # # #         return
# # # # #
# # # # #
# # # # #     def lookupMTClass(self):
# # # # #         pass
# # # # #
# # # # #     def lookupMTFunc(self):
# # # # #         pass
# # # # #
# # # # #     def lookupDT(self, refOfCT):
# # # # #         pass
# # # # #
# # # # #     def lookupDT(self, parameterList, refOfCT):
# # # # #         pass
# # # # #
# # # # #     def lookupFT(self, scopeStack):
# # # # #         pass
# # # # #
# # # # #     def compatibilty(self, type1, type2, operator):
# # # # #         if ((type1 == 'int' and type2 == 'int') or
# # # # #                 (type1 == 'float' and type2 == 'float') or
# # # # #                 (type1 == 'text' and type2 == 'text')) and (operator == '+' ):
# # # # #             return type1 or type2
# # # # #         elif ((type1 == 'int' and type2 == 'int') or
# # # # #                 (type1 == 'float' and type2 == 'float')) and (operator == '-' or operator == '*'):
# # # # #             return type1 or type2
# # # # #         elif type1 == 'char' and type2 == 'char' and  operator == '+':
# # # # #             return 'text'
# # # # #         elif (type1 == 'int' and type2 == 'float' or type1 == 'float' and type2 == 'int')  and  (operator == '+' or operator == '-' or operator == '*' or operator == '/'):
# # # # #             return 'float'
# # # # #         elif (type1 == 'text' and type2 == 'char' or type1 == 'char' and type2 == 'text') and  operator == '+':
# # # # #             return 'str'
# # # # #         elif ((type1 == 'int' and type2 == 'int') or
# # # # #                 (type1 == 'float' and type2 == 'float')) and operator == '/':
# # # # #             return 'float'
# # # # #         return 'NC'
# # # # #
# # # # # #
# # # # # # a = helpingFunctions()
# # # # # # a.insertFT('a', 'int', 1)
# # # # # # a.insertFT('b', 'int', 2)
# # # # # # a.insertMTClass('A', 'class', 'none', 1)
# # # # # # a.insertMTClass('B', 'class', 'none', 2)
# # # # # # print(len(a.mainTableClassLst))
# # # # # # print(a.mainTableClassLst)
# # # # # #
# # # # # # for i in range(len(a.mainTableClassLst)):
# # # # # #     if (a.mainTableClassLst[i][0]) == 'A':
# # # # # #         print( a.mainTableClassLst[i])
# # # # # #
# # # # # #
# # # # # # print(a.compatibilty('float', 'float', '-'))
# # # # # # if a.funcTableLst[0][0] == 'a':
# # # # # #     print('redeclartion')
# # # # #
# # # # # class B:
# # # # #     def __init__(self):
# # # # #         self.c = C()
# # # # #
# # # # # class C:
# # # # #     def __init__(self):
# # # # #         pass
# # # # # class A:
# # # # #
# # # # #     def __init__(self):
# # # # #         self.b = B()
# # # # #     # class B:
# # # # #     #     def __init__(self, a):
# # # # #     #         self.x = 1
# # # # #     #         self.c = C()
# # # # #     #
# # # # #     #     class C:
# # # # #     #         def __init__(self):
# # # # #     #             pass
# # # # #
# # # # #     def func(self):
# # # # #         a = A()
# # # # #
# # # # #         return a.B(1)
# # # # #
# # # # #     def func2(self):
# # # # #         print(self.func().x)
# # # # #
# # # # # a = A()
# # # # # # a.func2()
# # # # # # b = a.B(1)
# # # # # # print(b)
# # # # # a.b.c
# # # #
# # # # class helpingFunctions:
# # # #
# # # #     def __init__(self):
# # # #         self.mainTableClassLst = []
# # # #         self.mainTableFuncLst = []
# # # #         self.funcTableLst = []
# # # #         self.classDataTable = []
# # # #         self.allClasses = []
# # # #
# # # #     def insertMTClass(self, name, type, TM, parent, ref):
# # # #         # if self.lookupMTClass():
# # # #         #     Mtlst = [name, type, parent, ref]
# # # #         #     self.mainTableClassLst.append(Mtlst)
# # # #         #     return True
# # # #         # return False
# # # #
# # # #         for i in range(len(self.mainTableClassLst)):
# # # #             if self.mainTableClassLst[i][0] == name:
# # # #                 return False
# # # #         Mtlst = [name, type, TM,  parent, ref]
# # # #         self.mainTableClassLst.append(Mtlst)
# # # #         return True
# # # #
# # # #     def insertMTFunc(self, name, type, ref):
# # # #         # if self.lookupMTFunc(name):
# # # #         #     MtFunclst = [name, type, parent, ref]
# # # #         #     self.mainTableFuncLst.append(MtFunclst)
# # # #         #     return True
# # # #         # return False
# # # #
# # # #         if self.lookupMTFunc(name):
# # # #             MtFunclst = [name, type, parent, ref]
# # # #             self.mainTableFuncLst.append(MtFunclst)
# # # #             return True
# # # #         return False
# # # #
# # # #
# # # #     def insertFT(self, name, type, scope):
# # # #         # if self.lookupFT(name):
# # # #         #     FT = [name, type, scope]
# # # #         #     self.funcTableLst.append(FT)
# # # #         #     return True
# # # #         # return False
# # # #         if self.lookupFT(name):
# # # #             FT = [name, type, scope]
# # # #             self.funcTableLst.append(FT)
# # # #             return True
# # # #         return False
# # # #
# # # #     def insertDT(self, name, type, static, final, abstract):
# # # #         # if self.lookupDT():
# # # #         #     CDT = [name, type, static, final, abstract]
# # # #         #     self.classDataTable.append(CDT)
# # # #         #     return True
# # # #         # return False
# # # #
# # # #         if self.lookupDT():
# # # #             CDT = [name, type, static, final, abstract]
# # # #             self.classDataTable.append(CDT)
# # # #             return True
# # # #         return False
# # # #
# # # #     def insertInClass(self):
# # # #         self.allClasses.append(CDT)
# # # #         return True
# # # #
# # # #
# # # #     def lookupMTClass(self, name):
# # # #         if len(self.mainTableClassLst) != 0:
# # # #             for i in range(len(self.mainTableClassLst)):
# # # #                 if self.mainTableClassLst[i][0] == name:
# # # #                     return self.mainTableClassLst[i]
# # # #         return False
# # # #
# # # #
# # # #     def lookupMTFunc(self, name):
# # # #         if len(self.mainTableFuncLst) != 0:
# # # #             for i in range(len(self.mainTableFuncLst)):
# # # #                 if self.mainTableFuncLst[i][0] == name:
# # # #                     return self.mainTableFuncLst[i]
# # # #         return False
# # # #
# # # #     def lookupDT(self, refOfCT):
# # # #         pass
# # # #
# # # #     def lookupDT(self, parameterList, refOfCT):
# # # #         pass
# # # #
# # # #     def lookupFT(self, scopeStack):
# # # #         pass
# # # #
# # # #     def compatibilty(self, type1, type2, operator):
# # # #         if ((type1 == 'int' and type2 == 'int') or
# # # #                 (type1 == 'float' and type2 == 'float') or
# # # #                 (type1 == 'text' and type2 == 'text')) and (operator == '+'):
# # # #             return type1 or type2
# # # #         elif ((type1 == 'int' and type2 == 'int') or
# # # #                 (type1 == 'float' and type2 == 'float')) and (operator == '-' or operator == '*'):
# # # #             return type1 or type2
# # # #         elif type1 == 'char' and type2 == 'char' and  operator == '+':
# # # #             return 'text'
# # # #         elif (type1 == 'int' and type2 == 'float' or type1 == 'float' and type2 == 'int')  and  (operator == '+' or operator == '-' or operator == '*' or operator == '/'):
# # # #             return 'float'
# # # #         elif (type1 == 'text' and type2 == 'char' or type1 == 'char' and type2 == 'text') and  operator == '+':
# # # #             return 'str'
# # # #         elif ((type1 == 'int' and type2 == 'int') or
# # # #                 (type1 == 'float' and type2 == 'float')) and operator == '/':
# # # #             return 'float'
# # # #         return 'NC'
# # # #
# # # #
# # # # help = helpingFunctions()
# # # # help.insertMTClass('khadija', 'class', 'final', 'parent', '1')
# # # # print(help.mainTableClassLst)
# # # # a = help.lookupMTClass('khadija')
# # # # b = help.lookupMTClass('hajra')
# # # #
# # # # print(a[1])
# # # # if not b:
# # # #     print("a=")
# # #
# # #
# # # class A:
# # #     def __init__(self):
# # #         self.a = 1
# # #
# # # class A:
# # #     def __init__(self):
# # #         self.a = 23
# # #
# #
# # # d = 13
# # # for i in range(d):
# # #     print(1)
#
#
# from createAndDelete import createDeleteScope
#
# class helpingFunctions:
#
#     def __init__(self):
#         self.mainTableClassLst = []
#         self.mainTableFuncLst = []
#         self.funcTableLst = []
#         self.classDataTable = []
#         self.allClasses = []
#         self.createDelScope = createDeleteScope()
#
#
#     def insertMTClass(self, name, type, TM, parent, ref):
#         # if self.lookupMTClass():
#         #     Mtlst = [name, type, parent, ref]
#         #     self.mainTableClassLst.append(Mtlst)
#         #     return True
#         # return False
#
#         for i in range(len(self.mainTableClassLst)):
#             if self.mainTableClassLst[i][0] == name:
#                 return False
#         Mtlst = [name, type, TM,  parent, ref]
#         self.mainTableClassLst.append(Mtlst)
#         return True
#
#     def insertMTFunc(self, name, type, ref):
#         # if self.lookupMTFunc(name):
#         #     MtFunclst = [name, type, parent, ref]
#         #     self.mainTableFuncLst.append(MtFunclst)
#         #     return True
#         # return False
#
#         # if self.lookupMTFunc(name):
#         #     MtFunclst = [name, type, parent, ref]
#         #     self.mainTableFuncLst.append(MtFunclst)
#         #     return True
#         # return False
#         for i in range(len(self.mainTableFuncLst)):
#             if self.mainTableFuncLst[i][0] == name:
#                 if self.mainTableFuncLst[i][1] == type:
#                     return False
#         Mtlst = [name, type, ref]
#         self.mainTableFuncLst.append(Mtlst)
#         return True
#
#     def insertFT(self, name, type, scope):
#         # if self.lookupFT(name):
#         #     FT = [name, type, scope]
#         #     self.funcTableLst.append(FT)
#         #     return True
#         # return False
#         for i in range(len(self.funcTableLst)):
#             if self.funcTableLst[i][0] == name:
#                 print(self.createDelScope.ST())
#                 # if self.funcTableLst[i][2] == self.createDelScope.ST():
#                 return False
#         Mtlst = [name, type, scope]
#         self.funcTableLst.append(Mtlst)
#         return True
#
#     def insertDT(self, name, type, static, final, abstract):
#         # if self.lookupDT():
#         #     CDT = [name, type, static, final, abstract]
#         #     self.classDataTable.append(CDT)
#         #     return True
#         # return False
#
#         for i in range(len(self.classDataTable)):
#             if self.classDataTable[i][0] == name:
#                 if self.classDataTable[i][1] == type:
#                     return False
#         Mtlst = [name, type, static, final, abstract]
#         self.classDataTable.append(Mtlst)
#         return True
#
#     def insertInClass(self):
#         self.allClasses.append(self.classDataTable)
#         self.classDataTable = []
#         return True
#
#
#     def lookupMTClass(self, name):
#         if len(self.mainTableClassLst) != 0:
#             for i in range(len(self.mainTableClassLst)):
#                 if self.mainTableClassLst[i][0] == name:
#                     return self.mainTableClassLst[i]
#         return False
#
#
#     def lookupMTFunc(self, name):
#         if len(self.funcTableLst) != 0:
#             for i in range(len(self.funcTableLst)):
#                 if self.funcTableLst[i][0] == name:
#                     return self.funcTableLst[i]
#         return False
#
#     def lookupDT(self, refOfCT):
#         pass
#
#     def lookupDT(self, parameterList, refOfCT):
#         pass
#
#     def lookupFT(self, scopeStack):
#         pass
#
#     def compatibilty(self, type1, type2, operator):
#         if ((type1 == 'int' and type2 == 'int') or
#                 (type1 == 'float' and type2 == 'float') or
#                 (type1 == 'text' and type2 == 'text')) and (operator == '+'):
#             return type1 or type2
#         elif ((type1 == 'int' and type2 == 'int') or
#                 (type1 == 'float' and type2 == 'float')) and (operator == '-' or operator == '*'):
#             return type1 or type2
#         elif type1 == 'char' and type2 == 'char' and  operator == '+':
#             return 'text'
#         elif (type1 == 'int' and type2 == 'float' or type1 == 'float' and type2 == 'int')  and  (operator == '+' or operator == '-' or operator == '*' or operator == '/'):
#             return 'float'
#         elif (type1 == 'text' and type2 == 'char' or type1 == 'char' and type2 == 'text') and  operator == '+':
#             return 'str'
#         elif ((type1 == 'int' and type2 == 'int') or
#                 (type1 == 'float' and type2 == 'float')) and operator == '/':
#             return 'float'
#         return 'NC'
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
        # if self.lookupMTClass():
        #     Mtlst = [name, type, parent, ref]
        #     self.mainTableClassLst.append(Mtlst)
        #     return True
        # return False

        for i in range(len(self.mainTableClassLst)):
            if self.mainTableClassLst[i][0] == name:
                return False
        Mtlst = [name, type, TM,  parent, ref]
        self.mainTableClassLst.append(Mtlst)
        return True

    def insertMTFunc(self, name, type, ref):
        # if self.lookupMTFunc(name):
        #     MtFunclst = [name, type, parent, ref]
        #     self.mainTableFuncLst.append(MtFunclst)
        #     return True
        # return False

        # if self.lookupMTFunc(name):
        #     MtFunclst = [name, type, parent, ref]
        #     self.mainTableFuncLst.append(MtFunclst)
        #     return True
        # return False
        for i in range(len(self.mainTableFuncLst)):
            if self.mainTableFuncLst[i][0] == name:
                if self.mainTableFuncLst[i][1] == type:
                    return False
        Mtlst = [name, type, ref]
        self.mainTableFuncLst.append(Mtlst)
        return True

    def insertFT(self, name, type, scope, entireSt):
        # if self.lookupFT(name):
        #     FT = [name, type, scope]
        #     self.funcTableLst.append(FT)
        #     return True
        # return False
        for i in range(len(self.funcTableLst)):
            if self.funcTableLst[i][0] == name:
                if self.funcTableLst[i][2] in entireSt:
                    return False
        Mtlst = [name, type, scope]
        self.funcTableLst.append(Mtlst)
        return True

    def insertDT(self, name, type, static, final, abstract):
        # if self.lookupDT():
        #     CDT = [name, type, static, final, abstract]
        #     self.classDataTable.append(CDT)
        #     return True
        # return False

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

    def lookupDT(self, refOfCT):
        pass

    def lookupDT(self, parameterList, refOfCT):
        pass

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
a = helpingFunctions()
a.insertMTFunc(1, 2, 3)
print(a.lookupMTFunc(1))