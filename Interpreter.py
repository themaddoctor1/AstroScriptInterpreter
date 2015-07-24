import sys


##Makes the program easier to work with.
def interpretFile(file):
    lines = ""
    for line in file:
        lines = lines + line

    return lines.splitlines()

##Runs a single line of code.
def runLine(program = [""], RAM = {}):
    #The current line
    currentLine = program[0]

    if currentLine.startswith("for "):
        lastLine = 1;
        for i in range(1, len(program)):
            lastLine = i;
            if program[i] == "endfor":
                break

        subProgram = []

        for i in range(1, lastLine):
            subProgram.append(program[i][4:])

        for i in range(int(currentLine[4:])):
            runProgram(subProgram, RAM)

        return program[lastLine+1:len(program)]

    else:
        if currentLine.startswith("print "):
            print(str(valueOf(currentLine[6:], RAM)))
        elif currentLine.startswith("$"):
            endIndex = currentLine.index("$ ")
            name = currentLine[1:endIndex]

            RAM[name] = valueOf(currentLine[currentLine.index(" = ") + 3:], RAM)

        return program[1:]




##Takes charge of running the whole program.
def runProgram(program, RAM = {}):
    #Tracks what is left.
    progLeft = program[:]

    #Runs until nothing is left to be done.
    while len(progLeft) > 0:
        progLeft = runLine(progLeft, RAM)

#Interprets a value for the program.
def valueOf(value, RAM):
    newValue = str(value)

    print(newValue)

    #Plug in variables
    while "$" in newValue:

        #First, find the range inside of which the variable is stored.
        firstIndex = -1
        secondIndex = -1

        for i in range(len(newValue)):
            if newValue[i] == "$":
                if(firstIndex < 0):
                    firstIndex = i
                else:
                    secondIndex = i
                    break

        #Then, get the name of the variable.
        varName = newValue[firstIndex+1:int(secondIndex)]

        #Finally, put the value in the place of the placeholder.
        newValue = newValue.replace("$" + varName + "$", str(RAM[varName]))

    if newValue.startswith("#{"):

        #Isolates the function.
        function = newValue[2:newValue.index("}")] + " "

        ##Removes unnecessary blank spaces.
        while function[0] == " ":
            function = function[1:]
        while function[len(function)-2] == " ":
            function = function[:len(function)-2] + " "

        newValue = function

        if("(" in function):
            #First, find the range inside of which the parentheses set is located.
            startIndex = function.index("(")+1
            endIndex = -1
            count = 0

            for i in range(startIndex, len(function)):
                if newValue[i] == "(":
                    count += 1
                else:
                    endIndex = i
                    count -= 1
                if(count < 0):
                    break

            return int("# " + str(function[0:startIndex-1] + valueOf(function[startIndex,endIndex])) + function[endIndex+1])

        testIndex = 1

        while testIndex < len(function)-1:
            ch = function[testIndex]
            if ch == "^" or ch == "*" or ch == "/" or ch == "+" or ch == "-":
                if function[testIndex+1] != " ":
                    function = function[0:testIndex+1] + " " + function[testIndex+1:]
                if function[testIndex-1] != " ":
                    function = function[0:testIndex] + " " + function[testIndex:]
            testIndex += 1

        valueList = []
        valueList.append(str(function[0: function.index(" ")]))
        tempFunction = function[function.index(" ")+1:]

        while len(tempFunction) > 0:
            item = tempFunction[0:tempFunction.index(" ")]
            valueList.append(item)
            tempFunction = tempFunction[tempFunction.index(" ") + 1:]


        for i in range(1, len(valueList)-1):
            if valueList[i] == "^":
                valueList[i] = float(valueList[i-1]) ** float(valueList[i+1])
                newList = valueList[:i-1]
                newList.append(valueList[i])
                for v in newList[i+2:]:
                    newList.append(v)
                valueList = newList[:]

        for i in range(1, len(valueList)-1):
            if valueList[i] == "*":
                valueList[i] = float(str(valueList[i-1])) * float(str(valueList[i+1]))
                newList = valueList[:i-1]
                newList.append(valueList[i])
                for v in newList[i+2:]:
                    newList.append(v)
                valueList = newList[:]
            elif valueList[i] == "/":
                valueList[i] = float(valueList[i-1]) / float(valueList[i+1])
                newList = valueList[:i-1]
                newList.append(valueList[i])
                for v in newList[i+2:]:
                    newList.append(v)
                valueList = newList[:]

        for i in range(1, len(valueList)-1):
            if valueList[i] == "+":
                valueList[i] = float(valueList[i-1]) + float(valueList[i+1])
                newList = valueList[:i-1]
                newList.append(valueList[i])
                for v in newList[i+2:]:
                    newList.append(v)
                valueList = newList[:]
            elif valueList[i] == "-":
                valueList[i] = float(valueList[i-1]) - float(valueList[i+1])
                newList = valueList[:i-1]
                newList.append(valueList[i])
                for v in newList[i+2:]:
                    newList.append(v)
                valueList = newList[:]

        if len(valueList) == 1:
            return valueList[0]
        else:
            newValue = ""
            for c in valueList:
                newValue += str(str(c) + " ")
            return valueOf("#{" + newValue[:len(newValue)], RAM)



    return newValue


#Opens up the file containing the program
file = open("C:/Users/Christopher/Documents/PycharmProjects/AstroScriptInterpreter/program.txt")

#Transcribes the program into an array
programLines = interpretFile(file)

runProgram(programLines)

sys.exit()

