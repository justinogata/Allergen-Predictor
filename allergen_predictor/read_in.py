import pandas as pd
from Bio import SeqIO
import random

def load_positive_data(file_path):
    """
    Reads the IEDB CSV file and extracts the protein sequences.
    Assumes the file has a specific format where the sequence data is in
    the 'Name' column and the actual headers start on the second row.
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
    Reads a UniProt FASTA file and returns a random sample of the sequences.
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