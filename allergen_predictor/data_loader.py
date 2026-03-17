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
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: The file '{file_path}' was not found.")
    if not file_path.endswith('.csv'):
        raise ValueError("Error: The file must be a .csv format.")

    # Load the CSV, skipping the first metadata row
    df = pd.read_csv(file_path, header=1)
    
    # Samantha Reimer HW3 Issue: 
    # Validation: 
    #   - Ensure the CSV is not empty
    #   - Ensure required data column actually exists ('Name' column)
    # 
    # Errors raised: 
    #   ValueError: 
    #       - when CSV file is empty 
    #       - when the 'Name' column is missing from the CSV
    if df.empty:
        raise ValueError("Error: The CSV file is empty.")
    if 'Name' not in df.columns:
        raise ValueError("Error: The required 'Name' column is missing from the CSV.")        

    # Extract the sequence column and remove any empty entries
    sequences = df['Name'].dropna().tolist()

    # Samantha Reimer HW3 Issue: 
    # make sure extracted sequences are valid before returning
    # pass into _validate_sequences 
    return _validate_sequences(sequences)


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
    
    # Samantha Reimer HW3 Issue:
    # Error raised: 
    #   FileNotFoundError: missing FASTA file 
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: The file '{file_path}' was not found.")

    sequences = []
    
    # Parse the FASTA file and extract the sequence strings
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append(str(record.seq))


    # Samantha Reimer HW3 Issue: 
    # Validate FASTA sequences and randomly sample them 
    #
    # Input: 
    #   sequences: list of ammino acid seqences 
    #   sample size (int): number of sequences to randomly sample 
    # 
    # Output: 
    #   Random sample (list): sample of unique, validated amino acid sequences
    # 
    # Errors raised: 
    #   ValueError: 
    #       - if sample size exceeds the number of valid sequences
    valid_sequences = _validate_sequences(sequences)
    
    #edge case validation to see if sample size is too large
    if len(valid_sequences) < sample_size:
        raise ValueError(f"Error: Requested sample size ({sample_size}) exceeds valid sequences available ({len(valid_sequences)}).")
    
    #return a randomly selected sample 
    return random.sample(valid_sequences, sample_size)
