from Crypto.Cipher import AES
import os

try: 
    def decrypt(ciphertext_filename, key_filename):
        with open(ciphertext_filename, 'rb') as f:
            iv = f.read(16)
            tag = f.read(16)
            ciphertext = f.read()

        
        with open(key_filename, 'rb') as key_file:
            key = key_file.read()

        cipher = AES.new(key, AES.MODE_EAX, iv)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)

        return plaintext

    key_filename = 'key.txt'
    ciphertext_filename = 'output.txt'

    decrypted_text = decrypt(ciphertext_filename, key_filename)
    print("Decrypted text:", decrypted_text.decode())

    while True:
        if Exception != ValueError:
                with open('key.txt', 'r') as f:
                    hex_key = f.read()
                    print(f"right key was generated! {hex_key}")
                    break


except ValueError:
    print("no")