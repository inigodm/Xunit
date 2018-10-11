#!/bin/python
class TestCase:
    def __init__(self, name):
        self.name = name
        
    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.errorCount += 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)

class WasRun(TestCase):
    def __init__(self, name):
        self.log = ""
        TestCase.__init__(self, name)

    def testMethod(self):
        self.log += "testMethod "

    def testBrokenMethod(self):
        raise Exception

    def setUp(self):
        self.log += "Setup "
    
    def tearDown(self):
        self.log += "tearDown "