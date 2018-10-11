from XUnit import WasRun, TestCase

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
       self.test = WasRun("testMethod")
       self.test.run()
       assert(self.test.log == "Setup testMethod tearDown")

TestCaseTest("testTemplateMethod").run()