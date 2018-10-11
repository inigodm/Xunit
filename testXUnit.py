from XUnit import WasRun, TestCase, TestResult

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert(self.test.log == "Setup testMethod tearDown ")

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert (result.summary() == "1 run, 0 failed")
    
    def testFailedResultFormating(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert (result.summary() == "1 run, 1 failed")

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert (result.summary() == "1 run, 1 failed")

    def testSuite(self):
        suite = TestSuite()
        suite.add(TestCaseTest("testMethod"))
        suite.add(TestCaseTest("testMethod"))
        suite.add(TestCaseTest("testBrokenMethod"))
        result = suite.run()
        assert (result.summary() == "3 run, 1 failed")

print TestCaseTest("testTemplateMethod").run().summary()
print TestCaseTest("testResult").run().summary()
print TestCaseTest("testFailedResultFormating").run().summary()
print TestCaseTest("testFailedResult").run().summary()