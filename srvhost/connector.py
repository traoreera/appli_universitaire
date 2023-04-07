import socket
import threading

alias = input("alias >")
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('localhost',10))

def client_rsvs():
    
    while True:
        
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(msg)
        
        except: 
            print("error")
            client.close()
            break

def client_send():
    
    while True:
        
        msg = f'{alias}: {input("")}'
        
        client.send(msg.encode("utf-8"))

thread1 = threading.Thread(target=client_rsvs)
thread1.start()

thread2 = threading.Thread(target=client_send)
thread2.start()