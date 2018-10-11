from XUnit import WasRun, TestCase

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert(self.test.log == "Setup testMethod tearDown ")

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert (result.summary() == "1 run, 0 failed")

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()