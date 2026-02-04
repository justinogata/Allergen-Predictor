"""
Module: feature_extractor
Scope: Calculates physicochemical properties of protein sequences.
"""

from Bio.SeqUtils.ProtParam import ProteinAnalysis

def calculate_hydrophobicity(sequence):
    """
    Calculates the GRAVY (Grand Average of Hydropathy) score for a protein sequence.
    
    Args:
        sequence (str): The amino acid sequence (e.g., 'MVLTV').
        
    Returns:
        float: The calculated hydrophobicity score.
    """
    # Create a ProteinAnalysis object using Biopython
    analyzed_seq = ProteinAnalysis(sequence)
    
    # Calculate GRAVY score
    gravy_score = analyzed_seq.gravy()
    
    return gravy_score


# Test block to prove it runs
if __name__ == "__main__":
    test_seq = "RCTKLEYDPRCVYDP" # test epitope sequence of Arachis hypogaea (peanut)
    print(f"Test Sequence: {test_seq}")
    print(f"Hydrophobicity: {calculate_hydrophobicity(test_seq)}")