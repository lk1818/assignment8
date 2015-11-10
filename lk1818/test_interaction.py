import unittest
from interaction import *
from unittest import TestCase


''' Test whether the error handling pops up in a correct way, and whether the prompted input are transferred into what we need. '''
class InputTest(TestCase):

    def test_valid_input_list(self):
        a = '[1, 10, 100, 1000]'
        self.assertEqual(get_list(a), [1, 10, 100, 1000])
   
  
    def test_invalid_input_list(self):
        b = 'aaaa'
        self.assertRaises(InvalidListException, get_list, b)
   
        c = '[12,3'
        self.assertRaises(InvalidListException, get_list, c)

  
        d = '[12, 3]'
        self.assertRaises(InvalidPositionException, get_list, d) 
  
        f = '[1, a]'
        self.assertRaises(InvalidIntegerException, get_list, f)

    
    def test_valid_num_trials(self):
        g = '10000'
        self.assertEqual(get_int(g), 10000)

   
    def test_invalid_num_trials(self):
        h = '-1'
        self.assertRaises(InvalidIntegerException, get_int, h)

        i = 'a'
        self.assertRaises(InvalidIntegerException, get_int, i)


if __name__ == '__main__':
    unittest.main()
