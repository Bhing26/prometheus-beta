import os
import stat

def change_file_permissions(file_path, mode):
    """
    Change the permissions of a file.
    
    Args:
        file_path (str): Path to the file whose permissions are to be changed
        mode (int): The new permission mode (in octal, e.g., 0o755)
    
    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If the user lacks permission to change file permissions
        ValueError: If the mode is not a valid permission mode
    """
    # Validate input
    if not isinstance(mode, int):
        raise ValueError("Mode must be an integer representing file permissions")
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        # Change file permissions
        os.chmod(file_path, mode)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to modify {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error changing file permissions: {str(e)}")
    
    return True