import random

def encrypt_text(text):
    # Generate a random seed
    seed = random.randint(1, 100000)
    
    # Save the seed to a file
    with open("seed.txt", "w") as f:
        f.write(str(seed))
    
    # Use the seed to initialize the random number generator
    random.seed(seed)
    
    # Encrypt the text by randomly swapping characters
    text_list = list(text)
    for i in range(len(text_list)):
        j = random.randint(0, len(text_list)-1)
        text_list[i], text_list[j] = text_list[j], text_list[i]
    encrypted_text = ''.join(text_list)
    
    # Save the encrypted text to a file
    with open("output.txt", "w") as f:
        f.write(encrypted_text)
    
    return encrypted_text