import unittest
import mid_char

class TestMid_char(unittest.TestCase):

    def test_short_word(self):
        word = 'test'
        result = mid_char.get_middle(word)
        self.assertEqual(result, 'es')

if __name__ == '__main__':
    unittest.main()
