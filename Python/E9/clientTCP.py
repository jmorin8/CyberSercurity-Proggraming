import socket
import os
from cryptography.fernet import Fernet
import argparse

ip='127.0.0.1'
port=12345
buffer_size=2048

def socket_connection(var):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, port))

        print('[*] Connected to socket')
        print('[*] Sending message to server')

        try:
            client_socket.send(var) # send message to server
            print(f'[*] Message sent {var}')
            print(f'{client_socket.recv(buffer_size).decode()}') # server response

        except KeyboardInterrupt:
            print('[ERROR] Keyboard interrupt')

        client_socket.close()

    except socket.error as error:
        print(f'[ERROR] {str(error)}')


def create_key(var):
    print('[*] Creating encryption-key')
    clave = Fernet.generate_key()

    validate= os.path.exists('k.key')
    if validate:
        print('[INFO] Encryption-key already exists')
    else:
        keyFile = open('k.key', 'wb')
        keyFile.write(clave)
        keyFile.close()
        print('[*] Encryption-key created')

    f = Fernet(clave)
    encrypted_message= f.encrypt(var) # User message encrypted

    return encrypted_message # return encrypted message


if __name__=="__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-msg', '--message', dest='message', 
                        help='Message you want to send to the server', 
                        required=True, type=str,
                        )
    
    params = parser.parse_args()

    # Take user message and encode it into bytes
    message = params.message
    messsage_bytes = message.encode()

    socket_connection(create_key(messsage_bytes))
