class TestCase:
    def __init__(self,name):
        self.name = name

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

    def setUp(self):
        pass

class WasRun(TestCase):
    def __init__(self,name):
        self.wasRun = None
        TestCase.__init__(self,name)

    def testMethod(self):
        self.wasRun = 1

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testSetUp(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetUp)

    def testRunning(self):
        test = WasRun("testMethod")
        #assert(not test.wasRun) setUp으로 인해 지워짐
        test.run()
        assert(test.wasRun)

TestCaseTest("testSetUp").run()
TestCaseTest("testRunning").run()
