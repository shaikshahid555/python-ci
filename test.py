import unittest
from app import message

class AppTests(unittest.TestCase):
    def test_message(self):
        self.assertEqual(message(), "Hello from Python CI")

if __name__ == "__main__":
    unittest.main()
