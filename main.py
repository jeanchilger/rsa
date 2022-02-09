import typer

from commands import init as init_cmd, decrypt, encrypt

app = typer.Typer()

app.add_typer(encrypt.app, name="encrypt")
app.add_typer(decrypt.app, name="decrypt")

@app.command()
def init() -> None:
    """
    Initializes an environment. Any needed configuration will be prompted.
    """

    init_cmd()

if __name__ == "__main__":
    app()