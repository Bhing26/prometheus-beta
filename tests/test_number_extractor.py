import pytest
from src.number_extractor import extract_numbers

def test_extract_numbers_basic():
    assert extract_numbers("There are 123 apples and 45.67 oranges") == [123, 45.67]

def test_extract_numbers_negative():
    assert extract_numbers("Temperature: -10 degrees and 25.5 celsius") == [-10, 25.5]

def test_extract_numbers_mixed():
    assert extract_numbers("Price: $45.99 and quantity: 10") == [45.99, 10]

def test_extract_numbers_no_numbers():
    assert extract_numbers("No numbers here") == []

def test_extract_numbers_invalid_input():
    with pytest.raises(TypeError):
        extract_numbers(123)

def test_extract_numbers_complex_string():
    assert extract_numbers("Coordinates: 10.5, -20.3, 30") == [10.5, -20.3, 30]

def test_extract_numbers_multiple_formats():
    result = extract_numbers("Numbers: 42, -17, 3.14, -0.5")
    assert result == [42, -17, 3.14, -0.5]