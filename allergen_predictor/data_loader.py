import os
import pandas as pd
from Bio import SeqIO
import random

# Helper function to handle the biological validations
def _validate_sequences(sequences):
    """
    Validates a list of sequences for correct amino acid characters and length.
    
    Args:
        sequences (list): A list of protein sequence strings.
        
    Returns:
        list: A list of unique, validated protein sequences.
        
    Raises:
        ValueError: If a sequence contains invalid characters or violates length constraints.
    """
    valid_aa = set("ACDEFGHIKLMNPQRSTVWY")
    unique_seqs = list(set(sequences))
    validated = []

    # Samantha Reimer HW3 Issue: 
    # Validation loop to ensure biologically sound sequences 
    # Input: 
    #      unique_seqs: list of ammino acid seqences 
    #      valid_aa (set): set of valid amino acid characters
    #
    # Output: 
    #       validated: list of sequences that pass all validation checks
    #
    # Errors raised: 
    #       ValueError:
    #           - sequence length is less than 5 or greater than 100 amino acids
    #           - sequence contains invalid amino acid characters 
    for seq in unique_seqs:
        seq = str(seq).upper()
        
        #check sequence length constraint (between 5 and 100 AA)
        if len(seq) < 5 or len(seq) > 100: 
            raise ValueError(f"Length Error: Sequence '{seq}' is {len(seq)} AA long. Must be between 5 and 100 AA.")
            
        #check for invalid amino acid characters
        invalid_chars = set(seq) - valid_aa
        if invalid_chars:
            raise ValueError(f"Character Error: Sequence '{seq}' contains invalid characters {invalid_chars}.")
            
        validated.append(seq)
        
    return validated

def load_positive_data(file_path):
    """
    Reads the IEDB CSV file, extracts protein sequences, and validates them.
    
    Args:
        file_path (str): Path to the IEDB epitope CSV file.
        
    Returns:
        list: A list of unique, valid amino acid strings.
        
    Raises:
        FileNotFoundError: If the CSV file does not exist.
        ValueError: If the file is not a CSV, is empty, or lacks the 'Name' column.
    """

    # Samantha Reimer HW3 Issue: 
    # - Missing files from given path 
    # - Incorrect file format 
    # 
    # Errors raised: 
    #   FileNotFoundError: CSV file not found in given file path
    #   ValueError: CSV file format is incorrect (ex: .tsv instead of .csv extension)
    if not os.path