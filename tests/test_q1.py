"""Tests for Lab 0 Question 1"""

import sys
sys.path.append(".")
import unittest
from src.q1 import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_simple_palindrome(self) -> None:
        """Test a simple palindrome"""
        self.assertTrue(is_palindrome("racecar"))
    
    def test_not_palindrome(self) -> None:
        """Test a non-palindrome"""
        self.assertFalse(is_palindrome("hello"))
    
    def test_with_spaces(self) -> None:
        """Test palindrome with spaces"""
        self.assertTrue(is_palindrome("race car"))
    
    def test_with_punctuation(self) -> None:
        """Test palindrome with punctuation"""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
    
    def test_mixed_case(self) -> None:
        """Test with mixed case"""
        self.assertTrue(is_palindrome("RaceCar"))
    
    def test_empty_string(self) -> None:
        """Test empty string"""
        self.assertTrue(is_palindrome(""))
    
    def test_single_character(self) -> None:
        """Test single character"""
        self.assertTrue(is_palindrome("a"))

if __name__ == '__main__':
    unittest.main()
