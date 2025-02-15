import pytest
import sys
sys.path.append('.')
from src.bit_reversal import reverse_bits

def test_reverse_bits_standard_case():
    # Test case from the example in the function docstring
    assert reverse_bits(43261596) == 964176192

def test_reverse_bits_zero():
    # Test reversing zero
    assert reverse_bits(0) == 0

def test_reverse_bits_all_ones():
    # Test reversing a number with all bits set
    assert reverse_bits(0xFFFFFFFF) == 0xFFFFFFFF

def test_reverse_bits_alternating():
    # Test reversing a number with alternating bits
    assert reverse_bits(0xAAAAAAAA) == 0x55555555

def test_reverse_bits_boundary_cases():
    # Test some boundary cases
    test_cases = [
        (1, 2147483648),        # 00000000000000000000000000000001 -> 10000000000000000000000000000000
        (2147483648, 1),        # 10000000000000000000000000000000 -> 00000000000000000000000000000001
    ]
    
    for input_val, expected in test_cases:
        assert reverse_bits(input_val) == expected