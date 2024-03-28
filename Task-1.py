
import random

print("\t\tCaesar Cipher")

# Define the alphabet for encryption
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Get input from user
plain_text = input("Enter text: \n")

# Generate a random key between 1 and 26
key = random.randint(1, 26)
print("Key:", key)

# Encryption function
def encrypt(plain_text, key):
    cipher_text = ""
    print("Encrypting...")
    for char in plain_text:
        # Find the index of the character in the alphabet, add the key, and wrap around if needed
        ct = (alphabet.find(char) + key) % 52
        # Append the encrypted character to the cipher text
        cipher_text += alphabet[ct]

    print("Encrypted text:", cipher_text)
    return cipher_text

# Encrypt the input text
cipher_text = encrypt(plain_text, key)

# Decryption function
def decrypt(cipher_text, key):
    plain_text = ""
    print("Decrypting...")
    for char in cipher_text:
        # Find the index of the character in the alphabet, subtract the key, and wrap around if needed
        pt = (alphabet.find(char) - key) % 52
        # Append the decrypted character to the plain text
        plain_text += alphabet[pt]

    print("Decrypted text:", plain_text)
    return plain_text

# Decrypt the cipher text
plain_text1 = decrypt(cipher_text, key)

# Check if decryption was successful
if plain_text1 == plain_text:
    print("Caesar cipher Successful!")
else:
    print("Failed!")
