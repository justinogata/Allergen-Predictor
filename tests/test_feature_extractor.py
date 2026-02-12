import unittest
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from allergen_predictor.feature_extractor import (
    calculate_hydrophobicity,
    calculate_molecular_weight,
    calculate_isoelectric_point,
    calculate_aromaticity,
    calculate_instability_index
)

class TestFeatureExtractor(unittest.TestCase):

    # --- Test Case 1: Hydrophobicity (GRAVY) ---
    def test_hydrophobicity_normal(self):
        # 'A' (Alanine) is hydrophobic (1.8). 'R' (Arginine) is hydrophilic (-4.5).
        # 'AAA' should be 1.8. 'RRR' should be -4.5.
        self.assertAlmostEqual(calculate_hydrophobicity("AAA"), 1.8, places=2)
        self.assertAlmostEqual(calculate_hydrophobicity("RRR"), -4.5, places=2)

    def test_hydrophobicity_empty(self):
        # Should return 0.0 for empty input
        self.assertEqual(calculate_hydrophobicity(""), 0.0)

    # --- Test Case 2: Molecular Weight ---
    def test_weight_normal(self):
        # Glycine (G) residue weight is ~57.05 Da. 
        # 'GGG' should be ~171.15 Da
        # Biopython calculates exact weight including water.
        result = calculate_molecular_weight("GGG")
        self.assertTrue(result > 100) # Basic range check

    def test_weight_invalid(self):
        # Should handle characters like 'J' or numbers by returning 0.0
        self.assertEqual(calculate_molecular_weight("12345"), 0.0)

    # --- Test Case 3: Isoelectric Point (pI) ---
    def test_pI_normal(self):
        # Acidic proteins (lots of D/E) should have low pI (< 7)
        # Basic proteins (lots of K/R) should have high pI (> 7)
        acidic_seq = "DDDDEEEE"
        basic_seq = "RRRRKKKK"
        self.assertLess(calculate_isoelectric_point(acidic_seq), 7.0)
        self.assertGreater(calculate_isoelectric_point(basic_seq), 7.0)

    # --- Test Case 4: Aromaticity ---
    def test_aromaticity_calculation(self):
        # Sequence with only Phenylalanine (F) should be 1.0 (100% aromatic)
        # Sequence with only Alanine (A) should be 0.0 (0% aromatic)
        self.assertAlmostEqual(calculate_aromaticity("FFF"), 1.0, places=2)
        self.assertAlmostEqual(calculate_aromaticity("AAA"), 0.0, places=2)

    # --- Test Case 5: Instability Index ---
    def test_instability_index(self):
        # A stable protein (Index < 40) vs Unstable (Index > 40)
        # Short sequences can be tricky, so we test that it returns a float.
        result = calculate_instability_index("MVKVYAPASS")
        self.assertIsInstance(result, float)

if __name__ == '__main__':
    unittest.main()
