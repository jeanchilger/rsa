import configparser
import shutil
import typer
from pathlib import Path
from utils import file_helper

APP_NAME = "rsa-cryptosystem-py"


def create_env() -> bool:
    """
    Sets up a new environment, with needed files.

    Returns:
        bool: True if env was created, False otherwise
    """
    
    app_dir = typer.get_app_dir(APP_NAME)
    config_path = Path(app_dir) / "config.cfg"
    
    if not config_path.is_file():
        file_helper.create_dir(app_dir)
        return True
    else:
        return False


def delete_env() -> None:
    """
    Deletes the environment.
    """
    
    app_dir = typer.get_app_dir(APP_NAME)
    shutil.rmtree(app_dir)


def set_config(section: str, key: str, value: str) -> None:
    """
    Sets a config in appdir.

    Args:
        section (str): Section from config file.
        key (str): Key within section to be set.
        value (str, optional):  Value to be set.
    """

    app_dir = typer.get_app_dir(APP_NAME)
    config_path = Path(app_dir) / "config.cfg"
    
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(config_path)
    
    if not config.has_section(section):
        config.add_section(section)

    config.set(section, key, value)
    
    with open(config_path, "w") as cfg_file:
        config.write(cfg_file)


def read_config(section: str, key: str) -> str:
    """
    Reads a config from appdir.

    Args:
        section (str): Section from where config should be read.
        key (str): Key from where config should be read.

    Returns:
        str: The value of specified config.
    """
    
    app_dir = typer.get_app_dir(APP_NAME)
    config_path = Path(app_dir) / "config.cfg"
    
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(config_path)
    
    return config.get(section, key)
