def get_unique_substrings(input_string):
    """
    Takes a string as input and returns an array of all unique substrings.
    
    Args:
        input_string (str): The input string to extract substrings from.
    
    Returns:
        list: A list of unique substrings in the input string.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        return []
    
    # Use a set to collect unique substrings
    unique_substrings = set()
    
    # Generate all possible substrings
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            unique_substrings.add(input_string[start:end])
    
    # Convert set to list and return
    return list(unique_substrings)