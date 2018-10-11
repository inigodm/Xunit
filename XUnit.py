#!/bin/python
class TestCase:
    def __init__(self, name):
        self.name = name
        self.wasSetup = False
        
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
    
    def setUp(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = False
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = True

    def setUp(self):
        self.wasRun = False
        self.wasSetup = True