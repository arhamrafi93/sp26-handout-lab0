"""Tests for Lab 0 Question 1"""

import sys
sys.path.append(".")
import unittest
from src.q1 import is_palindrome

def TestIsPalindrome(unittest.TestCase):
    """
    Test a simple palindorme
    """
    self.assertTrue(is_palindrome("racecar"))

def test_not_palindrome(self):
    """ Test a non-palindrome"""
    self.assertFalse(is_palindrome("hello"))

def test_with_spaces(self):
        """Test palindrome with spaces"""
        self.assertTrue(is_palindrome("race car"))
    
def test_with_punctuation(self):
        """Test palindrome with punctuation"""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
    
def test_mixed_case(self):
        """Test with mixed case"""
        self.assertTrue(is_palindrome("RaceCar"))
    
def test_empty_string(self):
        """Test empty string"""
        self.assertTrue(is_palindrome(""))
    
def test_single_character(self):
        """Test single character"""
        self.assertTrue(is_palindrome("a"))


if __name__ == '__main__':
    unittest.main()