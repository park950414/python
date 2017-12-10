# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 20:37:38 2017

@author: park
"""

class Student:
    def __init__(self,name,hours,qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
    
    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

def makeStudent(infoStr):
    name,hours,qpoints = infoStr.split("\t")
    return Student(name,hours,qpoints)

def main():
    filename = input("Enter name the grade file:")
    infile = open(filename,"r")
    best = makeStudent(infile.readline())
    for line in infile:
        s = makeStudent(line)
        if s.gpa() > best.gpa():
            best = s
    infile.close()
    print("The best student is :",best.getName())
    print("hours:",best.getHours())
    print("GPA:",best.gpa())
    
main()