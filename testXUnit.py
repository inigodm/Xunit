from XUnit import WasRun, TestCase

class TestCaseTest(TestCase):
    def testRunning(self):
       test = WasRun("testMethod")
       assert (not test.wasRun)
       test.run()
       assert (test.wasRun)
    
    def testSetup(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetup)

TestCaseTest("testRunning").run()
TestCaseTest("testSetup").run()