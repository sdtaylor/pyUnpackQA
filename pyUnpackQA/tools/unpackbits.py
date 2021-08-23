import numpy as np

"""
Core of the module here using some bitwise operations.
"""

def unpackbits(qa_array, num_bits):
    """
    Iterate thru each bit to see if its set or not. 
    
    This uses two bitwise operators.
    
    This line shifts bits to the left
        bit_loc = 1 << bit
    It makes bit_loc the respective integer when that bit, and only that bit, is set.
    
    For example with 16 bits 1 in binary is:
        '0000000000000001'
    shifting it 10 bits to the left to represent the bit 10 location produces:
        '0000010000000000'
    Which is the  integer 1024    
    
    The bitwise_and statement will produce an array with values 0 or 1024 indicating
    all the locations where that bit was set.
    
    Parameters
    ----------
    qa_array : np.array
        An int-line numpy array.
    num_bits : int
        Number of bits to expand to.
        
    Returns
    -------
    np.array int8
        0/1 array with size qa_array.shape + (num_bits,)
        
    """
    original_shape = qa_array.shape
    new_shape = (num_bits,) + original_shape
    
    bit_array = np.empty(shape = new_shape, dtype=np.uint8)
    
    for bit in range(num_bits):
        bit_loc = 1<<bit
        bit_array[bit] = np.bitwise_and(qa_array,bit_loc) == bit_loc
    
    return np.moveaxis(bit_array, source = 0, destination = -1)


"""
This bit unpacking uses string formating to do the job. Not as fast as the
numpy method in unpackbits.py, but is easier to understand and is used for sanity
check testing. 
"""

def int16_to_bits(x):
    """
    Unpack a 16 bit integer into binary fields. See the syntax for
    this here https://docs.python.org/3/library/string.html#format-specification-mini-language
    
    Parameters
    ----------
    x : int16
        single integer.

    Returns
    -------
    List of binary fields aligned so int16_to_bits(1024)[0] = bit 0

    """
    assert isinstance(x, int), 'x should be integer'
    return [int(b) for b in f'{x:016b}'.format(x)[::-1]]