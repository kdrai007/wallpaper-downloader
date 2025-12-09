import typer
from core.services import create_user

app=typer.Typer()

@app.command()
def add_user_cli(username : str):
    create_user(username)
    typer.echo(f"user {username} created via CLI")

if __name__ == __main__:
    app()


