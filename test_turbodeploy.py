# test_turbodeploy.py
"""
Tests for TurboDeploy module.
"""

import unittest
from turbodeploy import TurboDeploy

class TestTurboDeploy(unittest.TestCase):
    """Test cases for TurboDeploy class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TurboDeploy()
        self.assertIsInstance(instance, TurboDeploy)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TurboDeploy()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
