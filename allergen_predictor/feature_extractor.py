"""
Module: feature_extractor
Scope: Calculates physicochemical properties of protein sequences.
"""

from Bio.SeqUtils.ProtParam import ProteinAnalysis

def extract_all_features(sequence):
    """
    Calculates multiple physiochemical properties for a given protein sequence.
    Instantiates Biopython's ProteinAnalysis only once to optimize execution time.
    
    Args:
        sequence (str): A validated amino acid string.
        
    Returns:
        dict: A dictionary containing the computed physiochemical features.
    """
    # Create the object only once
    analysis = ProteinAnalysis(sequence)
    
    # Extract all properties
    physicochemical_features = {
        'Molecular weight': analysis.molecular_weight(),   # Weight
        'Isoelectric point': analysis.isoelectric_point(), # Net pH charge is zero
        'Instability index': analysis.instability_index(), # Structural stability
        'Aromaticity': analysis.aromaticity(),             # Frequency of aromatic amino acids
        'Gravy': analysis.gravy()                          # Hydrophobicity
    }
    
    
    return physicochemical_features