import typer
import getpass
app = typer.Typer()
from rich import console
from rich import print
console = console.Console()

class Login():
    
    def __init__(self,username,password,**arkgv):
        self.username = username
        self.passwd = password
        self.arkgv = arkgv.keys()
        
        print()

@app.command()
def _login():
    username = input('username :')
    password = getpass.getpass('password:')
    
    Login(username=username,password=password)


if __name__ == "__main__":
    
    app()