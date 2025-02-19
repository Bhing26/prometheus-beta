def generate_unique_permutations(input_string):
    """
    Generate all possible unique permutations of a given string.
    
    Args:
        input_string (str): The input string to generate permutations from
    
    Returns:
        list: A list of unique permutations as strings
    
    Raises:
        TypeError: If input is not a string
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle edge cases
    if not input_string:
        return []
    
    # Convert to list to handle character manipulation
    chars = list(input_string)
    
    def backtrack(start):
        # Base case: if we've reached the end of permutation generation
        if start == len(chars):
            unique_permutations.add(''.join(chars))
        
        # Try swapping current char with every subsequent char
        for i in range(start, len(chars)):
            # Swap characters
            chars[start], chars[i] = chars[i], chars[start]
            
            # Recursively generate permutations
            backtrack(start + 1)
            
            # Backtrack to restore original order
            chars[start], chars[i] = chars[i], chars[start]
    
    # Use a set to store unique permutations
    unique_permutations = set()
    backtrack(0)
    
    return list(unique_permutations)