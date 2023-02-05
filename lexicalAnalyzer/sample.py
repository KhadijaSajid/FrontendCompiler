import re

file = open("code.txt", "r")
tokkens = open("tokken.txt", "a")
tokkens.truncate(0)
line = (file.read())
lineNo = 1
temp = ""

keywords = ["var", "if", "elsif", "else", "for", "while", "pass",
            "resume", "stop", "var", "class", "abstract", "final",
            "define", "send", "here", "constructor", "current", "childof",
            "parent", "static", "obj", "void", "list"]
punc = ["?", "{", "}", "(", ")", ":", ".", ",", "[", "]"]
datatypes = ["int", "float", "char", "text", "bool"]
boolVal = ["true", "false"]
PM_OP = ["+", "-"]
MDD_OP = ["*", "/", "%"]
RO_OP = ["<", ">", "<=", ">=", "==", "!=", "!"]
AO_OP = ["and", "or"]
NOT_OP = ["not"]
# INCDEC_OP = ["++", "--"]
comp_op = ["+=", "-="]
ASSIGN_OP = ["="]


def fileWrite(classPart, valuePart):
    tokkens.write("{}#{}#{}\n".format(classPart, valuePart, lineNo))


def validation(word):
    if word in keywords:
        fileWrite(word, word)
        return
    elif word.isspace():
        return
    elif word == '/n':
        return
    elif word == '':
        return
    elif word == ";":
        fileWrite(word, word)
    elif word in datatypes:
        fileWrite("DT", word)
        return
    elif word in punc:
        fileWrite(word, word)
        return
    elif word in PM_OP:
        fileWrite("PM", word)
        return

    elif word in MDD_OP:
        fileWrite("MDM", word)
        return
    elif word in RO_OP:
        fileWrite("RO", word)
        return

    elif word in AO_OP:
        fileWrite("AO", word)
        return

    elif word in NOT_OP:
        fileWrite("NOT", word)
        return

    elif word in comp_op:
        fileWrite("comp-op", word)
        return

    elif word in ASSIGN_OP:
        fileWrite("=", word)
        return

    elif integer(word):
        fileWrite("int-const", word)
        return
    elif word in boolVal:
        fileWrite("bool-const", word)
        return

    elif identifiers(word):
        fileWrite("id", word)
        return
    elif float(word):
        fileWrite("float-const", word)
        return
    else:
        fileWrite('"invalid"', word)
        return


def integer(word):
    if re.fullmatch("[+ -]?[0-9]+", word):
        return True
    return False


def identifiers(word):
    if re.fullmatch("^[a-zA-Z][a-zA-Z0-9_]*[a-zA-Z0-9]$", word) or re.fullmatch("[a-zA-Z]", word):
        return True
    return False


def float(word):
    if re.fullmatch("[+ -]?[0-9]*[.][0-9]*", word):
        return True
    return False


stringFlag, charFlag = False, False
dotFlag = False
digitFlag = False
plusFlag, minusFlag = False, False
greaterFlag, lessFlag, assignFlag = False, False, False
singleCmt, multiCmt = False, False
dFlag, invalidFlag = False, False
slash = False

