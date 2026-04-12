import pandas as pd
import os
from data_loader import load_positive_data, load_negative_data
from feature_extractor import extract_all_features

#conda install -c bioconda cd-hit
#cd-hit -i UniProt_negative.fasta -o UniProt_filtered.fasta -c 0.8 -n 5

def create_master_dataset(pos_file_path, neg_file_path, output_path, neg_sample_size):
    print("Initiating Batch Feature Extraction...")
    print("-" * 40)
    
    # Load the raw sequences
    print(f"Loading Positive Data from: {pos_file_path}")
    pos_seqs = load_positive_data(pos_file_path)
    
    print(f"Loading Negative Data from: {neg_file_path}")
    # Using the sample_size required by data loader
    neg_seqs = load_negative_data(neg_file_path, sample_size=neg_sample_size)
    
    master_dataset = []

    # Process Positive Sequences (Allergens)
    print(f"\nExtracting features for {len(pos_seqs)} positive sequences...")
    for i, seq in enumerate(pos_seqs):
        features = extract_all_features(seq)
        features['Label'] = 1  # 1 = Allergen
        master_dataset.append(features)
        
        # Print an update every 100 sequences so we know it hasn't frozen
        if (i + 1) % 100 == 0:
            print(f"  [+] Processed {i + 1} / {len(pos_seqs)} allergens")

    # Process Negative Sequences (Non-Allergens)
    print(f"\nExtracting features for {len(neg_seqs)} negative sequences...")
    for i, seq in enumerate(neg_seqs):
        features = extract_all_features(seq)
        features['Label'] = 0  # 0 = Non-Allergen
        master_dataset.append(features)
        
        # Print an update every 500 sequences (since there are usually more of these)
        if (i + 1) % 500 == 0:
            print(f"  [-] Processed {i + 1} / {len(neg_seqs)} non-allergens")

    # Save to CSV
    print("\nFormatting matrix and saving to CSV...")
    df = pd.DataFrame(master_dataset)
    
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    
    print("-" * 40)
    print(f"Master dataset saved to: {output_path}")
    print(f"Total sequences processed: {len(df)}")
    print(f"Features calculated: {len(df.columns) - 1}") # Subtract 1 for the Label column

if __name__ == '__main__':
    
    POSITIVE_DATA_FILE = "IEDB_positive.csv" 
    NEGATIVE_DATA_FILE = "UniProt_filtered.fasta" # Replace with your CD-HIT filtered file if you have it!
    
    # The file this script will generate
    OUTPUT_CSV_FILE = "data/master_dataset.csv"  
    
    # How many negative sequences to pull. 
    # (Update this number to match the actual number of sequences in your filtered file)
    NEGATIVE_SAMPLE_SIZE = 5000 
    
    create_master_dataset(
        pos_file_path=POSITIVE_DATA_FILE, 
        neg_file_path=NEGATIVE_DATA_FILE, 
        output_path=OUTPUT_CSV_FILE,
        neg_sample_size=NEGATIVE_SAMPLE_SIZE
    )