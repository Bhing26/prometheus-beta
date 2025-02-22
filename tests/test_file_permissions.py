import os
import pytest
import tempfile
from src.file_permissions import change_file_permissions

def test_change_file_permissions_success():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Test changing to read-only (0o444)
        result = change_file_permissions(temp_path, 0o444)
        assert result is True
        
        # Verify the permissions
        mode = os.stat(temp_path).st_mode
        assert (mode & 0o777) == 0o444
        
        # Test changing to read-write (0o666)
        result = change_file_permissions(temp_path, 0o666)
        assert result is True
        
        mode = os.stat(temp_path).st_mode
        assert (mode & 0o777) == 0o666
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_path):
            os.unlink(temp_path)

def test_change_file_permissions_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        change_file_permissions('nonexistent_file.txt', 0o755)

def test_change_file_permissions_invalid_mode():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Test invalid mode type
        with pytest.raises(ValueError):
            change_file_permissions(temp_path, '755')  # string instead of int
        
        with pytest.raises(ValueError):
            change_file_permissions(temp_path, 'abc')  # invalid type
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_path):
            os.unlink(temp_path)