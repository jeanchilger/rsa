import base64
import typer
from pathlib import Path
from typing import Optional, Union

from src import rsa
from utils import environ

app = typer.Typer()


@app.command()
def init() -> None:
    """
    Initializes an environment. Any needed configuration will be prompted.
    """
    
    # if env already exists, init shouldn't be used
    if not environ.create_env():
        raise typer.Exit()
    
    p = typer.prompt("Input the first prime number")
    q = typer.prompt("Input the second prime number")

    environ.set_config("args", "p", p)
    environ.set_config("args", "q", q)
    
    # generate the keys based on provided prime numbers
    private_key, public_key = rsa.generate_keys(int(p), int(q))
    
    private_key_b64 = base64.b64encode(str(private_key).encode())
    public_key_b64 = base64.b64encode(str(public_key).encode())
    
    environ.set_config("keys", "private", str(private_key_b64))
    environ.set_config("keys", "public", str(public_key_b64))
    
    typer.echo(f"Private key: {private_key}")
    typer.echo(f"Private key (base64): {private_key_b64}")
    typer.echo(f"Public key: {public_key}")
    typer.echo(f"Public key (base64): {public_key_b64}")


@app.command()
def encrypt(
    src: str = typer.Argument(
        ...,
        help="Source text to be encrypted. A path to a text file may be provided."
    ),
    dest: Path = typer.Option(
        None,
        help="Path to file where encryptation should be stored. If omitted, result will be written to stdout."
    ),
    pkey: str = typer.Option(
        None,
        help="Public key to be used for encryptation. If omitted, the public key from environment will be used."
    )
) -> None:
    """[summary]

    Args:
        src (str): [description]
        dest (Path, optional): [description]. Defaults to None.
        pkey (str, optional): [description]. Defaults to None.
    """


@app.command()
def decrypt(
    src: str = typer.Argument(
        ...,
        help="Source text to be decrypted. A path to a text file may be provided."
    ),
    dest: Path = typer.Option(
        None,
        help="Path to file where decryptation should be stored. If omitted, result will be written to stdout."
    ),
    pkey: str = typer.Option(
        None,
        help="Private key to be used for decryptation. If omitted, the private key from environment will be used."
    )
) -> None:
    pass

if __name__ == "__main__":
    app()