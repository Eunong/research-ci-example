import unittest

import main

class MainTest(unittest.TestCase):
    def test_helloworld(self):
        ret = main.helloworld("Test")
        print(f"main.helloworld return : {ret}")
        print(ret)
        self.assertEqual(ret, "Hello World Test123")

if __name__ == "__main__":
    unittest.main()