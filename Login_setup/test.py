import os

import typer


app = typer.Typer()


class Test():

    @app.command()
    def set_file(file):
        with open('set','+w') as f: f.write(file)
        print(f'content set sucessfully  {file}')
    @app.command()
    def set_change(file):
        with open('set','+w') as f:
            f.write(str(file))
            print(f"Old content set => New content set :{file}")
    
    @app.command(name='--test-db',help="test la base de donnes ",)
    def test_db():
        with open('set','r') as file :
            set_content = file.read()
            print(set_content)
            if set_content != 'login.db': print(f"set fille {set_content} isn't oportunity to test db")
    
    @app.command()
    def print_set():
        with open('set','r') as f: content = f.read()
        print(f'set content : {content}')
    
        


if __name__ == "__main__":
    app()