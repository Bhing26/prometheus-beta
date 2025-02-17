import pytest
from src.bit_reversal import reverse_bits

def test_reverse_bits_standard_case():
    """Test reversing bits for a standard input."""
    assert reverse_bits(43261596) == 964176192

def test_reverse_bits_zero():
    """Test reversing bits for zero."""
    assert reverse_bits(0) == 0

def test_reverse_bits_all_ones():
    """Test reversing bits for all 1s (maximum 32-bit unsigned integer)."""
    assert reverse_bits(0xFFFFFFFF) == 0xFFFFFFFF

def test_reverse_bits_power_of_two():
    """Test reversing bits for a power of two."""
    # 2^30 (1 << 30)
    assert reverse_bits(1073741824) == 2

def test_reverse_bits_random_number():
    """Test reversing bits for another random number."""
    assert reverse_bits(12345) == 3166517248

def test_reverse_bits_input_validation():
    """Test that the function handles large inputs by masking to 32 bits."""
    # Input larger than 32 bits
    large_input = 0x1FFFFFFFF
    assert reverse_bits(large_input) == reverse_bits(0xFFFFFFFF)