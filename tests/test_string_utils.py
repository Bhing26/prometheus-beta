import pytest
import sys
sys.path.append('.')
from src.string_utils import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    """Test basic removal of duplicate characters."""
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("aabbccdd") == "abcd"
    assert remove_duplicate_chars("python") == "python"

def test_remove_duplicate_chars_mixed_case():
    """Test that case sensitivity is preserved."""
    assert remove_duplicate_chars("HelloWORLD") == "HeloWRLD"

def test_remove_duplicate_chars_special_chars():
    """Test with special characters and numbers."""
    assert remove_duplicate_chars("a1b2c3a1b2c3") == "a1b2c3"

def test_remove_duplicate_chars_empty_string():
    """Test with empty string."""
    assert remove_duplicate_chars("") == ""

def test_remove_duplicate_chars_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        remove_duplicate_chars(123)
    with pytest.raises(TypeError):
        remove_duplicate_chars(None)