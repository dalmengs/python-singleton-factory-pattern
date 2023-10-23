from Singleton import Singleton

@Singleton
class TestService:
    def info(self):
        print("Test Service")