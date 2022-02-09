from utils import math


def generate_keys(p: int, q: int) -> list[tuple[int]]:
    """
    Given two prime numbers, generate the private and public keys.
    
    Instead of reusing the methods generate_private_key and
    generate_public_key it computes the intermediate values,
    to avoid repeated computations.

    Args:
        p (int): Prime number
        q (int): Prime number

    Returns:
        list: A list with a tuple (n, d) representing the
            private key in the first position and a
            tuple (n, e) representing the public key in the last
            position.
    """
    
    n = p * q
    tot = (p - 1) * (q - 1)
    
    e = math.select_smallest_coprime(tot, lower=2, upper=tot)
    d = pow(e, -1, tot)
    
    return (n, d), (n, e)


def generate_private_key(p: int, q: int) -> tuple[int]:
    """
    Given two prime numbers, generate a private key.

    Args:
        p (int): Prime number
        q (int): Prime number

    Returns:
        tuple: A tuple (n, d) representing the private key
    """
    
    n = p * q
    tot = (p - 1) * (q - 1)
    
    e = math.select_smallest_coprime(tot, lower=2, upper=tot)

    d = pow(e, -1, tot)
    
    return (n, d)


def generate_public_key(p: int, q: int) -> tuple[int]:
    """
    Given two prime numbers, generate a public key.

    Args:
        p (int): Prime number
        q (int): Prime number

    Returns:
        tuple: A tuple (n, e) representing the public key
    """
    
    n = p * q
    tot = (p - 1) * (q - 1)
    
    e = math.select_smallest_coprime(tot, lower=2, upper=tot)
    
    return (n, e)
