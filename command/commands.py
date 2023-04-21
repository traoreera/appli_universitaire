import json
from cryptography.fernet import Fernet


# Générer une clé de chiffrement
key = Fernet.generate_key()

# Écrire la clé dans un fichier
with open('key.key', 'wb') as key_file:
    key_file.write(key)

# Charger les données JSON
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Convertir les données en chaîne JSON
json_string = json.dumps(data)

# Chiffrer les données
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(json_string.encode())

# Écrire les données chiffrées dans un fichier
with open('data.encrypted', 'wb') as encrypted_file:
    encrypted_file.write(cipher_text)