from utils import math


def generate_keys(p: int, q: int) -> list[tuple[int]]:
    """
    Given two prime numbers, generate the private and public keys.

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
    
    e = math.select_coprime(tot)
    d = pow(e, -1, tot)
    
    return (n, d), (n, e)


def encrypt(text: str, pkey: tuple[int]) -> str:
    pass


def decrypt(text: str, pkey: tuple[int]) -> str:
    pass


def _encode_text(text: str) -> list[int]:
    """
    Converts the text to literal values to numerical values.
    Uses the table conversion A -> 1, B -> 2, ...

    Args:
        text (str): Text to be encoded.

    Returns:
        list[int]: Encoded text as a list of ints.
            Each position corresponds to a character
            from input text.
    """
    
    return [ord(c) - 63 for c in text]
