def reverse_bits(n: int) -> int:
    """
    Reverse the bits of a given 32-bit unsigned integer.
    
    Args:
        n (int): A 32-bit unsigned integer to reverse.
    
    Returns:
        int: The number with its bits reversed.
    
    Example:
        >>> reverse_bits(43261596)  # 00000010100101000001111010011100 
        >>> 964176192               # 00111001011110000010100101000000
    """
    # Ensure input is a 32-bit unsigned integer
    n = n & 0xFFFFFFFF
    
    # Initialize result
    result = 0
    
    # Iterate through all 32 bits
    for i in range(32):
        # Left shift result and add least significant bit of n
        result = (result << 1) | (n & 1)
        # Right shift n
        n >>= 1
    
    return result