import random
import unittest
from unique_chars import repeat_chars, unique_chars_set
from permutations import permutations
from counters import counts, counts_defaultdict, counts_counter
from palindrome import palindrome
from compress_string import compress_string, delete_string
from sort_search import *


class UniqueCharsTestCase(unittest.TestCase):
    """ https://github.com/donnemartin/interactive-coding-challenges#arrays-and-strings """
    
    def test_repeat_chars(self):
        self.assertTrue(repeat_chars(''))
        self.assertFalse(repeat_chars('foo'))
        self.assertTrue(repeat_chars('bar'))
    
    def test_unique_chars(self):
        self.assertTrue(unique_chars_set(''))
        self.assertFalse(unique_chars_set('foo'))
        self.assertTrue(unique_chars_set('bar'))

    def test_permutations(self):
        self.assertTrue(permutations('act', 'cat'))
        self.assertFalse(permutations('', 'foo'))
        self.assertFalse(permutations('Nib', 'bin'))
        self.assertTrue(permutations('a ct', 'ca t'))
        self.assertTrue(permutations('', ''))

    def test_counts(self):
        self.assertEqual(counts('hundred'), ['d'])
        self.assertEqual(set(counts('mississippi')), set(['s', 'i']))
        self.assertEqual(counts(''), [])

    def test_counts_defaultdict(self):
        self.assertEqual(counts_defaultdict('hundred'), ['d'])
        self.assertEqual(set(counts_defaultdict('mississippi')), set(['s', 'i']))
        self.assertEqual(counts_defaultdict(''), [])

    def test_counts_counter(self):
        self.assertEqual(counts_counter('hundred'), ['d'])
        self.assertEqual(set(counts_counter('mississippi')), set(['s', 'i']))
        self.assertEqual(counts_counter(''), [])

    def test_palindrome(self):
        self.assertTrue(palindrome('32123'))
        self.assertFalse(palindrome('hello'))
        self.assertTrue(palindrome('Sore was I ere I saw Eros'))

    def test_compress_string(self):
        self.assertEqual(compress_string(''), '')
        self.assertEqual(compress_string(None), None)
        self.assertEqual(compress_string('AABBCC'), 'AABBCC')
        self.assertEqual(compress_string('AAABCCDDDD'), 'A3BC2D4')

    def test_delete_string(self):
        self.assertEqual(delete_string('AABBCCAADD', 'A'), 'BBCCDD')
        self.assertEqual(delete_string('AAAAZZZZFGDFG', 'Z'), 'AAAAFGDFG')

    def test_bubble_sort(self):
        test_list = random.sample(xrange(1000), 100)

        self.assertEqual(bubble_sort(test_list), sorted(test_list))

    def test_selection_sort(self):
        test_list = random.sample(xrange(1000), 100)
        self.assertEqual(selection_sort(test_list), sorted(test_list))

if __name__ == '__main__':
    unittest.main()
