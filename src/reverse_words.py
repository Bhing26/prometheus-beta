def reverse_words(input_string):
    """
    Takes a string as input and returns the same string with its words reversed.
    
    Args:
        input_string (str): The input string to be reversed.
    
    Returns:
        str: A string with words in reverse order, separated by spaces.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty string
    if not input_string:
        return ""
    
    # Split the string into words and reverse
    return " ".join(input_string.split()[::-1])