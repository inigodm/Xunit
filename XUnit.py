#!/bin/python
import sys
import traceback
import inspect

class TestSuite:
    def __init__ (self):
        self.tests = []
    def add(self, testCase):
        self.tests.append(testCase)
    
    def run(self, result):
        for test in self.tests:
            test.run(result)
        return result

def build_assertion_error_msg():
    frame, filename, line_num, func, source_code, source_index = inspect.trace()[-1]
    code = source_code[source_index].strip().replace('assert ', '')        
    if '==' in code:
        res = obtain_token_values_from_frame(code.split('=='), frame)
        #print tokens[0].strip() in inspect.getargvalues(frame).locals
    return 'An assertion error occurred on file {} on line {} while asserting {} {}'.format(filename, line_num, code, res)        

def obtain_token_values_from_frame(tokens, frame):
    res = ""
    for tok in tokens:
        stripped = tok.strip()
        if stripped in inspect.getargvalues(frame).locals:
            res += build_log_for_field(tok, frame)
        elif stripped.split(".")[0] in inspect.getargvalues(frame).locals:
            res += build_log_for_obj_method(tok, frame)
        else:
            res += build_log_for_constant(tok, frame)
    return res

def build_log_for_obj_method(tok, frame):
    toks = tok.split('.')
    obj = None
    print tok
    for t in toks:
        if (obj == None):
            obj = inspect.getargvalues(frame).locals[t.strip()]
        else:
            obj = getattr(obj, t)
    return "\n{} = {}".format(tok, obj)
    
def build_log_for_field(tok, frame):
    return "\n{} = {}".format(tok.strip(), inspect.getargvalues(frame).locals[tok.strip()])

def build_log_for_constant(tok, frame):
    return "\n{} = {}".format(tok.strip(), tok.strip())

class TestCase:
    def __init__(self, name):
        self.name = name
        
    def run(self, result):
        result.testStarted()
        try:
            self.setUp()
            method = getattr(self, self.name)
            method()
        except AssertionError:
            result.addError(build_assertion_error_msg())
        except Exception, e:
            result.addError(e.args[0])
        self.tearDown()
        return result
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errormessages = []

    def testStarted(self):
        self.runCount += 1

    def addError(self, msg):
        self.errormessages.append(msg)
    
    def errorCount(self):
        return len(self.errormessages)

    def errorMsgs(self, index = -1):
        if (index == -1):
            return self.errormessages
        else:
            if index > len(self.errormessages) - 1:
                return "No such error"
            else:
                return self.errormessages[index]

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount())

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