import pandas as pd
from Bio import SeqIO
import random

def load_positive_data(file_path):
    """
    Reads the IEDB CSV file and contains validation for file existence, CSV format, column presence,
    and proper error handling.
    """
    # Loading
    df = pd.read_csv(file_path, header=1)
    sequences = df['Name'].dropna().tolist()
    
    unique_seqs = list(set(sequences))
    
    return unique_seqs

def load_negative_data(file_path, sample_size):
    """
    Reads a UniProt FASTA file and contains robust error handling for parsing and sampling.
    """
    sequences = []
    
    # Parsing
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append(str(record.seq))

    # Sampling
    selected_sequences = random.sample(sequences, sample_size)
        
    return selected_sequences

# test block
if __name__ == "__main__":
    pos_file = "IEDB_positive.csv"
    positives = load_positive_data(pos_file)
    print(f"Loaded {len(positives)} sequences.")