for char in line:
    #  single line comments
    if (char == "~" and not singleCmt) or (char != "~" and char != '\n' and singleCmt):
        singleCmt = True
        continue
    elif char == '\n' and singleCmt:
        lineNo += 1
        singleCmt = False
        continue

    # multi line comments
    elif (char == "^" and not multiCmt) or (char != "^" and multiCmt):
        multiCmt = True
        continue
    elif char == '\n' and multiCmt:
        lineNo += 1
        continue
    elif char == "^" and multiCmt:
        multiCmt = False
        continue




    # String tokkens

    elif char == "\\" and stringFlag and not slash:
        temp += char
        slash = True
        continue
    elif char == "\\" and slash and temp[-1] == "\\":
        temp += char
        slash = False
        continue

    elif char != '"' and slash or (char == '"' and slash):
        temp += char
        slash = False
        continue


    elif char != '"' and stringFlag and char != '\n':
        temp += char
        continue
    elif char != '"' and stringFlag and char == '\n':
        fileWrite('"invalid"', '"{}'.format(temp))
        temp = ""
        stringFlag = False
        lineNo += 1
        continue
    elif char == '"':
        if not stringFlag:
            validation(temp)
            temp = ""
            stringFlag = True
            continue
        elif stringFlag:
            if len(temp) == 0:
                fileWrite("str-const", temp)


            elif temp[-1] == "\\" and temp[-1] != "\\":
                fileWrite('"invalid"', temp)
            else:
                fileWrite("str-const", temp)
            temp = ""
            stringFlag = False
            continue



    # chars
    elif char == '\n' and charFlag:
        fileWrite('"invalid"', temp)
        temp = ""
        charFlag = False
        lineNo += 1
        continue

    elif char != "'" and charFlag:
        if len(temp) < 3:
            temp += char
            continue
        elif len(temp) == 3 and temp[1] == "\\":
            temp += char
            continue
        elif len(temp) == 3 and temp[1] != "\\" or (len(temp) > 3 and temp[1] == "\\"):
            fileWrite('"invalid"', temp)
            temp = ""
            temp += char
            charFlag = False
            continue


    elif char == "'":
        if not charFlag:
            plusFlag, minusFlag, singleCmt = False, False, False
            greaterFlag, lessFlag, assignFlag = False, False, False
            dotFlag, digitFlag = False, False
            dFlag, invalidFlag = False, False
            validation(temp)
            temp = ""
            charFlag = True

            temp += char
            continue
        elif charFlag:
            if len(temp) == 2 or (len(temp) == 3 and temp[1] == "\\"):
                temp += char
                fileWrite("char-const", temp)
                temp = ""
                charFlag = False
                continue


    elif char == "!":
        # if not expFlag:

        validation(temp)
        temp = ""
        temp += char
        continue




    # line breaker
    elif char == '\n':
        plusFlag, minusFlag, singleCmt = False, False, False
        greaterFlag, lessFlag, assignFlag = False, False, False
        dotFlag, charFlag, digitFlag = False, False, False
        dFlag, invalidFlag = False, False

        validation(temp)
        # fileWrite("line break", "\\n")
        temp = ""
        lineNo += 1
        continue

    elif char.isspace():
        plusFlag, minusFlag, singleCmt = False, False, False
        greaterFlag, lessFlag, assignFlag = False, False, False
        dotFlag, charFlag, digitFlag = False, False, False
        dFlag, invalidFlag = False, False

        if len(temp) == 0:
            continue
        validation(temp)
        temp = ""
        continue

    elif char == ":":
        validation(temp)
        validation(":")
        temp = ""
        continue

    # dot tokkens
    elif char == "." and not dotFlag:
        dotFlag = True
        if len(temp) != 0:
            if temp.isdigit():
                temp += char
                continue

            else:
                validation(temp)
                temp = char
                continue
    elif char == "." and dotFlag:
        validation(temp)
        temp = char
        digitFlag = False
        continue
    elif char != "." and dotFlag:
        if char.isalpha() and digitFlag:
            temp += char
            continue
        elif char.isalpha():
            if temp[-1] == ".":
                validation(temp)
                dotFlag = False
                temp = char
                continue
            temp += char
            continue

        elif char.isdigit():
            if len(temp) == 1:
                digitFlag = True
            temp += char
            continue
        else:
            validation(temp)
            dotFlag = False
            temp = ""
            temp += char
            validation(temp)
            temp = ""
            continue


    # plus tokkens
    # elif char == "+":
    #     if not plusFlag:
    #         validation(temp)
    #         temp = ""
    #         plusFlag = True
    #         temp += char
    #         continue
    #     elif plusFlag:
    #         if char == "+":
    #             plusFlag = False
    #             temp += char
    #             validation(temp)
    #             temp = ""
    #             continue
    # elif char != "+" and plusFlag:
    #     plusFlag = False
    #     validation(temp)
    #     temp = ""
    #     temp += char
    #     continue

    elif char == "+":
        if not plusFlag:
            validation(temp)
            temp = ""
            plusFlag = True
            temp += char
            continue
        validation(temp)
        temp = ""
        plusFlag = True
        temp += char
        continue


    elif char != "+" and plusFlag:
        if char == "=":
            plusFlag = False
            temp += char
            validation(temp)
            temp = ""
            continue
        plusFlag = False
        validation(temp)
        temp = ""
        temp += char
        continue


    # minus tokkens
    # elif char == "-":
    #     if not minusFlag:
    #         validation(temp)
    #         temp = ""
    #         minusFlag = True
    #         temp += char
    #         continue
    #     elif minusFlag:
    #         if char == "-":
    #             minusFlag = False
    #             temp += char
    #             validation(temp)
    #             temp = ""
    #             continue
    # elif char != "-" and minusFlag:
    #     minusFlag = False
    #     validation(temp)
    #     temp = ""
    #     temp += char
    #     continue

    elif char == "-":
        if not minusFlag:
            validation(temp)
            temp = ""
            minusFlag = True
            temp += char
            continue
        validation(temp)
        temp = ""
        minusFlag = True
        temp += char
        continue


    elif char != "-" and minusFlag:
        if char == "=":
            minusFlag = False
            temp += char
            validation(temp)
            temp = ""
            continue
        minusFlag = False
        validation(temp)
        temp = ""
        temp += char
        continue
    # greater than sign
    elif char == "<":
        if not greaterFlag:
            validation(temp)
            temp = ""
            greaterFlag = True
            temp += char
            continue
        validation(temp)
        temp = ""
        temp += char
        greaterFlag = True
        continue

    elif char != "<" and greaterFlag:
        if char == "=":
            greaterFlag = False
            temp += char
            validation(temp)
            temp = ""
            continue
        greaterFlag = False
        validation(temp)
        temp = ""
        temp += char
        continue

    # less than sign
    elif char == ">":
        if not lessFlag:
            validation(temp)
            temp = ""
            lessFlag = True
            temp += char
            continue
        validation(temp)
        temp = ""
        temp += char
        lessFlag = True
        continue
    elif char != ">" and lessFlag:
        if char == "=":
            lessFlag = False
            temp += char
            validation(temp)
            temp = ""
            continue
        lessFlag = False
        validation(temp)
        temp = ""
        temp += char
        continue

    elif char == "=" and not assignFlag:
        validation(temp)
        temp = ""
        assignFlag = True
        temp += char
        continue
    elif char != "=" and assignFlag:
        validation(temp)
        temp = ""
        temp += char
        assignFlag = False
        continue
    elif char == "=" and assignFlag:
        if len(temp) == 1:
            temp += char
            validation(temp)
            temp = ""
            assignFlag = False
            continue
        validation(temp)
        temp = ""
        temp += char
        assignFlag = False
        continue

    elif char == ";":
        validation(temp)
        validation(char)
        temp = ""
        continue

    elif char in punc \
            or char in MDD_OP \
            or char in ASSIGN_OP:
        validation(temp)
        validation(char)
        temp = ""
        continue
    temp += char


fileWrite("end-mark", "$")
file.close()
tokkens.close()
