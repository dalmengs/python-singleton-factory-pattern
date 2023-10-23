from Controller.TestController import TestController
from Service.TestService import TestService

if __name__ == "__main__":
    testController1 = TestController()
    testController2 = TestController()
    testService1 = TestService()
    testService2 = TestService()

    # Check if each instances are same by singleton pattern
    print(testController1 == testController2)
    print(testService1 == testService2)