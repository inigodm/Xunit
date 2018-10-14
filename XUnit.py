#!/bin/python

class TestSuite:
    def __init__ (self):
        self.tests = []
    def add(self, testCase):
        self.tests.append(testCase)
    
    def run(self, result):
        for test in self.tests:
            test.run(result)
        return result

class TestCase:
    def __init__(self, name):
        self.name = name
        
    def run(self, result):
        result.testStarted()
        try:
            self.setUp()
            method = getattr(self, self.name)
            method()
        except Exception, e:
            result.testFailed()
            result.addError(e)
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
        self.errormessages = []

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.errorCount += 1

    def addError(self, msg):
        self.errormessages += msg
    
    def errorMsgs(self, index = -1):
        if (index == -1):
            return self.errormessages
        else:
            if index > len(self.errormessages) - 1:
                return "No such error"
            else:
                return self.errormessages[index]

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)

class WasRun(TestCase):
    def __init__(self, name):
        self.log = ""
        TestCase.__init__(self, name)

    def testMethod(self):
        self.log += "testMethod "

    def testBrokenMethod(self):
        self.log += "testBrokenMethod "
        raise Exception("NotImplemented")

    def setUp(self):
        self.log += "Setup "
    
    def tearDown(self):
        self.log += "tearDown "