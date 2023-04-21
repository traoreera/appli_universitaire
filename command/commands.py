from cryptography.fernet import Fernet
import json
import ctypes
import tkinter.messagebox as messagebox

# Générer une clé aléatoire
key = Fernet.generate_key()

# Chiffrer les données JSON avec la clé
def encrypt_json(json_data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(json_data.encode())
    return encrypted_data

# Déchiffrer les données JSON avec la clé
def decrypt_json(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    return decrypted_data

# Charger les données JSON depuis un fichier
with open('data.json', 'r') as file:
    data = json.load(file)

# Chiffrer les données JSON et les écrire dans un fichier
encrypted_data = encrypt_json(json.dumps(data), key)
with open('data.encrypted', 'wb') as file:
    file.write(encrypted_data)

# Déchiffrer les données JSON depuis le fichier chiffré
with open('data.encrypted', 'rb') as file:
    encrypted_data = file.read()
decrypted_data = decrypt_json(encrypted_data, key)
print(json.loads(decrypted_data))


def Root_register(self):
        
        try:
            admin_modes = os.geteuid() == 0 # type: ignore
        except AttributeError:
            admin_modes = ctypes.windll.shell32.IsUserAnAdmin()

        if not admin_modes:
            print("no admin mods")
            messagebox.showwarning(
                title="admin", message="veuiller execute le logitiel en temp qu'administrateur du system")
            quit()

        else:
            pass
