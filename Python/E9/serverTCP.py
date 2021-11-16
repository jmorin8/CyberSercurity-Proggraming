# server Script 
import socket 
from cryptography.fernet import Fernet
import os

host='127.0.0.1'
port=12345
buffer_size=2048
connection_results = tuple()

# Creating socket
try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port)) 
    print('[*] Server socket created')

    try:
        server_socket.listen(1) #number of connections
        (conn, address)=server_socket.accept()
        print('[*] Socket listening')
        print(f'[*] Got connection from --> {address[0]}')    
        
        
        # receiving data
        while True:
            client_data = conn.recv(buffer_size) # received data from client
            print('[*] Received data from client')
            conn.send(b'[SERVER] Data received bye!') # message in bytes
            break
        conn.close()
        connection_results=(conn, address) # Save data connection
        
        # Searching key file
        for file in os.listdir('.'):
            if file.endswith('.key'):
                print(f'[*] Decrypting {file}')

                # Getting key file
                key_file = open(file,'rb')
                file_content = key_file.read()
                key_file.close()
                
                # Decrypting wt Fernet
                f = Fernet(file_content)
                
                encrypted_content = f.decrypt(client_data, None)
                decrypt_content = encrypted_content.decode()
                
                print(f'[*] Client message {decrypt_content}')
    
    except KeyboardInterrupt:
        print('[ERROR] Keyboard interrupt')

    server_socket.close()

except socket.error as error:
    print(f'[ERROR] {str(error)}')
