def remove_duplicate_chars(input_string):
    """
    Remove duplicate characters from a given string while preserving the original order.
    
    Args:
        input_string (str): The input string to remove duplicates from.
    
    Returns:
        str: A string with duplicate characters removed, maintaining original order.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use dict.fromkeys() to preserve order and remove duplicates
    return ''.join(dict.fromkeys(input_string))