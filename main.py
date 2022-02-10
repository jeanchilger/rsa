import base64
import typer
from pathlib import Path
from src import rsa
from utils import environ, file_helper

app = typer.Typer()


@app.command()
def init() -> None:
    """
    Initializes an environment. Any needed configuration will be prompted.
    """
    
    # if env already exists, asks for recreation
    if not environ.create_env():
        recreate = typer.confirm("Configurations exists. Wish to rebuild them?")
        
        if recreate:
            environ.delete_env()
            environ.create_env()
        
        else:
            raise typer.Exit()
    
    p = typer.prompt("Input the first prime number")
    q = typer.prompt("Input the second prime number")

    environ.set_config("args", "p", p)
    environ.set_config("args", "q", q)
    
    # generate the keys based on provided prime numbers
    private_key, public_key = rsa.generate_keys(int(p), int(q))
    
    private_key_b64 = base64.b64encode(
            f"{private_key[0]},{private_key[1]}".encode("utf-8"))
    public_key_b64 = base64.b64encode(
            f"{public_key[0]},{public_key[1]}".encode("utf-8"))
    
    environ.set_config("keys", "private", private_key_b64.decode("utf-8"))
    environ.set_config("keys", "public", public_key_b64.decode("utf-8"))
    
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
    """
    Encrypts a given text accordingly with RSA rules.
    """
    
    input_text = None
    if file_helper.is_path(src):
        input_text = file_helper.read_txt_file(src)
    else:
        input_text = src
    
    key = None
    if pkey is None:
        key = environ.read_config("keys", "public")
        
    else:
        key = pkey
        
    key = tuple(map(int, base64.b64decode(key).decode("utf-8").split(",")))
    
    encrypted_text = rsa.encrypt(input_text, key)
    
    if dest is not None:
        file_helper.write_txt_file(dest, encrypted_text)
    else:
        typer.echo(encrypted_text)
        


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
    input_text = None
    if file_helper.is_path(src):
        input_text = file_helper.read_txt_file(src)
    else:
        input_text = src
    
    key = None
    if pkey is None:
        key = environ.read_config("keys", "private")
    else:
        key = pkey
    
    key = tuple(map(int, base64.b64decode(key).decode("utf-8").split(",")))
    
    decrypted_text = rsa.decrypt(input_text, key)
    
    if dest is not None:
        file_helper.write_txt_file(dest, decrypted_text)
    else:
        typer.echo(decrypted_text)


if __name__ == "__main__":
    app()