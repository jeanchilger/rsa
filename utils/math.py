import math

def select_smallest_coprime(x: int, lower: int, upper: int) -> int:
    """
    Returns the smallest coprime number of x,
    that is larger than lower and greater than upper.

    Args:
        x (int): Number whose coprime must be obtained.
        lower (int): Lower range bound. Defaults to 1.
        upper (int): Upper range bound.

    Returns:
        int: The smallest coprime of x between lower and upper.
    """
    
    for y in range(lower, upper, 1):
        if math.gcd(x, y) == 1:
            return y
        