#
# Script to encrypt/decrypt messages with caesar cipher or crack it 
# 
import argparse

symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def do_encrypt(msg: str):    
    encrypted_msg = ''

    space = 1
    while space > 0:
        keyword = input('[INPUT] keyword to encrypt message: ') # keyword must have not spaces
        space = keyword.count(' ')

        if keyword.isalpha() == False: # keyword must be alphanumeric
            space = space + 1 

    key = len(keyword)

    print('[+] Encrypting "%s"' %msg)
    for char in msg:
        if char in symbols:
            index = symbols.find(char)
            finalIndex = index + key

            if finalIndex >= len(symbols):
                finalIndex = finalIndex - len(symbols)
            elif finalIndex < 0:
                finalIndex = finalIndex + len(symbols)
            
            encrypted_msg = encrypted_msg + symbols[finalIndex]
        else:
            encrypted_msg = encrypted_msg + char

    print('[+] Message encrypted --> %s' %encrypted_msg)


def do_decrypt(msg: str):
    decrypted_msg = ''

    space = 1
    while space > 0:
        keyword = input('[INPUT] keyword to decrypt message: ')  # keyword must have not spaces
        space = keyword.count(' ')

        if keyword.isalpha() == False:  # keyword must be alphanumeric
            space = space + 1 

    key = len(keyword)

    print('[+] Decrypting "%s"' %msg)
    for char in msg:
        if char in symbols:
            index = symbols.find(char)
            finalIndex = index - key

            if finalIndex >= len(symbols):
                finalIndex = finalIndex - len(symbols)
            elif finalIndex < 0:
                finalIndex = finalIndex + len(symbols)
            
            decrypted_msg = decrypted_msg + symbols[finalIndex]
        else:
            decrypted_msg = decrypted_msg + char

    print('[+] Message decrypted --> %s' %decrypted_msg)


def crackIt(msg: str):

    for key in range(len(symbols)):
        cracked_msg = ''

        for char in msg:
            if char in symbols:
                index = symbols.find(char)
                finalIndex = index - key

                if finalIndex < 0:
                    finalIndex = finalIndex + len(symbols)

                cracked_msg = cracked_msg + symbols[finalIndex]
            else:
                cracked_msg = cracked_msg + char

        print('Attempt #%s: %s' % (key, cracked_msg))


if __name__=='__main__':
    parser = argparse.ArgumentParser(usage='chiper_cesar.py [-option] "msg"')
    parser.add_argument('-e', '--encrypt', 
                        help='encrypt a message',
                        action='store_true',
                        )
    
    parser.add_argument('-d', '--decrypt', 
                        help='decrypt a message',
                        action='store_true',
                        )

    parser.add_argument('-c', '--crack', 
                        help='crack a encrypted message',
                        action='store_true',
                        )
    
    parser.add_argument('msg',
                        type=str,
                        help='message to encrypt/decrypt/crack',
                        )
    
    params = parser.parse_args()

    msg = params.msg
    if params.encrypt:
        do_encrypt(msg)
    elif params.decrypt:
        do_decrypt(msg)
    elif params.crack:
        crackIt(msg)