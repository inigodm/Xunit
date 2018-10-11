#!/bin/python
class WasRun:
    def __init__(self, name):
        self.wasRun = False
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()

    def testMethod(self):
        self.wasRun = True