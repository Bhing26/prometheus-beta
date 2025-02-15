import os
import sys
import pytest
from io import StringIO
from console_utils import clear_console_and_log

def test_clear_console_and_log(monkeypatch):
    # Redirect stdout to capture print output
    captured_output = StringIO()
    monkeypatch.setattr(sys, 'stdout', captured_output)
    
    # Test message logging
    test_message = "Hello, Console!"
    clear_console_and_log(test_message)
    
    # Check if the message was printed
    captured_output.seek(0)
    assert captured_output.read().strip() == test_message

def test_clear_console_and_log_empty_message(monkeypatch):
    # Redirect stdout to capture print output
    captured_output = StringIO()
    monkeypatch.setattr(sys, 'stdout', captured_output)
    
    # Test empty message logging
    clear_console_and_log("")
    
    # Check if an empty line was printed
    captured_output.seek(0)
    assert captured_output.read().strip() == ""

def test_clear_console_and_log_with_special_characters(monkeypatch):
    # Redirect stdout to capture print output
    captured_output = StringIO()
    monkeypatch.setattr(sys, 'stdout', captured_output)
    
    # Test message with special characters
    test_message = "Line 1\nLine 2\tTabbed\r\nCarriage Return"
    clear_console_and_log(test_message)
    
    # Check if the message was printed exactly
    captured_output.seek(0)
    assert captured_output.read().strip() == test_message