def reverse_bits(n: int) -> int:
    """
    Reverse the bits of a given 32-bit unsigned integer.
    
    Args:
        n (int): A 32-bit unsigned integer.
    
    Returns:
        int: The number with its bits reversed.
    
    Examples:
        >>> reverse_bits(43261596)  # Binary: 00000010100101000001111010011100
        964176192                   # Binary: 00111001011110000010100101000000
    """
    # Ensure input is a 32-bit unsigned integer
    n = n & 0xFFFFFFFF
    
    # Perform bit reversal using binary operations
    reversed_num = 0
    for i in range(32):
        # Shift the current reversed number left and add the least significant bit of n
        reversed_num = (reversed_num << 1) | (n & 1)
        # Shift n right to process next bit
        n >>= 1
    
    return reversed_num