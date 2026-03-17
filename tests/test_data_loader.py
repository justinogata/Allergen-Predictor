import unittest
import os
import pandas as pd
from allergen_predictor.data_loader import load_positive_data, load_negative_data, _validate_sequences

class TestDataLoader(unittest.TestCase):
    """
    Class to test the data_loader functions 
    """

    # temporary files for testing
    def setUp(self):
        self.dummy_csv = "test_data.csv"
        with open(self.dummy_csv, "w") as f:
            f.write("Metadata Row\n")
            f.write("ID,Name\n")
            f.write("1,MVLTI\n")
            f.write("2,ACDEF\n")
        
        self.dummy_fasta = "test_data.fasta"
        with open(self.dummy_fasta, "w") as f:
            f.write(">Seq1\nMVLTI\n")
            f.write(">Seq2\nACDEF\n")

    #remove temp files after tests are done
    def tearDown(self):
        if os.path.exists(self.dummy_csv):
            os.remove(self.dummy_csv)
        if os.path.exists(self.dummy_fasta):
            os.remove(self.dummy_fasta)
    
    #test missing files raise a FileNotFoundError.
    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            load_positive_data("nonexistent_file.csv")

    #test invalid amino acid characters
    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            _validate_sequences(["MVL1TI"]) 
    
    #test sequences outside the 5-100 AA constraint 
    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            _validate_sequences(["AAA"]) # Edge case: too short

    #test for requesting more samples than available
    def test_sample_size_too_large(self):
        with self.assertRaises(ValueError):
            load_negative_data(self.dummy_fasta, sample_size=50)

    #test basic case for positive data loading
    def test_successful_positive_load(self):
        result = load_positive_data(self.dummy_csv)
        self.assertEqual(len(result), 2)
        
if __name__ == '__main__':
    unittest.main()
