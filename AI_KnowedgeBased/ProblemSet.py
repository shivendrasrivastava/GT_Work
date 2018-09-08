# DO NOT MODIFY THIS FILE.
#
# Any modifications to this file will not be used when grading your project.
# If you have any questions, please contact the TAs.
#
#

import random
import re
import os
import json
from RFigure import RFigure
from RObject import RObject
from RProblem import RProblem

# A list of RavensProblems within one set.
#
# Your agent does not need to use this class explicitly.
class ProblemSet:
    # Initializes a new ProblemSet with the given name, an empty set of
    # problems, and a new random number generator.
    #
    # Your agent does not need to use this method.
    #
    # @param name The name of the problem set.
    def __init__(self,name):
        # The name of the problem set.
        self.name=name

        # A list of the problems in the problem set.
        self.problems=[]

        self.loadProblemSet()

    # Loads the problem set from the folder whose name matches that of this
    # problem set.
    #
    # Your agent does not need to use this method.
    def loadProblemSet(self):
        r = open("Problems" + os.sep + self.name + os.sep + "ProblemList.txt")
        line = self.getNextLine(r)
        while not line=="":
            self.loadProblem(line)
            line=self.getNextLine(r)

    def loadProblem(self, problemName):
        data_filename = "Problems" + os.sep + self.name + os.sep + problemName + os.sep + "ProblemData.txt"

        with open(data_filename) as r:
            problemType=self.getNextLine(r)

            hasVisual=self.getNextLine(r)=="true"
            hasVerbal=self.getNextLine(r)=="true"

            newProblem=RProblem(problemName, problemType, self.name, hasVisual, hasVerbal)
            if newProblem.hasVerbal:
                figures=[]
                currentFigure=None
                currentObject=None

                line = self.getNextLine(r)
                while not line=="":
                    if not line.startswith("\t"):
                        newFigure=RFigure(line, problemName, self.name)
                        figures.append(newFigure)
                        currentFigure=newFigure
                    elif not line.startswith("\t\t"):
                        line=line.replace("\t","")
                        newObject=RObject(line)
                        currentFigure.objects[line]=newObject
                        currentObject=newObject
                    elif line.startswith("\t\t"):
                        line=line.replace("\t","")
                        split=re.split(":",line)
                        currentObject.attributes[split[0]]=split[1]
                    line=self.getNextLine(r)
                for figure in figures:
                    newProblem.figures[figure.name]=figure
            else:
                newProblem.figures["A"]=RFigure("A", problemName, self.name)
                newProblem.figures["B"]=RFigure("B", problemName, self.name)
                newProblem.figures["C"]=RFigure("C", problemName, self.name)
                newProblem.figures["1"]=RFigure("1", problemName, self.name)
                newProblem.figures["2"]=RFigure("2", problemName, self.name)
                newProblem.figures["3"]=RFigure("3", problemName, self.name)
                newProblem.figures["4"]=RFigure("4", problemName, self.name)
                newProblem.figures["5"]=RFigure("5", problemName, self.name)
                newProblem.figures["6"]=RFigure("6", problemName, self.name)
                if newProblem.problemType=="3x3":
                    newProblem.figures["D"]=RFigure("D", problemName, self.name)
                    newProblem.figures["E"]=RFigure("E", problemName, self.name)
                    newProblem.figures["F"]=RFigure("F", problemName, self.name)
                    newProblem.figures["G"]=RFigure("G", problemName, self.name)
                    newProblem.figures["H"]=RFigure("H", problemName, self.name)
                    newProblem.figures["7"]=RFigure("7", problemName, self.name)
                    newProblem.figures["8"]=RFigure("8", problemName, self.name)
            self.problems.append(newProblem)

    # Returns the total number of problems answered in this set in a certain
    # type.
    def getTotal(self,result):
        count=0;
        for problem in self.problems:
            if problem.getCorrect()==result:
                count+=1
        return count

    def tryParseInt(self, i):
        try:
            int(i)
            return True
        except:
            return False

    def getNextLine(self, r):
        return r.readline().rstrip()
