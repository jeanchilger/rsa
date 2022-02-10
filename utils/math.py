import math

def select_coprime(x: int) -> int:
    """
    Returns a coprime number of x (that is smaller than x).

    Args:
        x (int): Number whose coprime must be obtained.

    Returns:
        int: A coprime number of x.
    """
    
    # 65537 is widely used
    if x > 65537 and math.gcd(x, 65537) == 1:
        return 65537
    
    for y in range(3, x):
        if math.gcd(x, y) == 1:
            return y
        