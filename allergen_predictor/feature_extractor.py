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
        'Molecular weight': analysis.molecular_weight(),
        'Isoelectric point': analysis.isoelectric_point(),
        'Instability index': analysis.instability_index(),
        'Aromaticity': analysis.aromaticity(),
        'Gravy': analysis.gravy()
    }
    
    # If you need secondary structure fractions, you can unpack them like this:
    # helix, turn, sheet = analysis.secondary_structure_fraction()
    # features['sec_struct_helix'] = helix
    
    return physicochemical_features