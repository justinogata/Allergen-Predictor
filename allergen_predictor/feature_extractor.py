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

def calculate_molecular_weight(sequence):
    """
    Calculates the molecular weight of the protein sequence.
    
    Args:
        sequence (str): The amino acid sequence.
        
    Returns:
        float: The molecular weight in Daltons.
    """
    analyzed_seq = ProteinAnalysis(sequence)
    return analyzed_seq.molecular_weight()
    
def calculate_isoelectric_point(sequence)
    """
    Calculates the Isoelectric Point (pI) of a protein sequence.
    This is the pH at which the protein carries no net electrical charge.
    """
    analyzed_seq = ProteinAnalysis(sequence)
    return analyzed_seq.isoelectric_point()

def calculate_aromaticity(sequence):
    """
    Calculates the fraction of amino acids that are aromatic. High aromaticity often 
    correlates with protein stability.
    """
    analyzed_seq = ProteinAnalysis(sequence)
    return analyzed_seq.aromaticity()

def calculate_instability_index(sequence):
    """
    Calculates the Instability Index. 
    Values < 40 indicate the protein is likely stable (common in allergens).
    Values > 40 indicate the protein is likely unstable.
    """
    analyzed_seq = ProteinAnalysis(sequence)
    return analyzed_seq.instability_index()

# Test block to prove it runs
if __name__ == "__main__":
    test_seq = "RCTKLEYDPRCVYDP" # test epitope sequence of Arachis hypogaea (peanut)
    print(f"Test Sequence: {test_seq}")
    print(f"Hydrophobicity: {calculate_hydrophobicity(test_seq)}")
    print(f"Molecular Weight: {calculate_molecular_weight(test_seq)}")
    print(f"Isoelectric Point: {calculate_isoelectric_point(test_seq)}")
    print(f"Aromaticity: {calculate_aromaticity(test_seq)}")
    print(f"Instability Index: {calculate_instability_index(test_seq)}")
