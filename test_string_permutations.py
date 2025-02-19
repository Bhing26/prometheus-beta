import pytest
from string_permutations import generate_unique_permutations

def test_unique_permutations_basic():
    # Test basic string permutations
    result = generate_unique_permutations('abc')
    assert len(result) == 6
    assert set(result) == {'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}

def test_unique_permutations_duplicates():
    # Test string with duplicate characters
    result = generate_unique_permutations('abb')
    assert len(result) == 3
    assert set(result) == {'abb', 'bab', 'bba'}

def test_unique_permutations_empty_string():
    # Test empty string case
    result = generate_unique_permutations('')
    assert result == []

def test_unique_permutations_single_char():
    # Test single character case
    result = generate_unique_permutations('x')
    assert result == ['x']

def test_unique_permutations_invalid_input():
    # Test non-string input
    with pytest.raises(TypeError):
        generate_unique_permutations(123)

def test_permutation_length_and_uniqueness():
    # Comprehensive test for a more complex string
    result = generate_unique_permutations('wxyz')
    assert len(result) == 24  # 4! unique permutations
    assert len(set(result)) == len(result)  # All permutations are unique