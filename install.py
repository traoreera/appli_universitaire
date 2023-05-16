import typer
import getpass
app = typer.Typer()


@app.command()
def _login():
    username = input('username :')
    password = getpass.getpass('password:')


if __name__ == "__main__":
    
    app()