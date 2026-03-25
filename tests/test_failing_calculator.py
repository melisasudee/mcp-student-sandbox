"""
TDD Test Suite for failing_calculator.py
Red Phase: Tests should FAIL until the bug is fixed
"""
import unittest
import sys
from pathlib import Path

# Parent dizini sys.path'a ekle
sys.path.insert(0, str(Path(__file__).parent.parent))

from failing_calculator import average_ratios


class TestAverageRatiosRedPhase(unittest.TestCase):
    """Test cases that should FAIL with the broken code"""
    
    def test_normal_numbers_without_zero(self):
        """Test with normal positive numbers (no zeros)"""
        result = average_ratios([10, 5, 2])
        # 100/10 + 100/5 + 100/2 = 10 + 20 + 50 = 80
        # 80 / 3 ≈ 26.67
        self.assertAlmostEqual(result, 26.666666666, places=5)
    
    def test_single_number(self):
        """Test with single positive number"""
        result = average_ratios([10])
        self.assertEqual(result, 10.0)
    
    def test_with_zero_should_not_crash(self):
        """
        CRITICAL TEST: [10, 5, 0] should NOT raise ZeroDivisionError
        After fix: zeros are skipped, function returns normally
        """
        # This should NOT raise ZeroDivisionError after fix
        try:
            result = average_ratios([10, 5, 0])
            self.assertIsNotNone(result)
            self.assertAlmostEqual(result, 15.0, places=5)
        except ZeroDivisionError:
            self.fail("average_ratios should not crash with zero in list")
    
    def test_zero_handling_expected_output(self):
        """
        After fix: zeros should be skipped
        With [10, 5, 0] → only process [10, 5]
        (100/10 + 100/5) / 2 = (10 + 20) / 2 = 15.0
        """
        result = average_ratios([10, 5, 0])
        self.assertAlmostEqual(result, 15.0, places=5)
    
    def test_all_zeros_should_not_crash(self):
        """All zeros should be handled gracefully (return 0)"""
        result = average_ratios([0, 0, 0])
        self.assertEqual(result, 0)
    
    def test_mixed_with_multiple_zeros(self):
        """Zeros at different positions"""
        result = average_ratios([0, 20, 0, 10])
        # Valid: [20, 10] → (100/20 + 100/10) / 2 = (5 + 10) / 2 = 7.5
        self.assertAlmostEqual(result, 7.5, places=5)
    
    def test_empty_list(self):
        """Empty list should return 0"""
        result = average_ratios([])
        self.assertEqual(result, 0)
    
    def test_large_numbers(self):
        """Test with larger numbers"""
        result = average_ratios([100, 50, 25])
        # 100/100 + 100/50 + 100/25 = 1 + 2 + 4 = 7
        # 7 / 3 ≈ 2.33
        self.assertAlmostEqual(result, 2.333333, places=5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
