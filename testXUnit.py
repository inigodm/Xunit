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
        r = 2
        assert test.log == "Setup testBrokenMethod tearDown "
        assert result.summary() == "1 run, 1 failed"
        assert result.errorMsgs(0) == "NotImplemented"
        assert 1 == r 
        
    def testErrors2(self):
        au = aux(1, 2)
        assert 2 == au.c()

    def testErrors3(self):
        au = aux(1, 2)
        assert 3 == au.b

    def testErrors4(self):
        au = aux(1, 2)
        assert 3 == au.d("lala")

    def testSuite(self):
        suite = TestSuite()
        suite.add(TestCaseTest("testTemplateMethod"))
        suite.add(TestCaseTest("testTemplateMethod"))
        suite.add(TestCaseTest("testBrokenMethod"))
        result = TestResult()
        suite.run(result)
        assert (result.summary() == "3 run, 1 failed")

class aux:
    def __init__(self, a , b):
        self.a = a
        self.b = b
    def c(self):
        return "dedo"
    def d(self, dede):
        return "d es " + dede

suite = TestSuite()
suite.addAll(TestCaseTest)
result = TestResult()
suite.run(result)
print result.errorMsgs(0)
print result.errorMsgs(1)
print result.errorMsgs(2)
#assert " while asserting 1 == r" in result.errorMsgs(0)
print result.summary()