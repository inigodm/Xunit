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

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
TestCaseTest("testFailedResultFormating").run()
TestCaseTest("testFailedResult").run()