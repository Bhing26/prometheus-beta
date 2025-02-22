import pytest
from src.unique_substrings import get_unique_substrings

def test_get_unique_substrings_basic():
    # Test a simple string
    result = get_unique_substrings("abc")
    expected = {"a", "b", "c", "ab", "bc", "abc"}
    assert set(result) == expected

def test_get_unique_substrings_empty():
    # Test empty string
    result = get_unique_substrings("")
    assert result == []

def test_get_unique_substrings_repeated_chars():
    # Test string with repeated characters 
    result = get_unique_substrings("aaa")
    expected = {"a", "aa", "aaa"}
    assert set(result) == expected

def test_get_unique_substrings_invalid_input():
    # Test non-string input
    with pytest.raises(TypeError):
        get_unique_substrings(123)

def test_get_unique_substrings_complex():
    # Test with a more complex string
    result = get_unique_substrings("hello")
    expected = {"h", "e", "l", "o", "he", "el", "ll", "lo", "hel", "ell", "llo", "hello"}
    assert set(result) == expected