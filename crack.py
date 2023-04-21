import os
import binascii
import subprocess

while True:
    try:

        
        
        # Generate a random key
        key = os.urandom(16)

        # Convert the key to a string of hexadecimal digits
        hex_key = binascii.hexlify(key).decode()
        print()

        # Save the key to a file named key.txt
        with open('key.txt', 'w') as f:
            f.write(hex_key)

        # Run the decrypt.py program
        subprocess.run(['python', 'decrypt.py'])

            


    except ValueError:
        print('ValueError occurred, retrying...')