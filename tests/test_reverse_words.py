import pytest
from src.reverse_words import reverse_words

def test_reverse_words_normal_case():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("python is awesome") == "awesome is python"

def test_reverse_words_single_word():
    assert reverse_words("hello") == "hello"

def test_reverse_words_empty_string():
    assert reverse_words("") == ""

def test_reverse_words_multiple_spaces():
    assert reverse_words("  hello   world  ") == "world hello"

def test_reverse_words_invalid_input():
    with pytest.raises(TypeError):
        reverse_words(123)
    with pytest.raises(TypeError):
        reverse_words(None)