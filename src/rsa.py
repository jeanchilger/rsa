import typer
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
    """
    Encrypt the given text using the provided key,
    accordingly to RSA rules.

    Args:
        text (str): Text to be encrypted.
        pkey (tuple[int]): Key to use during encryptation.

    Returns:
        str: The encrypted text.
    """

    n, e = pkey
    encoded_text = _encode_text(text)
    
    return " ".join([str((c ** e) % n) for c in encoded_text])


def decrypt(text: str, pkey: tuple[int]) -> str:
    """
    Decrypt the given text using the provided key,
    accordingly to RSA rules. The key used for encryption
    and decryption should be generated jointly.

    Args:
        text (str): Text to be decrypted.
        pkey (tuple[int]): Key to use during decryptation.

    Returns:
        str: The decrypted text.
    """
    
    n, d = pkey
    encoded_text = map(int, text.split(" "))

    return _decode_text([(c ** d) % n for c in encoded_text])


def _encode_text(text: str) -> list[int]:
    """
    Converts the text from literal values to numerical values.
    Uses the table conversion A -> 1, B -> 2, ...

    Args:
        text (str): Text to be encoded.

    Returns:
        list[int]: Encoded text as a list of ints.
            Each position corresponds to a character
            from input text.
    """
    
    return [ord(c) for c in text]


def _decode_text(text: list[int]) -> str:
    """
    Converts the text from numerical values to literal values.
    Uses the inverse table conversion of that used in _encode_text.

    Args:
        text (list[int]): List with each position
            representing a character to be decoded.

    Returns:
        str: Literal string converted from the input list of chars.
    """
    
    return "".join([chr(c) for c in text])
