import shutil
from pathlib import Path


def get_path(path: str) -> Path:
    """
    Produces a Path for the given string path.

    Args:
        path (str): Path as string.

    Returns:
        Path: Path object.
    """

    return Path(path.replace("\\", "/"))


def path_to_str(path: Path, absolute=True) -> str:
    """
    Returns the string representation for the given
    Path object.

    Args:
        path (Path): Path object to be converted.
        absolute (bool): Whether or not return the absolute path.

    Returns:
        str: String path representation.
    """

    return path.absolute().as_posix() if absolute else path.as_posix()


def exists(path: str) -> bool:
    """
    Returns whether or not given path existis.

    Args:
        path (str): Path to check existence.

    Returns:
        bool: True if path exists, False otherwise.
    """

    _p = get_path(path)
    
    return _p.exists()


def create_dir(path: str) -> None:
    """
    Creates a folder, if not exists, at the given location.
    Parent folders that don't exists are also created.

    Args:
        path (str): Path to create a new directory.
    """

    if not exists(path):
        get_path(path).mkdir(parents=True)


def create_file(path: str) -> None:
    """
    Creates an empty file at the given location.

    Args:
        path (str): Path where the file should be created.
    """

    if not exists(path):
        get_path(path).touch()


def copy_dir(src: str, dest: str) -> None:
    """
    Copy a full directory from src to dest.

    Args:
        src (str): Source.
        deset (str): Destination.
    """

    src_path = get_path(src)
    dest_path = get_path(dest)
    
    shutil.copytree(src_path, dest_path)


def copy_file(src: str, dest: str) -> None:
    """
    Copies a file from src to dest.

    Args:
        src (str): Source.
        deset (str): Destination.
    """

    src_path = get_path(src)
    dest_path = get_path(dest)
    
    shutil.copy(src_path, dest_path)


def get_cwd() -> Path:
    """
    Returns the current working directory (cwd).

    Returns:
        Path: cwd path.
    """

    return Path.cwd()