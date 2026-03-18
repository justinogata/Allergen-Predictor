import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from allergen_predictor.feature_extractor import extract_all_features

class TestFeatureExtractor(unittest.TestCase):
    
    def setUp(self):
        # A short and valid amino acid sequence to use for testing
        self.test_sequence = "MVLSPADKTN"

    def test_returns_dictionary(self):
        """Test that the function returns a dictionary object."""
        result = extract_all_features(self.test_sequence)
        self.assertIsInstance(result, dict, "The function should return a dictionary.")

    def test_contains_all_keys(self):
        """Test that the dictionary contains all 5 required physiochemical properties."""
        result = extract_all_features(self.test_sequence)
        expected_keys = [
            'Molecular weight', 
            'Isoelectric point', 
            'Instability index', 
            'Aromaticity', 
            'Gravy'
        ]
        
        for key in expected_keys:
            self.assertIn(key, result, f"Missing key in output: {key}")

    def test_computes_valid_floats(self):
        """Test that the computed values are numerical (floats)."""
        result = extract_all_features(self.test_sequence)
        
        # Verify that the values aren't returning None or Strings
        self.assertIsInstance(result['Molecular weight'], float)
        self.assertIsInstance(result['Isoelectric point'], float)

if __name__ == '__main__':
    unittest.main()