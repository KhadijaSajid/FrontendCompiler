class syntaxAnalyzer:
    def __init__(self):
        self.index = 0
        self.lineno = 0
        self.follow = ['while', 'if', 'for', 'resume', 'send', 'ID', 'var', 'obj'
                       'stop', 'pass', '}', 'final', 'abstract', 'static',
                       'class', 'def', 'constructor', '$', 'end-mark']
        self.condSelectionSet = ['here', '(', '!', 'id', 'int-const', 'float-const',
                                 'char-const', 'str-const', 'bool-const']
        self.arr_2d = ['.', 'MDM', 'RO', 'AND', 'OR', ';', '{', ')', ']', '>', '=', 'comp-op']
        self.bodylst = [';', '{', 'while', 'if', 'for', 'resume', 'stop', 'pass', 'send', 'id', 'var', 'obj']
        self.SSTlst = ['while', 'if', 'for', 'resume', 'stop', 'pass', 'send', 'id', 'var', 'obj']
        self.classlst = ['final', 'abstract', 'static', 'class']
        self.defslst = ['final', 'abstract', 'static', 'class', 'define']
        self.exp = [';', '{', ')', ',', ']', '>']
        self.pos = ['MDM', 'RO', 'AND', 'OR', 'PM', '=', 'comp-op']
        # self.bodylst = ['while', 'if', 'for', 'resume', 'send', 'id', 'var',
        #                'stop', 'pass', ';', '{']

    def validation(self):
        try:
            end_mark = ['end-mark']
            if self.S():
                if split[self.index][0] in end_mark:
                    return True

            return False
        except:
            return False

    def indexIncrease(self):
        self.index += 1
        self.lineno = split[self.index][2]
        return

    def S(self):
        try:

            if split[self.index][0] in self.defslst or split[self.index][0] in self.SSTlst or split[self.index][0] == 'end-mark':
                if self.SST():
                    if self.S():
                        return True
                elif self.defs():
                    if self.S():
                        return True
                elif split[self.index][0] == 'end-mark':
                    return True
            return False

        except:
            return False

    def defs(self):
        try:
            if split[self.index][0]  in self.defslst:
                if self.class_defs():
                    if self.defs2():
                        return True
                elif self.func_defs():
                    if self.defs2():
                        return True
            return False

        except:
            return False

    def defs2(self):
        try:
            if split[self.index][0] in self.defslst or  split[self.index][0] in self.SSTlst:
                if self.class_defs():
                    if self.defs2():
                        return True
                elif self.func_defs():
                    if self.defs2():
                        return True
                elif split[self.index][0] in self.SSTlst:
                    return True
            return False

        except:
            return False

    # if else
    def if_else(self):
        try:
            if split[self.index][0] == 'if':
                if split[self.index][0] == 'if':
                    self.indexIncrease()
                    if self.cond():
                        if self.body():
                            if self.elseCond():
                                return True
            return False
        except:
            return False

    def elseCond(self):
        try:
            if split[self.index][0] == 'else' or split[self.index][0] in self.follow:
                if split[self.index][0] == 'else':
                    self.indexIncrease()
                    if self.body():
                        return True
                elif split[self.index][0] in self.follow:
                    return True
            return False
        except:
            return False

    def cond(self):
        try:
            if split[self.index][0] in self.condSelectionSet:
                if self.expression():
                    return True
            return False
        except:
            return False

    # while loop

    def whileLoop(self):
        try:
            if split[self.index][0] == 'while':
                self.indexIncrease()
                if self.cond():
                    if self.body():
                        return True
            return False

        except:
            return False

    def forLoop(self):
        try:
            if split[self.index][0] == 'for':
                self.indexIncrease()
                if split[self.index][0] == '(':
                    self.indexIncrease()
                    if self.p1():
                        if self.p2():
                            if split[self.index][0] == ';':
                                self.indexIncrease()
                                if self.p3():
                                    if split[self.index][0] == ')':
                                        self.indexIncrease()
                                        if self.body():
                                            return True
            return False

        except:
            return False

    def p1(self):
        try:
            p1SelecSet = ['var', 'here', 'id', ';']
            if split[self.index][0] in p1SelecSet:
                if split[self.index][0] == 'var':
                    if self.declaration():
                        return True
                elif split[self.index][0] == 'here' or split[self.index][0] == 'id':
                    if self.assign_str():
                        return True
                elif split[self.index][0] == ';':
                    self.indexIncrease()
                    return True
            return False
        except:
            return False

    def p2(self):
        try:
            if split[self.index][0] in self.condSelectionSet or split[self.index][0] == ';':
                if split[self.index][0] in self.condSelectionSet:
                    if self.cond():
                        return True
                elif split[self.index][0] == ';':
                    return True
            return False
        except:
            return False

    def p3(self):
        try:
            p3SelectSet = ['here', 'id']
            if split[self.index][0] in p3SelectSet or split[self.index][0] == ')':
                if self.assign_str():
                    return True
                elif split[self.index][0] == ')':
                    return True
            return False
        except:
            return False

    def passStr(self):
        try:
            if split[self.index][0] == 'pass':
                self.indexIncrease()
                if split[self.index][0] == ';':
                    self.indexIncrease()
                    return True
            return False
        except:
            return False

    def breakStr(self):
        try:
            if split[self.index][0] == 'stop':
                self.indexIncrease()
                if split[self.index][0] == ';':
                    self.indexIncrease()
                    return True
            return False
        except:
            return False

    def continueStr(self):
        try:
            if split[self.index][0] == 'resume':
                self.indexIncrease()
                if split[self.index][0] == ';':
                    self.indexIncrease()
                    return True
            return False
        except:
            return False

    def returnSt(self):
        try:
            if split[self.index][0] == 'send':
                self.indexIncrease()
                if self.return1():
                    if split[self.index][0] == ';':
                        self.indexIncrease()
                        return True
            return False
        except:
            return False

    def return1(self):
        try:
            if split[self.index][0] in self.condSelectionSet or split[self.index][0] == ';' or split[self.index][0] == 'current':
                if self.expression():
                    return True
                elif self.return_obj_create():
                    return True
                elif split[self.index][0] == ';':
                    return True
            return False

        except:
            return False

    def return_obj_create(self):
        try:
            if split[self.index][0] == ';' or split[self.index][0] == 'current':
                if split[self.index][0] == ';':
                    return True

                elif split[self.index][0] == 'current':
                    self.indexIncrease()
                    if split[self.index][0] == 'id':
                        self.indexIncrease()
                        if split[self.index][0] == '(':
                            self.indexIncrease()
                            if self.arguments():
                                if split[self.index][0] == ')':
                                    self.indexIncrease()

                                    return True

            return False
        except:
            return False
    def declaration(self):
        try:
            if split[self.index][0] == 'var':
                self.indexIncrease()
                if split[self.index][0] == 'DT':
                    self.indexIncrease()
                    if split[self.index][0] == 'id':
                        self.indexIncrease()
                        if self.init():
                            if self.dec2():
                                return True
            return False
        except:
            return False

    def dec2(self):
        try:
            if split[self.index][0] == ',' or split[self.index][0] == ';':
                if split[self.index][0] == ',':
                    self.indexIncrease()
                    if split[self.index][0] == 'id':
                        self.indexIncrease()
                        if self.init():
                            if self.dec2():
                                return True
                elif split[self.index][0] == ';':
                    self.indexIncrease()
                    return True
            return False
        except:
            return False

    def init(self):
        try:
            if split[self.index][0] == '=' or split[self.index][0] == ',' or split[self.index][0] == ';':
                if split[self.index][0] == '=':
                    self.indexIncrease()
                    if self.init1():
                        return True
                elif split[self.index][0] == ',' or split[self.index][0] == ';':
                    return True
            return False
        except:
            return False

    def init1(self):
        try:
            if split[self.index][0] == ':' or split[self.index][0] == 'id':

                if split[self.index][0] == ':':
                    self.indexIncrease()
                    if self.expression():
                        return True
                elif split[self.index][0] == 'id':
                    self.indexIncrease()
                    if self.init():
                        return True
            return False
        except:
            return False

    def obj_declaration(self):
        try:
            if split[self.index][0] == 'obj':
                self.indexIncrease()
                if split[self.index][0] == 'id':
                    self.indexIncrease()
                    if split[self.index][0] == 'id':
                        self.indexIncrease()
                        if self.obj_create():
                            return True
            return False
        except:
            return False

    def obj_create(self):
        try:
            if split[self.index][0] == ';' or split[self.index][0] == '=':
                if split[self.index][0] == ";":
                    self.indexIncrease()
                    return True
                elif split[self.index][0] == '=':
                    self.indexIncrease()
                    if split[self.index][0] == 'current':
                        self.indexIncrease()
                        if split[self.index][0] == 'id':
                            self.indexIncrease()
                            if split[self.index][0] == '(':
                                self.indexIncrease()
                                if self.arguments():
                                    if split[self.index][0] == ')':
                                        self.indexIncrease()
                                        if split[self.index][0] == ';':
                                            self.indexIncrease()
                                            return True
                                        # if split[self.index + 1][0] == 'send':
                                        #     return True
                                        # elif split[self.index][0] == ';':
                                        #     self.indexIncrease()
                                        #     return True

            return False
        except:
            return False

    def func_call(self):
        try:
            if split[self.index][0] == 'id':
                self.indexIncrease()
                if self.bef_func_pos():
                    if split[self.index][0] == '(':
                        self.indexIncrease()
                        if self.arguments():
                            if split[self.index][0] == ')':
                                self.indexIncrease()
                                if self.after_func_pos:
                                    if split[self.index][0] == ';':
                                        self.indexIncrease()
                                        return True
            return False
        except:
            return False

    def arguments(self):
        try:
            if split[self.index][0] in self.condSelectionSet or split[self.index][0] == ')':
                if self.expression():
                    if self.arguments2():
                        return True
                elif split[self.index][0] == ')':
                    return True
            return False

        except:
            return False

    def arguments2(self):
        try:
            if split[self.index][0] == ',' or split[self.index][0] == ')':
                if split[self.index][0] == ',':
                    self.indexIncrease()
                    if self.expression():
                        if self.arguments2():
                            return True
                elif split[self.index][0] == ')':
                    return True
            return False
        except:
            return False

    def bef_func_pos(self):

        try:
            if split[self.index][0] == '.' or split[self.index][0] == '[' or split[self.index][0] == '<' or \
                    split[self.index][0] == '(':
                if split[self.index][0] == '.':
                    self.indexIncrease()
                    if split[self.index][0] == 'id':
                        self.indexIncrease()
                        if self.bef_func_pos():
                            return True
                elif split[self.index][0] == '[':
                    self.indexIncrease()
                    if self.expression():
                        if split[self.index][0] == ']':
                            self.indexIncrease()
                            if self.array_2d():
                                if split[self.index][0] == '.':
                                    self.indexIncrease()
                                    if split[self.index][0] == 'id':
                                        self.indexIncrease()
                                        if self.bef_func_pos():
                                            return True
                elif split[self.index][0] == '<':
                    self.indexIncrease()
                    if self.expression():
                        if split[self.index][0] == '>':
                            self.indexIncrease()
                            if self.list_nd():
                                if split[self.index][0] == '.':
                                    self.indexIncrease()
                                    if split[self.index][0] == 'id':
                                        self.indexIncrease()
                                        if self.bef_func_pos():
                                            return True
                elif split[self.index][0] == '(':
                    return True
            return False
        except:
            return False

    def array_2d(self):
        try:
            if split[self.index][0] in self.arr_2d or split[self.index][0] == '[':
                if split[self.index][0] == '[':
                    self.indexIncrease()
                    if self.expression():
                        if split[self.index][0] == ']':
                            self.indexIncrease()
                            return True
                elif split[self.index][0] in self.arr_2d:
                    return True
            return False
        except:
            return False

    def after_func_pos(self):
        try:
            if split[self.index][0] == '.' or ';':
                if split[self.index][0] == '.':
                    self.indexIncrease()
                    if split[self.index][0] == 'id':
                        self.indexIncrease()
                        if self.after_func_pos1():
                            return True
                elif split[self.index][0] == ';':
                    return True
            return False
        except:
            return False

    def after_func_pos1(self):
        try:
            if split[self.index][0] == '.' or split[self.index][0] == '(':
                if split[self.index][0] == '(':
                    self.indexIncrease()
                    if self.arguments():
                        if split[self.index][0] == ')':
                            self.indexIncrease()
                            if self.after_func_pos():
                                return True
                elif split[self.index][0] == '.':
                    self.indexIncrease()
                    if split[self.index][0] == 'id':
                        self.indexIncrease()
                        if self.bef1_func_pos():
                            if split[self.index][0] == '(':
                                self.indexIncrease()
                                if self.arguments():
                                    if split[self.index][0] == ')':
                                        self.indexIncrease()
                                        if self.after_func_pos():
                                            return True
            return False
        except:
            return False

    def bef1_func_pos(self):
        try:
            if split[self.index][0] == '.' or split[self.index][0] == '[' or split[self.index][0] == '<' or \
                    split[self.index][0] == '(':
                if split[self.index][0] == '.':
                    self.indexIncrease()
                    if split[self.index][0] == 'id':
                        self.indexIncrease()
                        if self.bef1_func_pos():
                            return True
                elif split[self.index][0] == '[':
                    self.indexIncrease()
                    if self.expression():
                        if split[self.index][0] == ']':
                            self.indexIncrease()
                            if self.array_2d():
                                if split[self.index][0] == '.':
                                    self.indexIncrease()
                                    if split[self.index][0] == 'id':
                                        self.indexIncrease()
                                        if self.bef1_func_pos():
                                            return True
                elif split[self.index][0] == '<':
                    self.indexIncrease()
                    if self.expression():
                        if split[self.index][0] == '>':
                            self.indexIncrease()
                            if self.list_nd():
                                if split[self.index][0] == '.':
                                    self.indexIncrease()
                                    if split[self.index][0] == 'id':
                                        self.indexIncrease()
                                        if self.bef1_func_pos():
                                            return True
                elif split[self.index][0] == '(':
                    return True
            return False
        except:
            return False

    def list_nd(self):
        try:
            if split[self.index][0] in self.arr_2d or split[self.index][0] == '<' or split[self.index][
                0] in self.condSelectionSet:
                if split[self.index][0] == '<':
                    self.indexIncrease()
                    if self.expression():
                        if split[self.index][0] == '>':
                            self.indexIncrease()
                            if self.list_nd():
                                return True
                elif split[self.index][0] in self.arr_2d or split[self.index][0] in self.follow:
                    return True

            return False

        except:
            return False

    def arrayDS(self):
        try:
            if split[self.index][0] == 'var':
                self.indexIncrease()
                if split[self.index][0] == 'dt':
                    self.indexIncrease()
                    if split[self.index][0] == 'id':
                        self.indexIncrease()
                        if split[self.index][0] == '=':
                            self.indexIncrease()
                            if split[self.index][0] == '[':
                                self.indexIncrease()
                                if self.avalues():
                                    if split[self.index][0] == ']':
                                        self.indexIncrease()
                                        if split[self.index][0] == ';':
                                            self.indexIncrease()
                                            return True
            return False

        except:
            return False

    def avalues(self):
        try:
            if split[self.index][0] in self.condSelectionSet or split[self.index][0] == '[' or split[self.index][
                0] == ']':
                if self.expression():
                    if self.avalues2():
                        return True
                elif split[self.index][0] == '[':
                    self.indexIncrease()
                    if self.array_pos():
                        if split[self.index][0] == ']':
                            self.indexIncrease()
                            if self.avalues2():
                                return True
                elif split[self.index][0] == ']':
                    return True
            return False
        except:
            return False

    def avalues2(self):
        try:
            if split[self.index][0] == ',' or split[self.index][0] == ']':
                if split[self.index][0] == ',':
                    self.indexIncrease()
                    if self.expression():
                        if self.avalues2():
                            return True
                    elif split[self.index][0] == '[':
                        self.indexIncrease()
                        if self.array_pos():
                            if split[self.index][0] == ']':
                                self.indexIncrease()
                                if self.avalues2():
                                    return True
                # if split[self.index][0] == ',':
                #     self.indexIncrease()
                #     if self.expression():
                #         if self.avalues2():
                #             return True
                # elif split[self.index][0] == ',':
                #     self.indexIncrease()
                #     if split[self.index][0] == '[':
                #         self.indexIncrease()
                #         if self.array_pos():
                #             if split[self.index][0] == ']':
                #                 self.indexIncrease()
                #                 if self.avalues2():
                #                     return True
                elif split[self.index][0] == ']':
                    return True
            return False
        except:
            return False

    def array_pos(self):
        try:
            if split[self.index][0] in self.condSelectionSet or split[self.index][0] == ']':
                if self.expression():
                    if self.array_pos2():
                        return True
                elif split[self.index][0] == ']':
                    return True
            return False
        except:
            return False

    def array_pos2(self):
        try:
            if split[self.index][0] == ',' or split[self.index][0] == ']':
                if split[self.index][0] == ',':
                    self.indexIncrease()
                    if self.expression():
                        if self.array_pos2():
                            return True
                elif split[self.index][0] == ']':
                    return True

            return False
        except:
            return False
    # def listDS(self):
    #     try:
    #         if split[self.index][0] == 'var':
    #             self.indexIncrease()
    #             if split[self.index][0] == 'id':
    #                 self.indexIncrease()
    #                 if split[self.index][0] == '=':
    #                     self.indexIncrease()
    #                     if split[self.index][0] == '(':
    #                         self.indexIncrease()
    #                         if self.lvalues():
    #                             if split[self.index][0] == ')':
    #                                 self.indexIncrease()
    #                                 if split[self.index][0] == ';':
    #                                     self.indexIncrease()
    #                                     return True
    #         return False
    #
    #     except:
    #         return False
    #
    # def lvalues(self):
    #     try:
    #         if split[self.index][0] in self.condSelectionSet or split[self.index][0] == '<' or split[self.index][
    #             0] == '>':
    #             if self.expression():
    #                 if self.lvalues2():
    #                     return True
    #             elif split[self.index][0] == '(':
    #                 self.indexIncrease()
    #                 if self.lvalues2():
    #                     if split[self.index][0] == ')':
    #                         self.indexIncrease()
    #                         if self.lvalues2():
    #                             return True
    #             elif split[self.index][0] == ')':
    #                 return True
    #         return False
    #     except:
    #         return False
    #
    # def lvalues2(self):
    #     try:
    #         if split[self.index][0] == ',' or split[self.index][0] == ')':
    #             if split[self.index][0] == ',':
    #                 self.indexIncrease()
    #                 if self.expression():
    #                     if self.lvalues2():
    #                         return True
    #             elif split[self.index][0] == ',':
    #                 self.indexIncrease()
    #                 if split[self.index][0] == '(':
    #                     self.indexIncrease()
    #                     if self.lvalues2():
    #                         if split[self.index][0] == ')':
    #                             self.indexIncrease()
    #                             if self.lvalues2():
    #                                 return True
    #             elif split[self.index][0] == ')':
    #                 return True
    #         return False
    #     except:
    #         return False

    def listDS(self):
        try:
            if split[self.index][0] == 'var':
                self.indexIncrease()
                if split[self.index][0] == 'id':
                    self.indexIncrease()
                    if split[self.index][0] == '=':
                        self.indexIncrease()
                        if split[self.index][0] == 'list':
                            self.indexIncrease()
                            if split[self.index][0] == '[':
                                self.indexIncrease()
                                if self.lvalues():
                                    if split[self.index][0] == ']':
                                        self.indexIncrease()
                                        if split[self.index][0] == ';':
                                            self.indexIncrease()
                                            return True
            return False

        except:
            return False

    def lvalues(self):
        try:
            if split[self.index][0] in self.condSelectionSet or split[self.index][0] == '[' or split[self.index][
                0] == ']':
                if self.expression():
                    if self.lvalues2():
                        return True
                elif split[self.index][0] == ',':
                    self.indexIncrease()
                    if split[self.index][0] == '[':
                        self.indexIncrease()
                        if self.lvalues2():
                            if split[self.index][0] == ']':
                                self.indexIncrease()
                                if self.lvalues2():
                                    return True
                elif split[self.index][0] == '[':
                    self.indexIncrease()
                    if self.lvalues():
                        if split[self.index][0] == ']':
                            self.indexIncrease()
                            if self.lvalues2():
                                return True
                elif split[self.index][0] == ']':
                    return True
            return False
        except:
            return False

    def lvalues2(self):
        try:
            if split[self.index][0] == ',' or split[self.index][0] == ']' or split[self.index][0] == '[':
                if split[self.index][0] == ',':
                    self.indexIncrease()
                    if self.expression():
                        if self.lvalues2():
                            return True
                    elif split[self.index][0] == ',':
                        self.indexIncrease()
                        if split[self.index][0] == '[':
                            self.indexIncrease()
                            if self.lvalues2():
                                if split[self.index][0] == ']':
                                    self.indexIncrease()
                                    if self.lvalues2():
                                        return True
                    elif split[self.index][0] == '[':
                        self.indexIncrease()
                        if self.lvalues():
                            if split[self.index][0] == ']':
                                self.indexIncrease()
                                if self.lvalues2():
                                    return True
                # if split[self.index][0] == ',':
                #     self.indexIncrease()
                #     if self.expression():
                #         if self.avalues2():
                #             return True
                # elif split[self.index][0] == ',':
                #     self.indexIncrease()
                #     if split[self.index][0] == '[':
                #         self.indexIncrease()
                #         if self.array_pos():
                #             if split[self.index][0] == ']':
                #                 self.indexIncrease()
                #                 if self.avalues2():
                #                     return True
                elif split[self.index][0] == '[':
                    self.indexIncrease()
                    if self.lvalues():
                        if split[self.index][0] == ']':
                            self.indexIncrease()
                            if self.lvalues2():
                                return True
                elif split[self.index][0] == ']':
                    return True
            return False
        except:
            return False

    def array_pos(self):
        try:
            if split[self.index][0] in self.condSelectionSet or split[self.index][0] == ']':
                if self.expression():
                    if self.array_pos2():
                        return True
                elif split[self.index][0] == ']':
                    return True
            return False
        except:
            return False

    def array_pos2(self):
        try:
            if split[self.index][0] == ',' or split[self.index][0] == ']':
                if split[self.index][0] == ',':
                    self.indexIncrease()
                    if self.expression():
                        if self.array_pos2():
                            return True
                elif split[self.index][0] == ']':
                    return True

            return False
        except:
            return False

    def func_defs(self):
        try:
            if split[self.index][0] == 'define':
                self.indexIncrease()
                if self.returnType():
                    if split[self.index][0] == 'id':
                        self.indexIncrease()
                        if split[self.index][0] == '(':
                            self.indexIncrease()
                            if self.decparameter():
                                if split[self.index][0] == ')':
                                    self.indexIncrease()
                                    if split[self.index][0] == '{':
                                        self.indexIncrease()
                                        if self.func_body():
                                            if split[self.index][0] == '}':
                                                self.indexIncrease()
                                                return True
            return False
        except:
            return False
    def returnType(self):
        try:
            if split[self.index][0] == 'DT' or split[self.index][0]  == 'void' or split[self.index][0]  == 'id':
                if split[self.index][0]  == 'DT'or split[self.index][0]  == 'void':
                    self.indexIncrease()
                    return True
                # elif split[self.index][0] == 'id':
                #     return True
            return False
        except:
            return False

    def func_body(self):
        try:
            if split[self.index][0] in self.bodylst or split[self.index][0] == 'define' or split[self.index][0] == '}':
                if self.func_defs():
                    return True
                elif self.MST():
                    return True
                elif split[self.index][0] == '}':
                    return True
            return False
        except:
            return False

    def parameters(self):
        try:
            if split[self.index][0] == 'var' or split[self.index][0] == ')':
                if self.declaration():
                    if self.parameters2():
                        return True
                elif split[self.index][0] == ')':
                    return True
            return False
        except:
            return False

    def decparameter(self):
        try:
            if split[self.index][0] == 'DT' or split[self.index][0] == ')':
                if split[self.index][0] == 'DT':
                    self.indexIncrease()
                    if split[self.index][0] == 'id':
                        self.indexIncrease()
                        if self.decparameter2():
                            if self.decparameter3():
                                return True
                elif split[self.index][0] == ')':
                    return True
            return False
        except:
            return False

    def decparameter2(self):
        try:
            if split[self.index][0] == ',' or split[self.index][0] == ')'  or split[self.index][0] == '=':
                if split[self.index][0] == '=':
                    self.indexIncrease()
                    if self.expression():
                        if self.decparameter3():
                            return True

                elif split[self.index][0] == ')' or split[self.index][0] == ',':
                    return True
            return False
        except:
            return False
    def decparameter3(self):
        try:
            if split[self.index][0] == ',' or split[self.index][0] == ')':
                if split[self.index][0] == ',':
                    self.indexIncrease()
                    if split[self.index][0] == 'DT':
                        self.indexIncrease()
                        if split[self.index][0] == 'id':
                            self.indexIncrease()
                            if self.decparameter2():
                                if self.decparameter3():
                                    return True

                elif split[self.index][0] == ')':
                    return True
            return False
        except:
            return False
    def parameters2(self):
        try:
            if split[self.index][0] == ',' or split[self.index][0] == ')':
                if split[self.index][0] == ',':
                    self.indexIncrease()
                    if self.declaration():
                        if self.parameters2():
                            return True
                elif split[self.index][0] == ')':
                    return True
            return False
        except:
            return False

    def expression(self):
        try:
            if split[self.index][0] in self.condSelectionSet:
                if self.this():
                    if self.AND():
                        if self.OR1():
                            return True
            return False
        except:
            return False

    def OR1(self):
        try:
            if split[self.index][0] in self.follow or split[self.index][0] in self.exp or split[self.index][0] == 'OR':
                if split[self.index][0] == 'OR':
                    self.indexIncrease()
                    if self.AND():
                        if self.OR1():
                            return True
                elif split[self.index][0] in self.follow or split[self.index][0] in self.exp:
                    return True
            return False
        except:
            return False

    def AND(self):
        try:
            if split[self.index][0] in self.condSelectionSet:
                if self.RO():
                    if self.AND1():
                        return True
            return False
        except:
            return False

    def AND1(self):
        try:
            if split[self.index][0] in self.follow or split[self.index][0] in self.exp or split[self.index][
                0] == 'OR' or split[self.index][0] == 'AND':
                if split[self.index][0] == 'AND':
                    self.indexIncrease()
                    if self.RO():
                        if self.AND1():
                            return True
                elif split[self.index][0] in self.follow or split[self.index][0] in self.exp or split[self.index][
                    0] == 'OR':
                    return True
            return False
        except:
            return False

    def RO(self):
        try:
            if split[self.index][0] in self.condSelectionSet:
                if self.PM():
                    if self.RO1():
                        return True
            return False
        except:
            return False

    def RO1(self):
        try:
            if split[self.index][0] in self.follow or split[self.index][0] in self.exp or split[self.index][
                0] == 'OR' or split[self.index][0] == 'AND' or split[self.index][0] == 'RO':
                if split[self.index][0] == 'RO':
                    self.indexIncrease()
                    if self.PM():
                        if self.RO1():
                            return True
                elif split[self.index][0] in self.follow or split[self.index][0] in self.exp or split[self.index][
                    0] == 'OR' or split[self.index][0] == 'AND':
                    return True
            return False
        except:
            return False

    def PM(self):
        try:
            if split[self.index][0] in self.condSelectionSet:
                if self.MDM():
                    if self.PM1():
                        return True
            return False
        except:
            return False

    def PM1(self):
        try:
            if split[self.index][0] in self.follow or split[self.index][0] in self.exp or split[self.index][0] == 'OR' or split[self.index][0] == 'AND' or split[self.index][0] == 'RO' or split[self.index][
                0] == 'PM':
                if split[self.index][0] == 'PM':
                    self.indexIncrease()
                    if self.MDM():
                        if self.PM1():
                            return True
                elif split[self.index][0] in self.follow or split[self.index][0] in self.exp or split[self.index][
                    0] == 'OR' or split[self.index][0] == 'AND' or split[self.index][0] == 'RO':
                    return True
            return False
        except:
            return False

    def MDM(self):
        try:
            if split[self.index][0] in self.condSelectionSet:
                if self.F():
                    if self.MDM1():
                        return True
            return False
        except:
            return False

    def MDM1(self):
        try:
            if split[self.index][0] in self.follow or split[self.index][0] in self.exp or split[self.index][0] == 'OR'\
                    or split[self.index][0] == 'AND' or split[self.index][0] == 'RO' or split[self.index][0] == 'PM' \
                    or split[self.index][0] == 'MDM':
                if split[self.index][0] == 'MDM':
                    self.indexIncrease()
                    if self.F():
                        if self.MDM1():
                            return True
                elif split[self.index][0] in self.follow or split[self.index][0] in self.exp or split[self.index][0] == 'OR'\
                        or split[self.index][0] == 'AND' or split[self.index][0] == 'RO' or\
                        split[self.index][0] == 'PM':
                    return True
            return False
        except:
            return False

    def F(self):
        try:
            if split[self.index][0] in self.condSelectionSet:
                if self.const():
                    return True
                elif split[self.index][0] == '(':
                    self.indexIncrease()
                    if self.expression():
                        if split[self.index][0] == ')':
                            self.indexIncrease()
                            return True
                elif split[self.index][0] == '!':
                    self.indexIncrease()
                    if self.F:
                        return True
                elif split[self.index][0] == 'id':
                    self.indexIncrease()
                    if self.possibilities():
                        return True
            return False

        except:
            return False

    def const(self):
        try:
            constlst = ['int-const', 'float-const', 'char-const', 'str-const', 'bool-const']
            if split[self.index][0] in constlst:
                if split[self.index][0] == constlst[0]:
                    self.indexIncrease()
                    return True
                elif split[self.index][0] == constlst[1]:
                    self.indexIncrease()
                    return True
                elif split[self.index][0] == constlst[2]:
                    self.indexIncrease()
                    return True
                elif split[self.index][0] == constlst[3]:
                    self.indexIncrease()
                    return True
                elif split[self.index][0] == constlst[4]:
                    self.indexIncrease()
                    return True
            return False

        except:
            return False

    def assign_str(self):
        try:
            if split[self.index][0] == 'here' or split[self.index][0] == 'id':
                if self.this():
                    if split[self.index][0] == 'id':
                        self.indexIncrease()
                        if self.possibilities():
                            if self.assign_op():
                                if self.expression():
                                    if split[self.index][0] == ';':
                                        self.indexIncrease()
                                        return True

            return False

        except:
            return False

    def this(self):
        try:
            thisSelectionSet = ['(', '!', 'id', 'int-const', 'float-const',
                                'char-const', 'str-const', 'bool-const', 'here']
            if split[self.index][0] in self.condSelectionSet or split[self.index][0] in thisSelectionSet:
                if split[self.index][0] == 'here':
                    self.indexIncrease()
                    if split[self.index][0] == '.':
                        self.indexIncrease()
                        return True
                elif split[self.index][0] in thisSelectionSet:
                    return True
            return False
        except:
            return False

    def assign_op(self):
        try:
            if split[self.index][0] == '=' or split[self.index][0] == 'comp-op':
                self.indexIncrease()
                return True
            return False
        except:
            return False

    def possibilities(self):
        try:
            poslist = ['.', '[', '<', '(', '=']
            if split[self.index][0] in self.follow or split[self.index][0] in self.exp or split[self.index][
                0] in self.pos \
                    or split[self.index][0] in poslist:
                # if split[self.index][0] == ':':
                #     self.indexIncrease()
                    if split[self.index][0] == '.':
                        self.indexIncrease()
                        if split[self.index][0] == 'id':
                            self.indexIncrease()
                            if self.list():
                                return True
                    elif split[self.index][0] == '[':
                        self.indexIncrease()
                        if self.expression():
                            if split[self.index][0] == ']':
                                self.indexIncrease()
                                if self.exp_pos1():
                                    return True
                    elif split[self.index][0] == '<':
                        self.indexIncrease()
                        if self.expression():
                            if split[self.index][0] == '>':
                                self.indexIncrease()
                                if self.exp_pos2():
                                    return True
                    elif split[self.index][0] == '(':
                        self.indexIncrease()
                        if self.arguments():
                            if split[self.index][0] == ')':
                                self.indexIncrease()
                                if split[self.index][0] == '.':
                                    self.indexIncrease()
                                    if split[self.index][0] == 'id':
                                        self.indexIncrease()
                                        if self.list():
                                            return True
                    elif split[self.index][0] in self.follow or split[self.index][0] in self.exp or split[self.index][
                        0] in self.pos:
                        return True
            return False

        except:
            return False

    def exp_pos1(self):
        try:
            if split[self.index][0] == '[' or split[self.index][0] == '.' or \
                    split[self.index][0] in self.follow or split[self.index][0] in self.exp or split[self.index][
                0] in self.pos:
                if self.array_2d():
                    if self.arr_list_pos():
                        return True
            return False

        except:
            return False

    def exp_pos2(self):
        try:
            if split[self.index][0] == '<' or split[self.index][0] == '.' or \
                    split[self.index][0] in self.follow or split[self.index][0] in self.exp or split[self.index][
                0] in self.pos:
                if self.list_nd():
                    if self.arr_list_pos():
                        return True
            return False
        except:
            return False

    def arr_list_pos(self):
        try:
            if split[self.index][0] == '.' or split[self.index][0] in self.follow or split[self.index][0] in self.exp or \
                    split[self.index][0] in self.pos:
                if split[self.index][0] == '.':
                    self.indexIncrease()
                    if split[self.index][0] == 'id':
                        self.indexIncrease()
                        if self.list():
                            return True
                elif split[self.index][0] in self.follow or split[self.index][0] in self.exp or split[self.index][
                    0] in self.pos:
                    return True
            return False
        except:
            return False

    def list(self):
        try:
            poslist = ['.', '[', '<', '(']
            if split[self.index][0] in self.follow or split[self.index][0] in self.exp or split[self.index][
                0] in self.pos \
                    or split[self.index][0] in poslist:
                if split[self.index][0] == '.':
                    self.indexIncrease()
                    if split[self.index][0] == 'id':
                        self.indexIncrease()
                        if self.list():
                            return True
                elif split[self.index][0] == '[':
                    self.indexIncrease()
                    if self.expression():
                        if split[self.index][0] == ']':
                            self.indexIncrease()
                            if self.exp_pos1():
                                return True
                elif split[self.index][0] == '<':
                    self.indexIncrease()
                    if self.expression():
                        if split[self.index][0] == '>':
                            self.indexIncrease()
                            if self.exp_pos2():
                                return True
                elif split[self.index][0] == '(':
                    self.indexIncrease()
                    if self.arguments():
                        if split[self.index][0] == ')':
                            self.indexIncrease()
                            if split[self.index][0] == '.':
                                self.indexIncrease()
                                if split[self.index][0] == 'id':
                                    self.indexIncrease()
                                    if self.list():
                                        return True
                elif split[self.index][0] in self.follow or split[self.index][0] in self.exp or split[self.index][
                    0] in self.pos:
                    return True
            return False

        except:
            return False

    def class_defs(self):
        try:
            if split[self.index][0] in self.classlst:
                if self.mod():
                    if split[self.index][0] == 'class':
                        self.indexIncrease()
                        if split[self.index][0] == 'id':
                            self.indexIncrease()
                            if self.inheritance():
                                if split[self.index][0] == '{':
                                    self.indexIncrease()
                                    if self.class_body():
                                        if split[self.index][0] == '}':
                                            self.indexIncrease()
                                            return True
            return False
        except:
            return False

    def mod(self):
        try:
            if split[self.index][0] in self.classlst:
                if split[self.index][0] == 'final' or split[self.index][0] == 'abstract' or split[self.index][
                    0] == 'static':
                    self.indexIncrease()
                    return True

                elif split[self.index][0] == 'class':
                    return True
            return False
        except:
            return False

    def inheritance(self):
        try:
            if split[self.index][0] == 'childof' or split[self.index][0] == '{':
                if split[self.index][0] == 'childof':
                    self.indexIncrease()
                    if split[self.index][0] == 'id':
                        self.indexIncrease()
                        return True

                elif split[self.index][0] == '{':
                    return True

                return False
        except:
            return False

    def class_body(self):
        try:
            classlst = ['final', 'abstract', 'static', 'var', 'define', 'constructor', '}']
            if split[self.index][0] in classlst:
                if split[self.index][0] == 'static':
                    self.indexIncrease()
                    if self.func_att():
                        if self.class_body():
                            return True
                elif split[self.index][0] == '}':
                    return True
                elif self.attribute():
                    if self.class_body():
                        return True
                elif self.func_decl():
                    if self.class_body():
                        return True
                elif self.constructor():
                    if self.class_body():
                        return True
            return False
        except:
            return False

    def func_decl(self):
        try:
            if split[self.index][0] == 'define' or split[self.index][0] == 'abstract':
                if self.func_defs():
                    return True
                elif self.abstract_func():
                    return True
                return False
        except:
            return False

    def abstract_func(self):
        try:
            if split[self.index][0] == 'abstract':
                self.indexIncrease()
                if split[self.index][0] == 'define':
                    self.indexIncrease()
                    if self.returnType():
                        if split[self.index][0] == 'id':
                            self.indexIncrease()
                            if split[self.index][0] == '(':
                                self.indexIncrease()
                                if self.decparameter():
                                    if split[self.index][0] == ')':
                                        self.indexIncrease()
                                        if split[self.index][0] == ';':
                                            self.indexIncrease()
                                            return True

            return False
        except:
            return False

    def constructor(self):
        try:
            if split[self.index][0] == 'constructor':
                self.indexIncrease()
                if split[self.index][0] == 'id':
                    self.indexIncrease()
                    if split[self.index][0] == '(':
                        self.indexIncrease()
                        if self.decparameter():
                            if split[self.index][0] == ')':
                                self.indexIncrease()
                                if self.body():
                                    return True

            return False
        except:
            return False

    def attribute(self):
        try:
            if split[self.index][0] == 'final' or split[self.index][0] == 'var':
                if split[self.index][0] == 'final':
                    self.indexIncrease()
                    if self.declaration():
                        return True
                elif self.declaration():
                    return True
                return False
        except:
            return False

    def func_att(self):
        try:
            if split[self.index][0] == 'final' or split[self.index][0] == 'var' or split[self.index][0] == 'define' or \
                    split[self.index][0] == 'abstract':

                if self.attribute() or self.func_decl():
                    return True
                return False
        except:
            return False

    def body(self):

        try:
            if split[self.index][0] in self.bodylst:
                if split[self.index][0] == ';':
                    self.indexIncrease()
                    return True
                elif self.SST():
                    return True
                elif split[self.index][0] == '{':
                    self.indexIncrease()
                    if self.MST():
                        if split[self.index][0] == '}':
                            self.indexIncrease()

                            return True
            return False

        except:
            return False

    def SST(self):
        try:
            if split[self.index][0] in self.SSTlst:
                if self.returnSt() or self.passStr() or self.obj_declaration() or self.whileLoop() or self.if_else() or self.forLoop() or self.continueStr() or self.breakStr():
                    return True
                elif split[self.index][0] == 'id':
                    self.indexIncrease()
                    if self.SST1():
                        return True
                elif split[self.index][0] == 'var':
                    self.indexIncrease()
                    if self.SST2():
                        return True
            return False

        except:
            return False

    def SST1(self):
        try:
            sst1lst = ['.', '[', '(', '<', '=', 'comp-op', 'id', ':']
            if split[self.index][0] in sst1lst:
                # if self.possibilities():
                if self.posColon():
                    if self.assign_op():
                        if self.expression():
                            if split[self.index][0] == ';':
                                self.indexIncrease()
                                return True
                elif self.bef_func_pos():
                    if split[self.index][0] == '(':
                        self.indexIncrease()
                        if self.arguments():
                            if split[self.index][0] == ')':
                                self.indexIncrease()
                                if self.after_func_pos():
                                    if split[self.index][0] == ';':
                                        self.indexIncrease()
                                        return True

            return False

        except:
            return False
    def posColon(self):
        try:
            folset = [':', '=']
            if split[self.index][0]  in folset:
                if split[self.index][0]  == ':':
                    self.indexIncrease()
                    if self.possibilities():
                        return True
                elif split[self.index][0] == '=':
                    return True
            return False
        except:
            return True
    def SST2(self):
        try:
            dt = ['DT']
            if split[self.index][0] in dt or split[self.index][0] == 'id':
                if split[self.index][0] == 'DT':
                    self.indexIncrease()

                    if split[self.index][0] == 'id':
                        self.indexIncrease()
                        if self.SST3():
                            return True
                elif split[self.index][0] == 'id':
                    self.indexIncrease()
                    if split[self.index][0] == '=':
                        self.indexIncrease()
                        if split[self.index][0] == 'list':
                            self.indexIncrease()
                            if split[self.index][0] == '[':
                                self.indexIncrease()
                                if self.lvalues():
                                    if split[self.index][0] == ']':
                                        self.indexIncrease()
                                        if split[self.index][0] == ';':
                                            self.indexIncrease()
                                            return True

            return False

        except:
            return False

    # def SST3(self):
    #     try:
    #         sst3lst = ['[', '=', ',', ';']
    #         if split[self.index][0] in sst3lst:
    #             if self.init():
    #                 if self.dec2():
    #                     return True
    #             elif split[self.index][0] in '=':
    #                 self.indexIncrease()
    #                 if split[self.index][0] == '[':
    #                     self.indexIncrease()
    #                     if self.avalues():
    #                         if split[self.index][0] == ']':
    #                             self.indexIncrease()
    #                             if split[self.index][0] == ';':
    #                                 self.indexIncrease()
    #                                 return True
    #
    #         return False
    #
    #     except:
    #         return False

    def SST3(self):
        try:
            # sst3lst = ['[', '=', ',', ';']
            sst3lst = ['=', ',', ';']
            if split[self.index][0] in sst3lst:
                if self.dec2():
                    return True
                elif split[self.index][0] in '=':
                    self.indexIncrease()
                    if self.SST5():
                        return True
            return False

        except:
            return False

    def SST5(self):

        try:
            sst3lst = ['[',  'id', ':']
            if split[self.index][0] in sst3lst:
                if self.init1():
                    if self.dec2():
                        return True
                if split[self.index][0] == '[':
                    self.indexIncrease()
                    if self.avalues():
                        if split[self.index][0] == ']':
                            self.indexIncrease()
                            if split[self.index][0] == ';':
                                self.indexIncrease()
                                return True

            return False

        except:
            return False
    def MST(self):
        try:
            if split[self.index][0] in self.SSTlst or split[self.index][0] == '}':
                if self.SST():
                    if self.MST():
                        return True
                elif split[self.index][0] == '}':
                    return True
            return False

        except:
            return False


tokken = open("../lexicalAnalyzer/tokken.txt", "r")
lines = (tokken.readlines())
split = []
for line in lines:
    split.append(line.split("#"))

# print(split)
syntaxanalyzer = syntaxAnalyzer()
if syntaxanalyzer.validation():
    print('syntactically correct')
else:
    print('syntax error at line', syntaxanalyzer.lineno)


