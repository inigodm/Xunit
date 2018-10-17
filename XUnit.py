#!/bin/python
import sys
import traceback
import inspect

class TestSuite:
    def __init__ (self):
        self.tests = []

    def addAll(self, clazz):
        members = inspect.getmembers(clazz, predicate=inspect.ismethod)
        for member in members:
            self.__addTests__(clazz, member)

    def add(self, testCase):
        self.tests.append(testCase)
    
    def run(self, result):
        for test in self.tests:
            test.run(result)
        return result
    
    def __addTests__(self, clazz, member):
        if member[0].startswith('test'):
            self.add(clazz(member[0]))

def build_assertion_error_msg():
    frame, filename, line_num, _, source_code, source_index = inspect.trace()[-1]
    code = source_code[source_index].strip().replace('assert ', '')        
    if '==' in code:
        res = obtain_token_values_from_frame(code.split('=='), frame)
    return 'An assertion error occurred on file {} on line {} while asserting {} {}'.format(filename, line_num, code, res)        

def obtain_token_values_from_frame(tokens, frame):
    return "".join([format(name, value) for name, value in calc_value_for_token(tokens, frame)])
    
def calc_value_for_token(tokens, frame):
    res = []
    for token in tokens:
        stripped = token.strip()
        try:
            res.append((stripped, calc_method_or_field_value(stripped, frame)))
        except Exception, e:
            #traceback.print_exc()
            res.append(("const", stripped))
    return res

def calc_method_or_field_value(tok, frame):
    if tok.endswith(")"):
        return calc_method_value(tok, frame)
    else:
        return calc_field_value(tok, frame)

def calc_method_value(tok, frame):
    method = obtain_method_or_field(tok[:tok.rfind('(')], frame)
    argsDict = calc_arguments(tok, frame, method)
    return method(**argsDict)

def calc_arguments(tok, frame, method):
    res = {}
    for param_name, param_value in zip(inspect.getargspec(method)[0][1:], calc_value_for_token(get_args(tok), frame)[0][1:]):
        res[param_name] = param_value
    return res

def get_args(tok):
    return [s.strip() for s in tok[tok.find('(') + 1:tok.find(')')].split(",")]

def calc_field_value(tok, frame):
    return obtain_method_or_field(tok, frame)

def obtain_method_or_field(name, frame):
    toks = name.split('.')
    obj = None
    for t in toks:
        if (obj == None):
            obj = inspect.getargvalues(frame).locals[t.strip()]
        else:
            obj = getattr(obj, t)
    return obj

def format_to_console(code, value):
    return "\n{} = {}".format(code, value)

format = format_to_console

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