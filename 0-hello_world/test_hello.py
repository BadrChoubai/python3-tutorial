import unittest
from hello import hello


class TestHello(unittest.TestCase):
    def test_output_is_hello_word(self):
        self.assertEquals(hello(), 'Hello, World!')


if __name__ == "__main__":
    unittest.main()
