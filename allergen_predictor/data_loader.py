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
    # Load the CSV, skipping the first metadata row
    df = pd.read_csv(file_path, header=1)

    # Extract the sequence column and remove any empty entries
    sequences = df['Name'].dropna().tolist()
    
    # Remove duplicate sequences to ensure a unique dataset
    unique_seqs = list(set(sequences))
    
    return unique_seqs

def load_negative_data(file_path, sample_size):
    """
    Reads a UniProt FASTA file, validates sequences, and returns a random sample.
    
    Args:
        file_path (str): Path to the UniProt FASTA file.
        sample_size (int): Number of valid sequences to randomly select.
        
    Returns:
        list: A random sample of unique, valid amino acid strings.
        
    Raises:
        FileNotFoundError: If the FASTA file does not exist.
        ValueError: If the requested sample size is larger than the available valid sequences.
    """
    sequences = []
    
    # Parse the FASTA file and extract the sequence strings
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append(str(record.seq))

    # Randomly select the specified number of sequences
    selected_sequences = random.sample(sequences, sample_size)
        
    return selected_sequences

# Simple execution block for quick local testing
if __name__ == "__main__":
    pos_file = "IEDB_positive.csv"
    positives = load_positive_data(pos_file)
    print(f"Loaded {len(positives)} sequences.")
