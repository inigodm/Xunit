from XUnit import WasRun, TestCase, TestResult, TestSuite

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        result = TestResult()
        test = WasRun("testMethod")
        test.run(result)
        assert(test.log == "Setup testMethod tearDown ")

    def testResult(self):
        result = TestResult()
        test = WasRun("testMethod")
        result = test.run(result)
        assert (result.summary() == "1 run, 0 failed")
        assert result.errorMsgs() == []
        assert result.errorMsgs(0) == "No such error"

    
    def testFailedResult(self):
        result = TestResult()
        test = WasRun("testBrokenMethod")
        result = test.run(result)
        assert test.log == "Setup testBrokenMethod tearDown "
        assert result.summary() == "1 run, 1 failed"
        assert result.errorMsgs(0) == "NotImplemented"
        assert 1 == 2
        assert "in statement assert 1 == 2" in result.errorMsgs(0)
        

    def testSuite(self):
        suite = TestSuite()
        suite.add(TestCaseTest("testTemplateMethod"))
        suite.add(TestCaseTest("testTemplateMethod"))
        suite.add(TestCaseTest("testBrokenMethod"))
        result = TestResult()
        suite.run(result)
        assert (result.summary() == "3 run, 1 failed")

suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testSuite"))
result = TestResult()
suite.run(result)
print result.errorMsgs()
print result.summary()