import configparser
import typer
from pathlib import Path
from utils import file_helper
from src import rsa

APP_NAME = "rsa-cryptosystem-py"


def main() -> None:
    """
    Initializes an environment. Any needed configuration will be prompted.
    """
    
    app_dir = typer.get_app_dir(APP_NAME)
    config_path = Path(app_dir) / "config.cfg"
    
    # if a config file already exists, init shouldn't be used
    if not config_path.is_file():
        file_helper.create_dir(app_dir)
    else:
        raise typer.Exit()
    
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(config_path)
    
    p = typer.prompt("Input the first prime number")
    q = typer.prompt("Input the second prime number")
    
    config.add_section("args")
    config.set("args", "p", p)
    config.set("args", "q", q)
    
    # generate the keys based on provided prime numbers
    private_key, public_key = rsa.generate_keys(int(p), int(q))
    
    config.add_section("keys")
    config.set("keys", "private", str(private_key))
    config.set("keys", "public", str(public_key))
    
    typer.echo(f"Private key: {private_key}")
    typer.echo(f"Public key: {public_key}")

    with open(config_path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    main()
