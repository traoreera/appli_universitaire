import requests
from rich.console import Console
from rich.progress import track
import typer

app = typer.Typer() # créer une application typer

@app.command() # créer une commande
def download(url: str, filename: str): # définir les arguments de la commande
    """Télécharger un fichier à partir d'une url donnée et l'enregistrer avec un nom de fichier donné."""
    console = Console() # créer un objet console
    response = requests.get(url, stream=True) # envoyer une requête GET à l'url avec l'option stream
    response.raise_for_status() # vérifier si la requête a réussi
    total_size = int(response.headers.get("content-length", 0)) # obtenir la taille totale du fichier
    with open(filename, "wb") as f: # ouvrir un fichier en mode écriture binaire
        for chunk in track(response.iter_content(chunk_size=1024), total=total_size): # itérer sur les morceaux de la réponse avec une barre de progression
            f.write(chunk) # écrire le morceau dans le fichier
    console.print(f"Téléchargé {filename} depuis {url}", style="green") # afficher un message de succès

if __name__ == "__main__":
    app() # exécuter l'application
