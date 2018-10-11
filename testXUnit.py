from XUnit import WasRun, TestCase

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
        return self

    def testRunning(self):
       assert (not self.test.wasRun)
       self.test.run()
       assert (self.test.wasRun)
    
    def testSetup(self):
       self.test.run()
       assert(self.test.wasSetup)

TestCaseTest("testRunning").setUp().run()
TestCaseTest("testSetup").setUp().run()