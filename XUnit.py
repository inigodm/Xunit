#!/bin/python
class WasRun:
    def __init__(self, name):
        self.wasRun = False

    def run(self):
        self.testMethod()

    def testMethod(self):
        self.wasRun = True