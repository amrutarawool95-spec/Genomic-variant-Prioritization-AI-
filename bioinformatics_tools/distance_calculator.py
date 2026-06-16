"""
Phylogenetic Distance Calculator
Calculate pairwise sequence distances for phylogenetic analysis
"""

import math
from typing import List, Dict, Tuple


def hamming_distance(seq1: str, seq2: str) -> int:
    """
    Calculate Hamming distance (number of differences).
    Sequences must be the same length.
    
    Args:
        seq1: First sequence
        seq2: Second sequence
        
    Returns:
        Number of differing positions
    """
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must have the same length")
    
    return sum(a != b for a, b in zip(seq1.upper(), seq2.upper()))


def hamming_distance_normalized(seq1: str, seq2: str) -> float:
    """
    Calculate normalized Hamming distance (0-1).
    
    Args:
        seq1: First sequence
        seq2: Second sequence
        
    Returns:
        Proportion of differing positions
    """
    if len(seq1) == 0:
        return 0.0
    
    return hamming_distance(seq1, seq2) / len(seq1)


def jukes_cantor_distance(seq1: str, seq2: str) -> float:
    """
    Calculate Jukes-Cantor distance.
    Corrects for multiple substitutions assuming uniform substitution rates.
    
    Args:
        seq1: First DNA sequence
        seq2: Second DNA sequence
        
    Returns:
        Jukes-Cantor distance
    """
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must have the same length")
    
    p = hamming_distance_normalized(seq1, seq2)
    
    # Avoid log(0) or log(negative)
    if p >= 0.75:
        return float('inf')
    
    return -0.75 * math.log(1 - (4.0 / 3.0) * p)


def kimura_2_parameter(seq1: str, seq2: str) -> float:
    """
    Calculate Kimura 2-parameter distance.
    Distinguishes transitions (A↔G, C↔T) from transversions.
    
    Args:
        seq1: First DNA sequence
        seq2: Second DNA sequence
        
    Returns:
        Kimura 2-parameter distance
    """
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must have the same length")
    
    seq1 = seq1.upper()
    seq2 = seq2.upper()
    
    transitions = 0
    transversions = 0
    
    transition_pairs = {('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')}
    
    for a, b in zip(seq1, seq2):
        if a != b:
            if (a, b) in transition_pairs:
                transitions += 1
            else:
                transversions += 1
    
    total_subs = transitions + transversions
    if total_subs == 0:
        return 0.0
    
    p = transitions / total_subs
    q = transversions / total_subs
    
    # Avoid log errors
    if p >= 0.5 or q >= 0.25:
        return float('inf')
    
    return -0.5 * math.log(1 - 2 * p - q) - 0.25 * math.log(1 - 2 * q)


def sequence_identity(seq1: str, seq2: str) -> float:
    """
    Calculate percentage sequence identity.
    
    Args:
        seq1: First sequence
        seq2: Second sequence
        
    Returns:
        Percentage identity (0-100)
    """
    if len(seq1) != len(seq2) or len(seq1) == 0:
        return 0.0
    
    matches = sum(a == b for a, b in zip(seq1.upper(), seq2.upper()))
    return (matches / len(seq1)) * 100


if __name__ == "__main__":
    # Example usage
    seq1 = "ATGCGATGCTAGCTAGCTGAGCTAG"
    seq2 = "ATGCGATGCTAGCTAGCTGAGCTAT"
    
    print("Distance Calculations:")
    print(f"Seq1: {seq1}")
    print(f"Seq2: {seq2}")
    print(f"\nHamming distance: {hamming_distance(seq1, seq2)}")
    print(f"Hamming distance (normalized): {hamming_distance_normalized(seq1, seq2):.4f}")
    print(f"Jukes-Cantor distance: {jukes_cantor_distance(seq1, seq2):.4f}")
    print(f"Kimura 2-parameter distance: {kimura_2_parameter(seq1, seq2):.4f}")
    print(f"Sequence identity: {sequence_identity(seq1, seq2):.2f}%")
