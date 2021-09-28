"""Linn Cao Nguyen Phuong
   Nov 10th, 2020
   Section A
   Lab 9: Classes
   CS151
"""
#version 2

import sys

class Lsystem:
    def __init__(self, filename = None):
        """Sets an empty string for the base
           Sets an empty list for the rules
           Reads the file
        """
        self.base = ''
        self.rules = []
        if filename != None:
            self.read(filename)


    def getBase(self):
        """Returns the value of base field
        """
        return self.base


    def setBase(self, b):
        """Assigns value b to base field
        """
        self.base = b


    def getRule(self, index):
        """Returns specified rule from rules field
        """
        return self.rules[index]


    def addRule(self, newrule):
        """Appends new rule to rules field
        """
        self.rules.append(newrule)


    def numRules(self):
        """Returns number of rules in rules list
        """
        return len(self.rules)


    def read(self, filename):
        """Opens the file
           Reads the L-system information
           Stores the information in appropriate fields
        """
        self.rules = []
        fp = open(filename, 'r')
        for line in fp:
            line = line.strip()
            words = line.split()
            if words[0] == 'base':
                self.setBase(words[1])
            elif words[0] == 'rule':
                self.addRule(words[1:])
        fp.close()


    def replace(self, istring):
        """Tests matching rules for characters
           Adds replacement to new string if a rule exists
        """
        tstring = ''
        for c in istring:
            found = False
            for rule in self.rules:
                if rule[0] == c:
                    tstring = tstring + rule[1]
                    found = True
                    break
                else:
                    tstring = tstring + c
        return tstring


    def buildString(self, iterations):
        """Return a string generated by applying the L-system rules n times
        """
        nstring = self.base
        for i in range(iterations):
            nstring = self.replace(nstring)
        return nstring

    
def main(argv):
    """Tests Lsystem class
       Prints the Lsystem
    """
    if len(argv) < 2:
        print('Usage: lsystem.py <filename>')
        exit()
    filename = argv[1]
    iterations = 2
    lsys = Lsystem()
    lsys.read(filename)
    print(lsys)
    print(lsys.getBase())
    for i in range(lsys.numRules()):
        rule = lsys.getRule(i)
        print(rule[0] + ' -> ' + rule[1])
    lstr = lsys.buildString(iterations)
    print(lstr)
    return


if __name__ == "__main__":
    main(sys.argv)