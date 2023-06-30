import requests
from rich.console import Console
from rich.progress import track
import typer

app = typer.Typer() # create a typer app

@app.command() # create a command
def download(url: str, filename: str): # define the command arguments
    """Download a file from a given url and save it with a given filename."""
    console = Console() # create a console object
    response = requests.get(url, stream=True) # send a GET request to the url with stream option
    response.raise_for_status() # check if the request was successful
    total_size = int(response.headers.get("content-length", 0)) # get the total size of the file
    with open(filename, "wb") as f: # open a file in write binary mode
        for chunk in track(response.iter_content(chunk_size=1024), total=total_size): # iterate over the response chunks with progress bar
            f.write(chunk) # write the chunk to the file
    console.print(f"Downloaded {filename} from {url}", style="green") # print a success message

if __name__ == "__main__":
    app() # run the app
