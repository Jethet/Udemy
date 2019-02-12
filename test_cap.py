# Here we use unittest: start with testing simple things and then to to more
# complex things.

import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)   # you call the function you want to test
        self.assertEqual(result, 'Python')

    def test_multip_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()
