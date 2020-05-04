import unittest
from mutate_tuple import mutate_tuple


class TestMutateTuple(unittest.TestCase):

    def test_return_type_is_tuple(self):
        self.assertIsInstance(mutate_tuple((0, 1), 1, 0), tuple)

    def test_changes_are_made(self):
        actual = mutate_tuple(('foo', 'bar', 'baz'), 'boo', 0)
        expected = ('boo', 'bar', 'baz')
        self.assertEqual(actual, expected)

    def test_single_value_in_tuple(self):
        '''This is tough but you can pass this using the `isinstance()` function'''
        self.assertEqual(mutate_tuple((1), 0, 0), 0)


if __name__ == "__main__":
    unittest.main()
