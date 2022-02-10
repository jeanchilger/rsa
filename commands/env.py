import typer
from utils import environ

app = typer.Typer()


@app.command()
def describe() -> None:
    """
    Shows local values of the environment.
    This will display the keys and the prime numbers used to
    generate them, along with any additional env-level information.
    """
    
    config = environ.get_env_config()
    
    for section in config.sections():
        typer.secho(section, bold=True)
        
        for key, value in config.items(section):
            typer.echo(typer.style(key, fg=typer.colors.BRIGHT_WHITE) + ": " + value)


if __name__ == "__main__":
    app()