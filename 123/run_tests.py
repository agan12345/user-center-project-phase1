import unittest

if __name__ == "__main__":
    tests = unittest.defaultTestLoader.discover("testcases", pattern="test_*.py")
    runner = unittest.TextTestRunner()
    runner.run(tests)