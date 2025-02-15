import re

def extract_numbers(input_string):
    """
    Extract all numbers from a given string.
    
    Args:
        input_string (str): The input string to extract numbers from.
    
    Returns:
        list: A list of numbers (as integers or floats) found in the input string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Extract integers and decimal numbers (including negative numbers)
    numbers = re.findall(r'-?\d+(?:\.\d+)?', input_string)
    
    # Convert to int or float 
    converted_numbers = []
    for num in numbers:
        try:
            # Try to convert to int if possible, otherwise keep as float
            converted_num = int(num) if num.isdigit() or (num.startswith('-') and num[1:].isdigit()) else float(num)
            converted_numbers.append(converted_num)
        except ValueError:
            # Fallback to original string if conversion fails
            converted_numbers.append(num)
    
    return converted_numbers